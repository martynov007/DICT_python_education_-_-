import random as rnd

if __name__ == '__main__':
    # stage 1
    print('HANGMAN\nTry to not being hanged')

    # stage 3
    TO_GUESS = rnd.choice(['apple', 'banana', 'cucumber', 'watermelon'])
    print(TO_GUESS)
    print('Guess the word:')
    user_guess = input()

    if user_guess == TO_GUESS:
        print('You\'r survived!')
    else:
        print('You\'r hanged!')
