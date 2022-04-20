import requests


class CurrencyExchange:
    def __init__(self) -> None:
        self.currency_rate_cache = {}
        self.exchanging_currency = input('Please enter your currency: ')

        currency_rate_res = requests.get(
            'http://www.floatrates.com/daily/{}.json'.format(self.exchanging_currency))

        if not currency_rate_res:
            print('Cant find that currency')
            return

        self.currency_rate = currency_rate_res.json()

        if self.currency_rate.get('usd'):
            self.currency_rate_cache.update({'usd': self.currency_rate['usd']['rate']})

        if self.currency_rate.get('eur'):
            self.currency_rate_cache.update({'eur': self.currency_rate['eur']['rate']
        })

        while True:
            currency_input = input(
                'Please enter currency that you want to receive: ').lower()
            self.currency = self.currency_rate.get(currency_input)

            if not self.currency:
                print('We dont exchange this currency')
                continue

            self.currency_amount = float(
                input('Please enter your currency amount to exchange: '))

            print('Checking the cache...')
            currency_rate = self.currency_rate_cache.get(self.currency)

            if currency_rate:
                print('It\'s in the cache!')
            else:
                print('It\'s not in the cache!')

                currency_rate = self.currency['rate']

                self.currency_rate_cache.update({self.currency: currency_rate})

            exchanged_sum = round(self.currency_amount * currency_rate, 2)
            print('You got {} {}'.format(exchanged_sum, self.currency.upper()))

if __name__ == "__main__":
    CurrencyExchange()