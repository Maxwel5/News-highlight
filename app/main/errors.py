from flask import render_template
from . import main

@main.app_errorhandler(404)
def four_Zero_four(error):
    return render_template('fourZerofour.html'),404