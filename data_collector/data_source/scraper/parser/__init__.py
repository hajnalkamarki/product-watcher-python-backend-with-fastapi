import re
from abc import ABC, abstractmethod
from typing import List

from bs4 import BeautifulSoup

from data_collector.data_source.common.data_source_types import DataSourceType
from data_collector.data_source.schemas.product import Product


class Parser(ABC):
    def __init__(
        self,
        html_content: str,
        ds_type: DataSourceType,
        first_only: bool = False,
    ) -> None:
        self.soup = BeautifulSoup(html_content, "html.parser")
        self.type = ds_type
        self.first_only = first_only

    @abstractmethod
    def parse(self) -> List[Product]:
        raise NotImplementedError()

    @classmethod
    def _get_currency(cls, price: str) -> str:
        matches = re.match(r"(\D*)[\d\,\.]+(\D*)", price).groups()

        return (matches[0] or matches[1]).strip()
