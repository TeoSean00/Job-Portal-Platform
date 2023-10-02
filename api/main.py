from fastapi import FastAPI
from .routers import staff, roles, skills
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
import datetime as dt
from enum import Enum, auto

from fastapi import HTTPException, Query

# Import database services
import database.services as db_services # This is for npm run dev

app = FastAPI()

# CORS policy for backend to interact with the frontend
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "https://is-212-spm.vercel.app",
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
