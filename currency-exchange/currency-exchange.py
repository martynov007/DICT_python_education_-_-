import json
import requests


class CurrencyExchange:
    def __init__(self) -> None:
        self.currency = input('Please enter your currency: ')
        self.currency_amount = float(input('Please enter your currency amount: '))
        currency_rate_res = requests.get('http://www.floatrates.com/daily/{}.json'.format(self.currency))

        if not currency_rate_res:
            print('Cant find that currency')
            return

        currency_rate_js = currency_rate_res.json()

        print('EUR: {}'.format(round(self.currency_amount * currency_rate_js['eur']['rate'], 2)))
        print('USD: {}'.format(round(self.currency_amount * currency_rate_js['usd']['rate'],2)))

        # exchange_rate = float(input('Enter exchange rate to USD for your currency: '))
        # for key, value in self.exchange_rates.items():
        #     self.exchange(key, value)

    def exchange(self, exchange_currency, rate):
        print('You will get {} {}'.format(self.currency * rate, exchange_currency))

if __name__ == "__main__":
    CurrencyExchange()