from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from . import Base


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    price = Column(String)
    currency = Column(String)
    data_source_id = Column(String, ForeignKey("data_source.id"))

    data_sources = relationship(
        "DataSource",
        back_populates="product",
    )
