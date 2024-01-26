import pickle


with open('news_dump', 'rb') as file:
    news_data = pickle.load(file)
print(news_data)