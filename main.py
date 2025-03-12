from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

def call_external_api():
    url = "https://demo.jetworkflow.com/ims/jetapi.php"
    
    params = {
        "method": "addSubRecord",
        "key": "ef0ba794a21b38b605517a507d1cd08c",
        "id_form": 105,
        "project": "autotest",
        "id_parent": 2,
        "text2": "Sample Value for Text2",
        "text3": "Sample Value for Text3"
    }

    response = requests.get(url, params=params)
    return {
        "status_code": response.status_code,
        "response_text": response.text
    }

@app.route('/run-api', methods=['GET'])
def run_api():
    result = call_external_api()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
