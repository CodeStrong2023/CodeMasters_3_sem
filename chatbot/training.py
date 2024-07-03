import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import SGD


lemmatizer = WordNetLemmatizer()

# Cargar los datos de intenciones desde el archivo JSON
intents = json.loads(open('intents.json').read())

# Inicializar listas para almacenar palabras, clases e instancias de documentos
words = []
classes = []
documents = []
ignore_letters = ['?', '!', '¿', '.', ',']

# Procesar las intenciones y generar documentos
for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list, intent["tag"]))
    if intent["tag"] not in classes:
        classes.append(intent["tag"])

# Lematizar las palabras y filtrar letras ignoradas
words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
words = sorted(set(words))

# Guardar las palabras y clases en archivos pickle
pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

# Crear listas de entrenamiento
training = []
output_empty = [0] * len(classes)

# Preparar los datos para el entrenamiento
for doc in documents:
    # Inicializar la bolsa de palabras
    bag = []
    word_patterns = doc[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]

    # Crear la bolsa de palabras
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)

    # Crear el vector de salida
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])

# Mezclar los datos de entrenamiento
random.shuffle(training)

# Convertir los datos de entrenamiento en arrays de NumPy
# Rellenar las bolsas de palabras con ceros para que tengan la misma longitud
max_len_bag = max(len(t[0]) for t in training)
max_len_out = len(classes)
for i, t in enumerate(training):
    training[i][0] += [0] * (max_len_bag - len(t[0]))
    training[i][1] += [0] * (max_len_out - len(t[1]))

train_x = np.array([i[0] for i in training])
train_y = np.array([i[1] for i in training])

# Crear la red neuronal
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

# Compilar el modelo
sgd = SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# Entrenar el modelo
model.fit(train_x, train_y, epochs=200, batch_size=5, verbose=1)

# Guardar el modelo
model.save('model.h5')
