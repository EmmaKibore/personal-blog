from flask_mail import Message
from flask import render_template
from . import mail

<<<<<<< HEAD
def mail_message(subject,template,to,**kwargs):
   sender_email = 'emmaKibore@gmail.com'

   email = Message(subject, sender=sender_email, recipients=[to])
   email.body= render_template(template + ".txt",**kwargs)
   email.html = render_template(template + ".html",**kwargs)
   mail.send(email)
=======
def mail_message(subject,template,to, **kwargs):
    sender_email = 'emmaKibore@gmail.com'

    email = Message(subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt", **kwargs)
    email.html = render_template(template + ".html", **kwargs)
    mail.send(email)
>>>>>>> 14aae2dcc0c6ce0324a855cec00bb71830ae2709
