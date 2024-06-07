from app.database import LocalSession
from app.database.models.product import Product as ProductModel
from app.schemas.product import Product as ProductSchema
from app.scraper import DataSourceType
from app.services.scraper import get_data_source


def add_product(
    ds_type: DataSourceType,
    search_term: str,
    first_only: bool = False,
) -> None:
    data_source = get_data_source(
        data_source_type=ds_type,
    )(first_only=first_only)

    with LocalSession.begin() as session:
        for product in data_source.get_data():
            if search_term == product.name:
                session.add(
                    ProductModel(
                        data_source_id=1,
                        **product.model_dump(),
                    ),
                )
                break


def get_product(
    ds_type: DataSourceType,
    search_term: str,
) -> ProductModel | None:
    with LocalSession.begin() as session:
        product = (
            session.query(ProductModel)
            .filter_by(
                name=search_term,
                data_source_id=1,  # TODO: replace
            )
            .first()
        )

        return ProductSchema(
            name=product.name,
            price=product.price,
            currency=product.currency,
        )
