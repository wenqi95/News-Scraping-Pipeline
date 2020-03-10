import requests
from json import loads

DEFAULT_SOURCES = [CNN]
CNN = 'cnn'
SORT_BY_TOP = 'top'
NEWS_API_KEY = ''
NEWS_API_ENDPOINT = "https://newsapi.org/v1/"
ARTICLES_API = "article"

def _buildUrl(endPoint = NEWS_API_ENDPOINT, apiName = ARTICLES_API):
    return endPoint + apiName
 
def getNewsFromSource(sources = DEFAULT_SOURCES, sortBy = SORT_BY_TOP):
    articles = []

    for source in sources:
        payload = {'apiKey' : NEWS_API_KEY,
                   'source' : source,
                   'sourBy' : sortBy} 
        response = requests.get(_buildUrl(), params = payload)
        res_json = loads(response.content.decode('utf-8'))