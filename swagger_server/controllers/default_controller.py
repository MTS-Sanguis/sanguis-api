import connexion
from swagger_server.models.inline_response_200 import InlineResponse200
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def bloodstations_get():
    """
    bloodstations_get
    

    :rtype: List[InlineResponse200]
    """
    return 'do some magic!'
