import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

# * needs amount for one cup
WATER = 200
MILK = 50
COFFEE_BEANS = 15

# * stage2
cups_amount = int(input('Write how many cups of coffee to make: '))

# * calculate needs for several cups
water_amount = cups_amount * WATER
milk_amount = cups_amount * MILK
coffee_beans_amount = cups_amount * COFFEE_BEANS

logging.info('For {} cups I need:\n\
{} ml of water\n\
{} ml of milk\n\
{} g of coffee beans'.format(
    cups_amount,
    water_amount,
    milk_amount,
    coffee_beans_amount
))

# logging.info('Starting to make a coffee')
# logging.info('Grinding coffee beans')
# logging.info('Boiling water')
# logging.info('Mixing boiled water with crushed coffee beans')
# logging.info('Pouring coffee into the cup')
# logging.info('Pouring some milk into the cup')
# logging.info('Coffee is ready!')
