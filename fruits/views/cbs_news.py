# importing some modules
from flask import Blueprint, request, redirect, render_template
from bs4 import BeautifulSoup
import requests
from fruits.models import CbsNews
from fruits import db
import json

cviews = Blueprint('cviews', __name__)

def get_cbs_news():
    url = "https://www.cbsnews.com/latest/rss/main"
    
    # get the data from xml site
    xml = requests.get(url) 

    data = []

    xml.content 
    soup = BeautifulSoup(xml.content, 'xml')

    xml_title = soup.find('title')
    #xml_title.text

    xml_link = soup.find('link')
    xml_image = soup.find('image')
    xml_description = soup.find('description')
      
#url = xml_title.text
            
            
    data.append({
        'title': xml_title,
        'link': xml_link,
        'image': xml_image,
        'description': xml_description
        })

    return data

     

@cviews.route('/cbs-news', methods=['GET', 'POST'])
def cbs_news():
     if request.method == 'POST':
        return redirect('/')

    # new data from cbs news
     data = get_cbs_news

    # existing data from database
     cnews = CbsNews.get_all_news()

    # loop through data
     for news in data:
        # check if news already exists in database
        if news.get('title').lower() not in [hn.title.lower() for hn in cnews]:
            cnew = CbsNews(xml_title=news['title'], xml_link=news['link'], xml_image=news['image'], xml_description=news['description'])
            cnew.save()
        else:
            continue

        return render_template('cbs_news.html', data=cnews)



@cviews.route('/cbs-news/search', methods=['GET', 'POST'])
def search_cbs_news():
    # /hacker-news/search?q=python
    query = request.args['q']
    # search in database for anythign that matches the query
    # SELECT * FROM hacker_news WHERE title LIKE '%python%'
    # data = db.session.query(HackerNews).filter(HackerNews.title.like(f'%{query}%')).all()
    # sql = text('SELECT * FROM hacker_news WHERE title LIKE :query')
    # data = db.engine.execute(sql, query=f'%{query}%').fetchall()
    data = CbsNews.query.filter(CbsNews.title.like(f'%{query}%')).all()
    # print(data)
    # [<HackNews 1>, <HackNews 2>]
    return {'data': [news.serialize() for news in data]}


@cviews.route('/search')
def search():
    return render_template('search.html')
