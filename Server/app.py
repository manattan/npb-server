from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool

app = Flask(__name__)
CORS(app, support_credentials=True)

engine = create_engine(
    f'postgresql://manattan:@localhost/npb', poolclass=QueuePool)


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


def convertToRes(arr):
    response = []
    for i in range(len(arr)):
        response.append(
            {'teamname': arr[i].teamname, 'num': arr[i].num, 'history': arr[i].history, 'id': arr[i].id})
    return response


@app.route('/api/team', methods=["GET"])
def searchByTeam():
    team = request.args.get('team')
    print('GET searchByTeam ', team)
    query = "select * from info where teamname='{}' order by id ASC;".format(
        team)
    result = get_all(query)
    response = convertToRes(result)
    return jsonify({'data': response})


@app.route('/api/num', methods=["GET"])
def searchByNum():
    num = request.args.get('num')
    print('GET searchByNum ', num)
    query = "select * from info where num='{}' order by id ASC;".format(
        num)
    result = get_all(query)
    response = convertToRes(result)
    return jsonify({'data': response})


@app.route('/api/keyword', methods=["GET"])
def searchByKeyword():
    key = request.args.get('keyword')
    print('GET searchByKeyword ', key)
    query = "select * from info where history like '%%{}%%' order by id ASC;".format(
        key)
    result = get_all(query)
    response = convertToRes(result)
    return jsonify({'data': response})


@app.route('/api/register/user', methods=["POST"])
def registerUser():
    payload = request.json
    currentq = "select * from userlist"
    res = get_all(currentq)
    id = len(res) + 1
    print({'id': id, 'uid': payload.get('uid'), 'email': payload.get(
        'email'), 'name': payload.get('name')})
    query = "insert into userlist values({}, '{}', '{}', '{}')".format(
        id, payload.get('uid'), payload.get('email'), payload.get('name'))
    insert(query)
    return jsonify({'data': 1})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2000, debug=True)
