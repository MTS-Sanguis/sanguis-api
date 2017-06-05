# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.blood_station import BloodStation
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestDefaultController(BaseTestCase):
    """ DefaultController integration test stubs """

    def test_get_blood_station_by_id(self):
        """
        Test case for get_blood_station_by_id

        
        """
        response = self.client.open('/bloodstation/{id}'.format(id=56),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_blood_stations(self):
        """
        Test case for get_blood_stations

        
        """
        response = self.client.open('/bloodstations',
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
