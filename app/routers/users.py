from fastapi import APIRouter, Depends, Response, Request, status
from sqlalchemy.orm import Session

from database import get_db
# from models import User

router = APIRouter()

router = APIRouter(previx="/users", tags=["users"], responses={404: {"description": "Not found"}})

# users 핸들러
@router.get("/")
async def get_users(db: Session = Depends(get_db)):
    # users = db.query(User).all()
    # return users
    return {"message": "users"}