import firebase_admin
from firebase_admin import credentials, db
from typing import List, Dict

# inicializar conexion con firebase
def init_firebase():
    cred = credentials.Certificate("./firebase_credentials.json")
    firebase_admin.initialize_app( cred, {
        "databaseURL": "https://readfilefastapi-default-rtdb.firebaseio.com/"
    })

# insert data in DB
def insert_data_to_firebase( path: str, data: dict ):
    ref = db.reference( path )
    ref.push( data ) # agregar el dict a la ruta


# ---------- SUBIR A FIREBASE ----------
def upload_to_firebase(data: List[Dict], path: str = "datos_excel"):
    ref = db.reference(path)
    for item in data:
        ref.push(item)  # Crea un nuevo nodo con ID único
