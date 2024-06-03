from bottle import post, request, template
from datetime import date, datetime
import json
import re

@post('/articles', method='post')
def addarticle():
    title = request.forms.get('TITLE')
    description = request.forms.get('DESCRIPTION')
    username = request.forms.get('USERNAME')
    link = request.forms.get('LINK')
    current_date = datetime.now()
    string = current_date.strftime('%Y-%m-%d %H:%M:%S')
    try:
        # �������� ������� ���� "calchistory.json" ��� ������
        with open("static\\articles.json", "r") as read_json:
            # ��������� ������ �� ����� � ������ articles
            articles = json.load(read_json)
    except FileNotFoundError:
            # ���� ���� �� ������, ������� ����� ������� history � ������� �������� ��� ������� ���������    
            articles = []



    articles.append({title:{'author': username, 'text': description, 'link': link, 'date': string}})
    with open("static\\articles.json", 'w') as outfile:
        json.dump(articles, outfile, indent = 3)
    
    return template('articles.tpl',title='Articles',
        message='Your articles page.',
        year=datetime.now().year,
        data=articles)
