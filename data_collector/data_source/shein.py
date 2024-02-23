from typing import List

from . import DataSource
from .common.product import Product


class SheinDataSource(DataSource):
    def __init__(self, base_url: str) -> None:

        super().__init__(base_url=base_url)

    def _fetch(self) -> object:
        return []

    def _parse(self) -> Product:
        return []

    def get_data(self) -> List[Product]:
        return []
