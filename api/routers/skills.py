from fastapi import APIRouter

router = APIRouter(
  prefix = "/skill",
  tags = ["Skill"],
)


@router.get("/")
def default_message():
    return {"skill router endpoints, refer to staff router endpoints for template!"}