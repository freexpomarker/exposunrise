from flask import Flask, jsonify
import json

app = Flask(r4tyoink)

@app.route('/get-data', methods=['GET'])
def get_data():
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
