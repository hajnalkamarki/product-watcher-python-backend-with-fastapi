from typing import List

import requests

from data_collector.data_source.common.data_source_types import DataSourceType
from data_collector.data_source.scraper import DataSource


class SheinDataSource(DataSource):
    def __init__(self) -> None:
        super().__init__()

    def _fetch(self) -> str:
        # TODO: search_expr should be an input param
        self._set_url(params={"search_expr": "shirt"})

        # TODO: error handling
        resp = requests.get(url=self.url)

        return resp.text

    def _parse(self) -> object:
        return []

    @classmethod
    def get_data_source_type(cls) -> DataSourceType:
        return DataSourceType.SHEIN

    def get_data(self) -> List[object]:
        data = self._fetch()
        return []
