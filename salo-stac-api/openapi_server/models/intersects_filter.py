# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.geometry import Geometry
from openapi_server import util

from openapi_server.models.geometry import Geometry  # noqa: E501

class IntersectsFilter(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, intersects=None):  # noqa: E501
        """IntersectsFilter - a model defined in OpenAPI

        :param intersects: The intersects of this IntersectsFilter.  # noqa: E501
        :type intersects: Geometry
        """
        self.openapi_types = {
            'intersects': Geometry
        }

        self.attribute_map = {
            'intersects': 'intersects'
        }

        self._intersects = intersects

    @classmethod
    def from_dict(cls, dikt) -> 'IntersectsFilter':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The intersectsFilter of this IntersectsFilter.  # noqa: E501
        :rtype: IntersectsFilter
        """
        return util.deserialize_model(dikt, cls)

    @property
    def intersects(self):
        """Gets the intersects of this IntersectsFilter.


        :return: The intersects of this IntersectsFilter.
        :rtype: Geometry
        """
        return self._intersects

    @intersects.setter
    def intersects(self, intersects):
        """Sets the intersects of this IntersectsFilter.


        :param intersects: The intersects of this IntersectsFilter.
        :type intersects: Geometry
        """

        self._intersects = intersects
