from typing import Dict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import database services
import database.services as db_services  # This is for npm run dev

from .routers import roles, skills, staff

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


@app.get("/healthcheck", response_model=Dict[str, str])
async def healthcheck():
    """
    ### Description:
    This endpoint connects to the backend and database and provides a status.

    ### Returns:
    Status code 200 if successfully connected to backend.
    Database connection will be reflected in string.

    ### Example:
    #### Request:
    ```
    GET/healthcheck
    ```
    #### Response:
    ```
    {
        "fastapi": "Successfully connected to FastAPI!",
        "database": "Database connection successful!"
    }
    ```
    ### Errors:
    `500 Internal Server Error`: Generic server error.
    """
    db_status = db_services.healthcheck()
    if db_status:
        msg = "Database connection successful!"
    else:
        msg = "Database connection failed!"
    return {"fastapi": "Successfully connected to FastAPI!", "database": msg}
