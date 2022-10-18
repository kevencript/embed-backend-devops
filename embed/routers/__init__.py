from fastapi import APIRouter

from embed.routers.v1.vegs import router as vegs_api
from embed.routers.v1.auth import router as auth_api

router = APIRouter()

router.include_router(vegs_api, prefix="/vegs", tags=["vegetables"])
router.include_router(auth_api, prefix="/auth", tags=["Auth"])
