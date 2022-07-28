from fastapi import APIRouter, Depends
import requests

from api.models.user import User
from jwt_decode import get_current_user

router = APIRouter(
    tags=['ISSPosition'],
    prefix='/social_api'
)


@router.get('/iss_position')
def get_iss_position(current_user: User = Depends(get_current_user)):
    iss_position = requests.get('http://api.open-notify.org/iss-now.json')
    iss_position = iss_position.json()
    return iss_position['iss_position']