from sqlalchemy import Column, Integer, Sequence, String
from sqlalchemy.orm import relationship

from app.database import Base


class DataSource(Base):
    __tablename__ = "data_source"

    id = Column(Integer, Sequence("data_source_id_seq"), primary_key=True)
    name = Column(String, index=True)

    product = relationship(
        "Product",
        back_populates="data_sources",
    )
