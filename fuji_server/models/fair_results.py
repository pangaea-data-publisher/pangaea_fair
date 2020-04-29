# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from fuji_server.models.base_model_ import Model
#from fuji_server.models.object import Object  # noqa: F401,E501
from fuji_server import util


class FAIRResults(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self):  # noqa: E501
        """FAIRResults - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'FAIRResults':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FAIRResults of this FAIRResults.  # noqa: E501
        :rtype: FAIRResults
        """
        return util.deserialize_model(dikt, cls)
