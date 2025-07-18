from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

# DATABASE_URL = "postgresql+asyncpg://username:password@ep-xxxxx.neon.tech/dbname"
DATABASE_URL = 'postgresql://neondb_owner:npg_BgrhMKzN89aS@ep-spring-flower-ae6fcmba-pooler.c-2.us-east-2.aws.neon.tech/manage-policy?sslmode=require&channel_binding=require'

engine = create_async_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession
)

Base = declarative_base()
