from fastapi import APIRouter
from endpoints import home_page

router = APIRouter()

router.include_router(home_page.router, tags=["Home page"])

