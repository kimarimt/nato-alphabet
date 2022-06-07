import pandas as pd


def get_nato():
    df = pd.read_csv('nato_phonetic_alphabet.csv')
    return {entry[0]: entry[1] for entry in df.values}


def main():
    word = input('Enter a word: ').upper()
    nato_scheme = get_nato()
    conversion = [nato_scheme[letter] for letter in word]
    print(conversion)


if __name__ == '__main__':
    main()
