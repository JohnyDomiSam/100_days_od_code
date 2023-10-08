import pandas as pd
import smtplib
from random import choice
import datetime as dt

my_email = "my_email@gmail.com"
password = "my_password"

letters = [
    "letter_templates/letter_1.txt",
    "letter_templates/letter_2.txt",
    "letter_templates/letter_3.txt",
]

# dict from pandas DataFrame
pd_data_frame = pd.read_csv("birthdays.csv")
new_dict = {
    (row.month, row.day): (row.r_name, row.email)
    for (index, row) in pd_data_frame.iterrows()
}

# datetime object
now = dt.datetime.now()
today_date = (now.day, now.month)
rec_name = new_dict[today_date][0]
rec_email = new_dict[today_date][1]

# check bithday, change name and send email
if today_date in new_dict:
    random_letter = choice(letters)

    with open(random_letter, "r") as letter:
        str_letter = letter.read()
        new_letter = str_letter.replace("[NAME]", rec_name)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=rec_email,
            msg=f"Subject:Hello\n\n{new_letter}",
        )
