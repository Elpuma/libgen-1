import requests
from bs4 import BeautifulSoup


class Book:
    """
    Book object
    """

    def __init__(self, tr):
        """
        tr
        ----
        like the whole row

        child_tds
        ------
        all td's inside tr

        """
        self.tr = tr
        self.child_tds = self.tr.find_all("td")
        assert self.child_tds is not None, "Invaild tr param"

    def _get_authors(self):
        return self.child_tds[1].text

    def get_authors(self):
        return [x.strip(" ") for x in self._get_authors().split(",")]

    def get_title(self):
        return self.child_tds[2].text

    def get_publisher(self):
        return self.child_tds[3].text

    def get_year(self):
        return self.child_tds[4].text

    def get_pages(self):
        return self.child_tds[5].text

    def get_language(self):
        return self.child_tds[6].text

    def get_deafault_href(self):
        return self.child_tds[2]["href"]

    def get_size(self):
        return self.child_tds[7]["href"]

    def get_file_extension(self):
        return self.child_tds[8]["href"]

    def _get_href_from_mirror(self, td):
        return td.a["href"]

    def get_mirrors(self):
        # return [ self._get_href_from_mirror(x) for x in self.child_tds[9::]]
        mirrors = {}
        for i, mirror in enumerate(self.child_tds[9:-1]):
            mirrors[mirror.a["title"]] = mirror.a["href"]
        return mirrors
