from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserCreate, UserResponse
from app.crud.user import create_user
from app.api.deps import get_db

router = APIRouter()


@router.post("/register", response_model=UserResponse)
async def create(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user(db, user)
