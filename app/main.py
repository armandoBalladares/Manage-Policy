from fastapi import FastAPI, UploadFile, File
from app.excel_processor import process_excel
from app.firebase import init_firebase, insert_data_to_firebase, upload_to_firebase
from io import BytesIO
app = FastAPI()

# Inicializa Firebase al arrancar el servidor
init_firebase()

@app.post("/upload-excel/")
async def upload_excel( file: UploadFile = File(...) ):
    
    contents = await file.read()
    # procesar arhivo excel
    data = process_excel( BytesIO(contents) )
    # insertar cada fila en Firebase
    # for record in data:
    #    insert_data_to_firebase("/excel_data", record)

    upload_to_firebase(data,"/excel_data")

    return {"status": 200, "message": "Operacion Exitosa.!", "rows_inserted": len(data) }
    