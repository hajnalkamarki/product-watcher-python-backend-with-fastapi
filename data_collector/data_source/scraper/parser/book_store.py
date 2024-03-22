from data_collector.data_source.scraper.parser import Parser


class BookStoreParser(Parser):
    def __init__(self, html_content: str):
        print(html_content)
        super().__init__(html_content=html_content)

    def parse(self):
        pass
