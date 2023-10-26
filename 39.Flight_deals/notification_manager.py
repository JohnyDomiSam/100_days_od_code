import smtplib


class NotificationManager:

    def __init__(self, price, dep_city_name, dep_iata_code, arr_city_name, arr_airport_iata, o_date, i_date):
        self.my_email = "kubinec.jan.test@gmail.com"
        self.password = ""
        self.message = f'Low price alert! Only {price} to fly from {dep_city_name}-{dep_iata_code} to {arr_city_name}-{arr_airport_iata}, from {o_date} to {i_date}'

    def send_email(self):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.password)
            connection.sendmail(
                from_addr=self.my_email,
                to_addrs="kubinec.jan.test@gmail.com",
                msg=f"Subject:Hello\n\n{self.message}",
            )
