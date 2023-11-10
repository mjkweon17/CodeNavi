from typing import Annotated, List
from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, Response, Request, HTTPException, status, Query
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session
from pydantic import BaseModel

from database import get_db
from models import HKLecture, HKReview, HKCompany, HKLectureStack

router = APIRouter(prefix="/lecture", tags=["lectures"], responses={404: {"description": "Not found"}})


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
    thumbnail: str | None = None
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
    stacks: str | None = None # 계산 필요
    keyword: str | None = None # keyword
    review_amount : int | None = None # 계산 필요
    review: List[Review] | None = None # 계산 필요


# 강의 목록 조회
# Response: List[LectureInDB]
@router.get("/")
async def get_lectures(db: Session = Depends(get_db)):
    lectures = db.query(HKLecture).all()
    lecture_list = []
    for lecture in lectures:
        lecture_in_db = LectureInDB()
        lecture_in_db.lecture_id = lecture.lecture_id
        lecture_in_db.title = lecture.title
        lecture_in_db.lecturer = lecture.lecturer
        lecture_in_db.thumbnail = lecture.thumbnail
        lecture_in_db.running_time = lecture.course_hours
        lecture_in_db.difficulty = lecture.difficulty
        lecture_in_db.original_price = lecture.price
        lecture_in_db.current_price = lecture.discount_price
        lecture_in_db.introduction = lecture.introduction
        lecture_in_db.link = lecture.link
        lecture_in_db.keyword = lecture.keyword
        lecture_in_db.stacks = lecture.stacks

        # HKReview에서 lecture_id가 lecture.lecture_id인 것들을 모두 가져온다.
        reviews = db.query(HKReview).filter(HKReview.lecture_id == lecture.lecture_id).all()

        # rating은 reviews의 star의 평균
        total_star = 0
        for review in reviews:
            total_star += review.star
        if(len(reviews) == 0):
            lecture_in_db.rating = 0
        else:
            lecture_in_db.rating = total_star / len(reviews)

        # review_amount는 reviews의 개수
        lecture_in_db.review_amount = len(reviews)

        # review는 reviews의 정보를 담은 리스트
        lecture_in_db.review = []
        for review in reviews:
            lecture_in_db.review.append(Review(review_id = review.review_id, star = review.star, good_review = review.good_review, bad_review = review.bad_review, created_at = review.created_at, user_id = review.user_id, user_name = review.user.user_name))

        # platform은 company_name
        lecture_in_db.platform = lecture.company.company_name

        lecture_list.append(lecture_in_db)

    return lecture_list

# 전체 강의 10개씩 조회
# Request: page
# Response: List[LectureInDB]
@router.get("/{page}")
async def get_lectures(page: int, db: Session = Depends(get_db)):
    lectures = db.query(HKLecture).limit(10).offset((page-1)*10).all()
    lecture_list = []
    for lecture in lectures:
        lecture_in_db = LectureInDB()
        lecture_in_db.lecture_id = lecture.lecture_id
        lecture_in_db.title = lecture.title
        lecture_in_db.lecturer = lecture.lecturer
        lecture_in_db.running_time = lecture.course_hours
        lecture_in_db.thumbnail = lecture.thumbnail
        lecture_in_db.difficulty = lecture.difficulty
        lecture_in_db.original_price = lecture.price
        lecture_in_db.current_price = lecture.discount_price
        lecture_in_db.introduction = lecture.introduction
        lecture_in_db.link = lecture.link
        lecture_in_db.keyword = lecture.keyword
        lecture_in_db.stacks = lecture.stacks

        # HKReview에서 lecture_id가 lecture.lecture_id인 것들을 모두 가져온다.
        reviews = db.query(HKReview).filter(HKReview.lecture_id == lecture.lecture_id).all()

        # rating은 reviews의 star의 평균
        total_star = 0
        for review in reviews:
            total_star += review.star
        if(len(reviews) == 0):
            lecture_in_db.rating = 0
        else:
            lecture_in_db.rating = total_star / len(reviews)

        # review_amount는 reviews의 개수
        lecture_in_db.review_amount = len(reviews)

        # review는 reviews의 정보를 담은 리스트
        lecture_in_db.review = []
        for review in reviews:
            lecture_in_db.review.append(Review(review_id = review.review_id, star = review.star, good_review = review.good_review, bad_review = review.bad_review, created_at = review.created_at, user_id = review.user_id, user_name = review.user.user_name))

        # platform은 company_name
        lecture_in_db.platform = lecture.company.company_name

        lecture_list.append(lecture_in_db)

    return lecture_list


