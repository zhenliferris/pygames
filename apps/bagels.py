import random

# the number of digits will affect the diffcuty of the game,
# the maximum guess should be increased if the number of digits adding up.
num_digits = 3
max_guesses = 10

# the main function of bagels game.


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

    # unlimited main(first) loop unless the user choose not
    while True:

        secret_number = get_secret_number()
        print('I have thought up a number.')
        print('You have {} guesses to get it.'.format(max_guesses))

        # initialize guess counter
        num_guesses = 1

        # HEX number contains 0 to F
        num_rang = list("0123456789ABCDEF")

        # second loop untill guess counter reaches limit or guessed the correct number
        while num_guesses <= max_guesses:
            guess = ''
            # restrain the input is 3 digits long HEX number, it needs to be modified for other digits
            while len(guess) != num_digits or not guess[0] in num_rang or not guess[1] in num_rang or not guess[2] in num_rang:
                print('Guesses #{}:'.format(num_guesses))
                guess = input('> ').lower()  # avoding Capital Letter issue

            clues = get_clues(guess, secret_number)
            print(clues)
            num_guesses += 1

            # rember guess & secret_number are strings not numbers.
            if guess == secret_number:
                break  # break when guessed the correct number
            if num_guesses > max_guesses:
                print('You ran out of guesses!')

        # after second loop showing the correct number and count of guesses
        print('The secret number was {}'.format(secret_number))

        # any input not satring with Y or y will break the main loop
        print('Play again? y/n')
        if not input('> ').lower().startswith('y'):
            break

    # ending of the game
    print('Thanks for your playing!')

# the function of generating n digits random HEX numbers


def get_secret_number():
    numbers = list('0123456789abcdef')
    random.shuffle(numbers)
    secret_number = ''
    for i in range(num_digits):
        secret_number += str(numbers[i])  # string not a number
    return secret_number

# the function of comparing two strings


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
        clues.sort()  # blending the clue messages
        return ' '.join(clues)


# if not executing directly then using it as module.
if __name__ == '__main__':
    bagels()
