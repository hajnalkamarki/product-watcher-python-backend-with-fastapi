from typing import Sequence

from data_collector.data_source.scraper import DataSource, DataSourceType
from data_collector.data_source.scraper.shein import SheinDataSource

DATA_SOURCE_CLASSES: Sequence[DataSource] = (SheinDataSource,)


def get_data_source(
    data_source_type: DataSourceType,
) -> DataSource:
    for ds_class in DATA_SOURCE_CLASSES:
        if ds_class.get_data_source_type() == data_source_type:
            return ds_class

    raise NotImplementedError("Unknown data source!")
