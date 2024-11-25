from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)
CORS(app) 

@app.route("/send-email", methods=["POST"])
def send_email():
    data = request.json
    try:
        sender_email = data['sender_email']
        password = data['password']
        smtp_server = data['smtp_server']
        port = data['port']
        recipient_emails = data['recipient_emails']
        subject = data['subject']
        html_content = data['html_content']

        message = MIMEMultipart("alternative")
        message['Subject'] = subject
        message['From'] = sender_email
        message['To'] = ", ".join(recipient_emails)

        html_part = MIMEText(html_content, 'html')
        message.attach(html_part)

        smtp = smtplib.SMTP(smtp_server, port)
        smtp.starttls()
        smtp.login(sender_email, password)
        smtp.sendmail(sender_email, recipient_emails, message.as_string())
        smtp.quit()

        return jsonify({"success": True, "message": "Email sent successfully!"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


if __name__ == '__main__':
  app.run(port=5000)
