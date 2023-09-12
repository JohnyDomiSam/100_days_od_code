import pandas

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
npa_csv = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter: row.code for (index, row) in npa_csv.iterrows()}

name = input("Write your name here: ").upper()
new_list = [new_dict[letter] for letter in name]
print(new_list)
