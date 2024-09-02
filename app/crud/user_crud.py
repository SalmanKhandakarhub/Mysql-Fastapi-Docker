from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from ..models.models import User
from ..schemas.user_schemas import UserCreate
from ..core.security import hash_password

async def get_email(db: AsyncSession, email: str):
    result = await db.execute(select(User).filter(User.email == email))
    return result.scalar_one_or_none()

async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(User).filter(User.email == email))
    return result.scalar_one_or_none()
    
async def create_user(db: AsyncSession, user: UserCreate):
    hashed_password = hash_password(user.password)  # You should have a secure hash function
    db_user = User(
        name=user.name,
        email=user.email,
        hashed_password=hashed_password,
        type=user.type
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def get_all_user(db: AsyncSession):
    result = await db.execute(select(User))
    return result.scalars().all()
    