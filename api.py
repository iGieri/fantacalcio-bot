from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from pymongo import MongoClient
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv

load_dotenv()

db_client = MongoClient(f"mongodb+srv://root:{os.environ['DB_PASSWORD']}@stats.bibxu.mongodb.net/?retryWrites=true&w=majority")
db = db_client.stats

app = Flask(__name__)

CORS(app)


@app.route('/api/data', methods=['GET'])
def data():
    query = db.data.find_one()

    print(query)

    return jsonify({"servers": query['servers'], "users": query['users']})



app.run("0.0.0.0", 8080, False)
