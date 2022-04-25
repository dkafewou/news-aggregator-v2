import os
import aiohttp
import json
from src.schemas.news import News


NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
NEW_API_URL = "https://newsapi.org/v2/top-headlines?q={}&apiKey={}&category={}"
REDDIT_API_URL = "https://www.reddit.com/r/news.json"
REDDIT_API_SEARCH_URL = "https://www.reddit.com/r/news/search.json?q={}"


async def request(url):
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.get(url, ssl=False) as response:
            data = await response.text()
            return json.loads(data)


async def get_news_api_info(query):
    result = await request(NEW_API_URL.format(query, NEWS_API_KEY, "general"))

    response = []
    for article in result.get('articles'):
        response.append(
            json.loads(News(headline=article.get('title'), link=article.get('url'), source="newsapi").to_json())
        )

    return response


async def get_reddit_info(query):
    url = REDDIT_API_URL
    if query:
        url = REDDIT_API_SEARCH_URL.format(query)

    result = await request(url)
    response = []
    articles = result.get('data').get('children')
    for article in articles:
        data = article.get('data')
        response.append(
            json.loads(News(headline=data.get('title'), link=data.get('url'), source="reddit").to_json())
        )

    return response


async def get_news(query):
    news_api_result = await get_news_api_info(query)
    reddit_result = await get_reddit_info(query)

    return news_api_result + reddit_result
