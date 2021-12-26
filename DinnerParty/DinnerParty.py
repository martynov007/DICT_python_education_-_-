import random
from typing import Type


class Person(object):
    """docstring for Person."""
    people = []

    def __init__(self):
        while not len(friends_name := input('Enter friend\'s name: ')) > 0:
                print('Name should have at least 1 symbol')

        self.name = friends_name
        while True:
            try:
                self.bonuses = int(input('Enter amount of bonuses. Should be int: '))
                break
            except ValueError:
                print('Invalid value. Reenter it.')

        self.bill = 0

        self.people.append(self)

class Dinner(object):
    """docstring for Dinner."""
    people = {}
    lucky_one = ''

    def __init__(self):
        try:
            self.amount = int(input('Enter amount of friends: '))
        except ValueError:
            print('not valid amount')
            return None

        if not self.amount > 0:
            print('No one join to the party')
            return None

        print('Enter the name of every friend (including you), each on a new line: ')

        for _ in range(self.amount):
            Person()

        self.bill_total = float(input('Enter the bill total: '))

        self.calc_bill()

        bonuses_choice = input('Do use bonuse?(+, -): ')

        if bonuses_choice == '+':
            person = max(Person.people, key=lambda x: x.bonuses)

            print(person.name, 'has max bonus:', person.bonuses, sep=' ')
            self.bill_total = self.bill_total - person.bonuses
            print('Bill amount now equals: ', self.bill_total)
            self.calc_bill()

        is_lucky = input('Wanna choose a lucky one ?(+,-): ')

        if is_lucky == '+':
            self.lucky_one = random.choice(Person.people)
            print(f'{self.lucky_one.name} is lucky one!! They don\'t pay for bill')

            self.lucky_one.bill = 0
            self.amount -= 1
            self.calc_bill()


    def calc_bill(self):
        for person in Person.people:
            if person.name != getattr(self.lucky_one, 'name', None):
                person.bill = round(self.bill_total/self.amount, 2)


def main():
    dinner = Dinner()
    for person in Person.people:
        print(f'Name: {person.name}\tBill: {person.bill}')

if __name__ == "__main__":
    main()

