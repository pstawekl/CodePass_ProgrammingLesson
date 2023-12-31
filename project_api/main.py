"""
    Project API

    API for config.json in project
"""


from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import uvicorn

from .apis.object_api import router as ObjectApiRouter

app = FastAPI(
    title="Project API",
    description="API for config.json in project",
    version="0.1.9",
)


origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ObjectApiRouter)

uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")