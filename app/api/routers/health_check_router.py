import logging
from typing import Callable
from fastapi import APIRouter, Request, Response
from fastapi.routing import APIRoute

from api.models.health_check_status import HealthCheckStatus


logger = logging.getLogger(__name__)


class LogRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            req = request.method, request.url
            logger.info(req)
            response: Response = await original_route_handler(request)
            resp = response.body, response.status_code
            logger.info(resp)
            return response

        return custom_route_handler


router = APIRouter(
    route_class=LogRoute,
    prefix='/social_api',
    tags=['healthCheck']
)


@router.get('/health_check', response_model=HealthCheckStatus)
def health_check():
    logger.info('Server Health Check')
    return HealthCheckStatus(is_server_running=True)
