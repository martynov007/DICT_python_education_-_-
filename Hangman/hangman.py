if __name__ == '__main__':
    # stage 1
    print('HANGMAN\nTry to not being hanged')

    # stage 2
    TO_GUESS = 'witch'
    print('Guess the word:')
    user_guess = input()

    if user_guess == TO_GUESS:
        print('You\'r survived!')
    else:
        print('You\'r hanged!')
