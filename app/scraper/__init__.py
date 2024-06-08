import json
import os
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, List, Optional

from app.schemas.product import Product

from ..common.data_source_types import DataSourceType

CONFIG_PATH = "app/scraper/config"


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
        self.data: str = ""
        self.results: List = list()
        self.type: DataSourceType = self.get_data_source_type()
        self.first_only: bool = first_only
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
        params: Optional[Dict] = None,
    ) -> List[Product]:
        raise NotImplementedError()
