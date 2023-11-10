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

# 수강평 조회
# Request: review_id
# Response: review_id, star, good_review, bad_review, created_at, user_id, user_name
@router.get("/{review_id}")
async def get_review(review_id: int, db: Session = Depends(get_db)):
    review = db.query(HKReview).filter(HKReview.review_id == review_id).first()
    result = {}
    result['review_id'] = review.review_id
    result['star'] = review.star
    result['good_review'] = review.good_review
    result['bad_review'] = review.bad_review
    result['created_at'] = review.created_at
    result['user_id'] = review.user.user_id
    result['user_name'] = review.user.user_name
    return result