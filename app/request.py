import urllib.request,json
from .models import News

# Getting api key
api_key = None

# Getting the news base url
base_url = None 

# Getting the articles url
articles_url = None

def configure_request(app):
    global api_key,base_url,articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_SOURCES_BASE_URL']
    articles_url = app.config['ARTICLES_BASE_URL']

def get_news_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_sources_url) as url:
        get_news_sources_data = url.read()
        get_news_sources_response = json.loads(get_news_sources_data)


        news_sources_results = None

        if get_news_sources_response['results']:
            news_sources_results_list = get_news_sources_response['results']
            news_sources_results = process_results(news_sources_results_list)


    return news_sources_results

def process_results(news_sources_list):
    '''
    Function  that processes the news_sources result and changes them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        news_sources_results: A list of news_sources objects
    '''
    news_sources_results = []
    for news_sources_item in news_sources_list:
        id = news_source_item.get('id')
        title = news_source_item.get('title')
        illustration = news_source_item.get('illustration')
        url = news_source_item.get('url')
        group = news_source_item.get('group')
        language = news_source_item.get('language')
        nation = news_source_item.get('nation')

        if poster:
            news_sources_object = News_sources(id,title,language,illustration,nation,url,group)
            news_sources_results.append(news_sources_object)

    return news_sources_results

def get_articles(id):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_articles_details_url) as url:
        articles_data = url.read()
        articles_response = json.loads(articles_data)

        articles_object = None
        if articles_response['articles']:
            
    return articles_object

def process_articles(articles_list):
	'''
    Function  that processes the articles result and converts them to a list of Objects
	'''
	articles_object = []
	for article_item in articles_list:
		id = article_item.get('id')
		narrator = article_item.get('narrator')
		title = article_item.get('title')
		illustration = article_item.get('illustration')
		url = article_item.get('url')
		image = article_item.get('urlToImage')
		date = article_item.get('documentedOn')
		
		if image:
			articles_result = Articles(id,narrator,title,illustration,url,image,date)
			articles_object.append(articles_result)

    return articles_object	


def search_news_sources(news_sources_name):
    search_news_sources_url = 'https://newsapi.org/v2/sources?apiKey=e7d60ddf9e4e4569af60f7177443303c'.format(api_key,news_name)
    with urllib.request.urlopen(search_news_sources_url) as url:
        search_news_sources_data = url.read()
        search_news_sources_response = json.loads(search_news_sources_data)
        search_movie_results = None

        if search_news_sources_response['results']:
            search_news_sources_list = search_news_sources_response['results']
            search_news_sources_results = process_results(search_news_sources_list)

    return search_news_sources_results