from flask import Flask
from flask_mail import Mail, Message

app =Flask(__name__)
mail=Mail(app)

app.config.update(
            DEBUG=True,
            #EMAIL SETTINGS
            MAIL_SERVER='smtp.gmail.com',
            MAIL_PORT=587,
            MAIL_USE_SSL=False,
            MAIL_USE_TLS=True,
            MAIL_USERNAME = 'ziguangtest@gmail.com',
            MAIL_PASSWORD = 'ziguangzhiye2011',
            )

mail=Mail(app)

@app.route("/")
def index():
    msg = Message(
    'Hello',
    sender='ziguangtest@gmail.com',
    recipients=
     ['ziguangtest@gmail.com'])
    msg.body = "This is the email body"
    print("before send")
    with app.app_context():
        mail.send(msg)
    print("after send")
    return "Sent"

if __name__ == "__main__":
    app.run(host = "10.117.174.214")
