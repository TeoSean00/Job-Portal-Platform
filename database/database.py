from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

AWS_RDS_MYSQL_URL = os.getenv("AWS_RDS_MYSQL_URL")

engine = create_engine(
    AWS_RDS_MYSQL_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()