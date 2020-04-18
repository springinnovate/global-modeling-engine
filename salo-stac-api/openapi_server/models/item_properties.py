# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class ItemProperties(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, datetime=None):  # noqa: E501
        """ItemProperties - a model defined in OpenAPI

        :param datetime: The datetime of this ItemProperties.  # noqa: E501
        :type datetime: str
        """
        self.openapi_types = {
            'datetime': str
        }

        self.attribute_map = {
            'datetime': 'datetime'
        }

        self._datetime = datetime

    @classmethod
    def from_dict(cls, dikt) -> 'ItemProperties':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The itemProperties of this ItemProperties.  # noqa: E501
        :rtype: ItemProperties
        """
        return util.deserialize_model(dikt, cls)

    @property
    def datetime(self):
        """Gets the datetime of this ItemProperties.

        Either a date-time or an interval, open or closed. Date and time expressions adhere to RFC 3339. Open intervals are expressed using double-dots.  Examples:  * A date-time: \"2018-02-12T23:20:50Z\" * A closed interval: \"2018-02-12T00:00:00Z/2018-03-18T12:31:12Z\" * Open intervals: \"2018-02-12T00:00:00Z/..\" or \"../2018-03-18T12:31:12Z\"  Only features that have a temporal property that intersects the value of `datetime` are selected.  If a feature has multiple temporal properties, it is the decision of the server whether only a single temporal property is used to determine the extent or all relevant temporal properties.  # noqa: E501

        :return: The datetime of this ItemProperties.
        :rtype: str
        """
        return self._datetime

    @datetime.setter
    def datetime(self, datetime):
        """Sets the datetime of this ItemProperties.

        Either a date-time or an interval, open or closed. Date and time expressions adhere to RFC 3339. Open intervals are expressed using double-dots.  Examples:  * A date-time: \"2018-02-12T23:20:50Z\" * A closed interval: \"2018-02-12T00:00:00Z/2018-03-18T12:31:12Z\" * Open intervals: \"2018-02-12T00:00:00Z/..\" or \"../2018-03-18T12:31:12Z\"  Only features that have a temporal property that intersects the value of `datetime` are selected.  If a feature has multiple temporal properties, it is the decision of the server whether only a single temporal property is used to determine the extent or all relevant temporal properties.  # noqa: E501

        :param datetime: The datetime of this ItemProperties.
        :type datetime: str
        """
        if datetime is None:
            raise ValueError("Invalid value for `datetime`, must not be `None`")  # noqa: E501

        self._datetime = datetime
