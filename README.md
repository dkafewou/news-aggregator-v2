# news-aggregator-v2

## How to set up (MacOS)

requirement: Python3.6+, NEWS_API_KEY (Register https://newsapi.org/register to get the api key)

- Clone the repo `git clone https://github.com/dkafewou/news-aggregator-v2.git` and `cd news-aggregator-v2`
- Create a virtual env `python3 -m venv news-env` and `source news-env/bin/activate` to activate it
- Install requirement `pip3 install -r requirements.txt`
- Export the api key `export NEWS_API_KEY='YOUR_NEWS_API_KEY'`
- To run the server `uvicorn main:app --reload` and server will be  running on http://127.0.0.1:8000 and http://127.0.0.1:8000/docs for doc
- To run test `pytest`