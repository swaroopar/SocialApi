from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session

from api_practice.schemas import Login
from api_practice.database import get_db
from api_practice.models import UserModel
from api_practice.hashing import Hash
from api_practice.tokens import create_access_token

router = APIRouter(
    tags=['Authentication'],
    prefix='/social_api'
)


@router.post('/login', status_code=status.HTTP_200_OK)
def check_credentials(request: Login, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.email_id == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid Username')
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid Password')

    access_token = create_access_token(data={"sub": user.email_id})
    return {"access_token": access_token, "token_type": "bearer"}
