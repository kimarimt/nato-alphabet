import pandas as pd
import os
import time


def clear():
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')


def get_nato():
    df = pd.read_csv('nato_phonetic_alphabet.csv')
    return {entry[0]: entry[1] for entry in df.values}


def main():
    try:
        word = input('Enter a word: ').upper()
        nato_scheme = get_nato()
        conversion = [nato_scheme[letter] for letter in word]
    except KeyError:
        print('only letters in the alphabet must be in the word')
        clear()
        main()
    else:
        print(conversion)


if __name__ == '__main__':
    main()
