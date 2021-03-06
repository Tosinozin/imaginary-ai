"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 06 January, 2018 @ 12:19 AM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
from flask import request, escape, flash
from flask_mail import Mail, Message

from views import app, back

mail = Mail(app)


@app.route('/contact/', methods=['POST'])
def contact():
    # Form elements
    name = escape(request.form['name'])
    email = escape(request.form['email'])
    message = escape(request.form['message'])
    # Message
    msg = Message(subject='Imaginary A.I. Contact form',
                  sender=(name, email),
                  recipients=['javafolabi@gmail.com'])
    msg.body = message
    mail.send(msg)
    flash('Message successfully sent')
    return back.redirect()
