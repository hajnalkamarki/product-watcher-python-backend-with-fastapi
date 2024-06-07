import json
import os

from schemas.config import AppConfig


class ConfigParser:
    @classmethod
    def load_app_config(cls, path: str, env: str) -> AppConfig:
        return AppConfig(**json.load(open(f"{os.getcwd()}/{path}/{env}.json")))
