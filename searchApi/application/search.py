from flask import Flask, jsonify, Blueprint
from application import mongo


search = Blueprint('search', __name__, url_prefix='/search')
# search for specific news using a keyword
# and returning a json containing all selected articles's data
@search.route('/find/<keyword>', methods=['GET'])
def get_news_by_keyword(keyword):
    articles = mongo.db.bbc_articles

    articles_list = []
    article = articles.find()
    keyword = keyword.lower()

    for i in article:
        if keyword in i['title'] or keyword in i['text']:
            i.pop('_id')
            articles_list.append(i)

    return jsonify(articles_list)