with open("./Mail Merge Project Start/Input/Names/invited_names.txt", "r") as names:
    names_list = names.readlines()

print(names_list)

for name in names_list:
    with open(
        "./Mail Merge Project Start/Input/Letters/starting_letter.txt", "r"
    ) as letter:
        str_letter = letter.read()
        new_name = name.rstrip()
        new_letter = str_letter.replace("[name]", new_name)

        with open(
            f"./Mail Merge Project Start/Output/ReadyToSend/{new_name}.txt",
            "w",
        ) as next_letter:
            next_letter.write(new_letter)
