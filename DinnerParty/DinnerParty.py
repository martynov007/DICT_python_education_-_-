class Person(object):
    """docstring for Person."""
    def __init__(self):
        while not len(friends_name := input()) > 0:
                print('Name should have at least 1 symbol')

        self.name = friends_name


class Dinner(object):
    """docstring for Dinner."""
    people = {}


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
            self.people.update({Person().name: 0})

        self.bill_total = float(input('Enter the bill total: '))
        
        for person in self.people:
            self.people.update({person: round(self.bill_total/self.amount, 2)})


    def __str__(self) -> str:
        return str(self.people)


def main():
    dinner = Dinner()
    print(dinner)

if __name__ == "__main__":
    main()
