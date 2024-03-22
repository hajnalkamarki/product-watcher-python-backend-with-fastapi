from abc import ABC, abstractmethod

from bs4 import BeautifulSoup


class Parser(ABC):
    def __init__(self, html_content: str):
        self.soup = BeautifulSoup(html_content, "html.parser")

    @abstractmethod
    def parse(self):
        raise NotImplementedError()
