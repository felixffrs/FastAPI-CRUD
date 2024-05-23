import typing as t

from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.security.http import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel
from starlette import status
from config import API_TOKEN

get_bearer_token = HTTPBearer(auto_error=False)

class UnauthorizedMessage(BaseModel):
    detail: str = "Bearer token missing or unknown"

async def get_token(
    auth: t.Optional[HTTPAuthorizationCredentials] = Depends(get_bearer_token),
) -> str:

    if auth is None or (token := auth.credentials) != API_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=UnauthorizedMessage().detail,
        )
    return token