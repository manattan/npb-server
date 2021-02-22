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


@app.route('/api/team', methods=["GET"])
def searchByTeam():
    team = request.args.get('team')
    print('GET searchByTeam ', team)
    query = "select * from allteam2020 where teamname='{}' order by id ASC;".format(
        team)
    result = get_all(query)
    response = []
    for i in range(len(result)):
        response.append(
            {'teamname': result[i].teamname, 'num': result[i].num, 'history': result[i].history, 'id': result[i].id})
    return jsonify({'data': response})

@app.route('/api/num', methods=["GET"])
def searchByNum():
    num = request.args.get('num')
    print('GET searchByNum ', num)
    query = "select * from allteam2020 where num='{}' order by id ASC;".format(
        num)
    result = get_all(query)
    response = []
    for i in range(len(result)):
        response.append(
            {'teamname': result[i].teamname, 'num': result[i].num, 'history': result[i].history, 'id': result[i].id})
    return jsonify({'data': response})



@app.route('/api/keyword', methods=["GET"])
@cross_origin(supports_credentials=True)
def searchByKeyword():
    key = request.args.get('keyword')
    print('GET searchByKeyword ', key)
    query = "select * from allteam2020 where history like '%%{}%%' order by id ASC;".format(
        key)
    result = get_all(query)
    response = []
    for i in range(len(result)):
        response.append(
            {'teamname': result[i].teamname, 'num': result[i].num, 'history': result[i].history,'id': result[i].id})
    return jsonify({'data': response})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2000, debug=True)
