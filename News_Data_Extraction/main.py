#Fetch the titles and descriptions of news articles given a start and  #end date for news articles search and a news topic

import requests

def get_news(topic,
             from_date,
             to_date,
             language='en',
             api_key='60f1f0108af54deaab996e728b94e9ca'):
    r = requests.get(
        f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}'
    )

    content = r.json()
    print(content)
    articles = content['articles']
    results = []
    for article in articles:
        print(
            f'Title\n{article["title"]} \nDescription\n{article["description"]}'
        )

        results.append(
        f'Title\n{article["title"]} \nDescription\n{article["description"]}')

    return results


print(get_news(topic='space', from_date='2024-6-29', to_date='2024-7-28'))


      