# 강의 목록 검색
# Request: keyword
# Response: 강의 목록
@router.get("/search/all")
async def search_lectures(keyword: str, db: Session = Depends(get_db)):
    lectures = db.query(HKLecture).filter(HKLecture.title.like('%'+keyword+'%')).all()
    return lectures

# 검색하면 20개씩만 보여주기
# Request: keyword, page
# Response: 강의 목록
@router.get("/search/{page}")
async def search_lectures(keyword: str, page: int, db: Session = Depends(get_db)):
    lectures = db.query(HKLecture).filter(HKLecture.title.like('%'+keyword+'%')).limit(20).offset((page-1)*20).all()
    return lectures


# 검색 pagination
# 필터(옵션, 여러 개 선택 가능): keyword, stack, difficulty, course_hours, price
# Request: keyword, stack, difficulty, course_hours, price
# Response: 강의 목록

'''
# Endpoint for lecture search with filters and pagination
@router.get("/search_filter", response_model=list[HKLecture])
def search_lectures(
        keyword: str = Query(None, title="Keyword filter"),
        stack: str = Query(None, title="Stack filter"),
        difficulty: str = Query(None, title="Difficulty filter"),
        course_hours: str = Query(None, title="Course Hours filter"),
        # 가격은 범위로
        price: str = Query(None, title="Price filter"),
        page: int = Query(1, title="Page number"),
        items_per_page: int = Query(10, title="Items per page"),
        db: Session = Depends(get_db)
):
    # Build a filter query based on the provided filters
    filters = []
    if keyword:
        filters.append(HKLecture.keyword.ilike(f"%{keyword}%"))
    # stack은 HKLectureStack의 stack_category의 stack_name
    if stack:
        filters.append(HKLectureStack.stack_category.has(stack_name=stack))
    if difficulty:
        filters.append(HKLecture.difficulty == difficulty)
    if course_hours:
        filters.append(HKLecture.course_hours == course_hours)
    # 가격은 범위로
    if price:
        price_range = price.split('-')
        filters.append(HKLecture.discount_price.between(price_range[0], price_range[1]))

    # Query for lectures with pagination
    lectures = (
        db.query(HKLecture)
        .filter(*filters)
        .offset((page - 1) * items_per_page)
        .limit(items_per_page)
        .all()
    )

    return lectures
'''

# 상세 강의 조회
@router.get("/detail/{lecture_id}")
async def get_lecture(lecture_id: int, db: Session = Depends(get_db)):

    lecture = db.query(HKLecture).filter(HKLecture.lecture_id == lecture_id).first()
    lecture_in_db = LectureInDB()
    lecture_in_db.lecture_id = lecture.lecture_id
    lecture_in_db.title = lecture.title
    lecture_in_db.lecturer = lecture.lecturer
    lecture_in_db.running_time = lecture.course_hours
    lecture_in_db.thumbnail = lecture.thumbnail
    lecture_in_db.difficulty = lecture.difficulty
    lecture_in_db.original_price = lecture.price
    lecture_in_db.current_price = lecture.discount_price
    lecture_in_db.introduction = lecture.introduction
    lecture_in_db.link = lecture.link
    lecture_in_db.keyword = lecture.keyword
    lecture_in_db.stacks = lecture.stacks

    # HKReview에서 lecture_id가 lecture.lecture_id인 것들을 모두 가져온다.
    reviews = db.query(HKReview).filter(HKReview.lecture_id == lecture.lecture_id).all()

    # rating은 reviews의 star의 평균

    total_star = 0
    for review in reviews:
        total_star += review.star
        total_star = 0
    if(len(reviews) == 0):
        lecture_in_db.rating = 0
    else:
        lecture_in_db.rating = total_star / len(reviews)

    # review_amount는 reviews의 개수
    lecture_in_db.review_amount = len(reviews)

    # review는 reviews의 정보를 담은 리스트
    lecture_in_db.review = []
    for review in reviews:
        lecture_in_db.review.append(Review(review_id = review.review_id, star = review.star, good_review = review.good_review, bad_review = review.bad_review, created_at = review.created_at, user_id = review.user_id, user_name = review.user.user_name))

    # platform은 company_name
    lecture_in_db.platform = lecture.company.company_name

    return lecture_in_db