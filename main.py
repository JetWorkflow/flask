from flask import Flask, request, jsonify
from flask_cors import CORS
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

        # Connect to SMTP server
        smtp = smtplib.SMTP(smtp_server, port)
        smtp.starttls()
        smtp.login(sender_email, password)

        # Send email to each recipient individually
        for recipient in recipient_emails:
            message = MIMEMultipart("alternative")
            message['Subject'] = subject
            message['From'] = sender_email
            message['To'] = recipient

            html_part = MIMEText(html_content, 'html')
            message.attach(html_part)

            smtp.sendmail(sender_email, recipient, message.as_string())

        smtp.quit()

        return jsonify({"success": True, "message": "Emails sent successfully!"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    app.run(port=5000)
