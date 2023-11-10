from fastapi import APIRouter, Depends, Response, Request, status
from sqlalchemy.orm import Session

from database import get_db
# from models import User

router = APIRouter(prefix="/lecutres", tags=["lecutres"], responses={404: {"description": "Not found"}})

# lectures handler

