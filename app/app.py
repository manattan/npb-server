from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

from app.models import allteam2020
from app.check import start

start()

@app.route('/')
def index():
    contents = allteam2020.query.all()
    print(contents)
    return render_template("index.html", contents=contents)

@app.route('/uniform/<num>')
def uniform(num):
    contents = allteam2020.query.filter_by(num=num).all()
    print(contents)
    return render_template("num.html",contents=contents)

@app.route('/team/<logo>')
def team(logo):
    contents = allteam2020.query.filter_by(teamname=logo).all()
    print(contents)
    return render_template("team.html", contents=contents)

@app.route('/search', methods=["POST"])
def search():
    team = request.form["teamname"]
    num = request.form["number"]
    print("{}, {}".format(team, num))
    content = allteam2020.query.filter_by(num=num, teamname=team).all()
    print(content)
    if content == []:
        print('なかったね')
        return redirect(url_for("result", isExisted=False,num=num, teamname=team))
    else:
        return redirect(url_for("result", isExisted=True, history=content[0].history,num=num, teamname=team))

@app.route('/result')
def result():
    isExisted = request.args.get('isExisted')
    num=request.args.get('num')
    history=request.args.get('history')
    team=request.args.get('team')
    print(history)
    if (isExisted):
        return render_template("result.html", history=history, num=num,teamname=team)
    else:
        return render_template("result.html",num=num,teamname=team)
