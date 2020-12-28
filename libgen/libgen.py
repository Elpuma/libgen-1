import pickle

import requests
from bs4 import BeautifulSoup

from libgen.page import _get_book_from_page, get_book_with_index

url = "http://libgen.rs/search.php?req=python&open=0&res=50&view=simple&phrase=1&column=def"


class Libgen:
    URL = "http://libgen.rs/search.php?req={0}&open=0&res={1}&view=simple&phrase=1&column=def"

    # used for storing indexies
    _tmp = "/tmp/libgen_keys"

    def __init__(self, search, result_per_page=10):
        self.search = str(search)
        self.result_per_page = str(result_per_page)
        result = requests.get(Libgen.URL.format(self.search, self.result_per_page))
        self.__soup = BeautifulSoup(result.text, "html.parser")

    def list_search_result(self):
        _keys_names = {}
        for key, book in enumerate(_get_book_from_page(self.__soup)):
            _keys_names[key + 1] = book.get_title()
            print("{} {}".format(key + 1, book.get_title()))

        # save with pickle
        self.__save_keys_and_names(_keys_names)

    def info(self, key):
        if self.check_in_keys_names(key):
            return get_book_with_index(self.__soup, key - 1)
        else:
            raise KeyError("Key not found in tmp file")

    def __save_keys_and_names(self, _dict):
        with open(Libgen._tmp, "wb") as t:
            pickle.dump(_dict, t, protocol=pickle.HIGHEST_PROTOCOL)

    def check_in_keys_names(self, _index):
        with open(Libgen._tmp, "rb") as t:
            b = pickle.load(t)
        return True if _index in b.keys() else False
