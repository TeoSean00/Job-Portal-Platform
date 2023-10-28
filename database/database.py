import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

AWS_RDS_MYSQL_URL = os.getenv("AWS_RDS_MYSQL_URL")

engine = create_engine(AWS_RDS_MYSQL_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
