from typing import Annotated
from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, Response, Request, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from pydantic import BaseModel

from database import get_db
from models import HKUser

router = APIRouter(prefix="/auth", tags=["auth"], responses={404: {"description": "Not found"}})

# Password encryption configuration
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(BaseModel):
    user_name: str
    email: str
    password: str
    github_id: str | None
    blog_link: str | None

class UserInDB(User):
    user_name: str
    email: str
    github_id: str | None
    blog_link: str | None

class UserInDB(User):
    hashed_password: str


# 회원가입
@router.post("/register", response_model=User)
async def register_user(user: User, db: Session = Depends(get_db)):
    if db.query(HKUser).filter(HKUser.user_name == user.user_name).first():
        raise HTTPException(status_code=400, detail="Username already registered")
    if db.query(HKUser).filter(HKUser.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = pwd_context.hash(user.password)
    db_user = HKUser(user_name=user.user_name, email=user.email, password=hashed_password, github_id=user.github_id, blog_link=user.blog_link, is_active=True, created_at=datetime.now())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
    

# 로그인
@router.post("/login")
async def login_user(user_name: str, password: str, db: Session = Depends(get_db)):
    user = db.query(HKUser).filter(HKUser.user_name == user_name).first()
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    if not pwd_context.verify(password, user.password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    return user