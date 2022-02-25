from fastapi import APIRouter
from endpoints import home_page, health_check

router = APIRouter()

router.include_router(home_page.router, tags=["Home page"])
router.include_router(health_check.router, tags=["Health Check"])

