import json
import os
from typing import Dict

from pydantic import BaseModel, ConfigDict, computed_field


class SourceConfig(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(extra="ignore", frozen=True)


class ScraperConfig(BaseModel):
    source: SourceConfig
    urls: Dict[str, str]

    model_config = ConfigDict(extra="ignore", frozen=True)


class AppConfig(BaseModel):
    env: str
    config_path: str

    model_config = ConfigDict(extra="ignore", frozen=True)

    @computed_field  # type: ignore[misc]
    @property
    def scraper_config(self) -> Dict[str, ScraperConfig]:
        return {
            k: ScraperConfig(**v)
            for k, v in json.load(
                open(
                    "{}/{}/{}/scraper.json".format(
                        os.getcwd(),
                        self.config_path,
                        self.env,
                    )
                )
            ).items()
        }
