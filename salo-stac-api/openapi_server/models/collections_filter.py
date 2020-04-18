# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class CollectionsFilter(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, collections=None):  # noqa: E501
        """CollectionsFilter - a model defined in OpenAPI

        :param collections: The collections of this CollectionsFilter.  # noqa: E501
        :type collections: List[str]
        """
        self.openapi_types = {
            'collections': List[str]
        }

        self.attribute_map = {
            'collections': 'collections'
        }

        self._collections = collections

    @classmethod
    def from_dict(cls, dikt) -> 'CollectionsFilter':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The collectionsFilter of this CollectionsFilter.  # noqa: E501
        :rtype: CollectionsFilter
        """
        return util.deserialize_model(dikt, cls)

    @property
    def collections(self):
        """Gets the collections of this CollectionsFilter.

        Array of Collection IDs to include in the search for items. Only Items in one of the provided Collections will be searched.  # noqa: E501

        :return: The collections of this CollectionsFilter.
        :rtype: List[str]
        """
        return self._collections

    @collections.setter
    def collections(self, collections):
        """Sets the collections of this CollectionsFilter.

        Array of Collection IDs to include in the search for items. Only Items in one of the provided Collections will be searched.  # noqa: E501

        :param collections: The collections of this CollectionsFilter.
        :type collections: List[str]
        """

        self._collections = collections
