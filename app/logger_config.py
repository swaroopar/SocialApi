import logging
from typing import Callable

from fastapi import Request, Response

from fastapi.routing import APIRoute

logger = logging.getLogger(__name__)


def setup_log_config():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s : %(levelname)-8s : [%(filename)s : %(lineno)d] : %(message)s'
    )


class LogRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            logger.info(f'Received {request.method} {request.url.path}')
            response: Response = await original_route_handler(request)
            logger.info(f'Returning HTTP {response.status_code} {response.body}')
            return response

        return custom_route_handler
