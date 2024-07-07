# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify, make_response
import json
import pickle
import numpy as np
from keras.models import load_model
import nltk
from nltk.stem import WordNetLemmatizer
import random

app = Flask(__name__, template_folder='templates')

# Cargar datos y modelos necesarios
lemmatizer = WordNetLemmatizer()
with open('intents.json', 'r', encoding='utf-8') as file:
    intents = json.load(file)
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('model.h5')

# Funciones de procesamiento de texto y predicción
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    max_index = np.where(res == np.max(res))[0][0]
    category = classes[max_index]
    return category

def get_response(tag, intents_json):
    list_of_intents = intents_json['intents']
    result = ""
    for i in list_of_intents:
        if i["tag"] == tag:
            result = random.choice(i['responses'])
            break
    return result

# Ruta para manejar solicitudes POST
@app.route('/chat', methods=['POST'])
def chat():
    message = request.form['message']
    category = predict_class(message)
    response_text = get_response(category, intents)
    response = make_response(response_text)
    response.headers['Content-Type'] = 'text/plain; charset=utf-8'
    return response


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
