from typing import Dict, List

import requests

from data_collector.data_source.common.data_source_types import DataSourceType
from data_collector.data_source.scraper import DataSource
from data_collector.data_source.scraper.parser.book_store import (
    BookStoreParser,
)


class BookStoreDataSource(DataSource):
    def __init__(self, first_only: bool = False) -> None:
        super().__init__(first_only=first_only)

    def _fetch(self, params: Dict) -> None:
        super()._fetch(params=params)

        # TODO: error handling
        resp = requests.get(url=self.url)

        self.data = resp.text

    def _parse(self, **kwargs) -> None:
        super()._parse(parser_cls=BookStoreParser)

    @classmethod
    def get_data_source_type(cls) -> DataSourceType:
        return DataSourceType.BOOK_STORE

    def get_number_of_pages(self) -> str:
        raise NotImplementedError()

    def get_data(
        self,
        params: Dict = None,
    ) -> List[object]:
        self.results = list()
        self._fetch(params={"search_expr": "1"})
        self._parse()

        print(self.results)  # TODO: remove

        return self.results
