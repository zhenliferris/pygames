import random


def guessnumber():
    maxlimit = 100

    while True:
        print("I am thinking a number between 0 and {}".format(maxlimit))
        target_number = random.randint(0, 100)
        count_guessed = 1

        while True:
            guess = ""
            while not guess.isdecimal() or int(guess) > maxlimit or int(guess) < 0:
                guess = input('> ')

            if int(guess) == target_number:
                break
            elif int(guess) < target_number:
                print("go larger")
            else:
                print("go smaller")

            count_guessed += 1

        print("the number was {}, your guess {} times".format(
            target_number, count_guessed))
        replay = input("play again? y/n ")
        if not replay.lower().startswith('y'):
            break

    print("thanks for playing")


if __name__ == '__main__':
    guessnumber()
