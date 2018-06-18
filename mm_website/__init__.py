import os
from flask import Flask, render_template
from flask_mail import Mail, Message

def create_app(test_config=None):
    app = Flask(__name__)
    mail = Mail(app)

    app.config.update(
        MAIL_SERVER='smtp.gmail.com',
        MAIL_PORT=465,
        MAIL_USE_SSL=True,
        MAIL_USERNAME=os.getenv('MAIL_USER'),
        MAIL_PASSWORD=os.getenv('MAIL_PASS')
    )

    mail = Mail(app)

    @app.route('/email')
    def email():
        msg = Message(
            'THIS IS A TEST',
            sender=os.getenv('MAIL_USER'),
            recipients=['mmeyers.07.95@gmail.com']
        )
        msg.body = "THIS IS A TEST MESSAGE BODY"
        mail.send(msg)
        return "Sent"

    @app.route('/')
    def about():
        return render_template('about.html')

    @app.route('/resume')
    def resume():
        return render_template('resume.html')

    @app.route('/projects')
    def projects():
        return render_template('projects.html')

    @app.route('/contact')
    def contact():
        return render_template('contact.html')

    return app
