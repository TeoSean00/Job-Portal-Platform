from fastapi import FastAPI
from pydantic import BaseModel
import pprint

app = FastAPI()

class RoleListing(BaseModel):
    role_listing_desc: str
    role_listing_open: str
    role_listing_close: str
    role_listing_creator: str


@app.get("/api/python")
def hello_world():
    return {"message": "Hello World"}

@app.post("/api/role_listing")
def create_role_listing(role_details: RoleListing):
    pprint.pprint(role_details)
    return {"message": "Created!"}