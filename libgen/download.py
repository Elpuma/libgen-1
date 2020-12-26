import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

from book import Book

"""
use
----
Download(Book, mirror, filename)
"""
MIRROR = "Gen.lib.rus.ec"
MIRROR_LIST = ["Gen.lib.rus.ec", "Libgen.lc", "z-library", "Libgen.pw", "BookFI.net"]


def _check_mirror(mirror, mirror_list=MIRROR_LIST):
    if mirror in mirror_list:
        return True
    else:
        return False


def download(filename, mirror_list_for_book, mirror=MIRROR):
    assert _check_mirror(mirror, mirror_list_for_book), "Useable mirror, not found"
    _content_href = _get_content_href_from_mirror(mirror, mirror_list_for_book)
    response = requests.get(_content_href)
    if response.ok:
        """
        Save response.content
        _save_to_file saves content
        """
        save_to_file(response, filename=filename)
    else:
        raise IOError("Unable to find content from mirror")


def _get_content_href_from_mirror(mirror, mirror_list):
    href = mirror_list.get(mirror)
    result = requests.get(href)
    if result.ok:
        soup = BeautifulSoup(result.text, "html.parser")
    else:
        raise IOError

    if mirror == MIRROR_LIST[0]:
        return soup.find("h2").a["href"]

    elif mirror == MIRROR_LIST[1]:
        pass
    elif mirror == MIRROR_LIST[2]:
        pass
    elif mirror == MIRROR_LIST[3]:
        pass
    elif mirror == MIRROR_LIST[4]:
        pass
    elif mirror == MIRROR_LIST[5]:
        pass


def save_to_file(response, filename):
    chunk_size = 1024
    try:
        total_size = int(response.headers["content-length"])
    except KeyError:
        total_size = response.content

    total_chunks = total_size / chunk_size
    file_iterable = response.iter_content(chunk_size=chunk_size)

    # implementing tqdm
    tqdm_iter = tqdm(
        iterable=file_iterable,
        total=total_chunks,
        unit="KB",
        desc=filename,
        leave=False,
    )

    # write to file
    with open(filename, "wb") as f:
        for data in tqdm_iter:
            f.write(data)
