from fastapi import APIRouter

from app.api.models.health_check_status import HealthCheckStatus

from app.logger_config import logger, LogRoute

router = APIRouter(
    route_class=LogRoute,
    prefix='/social_api',
    tags=['healthCheck']
)


@router.get('/health_check', response_model=HealthCheckStatus)
async def health_check():
    logger.info('Server Health Check')
    return HealthCheckStatus(is_server_running=True)
