from fastapi import FastAPI
from api.routers import staff, roles, skills
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

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

@app.get("/")
def default_message():
    return {"add /docs at end of the URL to see swagger ui documentation"}