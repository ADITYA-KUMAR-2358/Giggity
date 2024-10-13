import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("C:\Users\ADITYA KUMAR\Desktop\Giggity\giggity-71b03-firebase-adminsdk-j3bsh-920cf79023.json")
firebase_admin.initialize_app(cred, {
    databaseURL: 'https://console.firebase.google.com/u/0/project/giggity-71b03/database/giggity-71b03-default-rtdb/data/~2F'
}
)