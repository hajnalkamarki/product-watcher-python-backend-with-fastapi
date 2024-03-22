from abc import ABC, abstractmethod


class Parser(ABC):
    def __init__(self, html_content: str):
        self.html = html_content

    @abstractmethod
    def parse(self):
        raise NotImplementedError()
