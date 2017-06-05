import connexion
from swagger_server.models.answer_path import AnswerPath
from swagger_server.models.blood_station import BloodStation
from swagger_server.models.questionnaire import Questionnaire
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

import yaml


def get_blood_station_by_id(id):
    """
    get_blood_station_by_id
    
    :param id: 
    :type id: int

    :rtype: BloodStation
    """
    return 'do some magic!'


def get_blood_stations():
    """
    get_blood_stations
    

    :rtype: List[BloodStation]
    """
    return 'do some magic!'


def get_questionnaire():
    """
    get_questionnaire
    

    :rtype: Questionnaire
    """
    return Questionnaire.from_dict(yaml.load(open('questionnaire.yaml')))


def post_answers(answers=None):
    """
    post_answers
    
    :param answers: 
    :type answers: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        answers = AnswerPath.from_dict(connexion.request.get_json())
    return 'do some magic!'
