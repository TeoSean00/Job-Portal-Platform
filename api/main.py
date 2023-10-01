from fastapi import FastAPI
from .routers import staff, roles, skills

app = FastAPI()

# Backend entry point for all routers based on their high-level functions
app.include_router(staff.router)
app.include_router(roles.router)
app.include_router(skills.router)


@app.get("/")
def default_message():
    return {"add /docs at end of the URL to see swagger ui documemtation"}