from itertools import filterfalse
import random as rnd

if __name__ == '__main__':
    # stage 1
    print('HANGMAN\nTry to not being hanged')

    # stage 5
    HP = 8  # Health points
    TO_GUESS = 'water'
    already_guessed = []
    over = False

    while len(already_guessed) < len(TO_GUESS) \
            and HP != 0:
        formated_guess = ''.join([x if x in already_guessed
                                 else '-' for x in TO_GUESS])

        print(f'Guess a letter {formated_guess}:')

        #  здесь хочется проверить длину слова. Ну ладно, делаю по заданию
        user_guess = input()

        if user_guess in TO_GUESS \
                and user_guess not in already_guessed:
            already_guessed.append(user_guess)
        else:
            print('You didn\'t guess')

        HP -= 1

    print('Game over')
