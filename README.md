# Giggity

## Overview
Giggity is a modern, real-time chat application designed to provide users with a personalized and engaging messaging experience. Each user gets a unique chat box where their messages appear in green and others' messages in white — similar to WhatsApp's chat style. The app ensures privacy by clearing chat history every new session, allowing for fresh conversations every time.

Built using **Flask** for the backend and **Firebase Realtime Database** for data storage, Giggity offers seamless communication with a clean, intuitive UI.

---

## Key Features

- **Personalized Chat UI**  
  Each user sees their messages in a green chat bubble while others' messages appear in white, enhancing readability and familiarity.

- **Real-Time Messaging**  
  Messages update automatically every 2 seconds without page reloads, providing a smooth chat experience.

- **Session-Based Chat History**  
  Chat history is cleared automatically at the start of each new session to protect user privacy.

- **Firebase Realtime Database Integration**  
  Uses Firebase for reliable, scalable, and secure message storage and retrieval.

- **Simple and Responsive Interface**  
  Clean design optimized for desktop and mobile devices, making chatting effortless.

---

## Tech Stack

| Layer          | Technology                |
|----------------|---------------------------|
| Frontend       | HTML, CSS, JavaScript     |
| Backend        | Python, Flask             |
| Database       | Firebase Realtime Database|
| Hosting        | Firebase Hosting          |

---

## Installation & Setup

### Prerequisites
- Python 3.8+
- Firebase account
- Firebase CLI installed (`npm install -g firebase-tools`)
- Also go through the requrirements.txt files to check for prerequisites

### Step 1: Clone the Repository

```bash
git clone https://github.com/ADITYA-KUMAR-2358/Giggity.git
cd Giggity
