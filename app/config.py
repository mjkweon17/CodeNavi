from dotenv import load_dotenv
import os
from pydantic_settings  import BaseSettings

load_dotenv() # take environment variables from .env.

# database
class DB_Settings(BaseSettings):
    db_db: str = os.getenv("DB_DB")
    db_host: str = os.getenv("DB_HOST")
    db_password: str = os.getenv("DB_PASSWORD")
    db_port: int = int(os.getenv("DB_PORT"))
    db_user: str = os.getenv("DB_USER")