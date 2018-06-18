import os
from flask import Flask, render_template

def create_app(test_config=None):
    app = Flask(__name__)

    @app.route('/')
    def about():
        return render_template('about.html')

    @app.route('/resume')
    def resume():
        return render_template('resume.html')

    @app.route('/projects')
    def projects():
        return render_template('projects.html')

    return app
