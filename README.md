# API Documentation: Send Email with Attachments

## Overview
This API provides functionality to send emails to one or more recipients with optional file attachments. It uses an SMTP server to authenticate and send the emails.

## Base URL
- `http://127.0.0.1:5000`

## Endpoint
### `/send-email`

**Method:** `POST`

### Description
Sends an email with the provided details and optional file attachments to one or more recipients.

### Headers
- `Content-Type: multipart/form-data`

### Request Parameters
The request should be sent as `multipart/form-data` with the following fields:

| Key               | Type              | Required | Description |
|-------------------|-------------------|----------|-------------|
| `sender_email`    | `string`          | Yes      | The sender's email address. |
| `password`        | `string`          | Yes      | The password for the sender's email account. |
| `smtp_server`     | `string`          | Yes      | The SMTP server address (e.g., `smtp.gmail.com`). |
| `port`            | `integer`         | Yes      | The SMTP server port (e.g., `587` for TLS). |
| `recipient_emails`| `list of strings` | Yes      | A list of recipient email addresses. Use multiple fields with the same key for multiple recipients. |
| `subject`         | `string`          | Yes      | The subject of the email. |
| `html_content`    | `string`          | Yes      | The HTML content of the email. |
| `file`            | `file`            | No       | A file to be attached to the email. Optional. |

### Example cURL Request
```bash
curl -X POST http://127.0.0.1:5000/send-email \
-H "Content-Type: multipart/form-data" \
-F "sender_email=your_email@example.com" \
-F "password=your_password" \
-F "smtp_server=smtp.example.com" \
-F "port=587" \
-F "recipient_emails=recipient1@example.com" \
-F "recipient_emails=recipient2@example.com" \
-F "subject=Test Email with Attachment" \
-F "html_content=<h1>Hello, World!</h1>" \
-F "file=@path_to_file"
```

### Response
#### Success
```json
{
  "success": true,
  "message": "Emails sent successfully!"
}
```

#### Error
```json
{
  "success": false,
  "error": "<error message>"
}
```

### Error Handling
Common errors include:
- **SMTP Authentication Failure:** Incorrect sender email or password.
- **Invalid SMTP Server:** The SMTP server or port is incorrect.
- **File Handling Error:** The file upload or attachment process failed.
- **Recipient Errors:** Invalid email addresses.

### Notes
- Ensure the SMTP server and port are correctly configured for the email provider.
- For Gmail, you may need to enable "Less Secure Apps" or generate an app-specific password.
- Use valid email addresses for both sender and recipients.

## Running the API
To run the API locally, execute the script and access it on `http://127.0.0.1:5000`.
```bash
python app.py
```

