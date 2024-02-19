import json
from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict


class DataSourceType(Enum):
    SHEIN = "shein"


class DataSourceConfig:
    def __init__(self, ds_type: DataSourceType):
        self._set_type(ds_type=ds_type)
        self._set_config()

    def _set_type(self, ds_type: DataSourceType):
        self.type = ds_type

    def _set_config(self):
        self.config = json.load(
            open(f"config/{self.type.value}.json"),
        )


class DataSource(ABC):
    @abstractmethod
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def _set_url(self, params: Dict) -> None:
        self.url = self.base_url.format(**params)
