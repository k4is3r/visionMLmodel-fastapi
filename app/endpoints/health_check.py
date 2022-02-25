from fastapi import APIRouter

router = APIRouter()

@router.get("/health-check",
            name="Health Check",
            description="Api health check endpoint")
async def healt_check():
    """Endpoint for test API status"""
    return {"message":"API is activate"}

