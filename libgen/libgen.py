import pickle

import requests
from bs4 import BeautifulSoup

from libgen.page import _get_book_from_page

url = "http://libgen.rs/search.php?req=python&open=0&res=50&view=simple&phrase=1&column=def"


class libgen:
    URL = "http://libgen.rs/search.php?req={0}&open=0&res={1}&view=simple&phrase=1&column=def"

    # used for storing indexies
    _tmp = "/tmp/libgen_keys"

    def __init__(self, search, result_per_page=10):
        self.search = str(search)
        self.result_per_page = int(result_per_page)
        result = requests.get(libgen.URL.format(self.search, self.result_per_page))
        self.__soup = BeautifulSoup(result.text, "html.parser")

    def list_search_result(self):
        _keys_names = {}
        for key, book in enumerate(_get_book_from_page(self.__soup)):
            name = book.get_title()
            _keys_names[key + 1] = name
            print("{} {}".format(key + 1, name))

        # save wit pickle
        self.__save_keys_and_names(_keys_names)

    def book_info(self, key):
        self.check_in_keys_names(key)

    def __save_keys_and_names(self, _dict):
        with open(libgen._tmp, "wb") as t:
            pickle.dump(_dict, t)

    def check_in_keys_names(self, _index):
        with open(libgen._tmp, "rb") as t:
            b = pickle.load(t)
        print(b.get(_index)[0])


if __name__ == "__main__":
    p = libgen("python", 10)
    p.list_search_result()
