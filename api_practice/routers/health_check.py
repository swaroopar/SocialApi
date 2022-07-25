from fastapi import APIRouter, status

from api_practice.schemas import HealthCheckStatus
from api_practice.log import LoggerConfig

router = APIRouter(
    tags=['Health_Check'],
    prefix='/social_api'
)
msg_log = LoggerConfig()


@router.get('/health_check', status_code=status.HTTP_200_OK)
def health_check():
    HealthCheckStatus.is_server_running = True
    msg_log.logger.info('Request: GET localhost:8000/healthcheck')
    msg_log.logger.info('Response: Server is Up and Running')
    return HealthCheckStatus.is_server_running
