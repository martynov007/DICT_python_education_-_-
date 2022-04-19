class CurrencyExchange:
    exchange_rates = {
        'USD': 2.5,
        'UAH': 0.8,
        'RUB': 1000,
        'EUR': 2
    }

    def __init__(self) -> None:
        self.currency = float(input('Please enter your currency amount: '))
        # exchange_rate = float(input('Enter exchange rate to USD for your currency: '))
        for key, value in self.exchange_rates.items():
            self.exchange(key, value)

    def exchange(self, exchange_currency, rate):
        print('You will get {} {}'.format(self.currency * rate, exchange_currency))

if __name__ == "__main__":
    CurrencyExchange()