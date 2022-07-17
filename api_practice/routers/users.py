from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from api_practice.schemas import UserSchema, ShowUser
from api_practice.models import UserModel
from api_practice.database import get_db
from api_practice.hashing import Hash

router = APIRouter(
    prefix='/social_api',
    tags=['Users']
)


@router.post('/create_user', status_code=status.HTTP_201_CREATED, response_model=ShowUser)
def create_user(request: UserSchema, db: Session = Depends(get_db)):
    new_user = UserModel(user_name=request.user_name,
                         email_id=request.email_id, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.put('/update_user/{email_id}', status_code=status.HTTP_202_ACCEPTED)
def update_user(email_id, request: UserSchema, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.email_id == email_id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with {email_id} not found')
    user.update(vars(request))
    db.commit()
    return 'user details updated'


@router.get('/users', status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
    users = db.query(UserModel).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Records of users NOT found')
    return users
