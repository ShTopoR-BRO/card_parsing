import requests
from bs4 import BeautifulSoup

def chang(chash):
    result = []
    gloabal_res = []
    for i in chash:
        if len(result) == 3:
            gloabal_res.append(result)
            result = []
        else:
            result.append(i.text)
    return gloabal_res


def card_parsing():
    body = requests.get("https://www.sravni.ru/debetovye-karty/")
    body.encoding = 'utf-8'
    # print(body.status_code)
    bs = BeautifulSoup(body.text, "html.parser")

    bank_name = bs.find_all("span", class_="_106rrj0")

    cashback = bs.find_all("div", class_="_5gmjom _1livb46") 
    cashback = chang(cashback)


    result = []
    for i in bank_name:
        result.append({"bank": i.text})

    for i in range(len(cashback)):
        result[i]["data"] = cashback[i]
        
    return result