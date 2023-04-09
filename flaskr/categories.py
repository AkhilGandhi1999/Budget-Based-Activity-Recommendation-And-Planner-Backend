import requests
import datetime

from flask import (
    Blueprint, request, jsonify
)

bp = Blueprint('categories', __name__, url_prefix='/categories')

@bp.route('/get_categories', methods=('GET', 'POST'))
def get_categories():
    res = requests.post("http://127.0.0.1:5002/get_recommadations", json = request.get_json());
    return convertToRequiredFormat(res.json())

        
def convertToRequiredFormat(reponseBody):
    print(reponseBody)
    totalDays =  datetime.datetime.strptime(request.get_json().get('end_date'), '%Y-%m-%d').date().day - datetime.datetime.strptime(request.get_json().get('begin_date'), '%Y-%m-%d').date().day
    responseBodyToReturn = {}

    for i in range(totalDays+1):
        responseBodyToReturn.update({i+1 : []})

    day = 0
    for i in range((totalDays + 1) * 4):
        place = {}
        place['category'] = reponseBody.get('category')[i] 
        place['image'] = reponseBody.get('image')[i]
        place['location'] = reponseBody.get('location')[i]
        place['timeofday'] = reponseBody.get('timeofday')[i]
        place['rating'] = reponseBody.get('rating')[i]
        place['name'] = reponseBody.get('name')[i]
        place['price'] = reponseBody.get('price')[i]
        responseBodyToReturn.get(((int)((day/4) + 1))).append(place)
        day += 1

    return responseBodyToReturn