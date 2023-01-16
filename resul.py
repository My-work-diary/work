from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.qpskyvt.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.myworkdiary

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/api/result", methods=["GET"])
def result_get():
    result_list = list(db.worklist.find({}, {'_id': False}))

    return jsonify({'result': result_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)