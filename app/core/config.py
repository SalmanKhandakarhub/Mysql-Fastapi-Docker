import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL", "mysql+aiomysql://root:ows1234@mysqldb/BigFast_db")
    SECRET_KEY = os.getenv("SECRET_KEY", "gAfziUeqRfi4xFTlb7R4tieOcWLk3TKUpF37Zfv1Wdk=")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    class Config:
        env_file = ".env"

settings = Settings()