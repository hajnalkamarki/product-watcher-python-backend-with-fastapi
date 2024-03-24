from typing import List

from app.data_source.common.data_source_types import DataSourceType
from app.data_source.schemas.product import Product
from app.data_source.scraper.parser import Parser


class BookStoreParser(Parser):
    def __init__(
        self,
        html_content: str,
        ds_type: DataSourceType,
        first_only: bool = False,
    ) -> None:
        super().__init__(
            html_content=html_content,
            ds_type=ds_type,
            first_only=first_only,
        )

    def parse(self) -> List[Product]:
        products = list()

        for product in self.soup.find_all(
            "article",
            attrs={"class": "product_pod"},
        ):
            products.append(self._parse_product(product=product))
            if self.first_only:
                break

        return products

    def _parse_product(self, product) -> Product:
        full_price = self._parse_full_price(product=product)
        currency = self._get_currency(price=full_price)

        return Product(
            name=product.find("h3").text,
            price=full_price.replace(currency, ""),
            currency=currency,
        )

    @classmethod
    def _parse_full_price(cls, product) -> str:
        return product.find(
            "p",
            attrs={"class": "price_color"},
        ).text.replace("Â", "")
