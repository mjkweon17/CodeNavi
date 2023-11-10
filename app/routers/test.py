from fastapi import APIRouter, Depends, Response, Request, status
from sqlalchemy.orm import Session

from database import get_db
from models import HKUser

router = APIRouter(prefix="/test", tags=["test"], responses={404: {"description": "Not found"}})

# test 핸들러
@router.get("/")
async def get_users(db: Session = Depends(get_db)):
    users = db.query(HKUser).all()
    return users