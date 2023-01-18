from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, HTTPBearer

api_keys = [
    "fks4859s58r9498hgn"
]

bearer_scheme = HTTPBearer()

def api_key_auth(api_key: str = Depends(bearer_scheme)):
    if api_key not in api_keys:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Forbidden"
        )