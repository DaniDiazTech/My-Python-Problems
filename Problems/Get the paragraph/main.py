import requests

from bs4 import BeautifulSoup

word = input()
r = requests.get(input())
soup = BeautifulSoup(r.content, "html.parser")
paragraph = soup.find_all("p")
for p in paragraph:
    if word in p.text:
        print(p.text)
