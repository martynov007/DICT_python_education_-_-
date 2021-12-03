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


class AnnuityCreditCalculator:
    def __init__(self, rate = None, A = None, n = None, P = None) -> None:
        self.rate = rate or 0
        self.A = A or 0
        self.n = n or 0
        self.P = P or 0
        
        if self.rate < 0\
            or self.P < 0\
                or self.n < 0\
                    or self.A < 0:
            print('Incorrect parameters')
            return None

        if rate and A and n:
            self.calc_credit_amount()
            self.overpayment()
            return
        if rate and A and P:
            self.calc_monthes_amount()
            self.overpayment()
            return
        if n and rate and P:
            self.calc_montly_payment()
            self.overpayment()
            return 
        else:
            print('Incorrect parametres')
            return


    def calc_montly_payment(self):
        i = self.rate / (100 * 12)
        self.A = self.P * ((i * pow(1 + i, self.n))/(pow(1 + i, self.n) - 1))
        print(f'Your monthly payment = {math.ceil(self.A)}!')


    def calc_monthes_amount(self):
        i = self.rate / (100 * 12)
        self.n = math.ceil(math.log(self.A/(self.A - i * self.P), 1 + i))

        years = math.floor(self.n / 12)
        months = math.ceil(self.n % 12)

        if years > 0 and months > 0:
            print(
                f'It will take {years} year(s) and {months} month(s) to repay this loan!')
        elif years > 0:
            print(f'It will take {years} year(s) to repay this loan!')
        elif months > 0:
            print(f'It will take {months} month(s) to repay this loan!')


    def calc_credit_amount(self):
        i = self.rate / (100 * 12)
        self.P = self.A / ((i * pow(1 + i, self.n))/(pow(1+i, self.n) - 1))

        print(f'Your loan principal = {round(self.A)}!')


    def overpayment(self):
        print(f'Overpayment = {math.ceil((self.A * self.n) - self.P)}')


class DiffCreditCalculator():
    def __init__(self, rate = None, A = None, n = None, P = None) -> None:
        self.rate = rate or 0
        self.P = P or 0
        self.n = n or 0
        self.sum_overpayment = 0

        if A:
            print('Incorrect parameters')
            return None

        if self.rate <= 0\
                or self.n <= 0\
                    or self.P <= 0:
            print('Incorrect parameters')
            return None

        if rate and P and n:
            self.calc_credit_amount()
        else:
            print('Incorrect parametres')
            return

        self.overpayment()


    def calc_credit_amount(self):
        for m in range(1, self.n+1):
            i = self.rate / (100 * 12)
            self.D = (self.P / self.n) + i * (self.P - (self.P * (m - 1)/self.n))

            self.sum_overpayment += self.D

            print(f'Month {m}: payment is {math.ceil(self.D)}!')


    def overpayment(self):
        print(f'Overpayment = {math.ceil(self.sum_overpayment - self.P)}')


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--type', type=str)
    parser.add_argument('--interest', type=float)
    parser.add_argument('--principal', type=float)
    parser.add_argument('--payment', type=float)
    parser.add_argument('--periods', type=int)
    args = parser.parse_args('--type=diff --principal=500000 --periods=8 --interest=7.8'.split())

    choice = args.type
    A = args.payment
    rate = args.interest
    P = args.principal
    n = args.periods
    
    if not choice:
        print('Incorrect parameters')
        return

    match choice:
        case 'diff':
            DiffCreditCalculator(rate, A, n, P)
        case 'annuity':
            AnnuityCreditCalculator(rate, A, n, P)
        case _:
            print('not option for {}'.format(choice))


if __name__ == "__main__":
    main()
