import requests
from twilio.rest import Client

DIFF = 0
# Alphavantage API info
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "2SZZQRRMGD5LMQ9I"
URL = "https://www.alphavantage.co/query?"
parameters = {"function": "TIME_SERIES_DAILY",
              "symbol": STOCK,
              "apikey": API_KEY}

# Newsapi API info
NEWS_API_KEY = "f9c8979709224cb7b19fa2b77c8f8ba9"
NEWS_URL = "https://newsapi.org/v2/top-headlines"
news_parameters = {"q": "Tesla",
                   "category": "business",
                   "country": "us",
                   "apiKey": "f9c8979709224cb7b19fa2b77c8f8ba9"}

# Twilio info
account_sid = 'AC89d90d3e2bc457fe9433e12f1d26f32d'
auth_token = "auth_token"
print(auth_token)


def get_move():
    response_ts = requests.get(url=URL, params=parameters)
    response_ts.raise_for_status()
    data_ts = response_ts.json()
    date_list = list(data_ts["Time Series (Daily)"])
    y_close = float(data_ts["Time Series (Daily)"][date_list[0]]["4. close"])
    b_close = float(data_ts["Time Series (Daily)"][date_list[1]]["4. close"])
    global DIFF
    DIFF = 100 * round(((y_close - b_close) / ((y_close + b_close) / 2)), 2)
    return DIFF


if get_move() > 3 or get_move() < -3:
    response = requests.get(url=NEWS_URL, params=news_parameters)
    response.raise_for_status()
    data = response.json()
    title = data["articles"][0]["title"]
    article = data["articles"][0]["description"]
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"TSLA: {DIFF}%\nHeadline: {title}\nBrief: {article}",
        from_='+18182931791',
        to='+421905993795'
    )
