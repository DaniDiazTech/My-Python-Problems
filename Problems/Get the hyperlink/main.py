import requests

from bs4 import BeautifulSoup
act_number = int(input())
r = requests.get(input(), "html.parser")
site_soup = BeautifulSoup(r.content, "html.parser")
a = site_soup.find_all("a")
a_anchor = a[act_number - 1]
print(a_anchor.get('href'))
