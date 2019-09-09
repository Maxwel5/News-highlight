from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = "News Highlighter"
    bussiness_sources = get_sources('bussiness')
    world_sources = get_sources('world')
    entertainment_sources = get_sources('entertainment')
    sports_sources = get_sources('sports')
    
    render_template('index.html',title = title,bussiness_sources = bussiness_sources,world_sources = world_sources,entertainment_sources = entertainment_sources,sports_sources = sports_sources)