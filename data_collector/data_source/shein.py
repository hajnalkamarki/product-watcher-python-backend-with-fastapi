from typing import List

from data_collector.data_source.database.models import Product

from . import DataSource


class SheinDataSource(DataSource):
    def __init__(self, base_url: str) -> None:

        super().__init__(base_url=base_url)

    def _fetch(self) -> object:
        return []

    def _parse(self) -> Product:
        return []

    def get_data(self) -> List[Product]:
        return []
