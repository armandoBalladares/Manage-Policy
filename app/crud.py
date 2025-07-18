from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from .models import User

async def get_users(db: AsyncSession):
    result = await db.execute(select(User))
    return result.scalars().all()

async def create_user(db: AsyncSession, name: str, email: str):
    new_user = User(name=name, email=email)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user
