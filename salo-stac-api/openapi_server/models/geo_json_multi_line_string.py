# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class GeoJSONMultiLineString(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type=None, coordinates=None, bbox=None):  # noqa: E501
        """GeoJSONMultiLineString - a model defined in OpenAPI

        :param type: The type of this GeoJSONMultiLineString.  # noqa: E501
        :type type: str
        :param coordinates: The coordinates of this GeoJSONMultiLineString.  # noqa: E501
        :type coordinates: List[List[List[float]]]
        :param bbox: The bbox of this GeoJSONMultiLineString.  # noqa: E501
        :type bbox: List[float]
        """
        self.openapi_types = {
            'type': str,
            'coordinates': List[List[List[float]]],
            'bbox': List[float]
        }

        self.attribute_map = {
            'type': 'type',
            'coordinates': 'coordinates',
            'bbox': 'bbox'
        }

        self._type = type
        self._coordinates = coordinates
        self._bbox = bbox

    @classmethod
    def from_dict(cls, dikt) -> 'GeoJSONMultiLineString':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GeoJSON_MultiLineString of this GeoJSONMultiLineString.  # noqa: E501
        :rtype: GeoJSONMultiLineString
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self):
        """Gets the type of this GeoJSONMultiLineString.


        :return: The type of this GeoJSONMultiLineString.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GeoJSONMultiLineString.


        :param type: The type of this GeoJSONMultiLineString.
        :type type: str
        """
        allowed_values = ["MultiLineString"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def coordinates(self):
        """Gets the coordinates of this GeoJSONMultiLineString.


        :return: The coordinates of this GeoJSONMultiLineString.
        :rtype: List[List[List[float]]]
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this GeoJSONMultiLineString.


        :param coordinates: The coordinates of this GeoJSONMultiLineString.
        :type coordinates: List[List[List[float]]]
        """
        if coordinates is None:
            raise ValueError("Invalid value for `coordinates`, must not be `None`")  # noqa: E501

        self._coordinates = coordinates

    @property
    def bbox(self):
        """Gets the bbox of this GeoJSONMultiLineString.


        :return: The bbox of this GeoJSONMultiLineString.
        :rtype: List[float]
        """
        return self._bbox

    @bbox.setter
    def bbox(self, bbox):
        """Sets the bbox of this GeoJSONMultiLineString.


        :param bbox: The bbox of this GeoJSONMultiLineString.
        :type bbox: List[float]
        """

        self._bbox = bbox
