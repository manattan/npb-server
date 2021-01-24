from app.models import Main

def searchhistory(num, team):
    content = Main.query.filter_by(num=num, teamname=team).all()[0]
    print(content)
    return content.history
