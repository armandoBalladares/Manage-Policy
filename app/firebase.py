import firebase_admin
from firebase_admin import credentials, db

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