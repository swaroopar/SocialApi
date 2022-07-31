from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from jose import jwt

from app.api.models.token import Token
from app.api.authentication.users import users_db

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"


router = APIRouter()


@router.post("/login", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    for user in users_db:
        if users_db[user]['email'] == form_data.username and users_db[user]['password'] == form_data.password:
            data = {'sub': form_data.username}
            access_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
            return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                        detail='Entered Wrong Username or Password')

