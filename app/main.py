# import os

import uvicorn
from common.config_parser import ConfigParser
from fastapi import FastAPI, Request
from schemas.config import AppConfig

ENV_ENVIRONMENT = "dev"  # os.getenv("APP_ENV")
ENV_APP_CFG_PATH = "app/config/"  # os.getenv("APP_CFG_PATH")


app = FastAPI()
cfg: AppConfig = ConfigParser.load_app_config(
    path=ENV_APP_CFG_PATH,
    env=ENV_ENVIRONMENT,
)


@app.get("/")
async def root(request: Request):
    return {"message": "Hello World"}


@app.get("/test")
async def test():
    return {"message": "Test endpoint"}


if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host="127.0.0.1",
        port=8000,
    )
