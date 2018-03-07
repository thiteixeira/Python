'''
Run with 
  $ FLASK_APP=server.py flask run
and
  $ ./ngrok http 5000
'''

from flask import Flask, request
import requests
import random
import re

app = Flask(__name__)

FB_API_URL = 'https://graph.facebook.com/v2.6/me/messages'
VERIFY_TOKEN = 'e504rm2gv+77aiMnPe/SDibL2X7Wxp6ZzcRY7TdjU6E=' # generated using $openssl rand -base64 32
# generated from FB page
PAGE_ACCESS_TOKEN = 'EAAFGeXmRGRQBAFA73UuoubSMMkGt3Jf9TkOatCeZBOCOR2QMgEeMUTCxYaLknvKvLjVdVB5HAWbJZBqoRpgMEqr8ZAZBVSFZC3WwWeB23svZBuHHjnZAIaCmpoZAc3oGhOXWUWZBHhHMC7dPn9KuWWw5ThsdxAVrHGYZATMqVi9O1KywZDZD'

# Define variables
name = "Mona"
weather = "snowy"

# Define a dictionary with the predefined responses
responses = {
  "what's your name?": [
      "my name is {0}".format(name),
      "they call me {0}".format(name),
      "I go by {0}".format(name)
   ],
  "what's today's weather?": [
      "the weather is {0}".format(weather),
      "it's {0} today".format(weather)
    ],
  "default": ["default message"]
}

def get_bot_response(message):
    """This is just a dummy function, returning a variation of what
    the user said. Replace this function with one connected to chatbot."""
    #return "This is a dummy response to '{}'".format(message)
    
    # Check if the message is in the responses
    if message in responses:
        # Return the matching message
        bot_message = random.choice(responses[message])
    else:
        # Return the "default" message
        bot_message = random.choice(responses["default"])
    return bot_message


def verify_webhook(req):
    print req.args.get("hub.verify_token")
    if req.args.get("hub.verify_token") == VERIFY_TOKEN:
        return req.args.get("hub.challenge")
    else:
        return "incorrect"

def respond(sender, message):
    """Formulate a response to the user and
    pass it on to a function that sends it."""
    response = get_bot_response(message)
    send_message(sender, response)


def is_user_message(message):
    """Check if the message is a message from the user"""
    return (message.get('message') and
            message['message'].get('text') and
            not message['message'].get("is_echo"))

def send_message(recipient_id, text):
    """Send a response to Facebook"""
    payload = {
        'message': {
            'text': text
        },
        'recipient': {
            'id': recipient_id
        },
        'notification_type': 'regular'
    }

    auth = {
        'access_token': PAGE_ACCESS_TOKEN
    }

    response = requests.post(
        FB_API_URL,
        params=auth,
        json=payload
    )

    return response.json()

@app.route("/webhook",methods=['GET','POST'])
def listen():
    """This is the main function flask uses to 
    listen at the `/webhook` endpoint"""
    if request.method == 'GET':
        print request
        return verify_webhook(request)

    if request.method == 'POST':
        payload = request.json
        event = payload['entry'][0]['messaging']
        for x in event:
            if is_user_message(x):
                text = x['message']['text']
                sender_id = x['sender']['id']
                respond(sender_id, text)

        return "ok"
