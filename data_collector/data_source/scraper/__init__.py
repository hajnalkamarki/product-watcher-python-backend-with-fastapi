import json
import os
from abc import ABC, abstractmethod
from dataclasses import dataclass
from types import MappingProxyType
from typing import Dict, List, Type

from data_collector.data_source.scraper.parser import Parser

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
    def __init__(self, first_only: bool = False) -> None:
        self.data = ""
        self.results = list()
        self.type = self.get_data_source_type()
        self.first_only = first_only
        self.config = DataSourceConfig(
            **DataSourceConfig.get_config(
                ds_type=self.type,
            )
        )

    def _set_url(self, params: Dict) -> None:
        self.url = self.config.base_url.format(**params)

    def _fetch(self, params: Dict) -> None:
        self._set_url(params=params)

    def _parse(self, **kwargs) -> None:
        self.results += kwargs["parser_cls"](
            html_content=self.data,
            ds_type=self.type,
            first_only=self.first_only,
        ).parse()

    @staticmethod
    @abstractmethod
    def get_data_source_type() -> DataSourceType:
        raise NotImplementedError()

    @abstractmethod
    def get_number_of_pages(self) -> str:
        raise NotImplementedError()

    @abstractmethod
    def get_data(
        self,
        params: Dict = MappingProxyType({}),
    ) -> List[object]:
        raise NotImplementedError()
