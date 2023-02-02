import random


num_digits = 3
max_guesses = 10


def bagels():
    print('''Bagels, a deductive logic game.
    Origenal its deciamal version from <Big books of small projects>
    I modified to a Hex version. 
    
    I am think of a {}-digit hex number with no repeated digits.
    Try to guess the number. 
    Clues:
    Pico    one digit is correct but in the wrong position.
    Fermi   one digit is correct and in the wrong position.
    Bagels  No digit is correct.
    Example:
    secret number: 2a8 
    guess number: 8a6
    clues: Fermi Pico.'''.format(num_digits))

    while True:
        secret_number = get_secret_number()
        print('I have thought up a number.')
        print('You have {} guesses to get it.'.format(max_guesses))

        num_guesses = 1
        num_rang = list("0123456789abcdef")
        while num_guesses <= max_guesses:
            guess = ''
            while len(guess) != num_digits or not guess[0] in num_rang or not guess[1] in num_rang or not guess[2] in num_rang:
                print('Guesses #{}:'.format(num_guesses))
                guess = input('> ').lower()

            clues = get_clues(guess, secret_number)
            print(clues)
            num_guesses += 1

            if guess == secret_number:
                break
            if num_guesses > max_guesses:
                print('You ran out of guesses!')
                print('The secret number was {}'.format(secret_number))

        print('Play again? y/n')
        if not input('> ').lower().startswith('y'):
            break
    print('Play again')


def get_secret_number():
    numbers = list('0123456789abcdef')
    random.shuffle(numbers)
    secret_number = ''
    for i in range(num_digits):
        secret_number += str(numbers[i])
    return secret_number


def get_clues(guess, secret_number):
    if guess == secret_number:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_number[i]:
            clues.append('Fermi')
        elif guess[i] in secret_number:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)


if __name__ == '__main__':
    bagels()
