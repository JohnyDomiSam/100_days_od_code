import requests

CHAT_ID = "1383520281"
TELEGRAM_URL = "https://api.telegram.org/bot6769511991:AAGTePHE8DMpUVITwrJVIwnbcQVVdN9lWRI/sendMessage"


class NotificationManager:

    def __init__(self, message):
        self.message = message
        self.parameters = {"chat_id": CHAT_ID,
                           "text": self.message}

    def send_telegram(self):
        self.response = requests.post(url=TELEGRAM_URL, params=self.parameters)
        self.response.raise_for_status()
