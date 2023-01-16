from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.qpskyvt.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.myworkdiary

@app.route('/')
def home():
    return render_template('video.html')

#youtube 링크 post
@app.route("/youtube", methods=["POST"])
def youtube_post():
    url_receive = request.form['url_give']
    workName_receive = request.form['workName_give']

    doc = {
        'url': url_receive,
        'workName': workName_receive
    }
    db.workVedio.insert_one(doc)

    return jsonify({'msg':'저장 완료!'})

#운동 영상 보여주기
@app.route("/youtube", methods=["GET"])
def youtube_get():
    youtube_list = list(db.workVedio.find({}, {'_id': False}))

    return jsonify({'videos': youtube_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)