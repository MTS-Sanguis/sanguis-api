# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class BloodStationGeoData(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, latitude=None, longitude=None):
        """
        BloodStationGeoData - a model defined in Swagger

        :param latitude: The latitude of this BloodStationGeoData.
        :type latitude: float
        :param longitude: The longitude of this BloodStationGeoData.
        :type longitude: float
        """
        self.swagger_types = {
            'latitude': float,
            'longitude': float
        }

        self.attribute_map = {
            'latitude': 'Latitude',
            'longitude': 'Longitude'
        }

        self._latitude = latitude
        self._longitude = longitude

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BloodStation_GeoData of this BloodStationGeoData.
        :rtype: BloodStationGeoData
        """
        return deserialize_model(dikt, cls)

    @property
    def latitude(self):
        """
        Gets the latitude of this BloodStationGeoData.

        :return: The latitude of this BloodStationGeoData.
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """
        Sets the latitude of this BloodStationGeoData.

        :param latitude: The latitude of this BloodStationGeoData.
        :type latitude: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """
        Gets the longitude of this BloodStationGeoData.

        :return: The longitude of this BloodStationGeoData.
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """
        Sets the longitude of this BloodStationGeoData.

        :param longitude: The longitude of this BloodStationGeoData.
        :type longitude: float
        """

        self._longitude = longitude

