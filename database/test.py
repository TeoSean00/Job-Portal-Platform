from sqlalchemy.orm import sessionmaker
from database import engine
from models import RoleDetails  # Replace with your actual model file

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

try:
    # Query the first user (you can modify this based on your model)
    first_role = session.query(RoleDetails).first().role_name
    print("First role:", first_role)
except Exception as e:
    print("Error:", str(e))
finally:
    # Close the session
    session.close()