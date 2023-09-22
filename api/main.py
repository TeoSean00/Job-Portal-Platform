from fastapi import HTTPException, Depends, FastAPI
from sqlalchemy.orm import Session

# Import your SQLAlchemy models here

app = FastAPI()

# Function to get SQLAlchemy session
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

# Create
@app.post("/staff_details/")
def create_staff_details(fname: str, lname: str, dept: str, email: str, phone: str, biz_address: str, sys_role: str, db: Session = Depends(get_session)):
    staff = StaffDetails(fname=fname, lname=lname, dept=dept, email=email, phone=phone, biz_address=biz_address, sys_role=sys_role)
    db.add(staff)
    db.commit()
    db.refresh(staff)
    return staff

# Read
@app.get("/staff_details/{staff_id}")
def get_staff_details(staff_id: int, db: Session = Depends(get_session)):
    staff = db.query(StaffDetails).filter(StaffDetails.staff_id == staff_id).first()
    if staff is None:
        raise HTTPException(status_code=404, detail="Staff not found")
    return staff

# Update
@app.put("/staff_details/{staff_id}")
def update_staff_details(staff_id: int, new_dept: str, db: Session = Depends(get_session)):
    staff = db.query(StaffDetails).filter(StaffDetails.staff_id == staff_id).first()
    if staff:
        staff.dept = new_dept
        db.commit()
        return {"message": "Staff details updated successfully"}
    raise HTTPException(status_code=404, detail="Staff not found")

# Delete
@app.delete("/staff_details/{staff_id}")
def delete_staff_details(staff_id: int, db: Session = Depends(get_session)):
    staff = db.query(StaffDetails).filter(StaffDetails.staff_id == staff_id).first()
    if staff:
        db.delete(staff)
        db.commit()
        return {"message": "Staff deleted successfully"}
    raise HTTPException(status_code=404, detail="Staff not found")

