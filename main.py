from apps.bagels import bagels
from apps.guessnumber import guessnumber
from apps.tosscoins import tosscoins


def main():
    while True:

        menu = ""
        while not menu in list("0123"):
            print("""
        1. Bagels game
        2. Guess number game
        3. Toss coins game
        0. Exit""")
            menu = input('> ')

        if menu == "1":
            bagels()
        elif menu == "2":
            guessnumber()
        elif menu == "3":
            tosscoins()
            print("empty slot")
        elif menu == "0":
            break


if __name__ == '__main__':
    main()
