# SPDX-FileCopyrightText: 2020 PANGAEA (https://www.pangaea.de/)
#
# SPDX-License-Identifier: MIT

# coding: utf-8

from datetime import date, datetime  # noqa: F401

from fuji_server import util
from fuji_server.models.base_model_ import Model


class OutputCoreMetadataFound(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self):
        """OutputCoreMetadataFound - a model defined in Swagger"""
        self.swagger_types = {}

        self.attribute_map = {}

    @classmethod
    def from_dict(cls, dikt) -> "OutputCoreMetadataFound":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The output_core_metadata_found of this OutputCoreMetadataFound.  # noqa: E501
        :rtype: OutputCoreMetadataFound
        """
        return util.deserialize_model(dikt, cls)
