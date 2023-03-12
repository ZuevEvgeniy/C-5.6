import json
import requests
from config import money

class APIException(Exception):
    pass

class Convertor:
    @staticmethod
    def get_price(base, sum, amount):
        try:
            base_key = money[base.lower()]
        except KeyError:
            raise APIException(f"Валюта {base} не найдена!")

        try:
            sum_key = money[sum.lower()]
        except KeyError:
            raise APIException(f"Валюта {sym} не найдена!")

        if base_key == sum_key:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}!')
        
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}!')

        
        payload = {}
        headers = {
            "apikey": "ONUWVkXtKFhC0oAi3OqmYSZv18mwetxY"
        }
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={sum_key}&from={base_key}&amount={amount}"

        response = requests.request("GET", url, headers=headers, data=payload)
        resp = json.loads(response.content)
        new_price = resp.get("result")
        new_price=round(new_price,3)
        message =  f"Цена {amount} {base} в {sum} : {new_price}"
        return message
