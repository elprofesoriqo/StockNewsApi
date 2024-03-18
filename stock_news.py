import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://newsapi.org/v2/everything"



API_KEY = "A5A4GD61MV221GR5"
REQUEST= "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=YOUR_STOCK_SYMBOL&apikey=YOUR_API_KEY"

stock_parametrs = {
    "function": "TIME_SERIES_DAILY" ,
    "symbol": STOCK,
    "apikey": API_KEY
}
r = requests.get(REQUEST, params=stock_parametrs)
data = r.json()["Time Series (Daily)"]
data_list = [ value for key, value in data.items() ]
current_price_close = data_list[0]['4. close']
data_data= [key for key, value in data.items()]
current_date=data_data[0]
previous_day_price_close = data_list[1]['4. close']
previous_day_data=data_data[5]




API_NEWS_KEY = "692a441e098341f8b64e95a9fa302bbc"
NEWS_ENDPOINT= "https://newsapi.org/v2/everything?"




if abs((float(current_price_close) - float(previous_day_price_close)) / float(previous_day_price_close)) >= 0.05:
    news_parametrs= {
    "apiKey": API_NEWS_KEY,
    "q": COMPANY_NAME,
    "from": previous_day_data,
    "to": current_date,
    "sortBy": "popularity",
    "language": "en",
    "pageSize": 50
    }

    r_news= requests.get(NEWS_ENDPOINT, news_parametrs)
    data_news= r_news.json()["articles"][:3]


    format = [f"Headline: {article['title']}. \n Brief: {article['description']}" for article in data_news]
    # client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    # for article in format:
    #     message = client.messages.create(
    #         body=article,
    #         from_=VIRTUAL_TWILIO_NUMBER,
    #         to=VERIFIED_NUMBER
    # )



