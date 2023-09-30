from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import pytest
import os


@pytest.fixture(scope="module")
def engine():
    load_dotenv()
    AWS_RDS_MYSQL_URL = os.environ.get("AWS_RDS_MYSQL_URL")
    print("AWS_RDS_MYSQL_URL:", AWS_RDS_MYSQL_URL)
    return create_engine(AWS_RDS_MYSQL_URL)

@pytest.fixture(scope="module")
def session(engine):
    # Create a session
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal()


def test_database_connection(engine):
    # Check if the engine is connected
    assert engine.connect()

def test_session_creation(session):
    # Check if a session is created
    assert session

if __name__ == '__main__':
    pytest.main()
