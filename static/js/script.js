document.getElementById('sendButton').addEventListener('click', sendMessage);

// Clear messages on page load (new session)
window.onload = function () {
    clearChatHistory();
    fetchMessages();
};

// Function to send message to the server
function sendMessage() {
    const username = document.getElementById('username').value;
    const messageInput = document.getElementById('messageInput');
    const message = messageInput.value;

    if (username && message) {
        fetch('/send', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ sender: username, message: message }),
        }).then(response => {
            return response.json();
        }).then(data => {
            console.log(data);
            messageInput.value = ''; // Clear input field
            fetchMessages(); // Refresh messages
        });
    }
}

// Function to fetch messages from the server
function fetchMessages() {
    fetch('/messages')
        .then(response => response.json())
        .then(data => {
            const messagesDiv = document.getElementById('messages');
            messagesDiv.innerHTML = ''; // Clear current messages

            for (const key in data) {
                const message = data[key];
                const messageElement = document.createElement('div');
                messageElement.textContent = `${message.sender}: ${message.message}`;
                messagesDiv.appendChild(messageElement);
            }

            messagesDiv.scrollTop = messagesDiv.scrollHeight; // Scroll to bottom
        });
}

// Clear chat history function
function clearChatHistory() {
    fetch('/clear-history', { method: 'POST' })  // Make a request to clear the server-side history
        .then(response => response.json())
        .then(() => {
            const messagesDiv = document.getElementById('messages');
            messagesDiv.innerHTML = ''; // Clear current messages on the client side
        });
}

// Fetch messages every 2 seconds
setInterval(fetchMessages, 2000);

// Add event listener for Enter key press
document.getElementById('messageInput').addEventListener('keypress', (e) => {
  if (e.key === 'Enter') {
    sendMessage();
  }
});
