import urllib.request,json
from .models import News_Sources,Articles

# Getting api key
api_key = None

# Getting the news base url
base_url = None 

# Getting the articles url
# articles_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_SOURCES_BASE_URL']
    # articles_url = app.config['ARTICLES_BASE_URL']

def get_news_sources():

    get_news_sources_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_sources_url) as url:
        get_news_sources_data = url.read()
        get_news_sources_response = json.loads(get_news_sources_data)
        theoutput = None 
        if get_news_sources_response['sources']:
            news_results_list = get_news_sources_response['sources']
            theoutput = process_results(news_results_list)
    return theoutput


def process_results(sources_list):
    get_list=[]
    for newsitem in sources_list:
        id = newsitem.get('id')
        name = newsitem.get('name')
        description =newsitem.get('description')
        url = newsitem.get('url')
        obj = News_Sources(id,name,description,url)
        get_list.append(obj)
    return get_list


# news_sources_results = None

# if get_news_sources_response['results']:
# news_sources_results_list = get_news_sources_response['results']
# news_sources_results = process_results(news_sources_results_list)


# return news_sources_results

# def process_results(news_sources_list):
   
# news_sources_results = []
# for news_source_item in news_sources_list:
# id = news_source_item.get('id')
# name = news_source_item.get('name')
# news_object = News(id,name)
# news_sources_result.append(news_object)
# return news_sources_results




def get_articles(id):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_details_url = 'https://newsapi.org/v2/top-headlines?sources={}&apikey={}'.format(id,api_key)

    with urllib.request.urlopen(get_articles_details_url) as url:
        articles_details_data = url.read()
        articles_details_response = json.loads(articles_details_data)

        if articles_details_response['articles']:
            article_details_response_data=articles_details_response['articles']
            new_articles = process_articles(article_details_response_data)

    return new_articles

def process_articles(articles_list):
    ''' Function  that processes the articles result and converts them to a list of Objects '''
    articles = []
    for article_details_response in articles_list:
        id = article_details_response.get('id')
        author = article_details_response.get('author')
        title = article_details_response.get('title')
        description = article_details_response.get('description')
        url = article_details_response.get('url')
        image = article_details_response.get('urlToImage')
        date = article_details_response.get('publishedAt')
        content = article_details_response.get('content')

        articles_object = Articles(id,author,title,description,url,image,date,content)
        articles.append(articles_object)
    return articles