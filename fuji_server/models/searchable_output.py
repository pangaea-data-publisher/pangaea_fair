# SPDX-FileCopyrightText: 2020 PANGAEA (https://www.pangaea.de/)
#
# SPDX-License-Identifier: MIT

# coding: utf-8

from datetime import date, datetime  # noqa: F401

from fuji_server import util
from fuji_server.models.base_model_ import Model
from fuji_server.models.output_search_mechanisms import OutputSearchMechanisms


class SearchableOutput(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, search_mechanisms: list[OutputSearchMechanisms] | None = None):
        """SearchableOutput - a model defined in Swagger

        :param search_mechanisms: The search_mechanisms of this SearchableOutput.  # noqa: E501
        :type search_mechanisms: List[OutputSearchMechanisms]
        """
        self.swagger_types = {"search_mechanisms": list[OutputSearchMechanisms]}

        self.attribute_map = {"search_mechanisms": "search_mechanisms"}
        self._search_mechanisms = search_mechanisms

    @classmethod
    def from_dict(cls, dikt) -> "SearchableOutput":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Searchable_output of this SearchableOutput.  # noqa: E501
        :rtype: SearchableOutput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def search_mechanisms(self) -> list[OutputSearchMechanisms]:
        """Gets the search_mechanisms of this SearchableOutput.


        :return: The search_mechanisms of this SearchableOutput.
        :rtype: List[OutputSearchMechanisms]
        """
        return self._search_mechanisms

    @search_mechanisms.setter
    def search_mechanisms(self, search_mechanisms: list[OutputSearchMechanisms]):
        """Sets the search_mechanisms of this SearchableOutput.


        :param search_mechanisms: The search_mechanisms of this SearchableOutput.
        :type search_mechanisms: List[OutputSearchMechanisms]
        """

        self._search_mechanisms = search_mechanisms
