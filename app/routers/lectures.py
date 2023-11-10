from typing import Annotated, List
from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, Response, Request, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session
from pydantic import BaseModel

from database import get_db
from models import HKLecture, HKReview, HKCompany, HKLectureStack

router = APIRouter(prefix="/lecutres", tags=["lecutres"], responses={404: {"description": "Not found"}})


class Review(BaseModel):
    review_id: int
    star: int
    good_review: str
    bad_review: str
    created_at: datetime
    user_id: int
    user_name: str

class LectureInDB(BaseModel):
    lecture_id: int | None = None
    title: str | None = None
    lecturer: str | None = None
    running_time: str | None = None   # course_hours
    difficulty: str | None = None
    original_price : str | None = None  # price
    current_price : str | None = None   # discount_price
    introduction: str | None = None
    link: str | None = None
    rating: float | None = None # 계산 필요
    platform : str | None = None # company_name
    review_amount : int | None = None # 계산 필요
    review: List[Review] | None = None # 계산 필요
    stack: str | None = None # 계산 필요




# 강의 목록 조회
@router.get("/")
async def get_lectures(db: Session = Depends(get_db)):
    lectures = db.query(HKLecture).all()
    return lectures

# 상세 강의 조회
@router.get("/{lecture_id}")
async def get_lecture(lecture_id: int, db: Session = Depends(get_db)):

    lecture = db.query(HKLecture).filter(HKLecture.lecture_id == lecture_id).first()
    lecture_in_db = LectureInDB()
    lecture_in_db.lecture_id = lecture.lecture_id
    lecture_in_db.title = lecture.title
    lecture_in_db.lecturer = lecture.lecturer
    lecture_in_db.running_time = lecture.course_hours
    lecture_in_db.difficulty = lecture.difficulty
    lecture_in_db.original_price = lecture.price
    lecture_in_db.current_price = lecture.discount_price
    lecture_in_db.introduction = lecture.introduction
    lecture_in_db.link = lecture.link

    # HKReview에서 lecture_id가 lecture.lecture_id인 것들을 모두 가져온다.
    reviews = db.query(HKReview).filter(HKReview.lecture_id == lecture.lecture_id).all()

    # rating은 reviews의 star의 평균
    total_star = 0
    for review in reviews:
        total_star += review.star
    lecture_in_db.rating = total_star / len(reviews)

    # review_amount는 reviews의 개수
    lecture_in_db.review_amount = len(reviews)

    # review는 reviews의 정보를 담은 리스트
    lecture_in_db.review = []
    for review in reviews:
        lecture_in_db.review.append(Review(review_id = review.review_id, star = review.star, good_review = review.good_review, bad_review = review.bad_review, created_at = review.created_at, user_id = review.user_id, user_name = review.user.user_name))

    # platform은 company_name
    lecture_in_db.platform = lecture.company.company_name

    # stack는 lecture_stacks의 stack_name들을 모두 가져온다.
    stacks = db.query(HKLectureStack).filter(HKLectureStack.lecture_id == lecture.lecture_id).all()
    lecture_in_db.stack = []
    for stack in stacks:
        lecture_in_db.stack.append(stack.stack_category.stack_name)

    return lecture_in_db