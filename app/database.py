from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# DATABASE_URL = "postgresql+asyncpg://username:password@ep-xxxxx.neon.tech/dbname"

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_async_engine(DATABASE_URL, echo=True)

"""
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession
)
"""

async_session = async_sessionmaker(engine, expire_on_commit=False)

Base = declarative_base()



