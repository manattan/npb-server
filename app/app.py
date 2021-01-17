from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

from app.models import uniformNumber

@app.route('/')
def index():
    contents = uniformNumber.query.all()
    print(contents)
    return render_template("index.html", contents=contents)

@app.route('/uniform/<num>')
def uniform(num):
    contents = uniformNumber.query.filter_by(num=num).all()
    print(contents)
    return render_template("num.html",contents=contents)

@app.route('/team/<logo>')
def team(logo):
    contents = uniformNumber.query.filter_by(team=logo).all()
    print(contents)
    return render_template("team.html", contents=contents)

@app.route('/search', methods=["POST"])
def search():
    team = request.form["team"]
    num = request.form["number"]
    print("{}, {}".format(team, num))
    content = uniformNumber.query.filter_by(num=num, team=team).all()
    print(content)
    if content == []:
        print('なかったね')
        return redirect(url_for("result", isExisted=False,num=num, team=team))
    else:
        return redirect(url_for("result", isExisted=True, history=content[0].history,num=num, team=team))

@app.route('/result')
def result():
    isExisted = request.args.get('isExisted')
    num=request.args.get('num')
    history=request.args.get('history')
    team=request.args.get('team')
    print(history)
    if (isExisted):
        return render_template("result.html", history=history, num=num,team=team)
    else:
        return render_template("result.html",num=num,team=team)


if __name__ == "__main__":
    app.run(debug=True)