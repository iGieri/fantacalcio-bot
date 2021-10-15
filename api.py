from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3


conn = sqlite3.connect('data.db')

cur = conn.cursor()

# cur.execute('''drop table data''')

cur.execute('''
create table data (
    servers integer,
    users integer
)
''')

conn.commit()

conn.close()


app = Flask(__name__)

CORS(app)


@app.route('/api/data', methods=['GET'])
def data():
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    query = cur.execute('select * from data')

    return jsonify({'servers': query[-1][0], 'users': query[-1][1]})

@app.route('/api/sendData', methods=['POST'])
def receiveData():
    data = request.get_json()

    conn = sqlite3.connect('data.db')

    cur = conn.cursor()

    cur.execute(f"insert into data values({data['servers']}, {data['users']})")

    conn.commit()

    conn.close()

    return 'Thank you'

app.run("localhost", 8080, True)