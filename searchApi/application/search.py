from flask import Flask, jsonify, Blueprint
from application import mongo


search = Blueprint('search', __name__, url_prefix='/search')

@search.route('/find/<keyword>', methods=['GET'])
def get_news_by_keyword(keyword):
    '''
    args:
         keyword: used to filter serach results
    returns: 
         json object containing serach results
    '''
          
    articles = mongo.db.bbc_articles
    
    articles_list = []
    article = articles.find()
    keyword = keyword.lower()

    for i in article:
        if keyword in i['title'] or keyword in i['text']:
            i.pop('_id')
            articles_list.append(i)

    return jsonify(articles_list)