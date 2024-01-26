import requests
from datetime import datetime, timedelta
import pickle

time_now = datetime.now()
time_yesterday = time_now - timedelta(days=1)
year = time_yesterday.year
month = time_yesterday.month
day = time_yesterday.day

link = f"https://newsapi.org/v2/everything?q=games&from={year}-{month}-{day}&sortBy=publishedAt&apiKey=20039c5603de46b897ab8aeb806cfb10"
news_json = requests.get(link).json()
with open('news_dump', 'wb') as file:
    pickle.dump(news_json, file)


