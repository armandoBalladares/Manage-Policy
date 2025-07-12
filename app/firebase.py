import firebase_admin
from firebase_admin import credentials, db

# inicializar conexion con firebase
def init_firebase():
    cred = credentials.Certificate("firebase_credentials.json")
    firebase_admin.initialize_app( cred, {
        "databaseURL": "https://<TU_PROJECTO>.firebaseio.com/"
    })