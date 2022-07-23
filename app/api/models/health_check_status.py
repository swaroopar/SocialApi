from pydantic import BaseModel


class HealthCheckStatus(BaseModel):
    is_server_running: bool
