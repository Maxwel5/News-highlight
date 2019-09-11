from flask import render_template,request,url_for
from . import main
from ..request import get_news_sources,get_articles
from ..models import News_Sources

# Views
@main.route('/')
def index():
    allNews = get_news_sources()
    return render_template('index.html' , name = allNews)

@main.route('/news/<source>')
def sources(source):
    articles = get_articles(source)
    return render_template('articles.html',articles = articles)
    

