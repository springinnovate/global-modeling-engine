# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Link(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, href=None, rel=None, type=None, hreflang=None, title=None, length=None, method='GET', headers=None, body=None, merge=False):  # noqa: E501
        """Link - a model defined in OpenAPI

        :param href: The href of this Link.  # noqa: E501
        :type href: str
        :param rel: The rel of this Link.  # noqa: E501
        :type rel: str
        :param type: The type of this Link.  # noqa: E501
        :type type: str
        :param hreflang: The hreflang of this Link.  # noqa: E501
        :type hreflang: str
        :param title: The title of this Link.  # noqa: E501
        :type title: str
        :param length: The length of this Link.  # noqa: E501
        :type length: int
        :param method: The method of this Link.  # noqa: E501
        :type method: str
        :param headers: The headers of this Link.  # noqa: E501
        :type headers: object
        :param body: The body of this Link.  # noqa: E501
        :type body: object
        :param merge: The merge of this Link.  # noqa: E501
        :type merge: bool
        """
        self.openapi_types = {
            'href': str,
            'rel': str,
            'type': str,
            'hreflang': str,
            'title': str,
            'length': int,
            'method': str,
            'headers': object,
            'body': object,
            'merge': bool
        }

        self.attribute_map = {
            'href': 'href',
            'rel': 'rel',
            'type': 'type',
            'hreflang': 'hreflang',
            'title': 'title',
            'length': 'length',
            'method': 'method',
            'headers': 'headers',
            'body': 'body',
            'merge': 'merge'
        }

        self._href = href
        self._rel = rel
        self._type = type
        self._hreflang = hreflang
        self._title = title
        self._length = length
        self._method = method
        self._headers = headers
        self._body = body
        self._merge = merge

    @classmethod
    def from_dict(cls, dikt) -> 'Link':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The link of this Link.  # noqa: E501
        :rtype: Link
        """
        return util.deserialize_model(dikt, cls)

    @property
    def href(self):
        """Gets the href of this Link.


        :return: The href of this Link.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Link.


        :param href: The href of this Link.
        :type href: str
        """
        if href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href

    @property
    def rel(self):
        """Gets the rel of this Link.


        :return: The rel of this Link.
        :rtype: str
        """
        return self._rel

    @rel.setter
    def rel(self, rel):
        """Sets the rel of this Link.


        :param rel: The rel of this Link.
        :type rel: str
        """
        if rel is None:
            raise ValueError("Invalid value for `rel`, must not be `None`")  # noqa: E501

        self._rel = rel

    @property
    def type(self):
        """Gets the type of this Link.


        :return: The type of this Link.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Link.


        :param type: The type of this Link.
        :type type: str
        """

        self._type = type

    @property
    def hreflang(self):
        """Gets the hreflang of this Link.


        :return: The hreflang of this Link.
        :rtype: str
        """
        return self._hreflang

    @hreflang.setter
    def hreflang(self, hreflang):
        """Sets the hreflang of this Link.


        :param hreflang: The hreflang of this Link.
        :type hreflang: str
        """

        self._hreflang = hreflang

    @property
    def title(self):
        """Gets the title of this Link.


        :return: The title of this Link.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Link.


        :param title: The title of this Link.
        :type title: str
        """

        self._title = title

    @property
    def length(self):
        """Gets the length of this Link.


        :return: The length of this Link.
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this Link.


        :param length: The length of this Link.
        :type length: int
        """

        self._length = length

    @property
    def method(self):
        """Gets the method of this Link.

        Specifies the HTTP method that the link expects  # noqa: E501

        :return: The method of this Link.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this Link.

        Specifies the HTTP method that the link expects  # noqa: E501

        :param method: The method of this Link.
        :type method: str
        """
        allowed_values = ["GET", "POST"]  # noqa: E501
        if method not in allowed_values:
            raise ValueError(
                "Invalid value for `method` ({0}), must be one of {1}"
                .format(method, allowed_values)
            )

        self._method = method

    @property
    def headers(self):
        """Gets the headers of this Link.

        Object key values pairs they map to headers  # noqa: E501

        :return: The headers of this Link.
        :rtype: object
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this Link.

        Object key values pairs they map to headers  # noqa: E501

        :param headers: The headers of this Link.
        :type headers: object
        """

        self._headers = headers

    @property
    def body(self):
        """Gets the body of this Link.

        For POST requests, the link can specify the HTTP body as a JSON object.  # noqa: E501

        :return: The body of this Link.
        :rtype: object
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this Link.

        For POST requests, the link can specify the HTTP body as a JSON object.  # noqa: E501

        :param body: The body of this Link.
        :type body: object
        """

        self._body = body

    @property
    def merge(self):
        """Gets the merge of this Link.

        This is only valid when the server is responding to POST request.  If merge is true, the client is expected to merge the body value into the current request body before following the link. This avoids passing large post bodies back and forth when following links, particularly for navigating pages through the `POST /search` endpoint.  NOTE: To support form encoding it is expected that a client be able to merge in the key value pairs specified as JSON `{\"next\": \"token\"}` will become `&next=token`.  # noqa: E501

        :return: The merge of this Link.
        :rtype: bool
        """
        return self._merge

    @merge.setter
    def merge(self, merge):
        """Sets the merge of this Link.

        This is only valid when the server is responding to POST request.  If merge is true, the client is expected to merge the body value into the current request body before following the link. This avoids passing large post bodies back and forth when following links, particularly for navigating pages through the `POST /search` endpoint.  NOTE: To support form encoding it is expected that a client be able to merge in the key value pairs specified as JSON `{\"next\": \"token\"}` will become `&next=token`.  # noqa: E501

        :param merge: The merge of this Link.
        :type merge: bool
        """

        self._merge = merge