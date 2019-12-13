import urllib3
from bs4 import BeautifulSoup

url="https://vufind.lboro.ac.uk/Search/Results?page=4&type=AllFields"

http = urllib3.PoolManager()
response = http.request('GET', url)

soup=BeautifulSoup(response.data)

a = soup.findAll("a", {"class": "title getFull"})
arr = []
for i in a:
    book_info = i.text.strip()
    try:
        b = book_info.split(" / by ")
        print(str(b).replace("\'", "\"") + ",")
    except:
        pass
