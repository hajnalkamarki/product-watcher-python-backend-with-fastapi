from app.database import LocalSession
from app.database.models.product import Product
from app.scraper import DataSourceType
from app.services.scraper import get_data_source


def add_product(
    ds_type: DataSourceType,
    search_term: str,
    first_only: bool = False,
) -> None:
    with LocalSession.begin() as session:
        for product in get_data_source(data_source_type=ds_type)(
            first_only=first_only,
        ).get_data():
            print(product.model_dump())
            if search_term == product.name:
                session.add(
                    Product(
                        data_source_id=1,  # TODO: create
                        **product.model_dump(),
                    )
                )
                break


def get_product():
    raise NotImplementedError()
