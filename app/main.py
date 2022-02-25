from fastapi import FastAPI
from routers import router


app = FastAPI(
        title="VisionML",
        description="Vision ML model using fastapi",
        version="0.1"
        )

app.include_router(router)
