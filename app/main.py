from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from app.schemas.common import ApiResponse
from app.routes.image_route import router as image_route

import logging

app = FastAPI()

origins = [
    "https://primary-production-b57a.up.railway.app",
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(image_route)

logger = logging.getLogger(__name__)