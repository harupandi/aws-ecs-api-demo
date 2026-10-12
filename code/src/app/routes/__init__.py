from fastapi import APIRouter, HTTPException
from . import transactions, users

api_router = APIRouter(prefix="/api", tags=["api"])

api_router.include_router(users.router)
api_router.include_router(transactions.router)

