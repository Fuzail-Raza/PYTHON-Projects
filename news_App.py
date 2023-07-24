import requests
from newsapi import NewsApiClient

url = ('https://newsapi.org/v2/top-headlines?'
       'q=ESPN&'
       'country=us&'
       'apiKey=0687204042684a59b465c2212cce056d')

response = requests.get(url)
text=response.json()
print(text['articles'][0]['author'])
print(text['articles'][0]['title'])

for headline in text['articles']:
    print(headline['description'])