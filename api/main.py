import datetime as dt

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Import database services
import api.database.services as db_services  # This is for npm run dev

from .routers import roles, skills, staff

# from enum import Enum, auto


app = FastAPI()

# CORS policy for backend to interact with the frontend
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "https://is-212-spm.vercel.app",
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Backend entry point for all routers based on their high-level functions
app.include_router(staff.router)
app.include_router(roles.router)
app.include_router(skills.router)


@app.get("/healthcheck", response_model=dict)
async def healthcheck():
    db_status = db_services.healthcheck()
    if db_status:
        msg = "Database connection successful!"
    else:
        msg = "Database connection failed!"
    return {"fastapi": "Successfully connected to FastAPI!", "database": msg}
