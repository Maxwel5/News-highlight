from flask import render_template
from . import main
from ..request import get_sources, get_articles
from ..models import sources

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = "News highlight"
    bussiness_sources = get_sources('bussiness')
    world_sources = get_sources('world')
    entertainment_sources = get_sources('entertainment')
    sports_sources = get_sources('sports')
    
    return render_template('index.html',title = title,bussiness_sources = bussiness_sources,world_sources = world_sources,entertainment_sources = entertainment_sources,sports_sources = sports_sources)

@main.route('sources/<id>')
def index(id):
    '''
    article page to be viewed
    '''
    articles = get_articles(id)
    title =f'News highlight | {id}'

    return render_template('article.html',title = title,articles = articles)