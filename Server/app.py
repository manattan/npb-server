from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool
import os

app = Flask(__name__)
CORS(app, support_credentials=True)

URL = os.environ["DATABASE"]

engine = create_engine(
    URL, poolclass=QueuePool)

def get_all(query):
    con = engine.connect()
    try:
        return con.execute(query).fetchall()
    finally:
        con.close()


def insert(query):
    con = engine.connect()
    try:
        return con.execute(query)
    finally:
        con.close()


def convertData(arr):
    response = []
    for i in range(len(arr)):
        response.append(
            {'teamname': arr[i].teamname, 'num': arr[i].num, 'history': arr[i].history, 'id': arr[i].id})
    return response


def convertReq(arr):
    response = []
    for i in range(len(arr)):
        response.append({'id': arr[i].id, 'uid': arr[i].uid, 'dataid': arr[i].dataid,
                         'prevent': arr[i].prevent, 'new': arr[i].new, 'merged': arr[i].merged})
    return response


@app.route('/api/team', methods=["GET"])
def searchByTeam():
    team = request.args.get('team')
    query = "select * from info where teamname='{}' order by id ASC;".format(
        team)
    result = get_all(query)
    response = convertData(result)
    return jsonify({'data': response})


@app.route('/api/num', methods=["GET"])
def searchByNum():
    num = request.args.get('num')
    query = "select * from info where num='{}' order by id ASC;".format(
        num)
    result = get_all(query)
    response = convertData(result)
    return jsonify({'data': response})


@app.route('/api/keyword', methods=["GET"])
def searchByKeyword():
    key = request.args.get('keyword')
    query = "select * from info where history like '%%{}%%' order by id ASC;".format(
        key)
    result = get_all(query)
    response = convertData(result)
    return jsonify({'data': response})


@app.route('/api/register/user', methods=["POST"])
def registerUser():
    payload = request.json
    currentq = "select * from userlist;"
    res = get_all(currentq)
    for i in range(len(res)):
        if res[i]['uid'] == payload.get('uid'):
            print({'info': 'すでに会員登録されています'})
            return jsonify({'info': 'すでに会員登録されています'})
    id = len(res) + 1
    query = "insert into userlist values({}, '{}', '{}', '{}');".format(
        id, payload.get('uid'), payload.get('email'), payload.get('name'))
    insert(query)
    print({'info': '新規登録しました'})
    return jsonify({'info': '新規登録しました'})


@app.route('/api/editrequest', methods=["POST"])
def requestEdit():
    payload = request.json
    currentq = "select * from request"
    res = get_all(currentq)
    id = len(res) + 1
    query = "insert into request values({}, '{}', {}, '{}', '{}', {});".format(
        id, payload.get('uid'), payload.get('id'), payload.get('prevent'), payload.get('new'), 0)
    insert(query)
    print({'info': 'リクエストが登録されました'})
    return jsonify({'info': 'リクエストが登録されました'})


@app.route('/api/getRequest', methods=["GET"])
def getRequest():
    query = "select * from request where merged=0;"
    results = get_all(query)
    response = convertReq(results)
    return jsonify({'data': response})

@app.route('/api/mergeRequest', methods=["POST"])
def mergeRequest():
    id = request.json.get('id')
    print({'id: ', id})
    query = "select * from request where id={};".format(id)
    results = get_all(query)
    print(results)
    alterquery = "update info set history='{}' where id={}".format(results[0].new, results[0].dataid)
    print(alterquery)
    insert(alterquery)
    mergequery = "update request set merged=1 where id={}".format(id)
    insert(mergequery)
    print({'info': 'リクエストがmergeされました'})
    return jsonify({'info': 'リクエストがmergeされました'})

@app.route('/api/rejectRequest', methods=["POST"])
def rejectRequest():
    id = request.json.get('id')
    query = "update request set merged=2 where dataid={}".format(id)
    insert(query)
    print({'info': 'リクエストがrejectされました'})
    return jsonify({'info': 'リクエストがrejectされました'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2000, debug=True)
