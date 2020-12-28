from book import Book


def get_titles_from_page(soup):
    return [Book(x).get_title() for x in get_trs_from_page(soup)[1::]]


def _get_book_from_page(soup):
    return [Book(x) for x in get_trs_from_page(soup)[1::]]


def get_trs_from_page(soup):
    if soup:
        tr = soup.find_all("tr", valign="top")
        return tr
    else:
        raise NotImplementedError


def get_book_with_index(soup, index):
    return _get_book_from_page(soup)[index]
