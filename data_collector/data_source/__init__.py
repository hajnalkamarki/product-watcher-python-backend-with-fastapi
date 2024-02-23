import json
from abc import ABC, abstractmethod
from typing import Dict, List

from .common.data_source_types import DataSourceType
from .common.product import Product


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
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def _set_url(self, params: Dict) -> None:
        self.url = self.base_url.format(**params)

    @abstractmethod
    def _fetch(self) -> object:
        raise NotImplementedError()

    @abstractmethod
    def _parse(self) -> Product:
        raise NotImplementedError()

    @abstractmethod
    def get_data(self) -> List[Product]:
        raise NotImplementedError()
