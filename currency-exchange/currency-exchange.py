class CurrencyExchange:
    def __init__(self) -> None:
        self.currency = float(input('Please enter your currency amount: '))
        exchange_rate = float(input('Enter exchange rate to USD for your currency: '))
        self.exchange(exchange_rate)

    def exchange(self, rate):
        print('You will get {} dollars'.format(self.currency * rate))

if __name__ == "__main__":
    CurrencyExchange()