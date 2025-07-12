from fastapi import FastAPI, UploadFile, File, HTTPException
import pandas as pd, io, uuid, time
import firebase_admin
from firebase_admin import credentials, db

"""
# init firebase
cred = credentials.Certificate("serviceAccountKry.jdon")
firebase_admin.initialize_app(cred, { "databaseURL": "https://<TU-PROYECTO>.firebaseio.com"} )
root_ref = db.reference("/excel_uploads")
"""

app = FastAPI()

@app.post("/upload_excel")
async def upload_excel( file: UploadFile = File(...) ):

    """
    if not file.filename.lower().endswith((".xls","xlsx")):
        raise HTTPException( 400, "Archivos permitidos .xls .xlsx")
    content = await file.read()

    try:
        df = pd.read_excel( io.BytesIO( content ))
    except Exception as e:
        raise HTTPException( 500, f"Error al intentar leer el fichero de excel esperado: {e}")

    data = df.fillna("").to_dict(  orient="records")
    key = str( uuid.uuid4() )
    timestamp = int( time.time()*1000 )
    entry = { f"row{idx+1}": row for idx, row in enumerate(data) }
    entry["uploaded_at"] = timestamp
    root_ref.child(key).set(entry)
    """ 

    return {"status": 200 ,"message": "Operacion exitosa...!", "key": key }

