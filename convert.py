import requests

header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
        }

def nbu():
    link_nbu = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    response = requests.get(link_nbu, headers=header)
    obj = response.json()
    data_rub = {
        'Валюта: ': obj[18]['txt'],
        'id: ': obj[18]['cc'],
        'К гривне: ': obj[18]['rate'],
        'Дата: ': obj[18]['exchangedate'],
        'r030: ': obj[18]['r030']
    }

    data_eur = {
        'Валюта: ': obj[33]['txt'],
        'id: ': obj[33]['cc'],
        'К гривне: ': obj[33]['rate'],
        'Дата: ': obj[33]['exchangedate'],
        'r030: ': obj[33]['r030']
    }

    data_usd = {
        'Валюта: ': obj[26]['txt'],
        'id: ': obj[26]['cc'],
        'К гривне: ': obj[26]['rate'],
        'Дата: ': obj[26]['exchangedate'],
        'r030: ': obj[26]['r030']
    }

    data = {
        'RUB': data_rub,
        'EUR': data_eur,
        'USD': data_usd
    }
    return data


def convert(sum, id):
    price = sum * nbu()[id]['К гривне: ']
    return price
