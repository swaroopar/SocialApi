from fastapi import FastAPI
import uvicorn

from api.routers import health_check_router, iss_position_router, login_router
from logger_config import setup_log_config

setup_log_config()

app = FastAPI()

app.include_router(health_check_router.router)
app.include_router(login_router.router)
app.include_router(iss_position_router.router)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8080)
