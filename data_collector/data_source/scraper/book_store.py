from typing import List

from data_collector.data_source.common.data_source_types import DataSourceType
from data_collector.data_source.scraper import DataSource
from data_collector.data_source.scraper.parser.book_store import BookStoreParser


class BookStoreDataSource(DataSource):
    def __init__(self) -> None:
        super().__init__()

    def _parse(self) -> object:
        return []

    @classmethod
    def get_data_source_type(cls) -> DataSourceType:
        return DataSourceType.BOOK_STORE

    def get_data(self) -> List[object]:
        # TODO: search_expr should be an input param
        data = self._fetch(params={"search_expr": ""})
        BookStoreParser(html_content=data).parse()
        return []
