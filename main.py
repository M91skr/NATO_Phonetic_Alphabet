# ---------------------------------------- Add Required Library ----------------------------------------

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# ---------------------------------------- Create Word List ----------------------------------------

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


# ---------------------------------------- get word ----------------------------------------

def generate_phonetic():
    word = input("Enter a word: ").upper()

    # ---------------------------------------- Nato List Suggestion ----------------------------------------

    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
