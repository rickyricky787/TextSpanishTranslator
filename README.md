# TextSpanishTranslator
A short Python script that enables you to text a phrase to a Twilio # from your phone and receive its Spanish translation

## Purpose
I simply did this small snippet for fun and to try out Twilio's API. An actual usage for this snippet could be for needing a Spanish translation when there is no internet available. It is meant to translate from English to Spanish, but you can input any language that Google translate supports, as it will auto-detect the language and translate the phrase in Spanish.

## How to Use
You must need a Twilio account and number. Register at https://www.twilio.com/try-twilio.
You also need a hosting service so that Twilio can connect to your localhost and recieve messages from your phone. "ngrok" is reccomended by Twilio, as it is easy to set up. Register at https://ngrok.com/ and follow download instructions.
- Clone this repo, and open the terminal on its directory
- On terminal: `pip3 install flask && pip3 install twilio && pip3 install googletrans==3.1.0a0`
- Run '`python3 main.py`
- Open another terminal tab and fire up "ngrok". Example: `./ngrok http 5000`
- Follow instructions on how to connect ngrok with Twilio here (Step 4): https://www.twilio.com/blog/2013/10/test-your-webhooks-locally-with-ngrok.html
- Pick up your phone, text to your Twilio number, and get a Spanish translation.

## Demo
 ![](demo.gif)
