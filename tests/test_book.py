import requests
from bs4 import BeautifulSoup

from book import Book

url = "http://libgen.rs/search.php?req=python&lg_topic=libgen&open=0&view=simple&res=25&phrase=1&column=def"

r = requests.get(url)
b = BeautifulSoup(r.text, "html.parser")
tr = b.find_all("tr", valign="top")[2]
book = Book(tr)
print(book)
