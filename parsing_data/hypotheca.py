import requests
from bs4 import BeautifulSoup

body = requests.get("https://www.sravni.ru/ipoteka/")
# print(body.status_code)
body.encoding = 'utf-8'
bs = BeautifulSoup(body.text, "html.parser")

card_name = bs.find_all("span", class_="Caption_caption__3vHDe")
for i in card_name:
    print(i.text)
    
interest_rate = bs.find_all("div", class_="Row_grid__hxeUe Row_cellGroup__0nmeR")
for i in interest_rate:
    print(i.text)    
    
