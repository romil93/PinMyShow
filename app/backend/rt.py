import requests
from pymongo import MongoClient
import json

from config import Config


def rt_search(search_string, limit, page):
    API_KEY = Config.API_KEY_RT
    search_url = "http://api.rottentomatoes.com/api/public/v1.0/movies.json?page_limit={0}&page={1}&apikey={2}&q={3}".format(
        limit,
        page,
        API_KEY,
        search_string)
    search_result = json.loads(requests.get(search_url).content)
    return search_result


def rt_boxoffice(limit):
    API_KEY = Config.API_KEY_RT
    search_url = "http://api.rottentomatoes.com/api/public/v1.0/lists/movies/box_office.json?limit={0}&country=in&apikey={1}".format(
        limit,
        API_KEY)
    search_result = json.loads(requests.get(search_url).content)
    return search_result


def rt_upcoming(limit, page):
    API_KEY = Config.API_KEY_RT
    search_url = "http://api.rottentomatoes.com/api/public/v1.0/lists/movies/upcoming.json?page_limit={0}&page={1}&country=in&apikey={2}".format(
        limit,
        page,
        API_KEY)
    search_result = json.loads(requests.get(search_url).content)
    return search_result


def db_lookup(imdb_id):
    client = MongoClient()
    db = client[Config.DB_MOVIES]
    collection = db[Config.COLLECTION_OMDB]
    return collection.find_one({'imdb_id': imdb_id})









