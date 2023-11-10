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
    user_id: int | None = None
    user_name: str | None = None
    bookmark_num: int | None = None
    review_num: int | None = None
    user_stacks: List[str] | None = None

# 사용자 정보 GET
@router.get("/{user_id}")
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(HKUser).filter(HKUser.user_id == user_id).first()
    user_in_db = UserInDB()
    user_in_db.user_id = user.user_id
    user_in_db.user_name = user.user_name
    user_in_db.bookmark_num = len(user.bookmarks)
    user_in_db.review_num = len(user.reviews)
    # stack
    user_stacks = []
    for user_stack in user.user_stacks:
        user_stacks.append(user_stack.stack_category.stack_name)
    user_in_db.user_stacks = user_stacks

    return user_in_db

# bookmark 목록 조회
class UserBookmark(BaseModel):
    bookmark_id: int | None = None
    lecture_id: int | None = None
    title: str | None = None
    lecturer: str | None = None
    original_price: str | None = None
    current_price: str | None = None

# Response: user_id
# Request: bookmark 개수, UserBookmark 리스트
@router.get("/{user_id}/bookmarks")
async def get_bookmarks(user_id: int, db: Session = Depends(get_db)):
    user = db.query(HKUser).filter(HKUser.user_id == user_id).first()
    bookmarks = user.bookmarks
    user_bookmarks = []
    for bookmark in bookmarks:
        user_bookmark = UserBookmark()
        user_bookmark.bookmark_id = bookmark.bookmark_id
        user_bookmark.lecture_id = bookmark.lecture.lecture_id
        user_bookmark.title = bookmark.lecture.title
        user_bookmark.lecturer = bookmark.lecture.lecturer
        user_bookmark.original_price = bookmark.lecture.price
        user_bookmark.current_price = bookmark.lecture.discount_price
        user_bookmarks.append(user_bookmark)
    return user_bookmarks

# 자신이 작성한 review 목록 조회
class UserReview(BaseModel):
    review_id: int | None = None
    lecture_id: int | None = None
    title: str | None = None
    lecturer: str | None = None
    review_content: str | None = None
    review_date: datetime | None = None
    review_star: int | None = None
    good_review: str | None = None
    bad_review: str | None = None

# Response: user_id
# Request: review 개수, UserReview 리스트
@router.get("/{user_id}/reviews")
async def get_reviews(user_id: int, db: Session = Depends(get_db)):
    user = db.query(HKUser).filter(HKUser.user_id == user_id).first()
    reviews = user.reviews
    user_reviews = []
    for review in reviews:
        user_review = UserReview()
        user_review.review_id = review.review_id
        user_review.lecture_id = review.lecture.lecture_id
        user_review.title = review.lecture.title
        user_review.lecturer = review.lecture.lecturer
        user_review.review_content = review.good_review
        user_review.review_date = review.created_at
        user_review.review_star = review.star
        user_review.good_review = review.good_review
        user_review.bad_review = review.bad_review
        user_reviews.append(user_review)
    return user_reviews