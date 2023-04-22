import requests

from flask import (
    Blueprint, request, jsonify
)

bp = Blueprint('hotels', __name__, url_prefix='/hotels')

# @bp.route('/get_hotel_ammenities')
# def get_hotel_ammenities():
#     res = requests.get("http://127.0.0.1:5200/get_ammenities");
#     return res.json()

@bp.route('/get_hotel_recommandations')
def get_hotel_recommandations():
    print('asdfsadfas')
    res = requests.get("http://127.0.0.1:5200/get_hotel_recommandations");
    return convertToRequiredFormat(res.json())

def convertToRequiredFormat(reponseBody):
    responseBodyToReturn = {}

    totalDays = 3
    for i in range(totalDays+1):
        responseBodyToReturn.update({i+1 : []})

    for i in range((totalDays + 1)):
        place = {}
        place['address'] = reponseBody.get('address')[i] 
        place['experience'] = reponseBody.get('experience')[i]
        place['image'] = reponseBody.get('image')[i]
        place['location'] = reponseBody.get('location')[i]
        place['name'] = reponseBody.get('name')[i]
        place['rating'] = reponseBody.get('rating')[i]
        responseBodyToReturn.get(i + 1).append(place)
    
    return responseBodyToReturn