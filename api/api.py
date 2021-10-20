from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)


@app.route('/api/data', methods=['GET'])
def data():
    query = ''

    with open('stats.json', 'r') as db:
        query = db.read()
    
    print(query)

    return query

@app.route('/api/sendData', methods=['POST'])
def receiveData():
    data = request.get_json()

    print(data)

    with open('stats.json', 'w') as db:
        db.write(f'''{{
    "servers": {data['servers']},
    "users": {data['users']}
}}
''')

    return 'Thank you'

app.run("0.0.0.0", 8080, False)
