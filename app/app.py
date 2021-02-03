from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

from app.models import allteam2020

@app.route('/')
def index():
    contents = allteam2020.query.all()
    return render_template("index.html", contents=contents)

@app.route('/uniform/<num>')
def uniform(num):
    contents = allteam2020.query.filter_by(num=num).all()
    return render_template("num.html",contents=contents)

@app.route('/team/<logo>')
def team(logo):
    contents = allteam2020.query.filter_by(teamname=logo).all()
    return render_template("team.html", contents=contents)

@app.route('/search', methods=["POST"])
def search():
    team = request.form["teamname"]
    num = request.form["number"]
    content = allteam2020.query.filter_by(num=num, teamname=team).all()
    if content == []:
        print('なかったね')

        return render_template("result.html",num=num, teamname=team)
    else:
        print(team)
        print(num)
        return render_template("result.html", isExisted=True,teamname=team, history=content[0].history,num=num)

@app.route('/result')
def result():
    isExisted = request.args.get('isExisted')
    num=request.args.get('num')
    history=request.args.get('history')
    team=request.args.get('team')
    if (isExisted):
        return render_template("result.html", history=history, num=num,teamname=team)
    else:
        return render_template("result.html",num=num,teamname=team)

