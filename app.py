from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow requests from HTML form

# Replace with your email credentials
EMAIL_ADDRESS = 'your_email@gmail.com'
EMAIL_PASSWORD = 'your_app_password'  # Use Gmail App Password

@app.route('/', methods=['POST'])
def receive_message():
    data = request.form
    sender_email = data.get('email')
    message = data.get('message')

    try:
        msg = MIMEText(f"Message from {sender_email}:\n\n{message}")
        msg['Subject'] = "New Message from Zone Creators"
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS  # Send to yourself

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        return jsonify({'status': 'Message sent successfully'}), 200
    except Exception as e:
        return jsonify({'status': 'Failed', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
