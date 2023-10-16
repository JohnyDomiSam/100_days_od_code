import requests

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
response = requests.get(url=NEWS_URL, params=news_parameters)
response.raise_for_status()
data = response.json()
title = data["articles"][0]["title"]
article = data["articles"][0]["description"]
print(article)


def get_news():
    response = requests.get(url=URL, params=parameters)
    response.raise_for_status()
    data = response.json()
    date_list = list(data["Time Series (Daily)"])
    y_close = float(data["Time Series (Daily)"][date_list[0]]["4. close"])
    b_close = float(data["Time Series (Daily)"][date_list[1]]["4. close"])
    diff = 100 * round(((y_close - b_close)/((y_close + b_close)/2)), 2)
    if diff > 5:
        return f"{diff} %, big move !"
    else:
        return f"{diff} %, small move"





## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

