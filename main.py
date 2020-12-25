from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from googletrans import Translator

app = Flask(__name__)

@app.route("/sms", methods=["GET", "POST"])
def sms_reply():

    # Get the message recieved
    message = request.form['Body']

    # Translate the message
    translator = Translator()
    translation = translator.translate(message, dest='es')

    # Send the translation back
    resp = MessagingResponse()
    resp.message(translation.text)

    return str(resp)

if __name__ == "__main__":
    app.run(debug="True")