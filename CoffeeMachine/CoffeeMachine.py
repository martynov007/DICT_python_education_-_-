import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

# * needs amount for one cup
WATER = 200
MILK = 50
COFFEE_BEANS = 15

# * stage3
water_has = int(input('Write how many ml of water the coffee machine has:'))
milk_has = int(input('Write how many ml of milk the coffee machine has:'))
coffee_beans_has = int(
    input('Write how many grams of coffee beans the coffee machine has:'))

cups_need = int(input('Write how many cups of coffee to make: '))

# * calculate needs for several cups
water_need = cups_need * WATER
milk_need = cups_need * MILK
coffee_beans_need = cups_need * COFFEE_BEANS

cups_has = round(min([wt, ml, cf_bns])) if (wt := water_has/WATER) >= 1 and\
    (ml := milk_has/MILK) >= 1 and\
    (cf_bns := coffee_beans_has/COFFEE_BEANS) >= 1 else 0

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

logging.info('For {} cups I need:\n\
{} ml of water\n\
{} ml of milk\n\
{} g of coffee beans'.format(
    cups_need,
    water_need,
    milk_need,
    coffee_beans_need
))

# logging.info('Starting to make a coffee')
# logging.info('Grinding coffee beans')
# logging.info('Boiling water')
# logging.info('Mixing boiled water with crushed coffee beans')
# logging.info('Pouring coffee into the cup')
# logging.info('Pouring some milk into the cup')
# logging.info('Coffee is ready!')
