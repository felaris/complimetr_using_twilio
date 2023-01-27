import os
from twilio.rest import Client

from dotenv import load_dotenv
from flask import (
    Flask,
    flash, 
    render_template, 
    redirect,
    request,
    url_for,
)

load_dotenv()
app = Flask(__name__)
app.secret_key = "ssssh don't tell anyone"

TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
TWILIO_AUTH_TOKEN   = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_ACCOUNT_SID  = os.getenv('TWILIO_ACCOUNT_SID')

client = Client(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN)



def get_sent_messages():
    messages = client.messages.list(from_=TWILIO_PHONE_NUMBER)
    return messages

def send_message(to, body):
    message = client.messages.create(body=body,from_=TWILIO_PHONE_NUMBER,to=to)
              
    #print(message.sid)
#send_message("+233544956815","Hello, i am testing this to see if it works")

@app.route("/", methods=["GET"])
def index():
    messages = get_sent_messages()
    return render_template("index.html", messages=messages)

@app.route("/add-compliment", methods=["POST"])
def add_compliment():
    sender = request.values.get('sender', 'Someone')
    receiver = request.values.get('receiver', 'Someone')
    compliment = request.values.get('compliment', 'wonderful')
    to = request.values.get('to')
    body = f'{sender} says: {receiver} is {compliment}. See more compliments at {request.url_root}'
    send_message(to, body)
    flash('Your message was successfully sent')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
