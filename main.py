from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

app = Flask(__name__)
CORS(app)

@app.route("/send-email", methods=["POST"])
def send_email():
    try:
        # Extract JSON data
        sender_email = request.form['sender_email']
        password = request.form['password']
        smtp_server = request.form['smtp_server']
        port = int(request.form['port'])
        recipient_emails = request.form.getlist('recipient_emails')  # Expecting multiple emails as a list
        subject = request.form['subject']
        html_content = request.form['html_content']

        # File upload handling
        uploaded_file = request.files.get('file')  # Expecting a file with key 'file'

        # Connect to SMTP server
        smtp = smtplib.SMTP(smtp_server, port)
        smtp.starttls()
        smtp.login(sender_email, password)

        # Send email to each recipient individually
        for recipient in recipient_emails:
            message = MIMEMultipart()
            message['Subject'] = subject
            message['From'] = sender_email
            message['To'] = recipient

            # Add HTML content
            html_part = MIMEText(html_content, 'html', 'utf-8')
            message.attach(html_part)

            # Add the uploaded file as an attachment, if present
            if uploaded_file:
                file_data = uploaded_file.read()
                attachment = MIMEBase('application', 'octet-stream')
                attachment.set_payload(file_data)
                encoders.encode_base64(attachment)
                attachment.add_header(
                    'Content-Disposition',
                    f'attachment; filename="{uploaded_file.filename}"'
                )
                message.attach(attachment)

            # Send the email
            smtp.sendmail(sender_email, recipient, message.as_string())

        smtp.quit()
        return jsonify({"success": True, "message": "Emails sent successfully!"})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    app.run(port=5000)
