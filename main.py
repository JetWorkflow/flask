from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/hello')
def hello():
    return 'Hello, World!'

from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app) 

@app.route('/save-email', methods=['POST', 'OPTIONS'])
def save_email():
    if request.method == 'OPTIONS':  
        return '', 200  

    if request.method == 'POST':  
        try:
            data = request.json
            html_content = data['content']
            
            with open("temp_email_content.html", "w") as file:
                file.write(html_content)
            
            return jsonify({"message": "Content saved successfully"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000)  


if __name__ == '__main__':
  app.run(port=5000)
