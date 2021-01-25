from app.models import allteam2020

def searchhistory(num, team):
    content = allteam2020.query.filter_by(num=num, teamname=team).all()[0]
    # print(content.history)
    return content.history
