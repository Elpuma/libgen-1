import requests
from bs4 import BeautifulSoup


class Download:
    def __init__(self, Book, mirror):
        self.Book = Book
        self.download = self._check_mirror(mirror)

    def _check_mirror(self, mirror):
        if mirror in self.Book.get_mirrors().keys():
            return True
        else:
            return False

    def download(self):
        pass

    def _get_download_url(self, mirror):
        if mirror == "Gen.lib.rus.ec":
            download_url = "adf"
        else:
            pass

    def _save_to_file(self, content):
        _file_name = (
            self.Book.get_title()
            + self.Book.get_year()
            + "."
            + self.Book.get_file_extension()
        )
        with open(_file_name, "wb") as f:
            f.write(content)
