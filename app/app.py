from flask import Flask, render_template

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

if __name__ == "__main__":
    app.run(debug=True)