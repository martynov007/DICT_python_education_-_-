import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

# * stage6

class CoffeeMachine:
    def __init__(self, action) -> None:
        self.action = action

        if action == 'buy':
            buy_coffee()
        elif action.strip().lower() == 'fill':
            fill_inventory()
        elif action.strip().lower() == 'take':
            withdraw_money()
        elif action.strip().lower() == 'remaining':
            show_inventory()
        else:
            logging.warning('\nchoice right option')

# * init coffee machine
WATER = 400
MILK = 540
COFFEE_BEANS = 120
CUPS = 9
MONEY = 550


def show_inventory():
    global WATER, MILK, COFFEE_BEANS, CUPS

    logging.info('The coffee machine has:\n\
{} ml of water\n\
{} ml of milk\n\
{} g of coffee beans\n\
{} of cups\n\
{} of money'.format(
        WATER,
        MILK,
        COFFEE_BEANS,
        CUPS,
        MONEY,
    ))


def buy_coffee():
    global WATER, MILK, COFFEE_BEANS, CUPS, MONEY

    coffee_choice = input('\nWhat do you want to buy? \
1 - espresso, \
2 - latte, \
3 - cappuccino, back – to main menu:')

    if coffee_choice == '1':
        if is_enough_prods(250, 16):
            WATER -= 250
            COFFEE_BEANS -= 16
            MONEY += 4
    elif coffee_choice == '2':
        if is_enough_prods(350, 20, 75):
            WATER -= 350
            MILK -= 75
            COFFEE_BEANS -= 20
            MONEY += 7
    elif coffee_choice == '3':
        if is_enough_prods(200, 12, 100):
            WATER -= 200
            MILK -= 100
            COFFEE_BEANS -= 12
            MONEY += 6
    elif coffee_choice == 'back':
        return 'back'
    else:
        print('\nwe don\'t have this kind of coffee')
        return None

    CUPS -= 1


def is_enough_prods(water, beans, milk=0):
    global WATER, MILK, COFFEE_BEANS, CUPS, MONEY

    if WATER < water:
        logging.info('Sorry, not enough water!')
        return False

    if COFFEE_BEANS < beans:
        logging.info('Sorry, not enough coffee beans!')
        return False

    if CUPS-1 < 0:
        logging.info('Sorry, not enough cups!')
        return False

    if MILK < milk:
        logging.info('Sorry, not enough milk!')
        return False

    logging.info('I have enough resources, making you a coffee!')
    return True


def fill_inventory():
    global WATER, MILK, COFFEE_BEANS, CUPS

    WATER += int(input('Write how many ml of water you want to add:'))
    MILK += int(input('Write how many ml of milk you want to add:'))
    COFFEE_BEANS += int(
        input('Write how many grams of coffee beans you want to add:'))
    CUPS += int(input('Write how many disposable coffee cups you want to add:'))


def withdraw_money():
    global MONEY

    logging.info('\nwithdrawed {}'.format(MONEY))

    MONEY = 0


while True:
    action = input('\nWrite action (buy, fill, take, remaining, exit):')

    if action == 'exit':
        break

    CoffeeMachine(action)

