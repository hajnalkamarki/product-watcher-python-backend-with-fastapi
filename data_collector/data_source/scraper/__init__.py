import json
import os
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, List

import requests

from ..common.data_source_types import DataSourceType

CONFIG_PATH = "data_collector/data_source/scraper/config"


@dataclass(kw_only=True)
class DataSourceConfig:
    base_url: str

    @staticmethod
    def get_config(ds_type: DataSourceType):
        return json.load(
            open(f"{os.getcwd()}/{CONFIG_PATH}/{ds_type.value}.json"),
        )


class DataSource(ABC):
    def __init__(self) -> None:
        self.config = DataSourceConfig(
            **DataSourceConfig.get_config(
                ds_type=self.get_data_source_type(),
            )
        )

    def _set_url(self, params: Dict) -> None:
        self.url = self.config.base_url.format(**params)

    def _fetch(self, params: Dict) -> str:
        self._set_url(params=params)

        # TODO: error handling
        resp = requests.get(url=self.url)

        return resp.text

    @abstractmethod
    def _parse(self) -> object:
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def get_data_source_type() -> DataSourceType:
        raise NotImplementedError()

    @abstractmethod
    def get_data(self) -> List[object]:
        raise NotImplementedError()
