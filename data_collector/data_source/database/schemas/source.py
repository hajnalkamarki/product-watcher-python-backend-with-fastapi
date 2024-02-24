from pydantic import BaseModel


class DataSourceBase(BaseModel):
    name: str


class DataSource(DataSourceBase):
    id: int

    class Config:
        orm_mode = True


class DataSourceCreate(DataSourceBase):
    pass
