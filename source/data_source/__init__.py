from abc import ABC, abstractmethod
from typing import Dict


class DataSource(ABC):
    @abstractmethod
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def _set_url(self, params: Dict) -> None:
        self.url = self.base_url.format(**params)
