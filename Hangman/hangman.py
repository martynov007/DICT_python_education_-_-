import random as rnd

if __name__ == '__main__':
    # stage 1
    print('HANGMAN\nTry to not being hanged')

    # stage 4
    TO_GUESS = rnd.choice(['apple', 'banana', 'cucumber', 'watermelon'])
    formated_guess = TO_GUESS[:3] + '-' * (len(TO_GUESS) - 3)

    print(f'Guess the word {formated_guess}:')
    user_guess = input()

    if user_guess == TO_GUESS:
        print('You\'r survived!')
    else:
        print('You\'r hanged!')
