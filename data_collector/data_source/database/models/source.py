from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from . import Base


class DataSource(Base):
    __tablename__ = "data_source"

    id = Column(String, primary_key=True, index=True)

    product = relationship(
        "Product",
        back_populates="data_sources",
    )
