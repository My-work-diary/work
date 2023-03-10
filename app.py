from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.qpskyvt.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.myworkdiary


@app.route('/video')
def video():
    return render_template('video.html')


@app.route('/main')
def main():
    return render_template('main.html')


@app.route('/')
def home():
    return render_template('cover.html')


@app.route('/resul')
def resul():
    return render_template('resul.html')

@app.route('/result')
def result():
    return render_template('result.html')

######################################################재욱님############################################
# youtube 링크 post
@app.route("/youtube", methods=["POST"])
def youtube_post():
    url_receive = request.form['url_give']
    workName_receive = request.form['workName_give']

    doc = {
        'url': url_receive,
        'workName': workName_receive
    }
    db.workVedio.insert_one(doc)

    return jsonify({'msg': '저장 완료!'})


# 운동 영상 보여주기
@app.route("/youtube", methods=["GET"])
def youtube_get():
    youtube_list = list(db.workVedio.find({}, {'_id': False}))

    return jsonify({'videos': youtube_list})


############################################윤선님#########################################

# -------목표 입력하기
@app.route("/goal", methods=["POST"])
def goal_post():
    title_receive = request.form['title_give']
    goal_num_receive = request.form['goal_num_give']
    goal_set_receive = request.form['goal_set_give']
    day_receive = request.form['day_give']

    goal_list = list(db.worklist.find({}, {'_id': False}))
    count = len(goal_list) + 1

    doc = {
        'num': count,
        'day': day_receive,
        'title': title_receive,
        'goal_num': int(goal_num_receive),
        'goal_set': int(goal_set_receive),
        'result_num': 0,
        'result_set': 0
    }
    find = db.worklist.find_one({'day': day_receive, 'title': title_receive})
    check = 0;
    if (find is None):
        check = 1;
        db.worklist.insert_one(doc)
    else:
        check = 0;

    return jsonify({'check': check})


# -------목표 보여주기
@app.route("/goal", methods=["GET"])
def goal_get():
    goal_list = list(db.worklist.find({}, {'_id': False}))
    return jsonify({'goals': goal_list})


# ----------목표 삭제
@app.route("/goal/delete", methods=["POST"])
def bucket_cancel():
    # day_receive = request.form['day_give']
    # title_receive = request.form['day_give']
    num_receive = request.form['num_give']
    print(num_receive)
    db.worklist.delete_one({'num': int(num_receive)})
    return jsonify({'msg': '삭제 완료'})


# -----목표 제목 셀렉트 박스에 보여주기
@app.route("/result/title", methods=["GET"])
def title_get():
    goal_list = list(db.worklist.find({}, {'_id': False}))
    return jsonify({'goals': goal_list})


# -----결과 입력하기
@app.route("/result/show", methods=["POST"])
def result_post():
    day_receive = request.form['day_give']
    title_receive = request.form['title_give']
    result_num_receive = request.form['result_num_give']
    result_set_receive = request.form['result_set_give']

    find = db.worklist.find_one({'day': day_receive, 'title': title_receive})
    check = 0;
    if (find is None):
        check = 0;
    else:
        check = 1;
        db.worklist.update_one({'title': title_receive, 'day': day_receive},
                               {'$set': {'result_num': int(result_num_receive), 'result_set': int(result_set_receive)}})

    return jsonify({'goal_check': check})


# -----결과 입력 보여주기
@app.route("/result/show", methods=["GET"])
def result_get():
    result_list = list(db.worklist.find({}, {'_id': False}))
    return jsonify({'results': result_list})


# ------결과 입력 페이지 연결



###############################################동윤님############################################



@app.route("/api/result", methods=["GET"])
def result_get2():
    result_list = list(db.worklist.find({}, {'_id': False}))

    return jsonify({'result': result_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
