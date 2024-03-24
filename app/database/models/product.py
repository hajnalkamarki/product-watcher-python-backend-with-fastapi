from sqlalchemy import Column, ForeignKey, Integer, Sequence, String
from sqlalchemy.orm import relationship

from app.database import Base


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, Sequence("product_id_seq"), primary_key=True)
    name = Column(String, index=True)
    price = Column(String)
    currency = Column(String)
    data_source_id = Column(Integer, ForeignKey("data_source.id"))

    data_sources = relationship(
        "DataSource",
        back_populates="product",
    )
