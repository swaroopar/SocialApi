from fastapi import FastAPI, Security
import uvicorn

from api.routers import health_check_router, login_router
from app.api.authentication.jwt_decode import get_current_user
from logger_config import setup_log_config

setup_log_config()

app = FastAPI()

app.include_router(router=health_check_router.router, dependencies=[Security(get_current_user, scopes=[])])
app.include_router(login_router.router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8080)
