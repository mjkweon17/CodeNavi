from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'HKUser'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    github_id = Column(String(255), nullable=True)
    blog_link = Column(String(255), nullable=True)

class Company(Base):
    __tablename__ = 'HKCompany'

    company_id = Column(Integer, primary_key=True, autoincrement=True)
    company_name = Column(String(255), nullable=False)

class Lecture(Base):
    __tablename__ = 'HKLecture'

    lecture_id = Column(Integer, primary_key=True, autoincrement=True)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    language = Column(String(255), nullable=False, default='korean')
    title = Column(String(255), nullable=False)
    thumbnail = Column(String(255))
    lecturer = Column(String(255), nullable=False)
    course_hours = Column(String(255))
    difficulty = Column(String(255))
    company_id = Column(Integer, ForeignKey('HKCompany.company_id'), nullable=False)
    price = Column(String(255))
    discount_rate = Column(String(255))
    introduction = Column(Text)

    company = relationship('HKCompany', back_populates='lectures')

class Review(Base):
    __tablename__ = 'HKReview'

    review_id = Column(Integer, primary_key=True, autoincrement=True)
    lecture_id = Column(Integer, ForeignKey('HKLecture.lecture_id'), nullable=False)
    user_id = Column(Integer, ForeignKey('HKUser.user_id'), nullable=False)
    star = Column(Integer, nullable=False)
    good_review = Column(Text, nullable=False)
    bad_review = Column(Text, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    lecture = relationship('HKLecture', back_populates='reviews')
    user = relationship('HKUser', back_populates='reviews')

class Bookmark(Base):
    __tablename__ = 'HKBookmark'

    bookmark_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('HKUser.user_id'), nullable=False)
    lecture_id = Column(Integer, ForeignKey('HKLecture.lecture_id'), nullable=False)

    user = relationship('HKUser', back_populates='bookmarks')
    lecture = relationship('HKLecture', back_populates='bookmarks')

class StackCategory(Base):
    __tablename__ = 'HKSTACK_CATEGORY'

    stack_category_id = Column(Integer, primary_key=True, autoincrement=True)
    parent_id = Column(Integer, ForeignKey('HKSTACK_CATEGORY.stack_category_id'))
    stack_name = Column(Integer, nullable=False)

    parent = relationship('HKSTACK_CATEGORY', remote_side=[stack_category_id], back_populates='children')
    children = relationship('HKSTACK_CATEGORY')

class LectureStack(Base):
    __tablename__ = 'HKLectureStack'

    lecture_stack_id = Column(Integer, primary_key=True, autoincrement=True)
    stack_category_id = Column(Integer, ForeignKey('HKSTACK_CATEGORY.stack_category_id'), nullable=False)
    lecture_id = Column(Integer, ForeignKey('HKLecture.lecture_id'), nullable=False)

    stack_category = relationship('HKSTACK_CATEGORY', back_populates='lecture_stacks')
    lecture = relationship('HKLecture', back_populates='lecture_stacks')

class UserStack(Base):
    __tablename__ = 'HKUserStack'

    user_stack_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('HKUser.user_id'), nullable=False)
    stack_category_id = Column(Integer, ForeignKey('HKSTACK_CATEGORY.stack_category_id'), nullable=False)

    user = relationship('HKUser', back_populates='user_stacks')
    stack_category = relationship('HKSTACK_CATEGORY', back_populates='user_stacks')

class Board(Base):
    __tablename__ = 'HKBoard'

    board_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('HKUser.user_id'), nullable=False)
    title = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    is_active = Column(Boolean, nullable=False, default=True)
    content = Column(Text, nullable=False)

    user = relationship('HKUser', back_populates='boards')

# Define relationships
Company.lectures = relationship('HKLecture', back_populates='company')
Lecture.reviews = relationship('HKReview', back_populates='lecture')
User.reviews = relationship('HKReview', back_populates='user')
User.bookmarks = relationship('HKBookmark', back_populates='user')
StackCategory.lecture_stacks = relationship('HKLectureStack', back_populates='stack_category')
StackCategory.user_stacks = relationship('HKUserStack', back_populates='stack_category')
User.boards = relationship('HKBoard', back_populates='user')

# 사용할 때는 각 클래스를 사용하여 데이터베이스 쿼리를 수행할 수 있습니다.
# 예를 들어, 사용자를 생성하려면:
# user = HKUser(password='password123', github_id='your_github_id', blog_link='your_blog_link')
# session.add(user)
# session.commit()