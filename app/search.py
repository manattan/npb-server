from app.models import uniformNumber

def search(num, team):
    content = uniformNumber.query.filter_by(num=num, team=team).all()[0]
    print(content)
    return content.history
