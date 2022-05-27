import os
from datetime import timedelta

from dotenv import load_dotenv

load_dotenv("local.env")

DATABASE_URL: str = os.getenv("DATABASE_URL")