import os
import firebase_admin
from firebase_admin import credentials, db
from flask import Flask, render_template, request, jsonify, abort
from dotenv import load_dotenv

# Load environment variables (if using a .env file)
load_dotenv()

# Firebase Configuration (Avoid Hardcoded File Paths)
FIREBASE_CRED_PATH = os.getenv("FIREBASE_CRED_PATH", "firebase_credentials.json")  # Default filename if env variable is not set
DATABASE_URL = os.getenv("FIREBASE_DB_URL", "https://giggity-71b03-default-rtdb.firebaseio.com/")

# Initialize Firebase Admin SDK
try:
    cred = credentials.Certificate(FIREBASE_CRED_PATH)
    firebase_admin.initialize_app(cred, {'databaseURL': DATABASE_URL})
except Exception as e:
    print(f"Error initializing Firebase: {e}")
    exit(1)

app = Flask(__name__)

# Firebase Database Reference
MESSAGE_REF = "messages"

def send_message(sender: str, message: str) -> bool:
    """Push a new message to Firebase Database."""
    try:
        ref = db.reference(MESSAGE_REF)
        ref.push({'sender': sender, 'message': message})
        return True
    except Exception as e:
        print(f"Error sending message: {e}")
        return False

def fetch_messages():
    """Retrieve all messages from Firebase Database."""
    try:
        ref = db.reference(MESSAGE_REF)
        messages = ref.get()
        return messages if messages else {}
    except Exception as e:
        print(f"Error fetching messages: {e}")
        return {}

def clear_chat_history() -> bool:
    """Delete all messages from Firebase Database."""
    try:
        ref = db.reference(MESSAGE_REF)
        ref.delete()
        return True
    except Exception as e:
        print(f"Error clearing chat history: {e}")
        return False

@app.route('/')
def index():
    """Render the chat interface."""
    return render_template('index.html')

@app.route('/messages', methods=['GET'])
def get_messages():
    """Fetch and return all messages."""
    messages = fetch_messages()
    return jsonify(messages), 200

@app.route('/send', methods=['POST'])
def send():
    """Handle sending messages."""
    data = request.get_json()
    if not data or 'sender' not in data or 'message' not in data:
        abort(400, description="Invalid request. 'sender' and 'message' fields are required.")

    success = send_message(data['sender'], data['message'])
    return jsonify({"status": "Message sent!" if success else "Failed to send message"}), (200 if success else 500)

@app.route('/clear-history', methods=['POST'])
def clear_history():
    """Handle clearing chat history."""
    success = clear_chat_history()
    return jsonify({"status": "Chat history cleared!" if success else "Failed to clear chat history"}), (200 if success else 500)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
