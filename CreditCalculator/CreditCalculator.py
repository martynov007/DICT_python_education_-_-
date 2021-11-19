import math


class CreditCalculator:
    def __init__(self, credit_amount) -> None:
        try:
            self.credit_amount = float(credit_amount)

        except Exception:
            print('It should be numbers!')


    def calc_monthly_payment(self, payment_amount):
        self.payment_amount = float(payment_amount)
        self.month_amount = math.ceil(self.credit_amount/self.payment_amount)

        print('Monthly payment is {}'.format(self.month_amount))


    def calc_payment_amount(self, month_amount):
        self.month_amount = float(month_amount)
        self.payment_amount = self.credit_amount/self.month_amount

        if not self.payment_amount.is_integer():
            seiled_payment = math.ceil(self.payment_amount)
            self.last_payment = seiled_payment - self.payment_amount
            self.payment_amount = seiled_payment

        print('Payment amount is {}'.format(self.payment_amount))
        try:
            print('Last payment amount is {}'.format(self.last_payment))
        except AttributeError:
            pass


    def __str__(self) -> str:
        return ('Credit amount: {}'
                '\nMonth amount: {}'
                '\nPayment amount: {}').format(
                    self.credit_amount,
                    self.month_amount,
                    self.payment_amount
        )


def main():
    credit_calc = CreditCalculator(input('Enter the credit amount\n'))
    choice = input(('What do you want to calculate?'
                    '\ntype "m" – for amount of monthly payments,'
                    '\ntype "p" – for the monthly payment:'))

    match choice:
        case 'm':
            payment_amount = input('Enter the payment per month: ')
            credit_calc.calc_monthly_payment(payment_amount)
        case 'p':
            month_amount = input('Enter the amount of months: ')
            credit_calc.calc_payment_amount(month_amount)
        case _:
            print('not option for {}'.format(choice))


if __name__ == "__main__":
    main()
