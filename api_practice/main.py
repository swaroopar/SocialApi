from fastapi import FastAPI
import uvicorn

from api_practice import models
from api_practice.database import engine
from api_practice.routers import users, authenticate, health_check

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(users.router)
app.include_router(authenticate.router)
app.include_router(health_check.router)

if __name__ == '__main__':
    uvicorn.run(app)
