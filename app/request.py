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

def get_movie(id):
    get_movie_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_movie_details_url) as url:
        movie_details_data = url.read()
        movie_details_response = json.loads(movie_details_data)

        movie_object = None
        if movie_details_response:
            id = movie_details_response.get('id')
            title = movie_details_response.get('original_title')
            overview = movie_details_response.get('overview')
            poster = movie_details_response.get('poster_path')
            vote_average = movie_details_response.get('vote_average')
            vote_count = movie_details_response.get('vote_count')

            movie_object = Movie(id,title,overview,poster,vote_average,vote_count)

    return movie_object

def search_movie(movie_name):
    search_movie_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(api_key,movie_name)
    with urllib.request.urlopen(search_movie_url) as url:
        search_movie_data = url.read()
        search_movie_response = json.loads(search_movie_data)
        search_movie_results = None

        if search_movie_response['results']:
            search_movie_list = search_movie_response['results']
            search_movie_results = process_results(search_movie_list)

    return search_movie_results