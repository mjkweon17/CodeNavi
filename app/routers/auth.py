from typing import Annotated

from fastapi import APIRouter, Depends, Response, Request, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials


from database import get_db
from models import HKUser


security = HTTPBasic()

router = APIRouter()

router = APIRouter(previx="/users", tags=["users"], responses={404: {"description": "Not found"}})


@app.get("/users/me")
def read_current_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    return {"username": credentials.username, "password": credentials.password} 