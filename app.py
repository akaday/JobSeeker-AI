from fastapi import FastAPI
from endpoints import router as jobs_router

app = FastAPI()

app.include_router(jobs_router, prefix="/api")
