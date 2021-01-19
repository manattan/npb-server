from app.models import uniformNumber

def searchhistory(num, team):
    content = uniformNumber.query.filter_by(num=num, team=team).all()[0]
    print(content)
    return content.history
