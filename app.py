import firebase_admin
from firebase_admin import credentials, db
from flask import Flask, render_template, request, jsonify
import threading

# Initializing Firebase
cred = credentials.Certificate("C:\\Users\\ADITYA KUMAR\\Desktop\\Giggity\\giggity-71b03-firebase-adminsdk-j3bsh-920cf79023.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://giggity-71b03-default-rtdb.firebaseio.com/'
})

app = Flask(__name__)

# Function to send a message to the Firebase database
def send_message(sender, message):
    ref = db.reference('messages')
    ref.push({
        'sender': sender,
        'message': message
    })

# Function to fetch messages from the Firebase database
def fetch_messages():
    ref = db.reference('messages')
    return ref.get()

# Function to clear the chat history
def clear_chat_history():
    ref = db.reference('messages')
    ref.delete()  # This deletes all messages under the 'messages' reference in Firebase

# HTML route
@app.route('/')
def index():
    return render_template('index.html')

# Fetch messages route
@app.route('/messages', methods=['GET'])
def get_messages():
    messages = fetch_messages()
    return jsonify(messages)

# Send message route
@app.route('/send', methods=['POST'])
def send():
    data = request.get_json()
    send_message(data['sender'], data['message'])
    return jsonify({"status": "Message sent!"})

# Route to clear chat history
@app.route('/clear-history', methods=['POST'])
def clear_history():
    clear_chat_history()
    return jsonify({"status": "Chat history cleared!"})

# Entry point for Cloud Functions
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)


if __name__ == '__main__':
    app.run(debug=True)
