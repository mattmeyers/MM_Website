import os
from flask import Flask, render_template, redirect, url_for, request
from flask_mail import Mail, Message
from smtplib import SMTPException

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

    @app.route('/send_email', methods=["POST"])
    def send_email():
        msg = Message(
            'Website Message',
            sender=os.getenv('MAIL_USER'),
            recipients=[os.getenv('MAIL_RECEIVER')]
        )
        msg.body = f'Name: {request.form["name"]}\n\nEmail: {request.form["email"]}\n\nMessage: {request.form["message"]}'
        mail.send(msg)
        return redirect(url_for('contact'))

    @app.route('/')
    def about():
        return render_template('about.html')

    @app.route('/resume')
    def resume():
        return render_template('resume.html')

    @app.route('/projects')
    def projects():
        return render_template('projects.html')

    @app.route('/contact', methods=["GET","POST"])
    def contact():
        if (request.method == "POST"):
            msg = Message(
                'Website Message',
                sender=os.getenv('MAIL_USER'),
                recipients=[os.getenv('MAIL_RECEIVER')]
            )
            msg.body = f'Name: {request.form["name"]}\n\nEmail: {request.form["email"]}\n\nMessage: {request.form["message"]}'
            try:
                mail.send(msg)
                return render_template('contact.html', success=1)
            except SMTPException as e:
                return render_template('contact.html', success=0)

        return render_template('contact.html')

    return app
