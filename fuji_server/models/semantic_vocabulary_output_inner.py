# SPDX-FileCopyrightText: 2020 PANGAEA (https://www.pangaea.de/)
#
# SPDX-License-Identifier: MIT

# coding: utf-8

from datetime import date, datetime  # noqa: F401

from fuji_server import util
from fuji_server.models.base_model_ import Model


class SemanticVocabularyOutputInner(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, namespace: str | None = None, is_namespace_active: bool = False):
        """SemanticVocabularyOutputInner - a model defined in Swagger

        :param namespace: The namespace of this SemanticVocabularyOutputInner.  # noqa: E501
        :type namespace: str
        :param is_namespace_active: The is_namespace_active of this SemanticVocabularyOutputInner.  # noqa: E501
        :type is_namespace_active: bool
        """
        self.swagger_types = {"namespace": str, "is_namespace_active": bool}

        self.attribute_map = {"namespace": "namespace", "is_namespace_active": "is_namespace_active"}
        self._namespace = namespace
        self._is_namespace_active = is_namespace_active

    @classmethod
    def from_dict(cls, dikt) -> "SemanticVocabularyOutputInner":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SemanticVocabulary_output_inner of this SemanticVocabularyOutputInner.  # noqa: E501
        :rtype: SemanticVocabularyOutputInner
        """
        return util.deserialize_model(dikt, cls)

    @property
    def namespace(self) -> str:
        """Gets the namespace of this SemanticVocabularyOutputInner.


        :return: The namespace of this SemanticVocabularyOutputInner.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace: str):
        """Sets the namespace of this SemanticVocabularyOutputInner.


        :param namespace: The namespace of this SemanticVocabularyOutputInner.
        :type namespace: str
        """

        self._namespace = namespace

    @property
    def is_namespace_active(self) -> bool:
        """Gets the is_namespace_active of this SemanticVocabularyOutputInner.


        :return: The is_namespace_active of this SemanticVocabularyOutputInner.
        :rtype: bool
        """
        return self._is_namespace_active

    @is_namespace_active.setter
    def is_namespace_active(self, is_namespace_active: bool):
        """Sets the is_namespace_active of this SemanticVocabularyOutputInner.


        :param is_namespace_active: The is_namespace_active of this SemanticVocabularyOutputInner.
        :type is_namespace_active: bool
        """

        self._is_namespace_active = is_namespace_active
