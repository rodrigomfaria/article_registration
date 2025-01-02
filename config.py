from dotenv import load_dotenv
import os

load_dotenv()

API_V1_STR = os.getenv("API_V1_STR")
DB_URL = os.getenv("DB_URL")
JWT_SECRET = os.getenv("JWT_SECRET")
ALGORITHM = os.getenv("ALGORITHM")
