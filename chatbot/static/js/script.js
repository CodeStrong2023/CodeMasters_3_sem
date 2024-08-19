// -*- coding: utf-8 -*-
const chatMessages = document.getElementById('chatMessages');
const userInput = document.getElementById('userInput');
const sendBtn = document.getElementById('sendBtn');

// Función para manejar el envío de mensajes
function handleMessageSubmit(event) {
    event.preventDefault();
    const userMessage = userInput.value.trim();

    if (userMessage) {
        // Mostrar el mensaje del usuario
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('user-message');
        messageDiv.textContent = userMessage;
        chatMessages.appendChild(messageDiv);

        // Crear una instancia de XMLHttpRequest
        const xhr = new XMLHttpRequest();

        // Abrir una solicitud POST al archivo app.py
        xhr.open('POST', '/chat', true);

        // Enviar los datos del formulario
        const formData = new FormData();
        formData.append('message', userMessage);
        xhr.send(formData);

        // Manejar la respuesta del servidor
        xhr.onreadystatechange = function() {
            if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
                const botResponse = this.responseText;

                // Mostrar la respuesta del bot
                const botMessageDiv = document.createElement('div');
                botMessageDiv.classList.add('bot-response');
                botMessageDiv.textContent = botResponse;
                chatMessages.appendChild(botMessageDiv);

                // Limpiar el campo de entrada
                userInput.value = '';

                // Desplazar el scroll al final del chat
                chatMessages.scrollTop = chatMessages.scrollHeight;
            }
        };
    }
}

// Agregar el manejador de eventos al formulario
sendBtn.addEventListener('click', handleMessageSubmit);
userInput.addEventListener('keypress', function(event) {
    if (event.key === 'Enter' && !event.shiftKey) {
        // Evitar el comportamiento predeterminado de Enter (salto de línea)
        event.preventDefault();
        // Enviar el mensaje
        handleMessageSubmit(event);
    }
});
