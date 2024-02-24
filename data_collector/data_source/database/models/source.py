from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from . import Base


class DataSource(Base):
    __tablename__ = "data_source"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)

    product = relationship(
        "Product",
        back_populates="data_sources",
    )
