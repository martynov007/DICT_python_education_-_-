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


class ImprovedCreditCalculator:
    def calc_montly_payment(self, n, year_interest_rate, P):
        i = year_interest_rate / (100 * 12)
        self.A = P * ((i * pow(1 + i, n))/(pow(1 + i, n) - 1))
        print(f'Your monthly payment = {self.A}!')
        
        
    def calc_monthes_amount(self, A, year_interest_rate, P):
        i = year_interest_rate / (100 * 12)
        self.n = math.ceil(math.log(A/(A - i * P), 1 + i))

        years = math.floor(self.n / 12)
        months = math.ceil(self.n % 12)

        if years > 0 and months > 0:
            print(
                f'It will take {years} year(s) and {months} month(s) to repay this loan!')
        elif years > 0:
            print(f'It will take {years} year(s) to repay this loan!')
        elif months > 0:
            print(f'It will take {months} month(s) to repay this loan!')

    def calc_credit_amount(self, A, year_interest_rate, n):
        i = year_interest_rate / (100 * 12)
        self.P = A / ((i * pow(1 + i, n))/(pow(1+i, n) - 1))

        print(f'Your loan principal = {self.P}!')
        

def main():
    improved_credit_calc = ImprovedCreditCalculator()
    choice = input(('What do you want to calculate?'
                    '\ntype "n" for number of monthly payments,'
                    '\ntype "a" for annuity monthly payment amount,'
                    '\ntype "p" for loan principal:'))

    match choice:
        case 'n':
            P = float(input('Enter the loan principal: '))
            A = float(input('Enter the monthly payment: '))
            rate = float(input('Enter the loan interest: '))
            improved_credit_calc.calc_monthes_amount(A, rate, P)
        case 'p':
            A = float(input('Enter the monthly payment: '))
            n = float(input('Enter the number of periods: '))
            rate = float(input('Enter the loan interest: '))
            improved_credit_calc.calc_credit_amount(A, rate, n)
        case 'a':
            P = float(input('Enter the loan principal: '))
            n = float(input('Enter the number of periods: '))
            rate = float(input('Enter the loan interest: '))
            improved_credit_calc.calc_montly_payment(n, rate, P)
        case _:
            print('not option for {}'.format(choice))


if __name__ == "__main__":
    main()
