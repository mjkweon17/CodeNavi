from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class HKUser(Base):
    __tablename__ = 'HKUser'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    password = Column(String(255), nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime, nullable=False)
    github_id = Column(String(255), nullable=False)
    blog_link = Column(String(255), nullable=False)

class HKCompany(Base):
    __tablename__ = 'HKCompany'
    company_id = Column(Integer, primary_key=True, autoincrement=True)
    company_name = Column(String(255), nullable=False)

class HKLecture(Base):
    __tablename__ = 'HKLecture'
    lecture_id = Column(Integer, primary_key=True, autoincrement=True)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime, nullable=False)
    language = Column(String(255), nullable=False, default='korean')
    title = Column(String(255), nullable=False)
    thumbnail = Column(String(255), nullable=True)
    lecturer = Column(String(255), nullable=False)
    course_hours = Column(String(255), nullable=True)
    difficulty = Column(String(255), nullable=True)
    company_id = Column(Integer, ForeignKey('HKCompany.company_id'), nullable=False)
    price = Column(String(255), nullable=True)
    discount_rate = Column(String(255), nullable=True)
    introduction = Column(Text, nullable=True)
    company = relationship('HKCompany', back_populates='lectures')

class HKReview(Base):
    __tablename__ = 'HKReview'
    review_id = Column(Integer, primary_key=True, autoincrement=True)
    lecture_id = Column(Integer, ForeignKey('HKLecture.lecture_id'), nullable=False)
    user_id = Column(Integer, ForeignKey('HKUser.user_id'), nullable=False)
    star = Column(Integer, nullable=False)
    good_review = Column(Text, nullable=False)
    bad_review = Column(Text, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime, nullable=False)
    lecture = relationship('HKLecture', back_populates='reviews')
    user = relationship('HKUser', back_populates='reviews')

class HKBookmark(Base):
    __tablename__ = 'HKBookmark'
    bookmark_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('HKUser.user_id'), nullable=False)
    lecture_id = Column(Integer, ForeignKey('HKLecture.lecture_id'), nullable=False)
    user = relationship('HKUser', back_populates='bookmarks')
    lecture = relationship('HKLecture', back_populates='bookmarks')

class HKStackCategory(Base):
    __tablename__ = 'HKStackCategory'
    stack_category_id = Column(Integer, primary_key=True, autoincrement=True)
    parent_id = Column(Integer, ForeignKey('HKStackCategory.stack_category_id'), nullable=True)
    stack_name = Column(Integer, nullable=False)
    parent = relationship('HKStackCategory', remote_side=[stack_category_id])

class HKLectureStack(Base):
    __tablename__ = 'HKLectureStack'
    lecture_stack_id = Column(Integer, primary_key=True, autoincrement=True)
    stack_category_id = Column(Integer, ForeignKey('HKStackCategory.stack_category_id'), nullable=False)
    lecture_id = Column(Integer, ForeignKey('HKLecture.lecture_id'), nullable=False)
    stack_category = relationship('HKStackCategory', back_populates='lecture_stacks')
    lecture = relationship('HKLecture', back_populates='lecture_stacks')

class HKUserStack(Base):
    __tablename__ = 'HKUserStack'
    user_stack_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('HKUser.user_id'), nullable=False)
    stack_category_id = Column(Integer, ForeignKey('HKStackCategory.stack_category_id'), nullable=False)
    user = relationship('HKUser', back_populates='user_stacks')
    stack_category = relationship('HKStackCategory', back_populates='user_stacks')

class HKBoard(Base):
    __tablename__ = 'HKBoard'
    board_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('HKUser.user_id'), nullable=False)
    title = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    content = Column(Text, nullable=False)
    user = relationship('HKUser', back_populates='boards')

# Set up relationships
HKCompany.lectures = relationship('HKLecture', back_populates='company')
HKLecture.reviews = relationship('HKReview', back_populates='lecture')
HKUser.reviews = relationship('HKReview', back_populates='user')
HKUser.bookmarks = relationship('HKBookmark', back_populates='user')
HKStackCategory.lecture_stacks = relationship('HKLectureStack', back_populates='stack_category')
HKStackCategory.user_stacks = relationship('HKUserStack', back_populates='stack_category')
HKUser.boards = relationship('HKBoard', back_populates='user')
