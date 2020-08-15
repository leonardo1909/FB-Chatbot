from flask import Flask, request
from pymessenger.bot import Bot
from decouple import config

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{config("DB_USER")}:{config("DB_PASSWORD")}@{config("DB_HOST")}:5432/{config("DB_NAME")}'
db = SQLAlchemy(app)
# migrate = Migrate(app, db)

ACCESS_TOKEN = config('ACCESS_TOKEN')
VERIFY_TOKEN = config('VERIFY_TOKEN')
bot = Bot(ACCESS_TOKEN)


class User(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    facebook_id = db.Column(
        db.String(200),
        unique=True,
        nullable=False
    )


class Message(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    user = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False
    )
    message = db.Column(
        db.String(200),
        nullable=False
    )
    response = db.Column(
        db.String(200),
        nullable=False
    )


@app.route('/', methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    else:
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    recipient_id = message['sender']['id']
                    message_text = message['message'].get('text')
                    if message_text:
                        if len(message_text) > 280 or not message_text.isnumeric():
                            send_message(recipient_id, message_text)
                        else:
                            user = User.query.filter_by(
                                facebook_id=recipient_id
                            )
                            if not user:
                                user = User(
                                    facebook_id=recipient_id
                                )
                                db.session.add(user)
                                db.session.commit()
                            else:
                                user = user.first()

                            message_number = int(message_text)

                            response = ''
                            if message_number % 3 == 0:
                                response += 'Fizz'
                            if message_number % 5 == 0:
                                response += 'Buzz'
                            if not response:
                                response = str(message_number)

                            message = Message(
                                user=user.id,
                                message=message_text,
                                response=response
                            )
                            # message.user.append(user)
                            db.session.add(message)
                            db.session.commit()

                            send_message(recipient_id, response)
    return "response done"


def verify_fb_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Token de verificação inválido.'


def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    return


# Add description here about this if statement.
if __name__ == "__main__":
    app.run()
