from flask import current_app, render_template
from flask_mail import Message

from xanadu import mail


def send_email(to, subject, template, **kwargs):
    """send out xanadu's emails """
    msg = Message(
        subject,
        sender=current_app.config['MAIL_USERNAME'],
        recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)
