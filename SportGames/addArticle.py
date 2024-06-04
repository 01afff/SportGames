from bottle import post, request, template
from datetime import date, datetime
import json
import re


regex = re.compile(r'\d{2}.\d{2}.\d{4}$')

def isValidDate(date):
    try:  
        if re.fullmatch(regex, date):
            if(datetime.strptime(date, '%d.%m.%Y') <= datetime.now()): 
                return True
        return False
    except:
        return False
         


@post('/articles', method='post')
def addarticle():
    title = request.forms.get('TITLE')
    description = request.forms.get('DESCRIPTION')
    username = request.forms.get('USERNAME')
    link = request.forms.get('LINK')
    current_date = request.forms.get('DATE')
    if(not isValidDate(current_date)):
        return f"Incorrect date! The date must be in the format \"dd.MM.yyyy\"!" 
    

    try:
        # �������� ������� ���� "calchistory.json" ��� ������
        with open("static\\articles.json", "r") as read_json:
            # ��������� ������ �� ����� � ������ articles
            articles = json.load(read_json)
    except FileNotFoundError:
            # ���� ���� �� ������, ������� ����� ������� history � ������� �������� ��� ������� ���������    
            articles = []
    except:
        articles = []


    articles.append({title:{'author': username, 'text': description, 'link': link, 'date': current_date}})
    if(articles != []):
        articles.sort(key=lambda x: x[list(x.keys())[0]]['date'], reverse=True)
    with open("static\\articles.json", 'w') as outfile:
        json.dump(articles, outfile, indent = 3)
    

    return template('articles.tpl',title='Articles',
        message='Your articles page.',
        year=datetime.now().year,
        data=articles)
