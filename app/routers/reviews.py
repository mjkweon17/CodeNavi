from typing import Annotated, List
from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, Response, Request, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session
from pydantic import BaseModel

from database import get_db
from models import HKUser, HKReview, HKBookmark, HKUserStack, HKStackCategory, HKLecture

router = APIRouter(prefix="/reviews", tags=["reviews"], responses={404: {"description": "Not found"}})

# 수강평 작성 post
# Request: user_id, lecture_id, star, good_review, bad_review
# Response: review_id
@router.post("/")
async def create_review(user_id: int, lecture_id: int, star: int, good_review: str, bad_review: str, db: Session = Depends(get_db)):
    review = HKReview(user_id=user_id, lecture_id=lecture_id, star=star, good_review=good_review, bad_review=bad_review, is_active=True, created_at=datetime.now())
    db.add(review)
    db.commit()
    db.refresh(review)
    return review.review_id