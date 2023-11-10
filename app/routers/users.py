from typing import Annotated, List
from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, Response, Request, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session
from pydantic import BaseModel

from database import get_db
from models import HKUser, HKReview, HKBookmark, HKUserStack, HKStackCategory

router = APIRouter(prefix="/users", tags=["users"], responses={404: {"description": "Not found"}})

class UserInDB(BaseModel):
    user_name: str | None = None
    bookmark_num: int | None = None
    review_num: int | None = None
    user_stacks: List[str] | None = None

# 사용자 정보 GET
@router.get("/{user_id}")
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(HKUser).filter(HKUser.user_id == user_id).first()
    user_in_db = UserInDB()
    user_in_db.user_name = user.user_name
    user_in_db.bookmark_num = len(user.bookmarks)
    user_in_db.review_num = len(user.reviews)
    # stack
    user_stacks = []
    for user_stack in user.user_stacks:
        user_stacks.append(user_stack.stack_category.stack_name)
    user_in_db.user_stacks = user_stacks

    return user_in_db

