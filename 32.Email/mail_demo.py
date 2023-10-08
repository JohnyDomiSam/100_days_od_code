import smtplib

my_email = "kubinec.jan.test@gmail.com"
password = "mdiavnbjmaklxydx"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="jkubinec.test@yahoo.com",
        msg="Subject:Hello\n\nHello",
    )
