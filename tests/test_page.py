import requests
from bs4 import BeautifulSoup

from book import Book
from Page import get_titles_from_page, get_trs_from_page

url = "http://libgen.rs/search.php?req=python&lg_topic=libgen&open=0&view=simple&res=25&phrase=1&column=def"

r = requests.get(url)
b = BeautifulSoup(r.text, "html.parser")
tr1 = get_trs_from_page(b)[2]
print(Book(tr1))
print(get_titles_from_page(b))
