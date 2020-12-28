import requests
from bs4 import BeautifulSoup

from book import Book
from download import _get_content_href_from_mirror, download

url = "http://libgen.rs/search.php?req=python&lg_topic=libgen&open=0&view=simple&res=25&phrase=1&column=def"

r = requests.get(url)
b = BeautifulSoup(r.text, "html.parser")
tr = b.find_all("tr", valign="top")[2]
book = Book(tr)
mirror = book.get_mirrors().get("Gen.lib.rus.ec")
download = download(
    "default.pdf",
    book.get_mirrors(),
    "Gen.lib.rus.ec",
)
