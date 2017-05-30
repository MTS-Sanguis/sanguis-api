import connexion
from swagger_server.models.blood_station import BloodStation
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def bloodstations_get():
    """
    bloodstations_get
    

    :rtype: List[BloodStation]
    """
    return 'do some magic!'
