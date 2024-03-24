from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str


class Product(ProductBase):
    price: str
    currency: str

    class Config:
        orm_mode = True


class ProductCreate(ProductBase):
    pass
