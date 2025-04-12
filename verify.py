from flask import Flask, request, render_template, redirect, url_for, session
from twilio.rest import Client
import random
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Twilio config
account_sid = 'ACd121ee485b93ab2d2bc71c0421d45102'
auth_token = '7d03660600f12c4b7a22b898ed988eb1'
twilio_whatsapp_number = '917990261094'

client = Client(account_sid, auth_token)

# Route: Home page - Get phone number
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        phone = request.form['phone']
        otp = str(random.randint(100000, 999999))
        session['otp'] = otp
        session['phone'] = phone

        message = client.messages.create(
            from_=twilio_whatsapp_number,
            body=f"Your WhatsApp OTP is {otp}",
            to=f'whatsapp:{phone}'
        )
        return redirect(url_for('verify'))

    return render_template('index.html')

# Route: Verify OTP
@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        user_otp = request.form['otp']
        if user_otp == session.get('otp'):
            return "✅ OTP Verified Successfully!"
        else:
            return "❌ Incorrect OTP. Try again."

    return render_template('verify.html')

if __name__ == '__main__':
    app.run(debug=True)
