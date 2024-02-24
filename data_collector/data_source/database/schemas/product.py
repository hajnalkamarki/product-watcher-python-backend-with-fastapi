from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str


class Product(ProductBase):
    id: int
    price: int
    currency: str
    data_source_id: int

    class Config:
        orm_mode = True


class ProductCreate(ProductBase):
    pass
