from fastapi import FastAPI, UploadFile, File, Depends
from app.excel_processor import process_excel
from app.firebase import init_firebase, insert_data_to_firebase
from io import BytesIO
from sqlalchemy.ext.asyncio import AsyncSession
from .database import SessionLocal, engine, Base
from .crud import get_users, create_user

app = FastAPI()

# init firebase to load server
init_firebase()

# Create tables
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Dependency for get DB
async def get_db():
    async with SessionLocal() as session:
        yield session

@app.post("/upload-excel/")
async def upload_excel( file: UploadFile = File(...) ):
    contents = await file.read()
    data = process_excel( BytesIO(contents) )
    insert_data_to_firebase("/excel_data", data )
    return {"status": 200, "message": "Operacion Exitosa.!", "rows_inserted": len(data) }

@app.get("/users")
async def read_users(db: AsyncSession = Depends(get_db)):
    return await get_users(db)

@app.post("/users")
async def new_user(name: str, email: str, db: AsyncSession = Depends(get_db)):
    return await create_user(db, name, email)