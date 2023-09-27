import pandas

npa_csv = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter: row.code for (index, row) in npa_csv.iterrows()}
correct_guess = False
while not correct_guess:
    try:
        name = input("Write your name here: ").upper()
        new_list = [new_dict[letter] for letter in name]
    except KeyError:
        print("Sory, only letters in alphabet plesase")
    else:
        correct_guess = True
        print(new_list)
