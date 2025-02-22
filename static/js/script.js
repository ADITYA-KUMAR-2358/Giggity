document.addEventListener('DOMContentLoaded', () => {
    const sendButton = document.getElementById('sendButton');
    const messageInput = document.getElementById('messageInput');
    const messagesDiv = document.getElementById('messages');
    const usernameInput = document.getElementById('username');
    
    let lastFetchedMessages = '';

    // Attach event listeners
    sendButton.addEventListener('click', sendMessage);
    messageInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') sendMessage();
    });

    // Initialize chat on page load
    initializeChat();

    function initializeChat() {
        clearChatHistory();
        fetchMessages();
        setInterval(fetchMessages, 2000); // Fetch messages every 2 seconds
    }

    // Function to send a message to the server
    function sendMessage() {
        const username = usernameInput.value.trim();
        const message = messageInput.value.trim();

        if (!username || !message) return; // Prevent empty messages

        fetch('/send', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ sender: username, message })
        })
        .then(response => response.json())
        .then(data => {
            console.log('Message sent:', data);
            messageInput.value = ''; // Clear input field
            fetchMessages(true); // Fetch new messages immediately
        })
        .catch(error => console.error('Error sending message:', error));
    }

    // Function to fetch messages from the server
    function fetchMessages(forceUpdate = false) {
        fetch('/messages')
        .then(response => response.json())
        .then(data => {
            const messagesJSON = JSON.stringify(data);
            if (!forceUpdate && messagesJSON === lastFetchedMessages) return; // Prevent unnecessary updates
            lastFetchedMessages = messagesJSON;

            messagesDiv.innerHTML = ''; // Clear old messages
            const fragment = document.createDocumentFragment();

            Object.values(data).forEach(({ sender, message }) => {
                const messageElement = document.createElement('div');
                messageElement.textContent = `${sender}: ${message}`;
                messageElement.className = sender === usernameInput.value ? 'message-outgoing' : 'message-incoming';
                fragment.appendChild(messageElement);
            });

            messagesDiv.appendChild(fragment);
            messagesDiv.scrollTop = messagesDiv.scrollHeight; // Auto-scroll to latest message
        })
        .catch(error => console.error('Error fetching messages:', error));
    }

    // Function to clear chat history
    function clearChatHistory() {
        fetch('/clear-history', { method: 'POST' })
        .then(response => response.json())
        .then(() => messagesDiv.innerHTML = '') // Clear client-side messages
        .catch(error => console.error('Error clearing chat history:', error));
    }
});
