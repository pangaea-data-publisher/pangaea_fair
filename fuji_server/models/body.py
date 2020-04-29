# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from fuji_server.models.base_model_ import Model
from fuji_server import util


class Body(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, object_identifier: str=None, oaipmh_provider: str=None, test_debug: bool=False):  # noqa: E501
        """Body - a model defined in Swagger

        :param object_identifier: The object_identifier of this Body.  # noqa: E501
        :type object_identifier: str
        :param oaipmh_provider: The oaipmh_provider of this Body.  # noqa: E501
        :type oaipmh_provider: str
        :param test_debug: The test_debug of this Body.  # noqa: E501
        :type test_debug: bool
        """
        self.swagger_types = {
            'object_identifier': str,
            'oaipmh_provider': str,
            'test_debug': bool
        }

        self.attribute_map = {
            'object_identifier': 'object_identifier',
            'oaipmh_provider': 'oaipmh_provider',
            'test_debug': 'test_debug'
        }
        self._object_identifier = object_identifier
        self._oaipmh_provider = oaipmh_provider
        self._test_debug = test_debug

    @classmethod
    def from_dict(cls, dikt) -> 'Body':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The body of this Body.  # noqa: E501
        :rtype: Body
        """
        return util.deserialize_model(dikt, cls)

    @property
    def object_identifier(self) -> str:
        """Gets the object_identifier of this Body.

        The full identifier of data object that needs to be evaluated  # noqa: E501

        :return: The object_identifier of this Body.
        :rtype: str
        """
        return self._object_identifier

    @object_identifier.setter
    def object_identifier(self, object_identifier: str):
        """Sets the object_identifier of this Body.

        The full identifier of data object that needs to be evaluated  # noqa: E501

        :param object_identifier: The object_identifier of this Body.
        :type object_identifier: str
        """
        if object_identifier is None:
            raise ValueError("Invalid value for `object_identifier`, must not be `None`")  # noqa: E501

        self._object_identifier = object_identifier

    @property
    def oaipmh_provider(self) -> str:
        """Gets the oaipmh_provider of this Body.

        The endpoint of oai-pmh provider  # noqa: E501

        :return: The oaipmh_provider of this Body.
        :rtype: str
        """
        return self._oaipmh_provider

    @oaipmh_provider.setter
    def oaipmh_provider(self, oaipmh_provider: str):
        """Sets the oaipmh_provider of this Body.

        The endpoint of oai-pmh provider  # noqa: E501

        :param oaipmh_provider: The oaipmh_provider of this Body.
        :type oaipmh_provider: str
        """

        self._oaipmh_provider = oaipmh_provider

    @property
    def test_debug(self) -> bool:
        """Gets the test_debug of this Body.

        Indicate if the detailed evaluation procedure of the metrics should to be included in the response  # noqa: E501

        :return: The test_debug of this Body.
        :rtype: bool
        """
        return self._test_debug

    @test_debug.setter
    def test_debug(self, test_debug: bool):
        """Sets the test_debug of this Body.

        Indicate if the detailed evaluation procedure of the metrics should to be included in the response  # noqa: E501

        :param test_debug: The test_debug of this Body.
        :type test_debug: bool
        """

        self._test_debug = test_debug
