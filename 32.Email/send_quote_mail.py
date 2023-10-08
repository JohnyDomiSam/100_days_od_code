import datetime as dt
from random import choice
import smtplib

my_email = "test.test@gmail.com"
password = "my_password"

# datetime object
now = dt.datetime.now()
weekday = now.weekday()

# list z txt súboru
with open(file="quotes.txt") as data:
    file = data.read()
    data_list = file.splitlines()
random_quote = choice(data_list)

# skontroluj či je správny deň a pošli mail s random_quote
if weekday == 3:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="jkubinec.test@yahoo.com",
            msg=f"Subject:Hello\n\n{random_quote}",
        )
else:
    print("wrong day")
