import logging
from fastapi import APIRouter
from api.models.health_check_status import HealthCheckStatus

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix='/social_api'
)


@router.get('/health_check', response_model=HealthCheckStatus)
def health_check():
    logger.info('Health check performance')

    return HealthCheckStatus(is_server_running=True)

