from fastapi import APIRouter

router = APIRouter(
  prefix = "/role",
  tags = ["Role"],
)


@router.get("/")
def default_message():
    return {"role router endpoints, refer to staff router endpoints for template!"}