# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class BloodStationWeekWorkingHours(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, week_day=None, working_hours=None):
        """
        BloodStationWeekWorkingHours - a model defined in Swagger

        :param week_day: The week_day of this BloodStationWeekWorkingHours.
        :type week_day: str
        :param working_hours: The working_hours of this BloodStationWeekWorkingHours.
        :type working_hours: str
        """
        self.swagger_types = {
            'week_day': str,
            'working_hours': str
        }

        self.attribute_map = {
            'week_day': 'WeekDay',
            'working_hours': 'WorkingHours'
        }

        self._week_day = week_day
        self._working_hours = working_hours

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BloodStation_WeekWorkingHours of this BloodStationWeekWorkingHours.
        :rtype: BloodStationWeekWorkingHours
        """
        return deserialize_model(dikt, cls)

    @property
    def week_day(self):
        """
        Gets the week_day of this BloodStationWeekWorkingHours.

        :return: The week_day of this BloodStationWeekWorkingHours.
        :rtype: str
        """
        return self._week_day

    @week_day.setter
    def week_day(self, week_day):
        """
        Sets the week_day of this BloodStationWeekWorkingHours.

        :param week_day: The week_day of this BloodStationWeekWorkingHours.
        :type week_day: str
        """
        allowed_values = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
        if week_day not in allowed_values:
            raise ValueError(
                "Invalid value for `week_day` ({0}), must be one of {1}"
                .format(week_day, allowed_values)
            )

        self._week_day = week_day

    @property
    def working_hours(self):
        """
        Gets the working_hours of this BloodStationWeekWorkingHours.

        :return: The working_hours of this BloodStationWeekWorkingHours.
        :rtype: str
        """
        return self._working_hours

    @working_hours.setter
    def working_hours(self, working_hours):
        """
        Sets the working_hours of this BloodStationWeekWorkingHours.

        :param working_hours: The working_hours of this BloodStationWeekWorkingHours.
        :type working_hours: str
        """

        self._working_hours = working_hours

