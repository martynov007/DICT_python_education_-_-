from itertools import filterfalse
import random as rnd

if __name__ == '__main__':
    # stage 1
    print('HANGMAN\nTry to not being hanged')

    # stage 8
    HP = 8  # Health points
    TO_GUESS = 'water'
    already_guessed = []
    opnd_ltr = []
    do_play = True

    while do_play:
        print('Type "play" to play the game, "exit" to quit:')
        answer = input()

        if answer == 'exit':
            break
        elif answer != 'play':
            continue

        while len(opnd_ltr) < len(TO_GUESS) \
                and HP != 0:
            formated_guess = ''.join([x if x in opnd_ltr
                                     else '-' for x in TO_GUESS])

            print(f'\nGuess a letter {formated_guess}:')

            user_guess = input()
            if len(user_guess) > 1:
                print('You should input a single letter.')
                continue

            if not str.isalpha(user_guess)\
                    or not str.islower(user_guess):
                print('Please enter a lowercase English letter.')
                continue

            if user_guess in already_guessed:
                print('You\'ve already guessed this letter')
            elif user_guess not in TO_GUESS:
                print('That letter doesn\'t appear in the word')
                HP -= 1
            else:
                opnd_ltr.append(user_guess)

            already_guessed.append(user_guess)

        print('Game over')
