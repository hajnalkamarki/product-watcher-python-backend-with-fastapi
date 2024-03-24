from typing import Sequence, Type

from app.scraper import DataSource, DataSourceType
from app.scraper.book_store import BookStoreDataSource

DATA_SOURCE_CLASSES: Sequence[Type[DataSource]] = (BookStoreDataSource,)


def get_data_source(
    data_source_type: DataSourceType,
) -> Type[DataSource]:
    for ds_class in DATA_SOURCE_CLASSES:
        if ds_class.get_data_source_type() == data_source_type:
            return ds_class

    raise NotImplementedError("Unknown data source!")
