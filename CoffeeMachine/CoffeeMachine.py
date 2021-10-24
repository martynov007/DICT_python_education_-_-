import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

# * stage4
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

    coffee_choice = input('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')

    if coffee_choice == '1':
        WATER -= 250
        COFFEE_BEANS -= 16
        MONEY += 4
    elif coffee_choice == '2':
        WATER -= 350
        MILK -= 75
        COFFEE_BEANS -= 20
        MONEY += 7
    elif coffee_choice == '3':
        WATER -= 200
        MILK -= 100
        COFFEE_BEANS -= 12
        MONEY += 6
    else:
        print('\nwe don\'t have this kind of coffee')
        return None
    
    CUPS -= 1

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
    show_inventory()

    action = input('\nWrite action (buy, fill, take):')

    if action == 'buy':
        buy_coffee()
    elif action == 'fill':
        fill_inventory()
    elif action == 'take':
        withdraw_money()
    # elif action == 'exit':
    #     break
    else:
        logging.warning('\nchoice right option')



# * calculate needs for several cups
water_need = cups_need * WATER
milk_need = cups_need * MILK
coffee_beans_need = cups_need * COFFEE_BEANS



if cups_has == cups_need:
    logging.info('Yes, I can make that amount of coffee')
elif cups_has > cups_need:
    logging.info('Yes, I can make that amount of coffee (and even {} more than that'
                 .format(cups_has - cups_need))
elif cups_has < cups_need\
        and cups_has > 0:
    logging.info('No, I can make only {} cups of coffee'.format(cups_has))
else:
    # * тут я немного улучшил условия ведь странно выглядело бы
    # * нет, я могу сделать лишь 0 чашек кофе
    logging.info('I can\'t do even 1 cup of coffee')

# logging.info('Starting to make a coffee')
# logging.info('Grinding coffee beans')
# logging.info('Boiling water')
# logging.info('Mixing boiled water with crushed coffee beans')
# logging.info('Pouring coffee into the cup')
# logging.info('Pouring some milk into the cup')
# logging.info('Coffee is ready!')
