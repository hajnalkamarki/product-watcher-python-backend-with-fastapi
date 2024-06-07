from typing import Dict

from pydantic import BaseModel


class SourceConfig(BaseModel):
    id: int
    name: str


class ScraperConfig(BaseModel):
    source: SourceConfig
    urls: Dict[str, str]


class AppConfig(BaseModel):
    scrapers: Dict[str, ScraperConfig]
