import requests

from bs4 import BeautifulSoup

index = int(input())
r = requests.get(input())
my_soup = BeautifulSoup(r.content, "html.parser")
h2 = my_soup.find_all('h2')
print(h2[index].text)
