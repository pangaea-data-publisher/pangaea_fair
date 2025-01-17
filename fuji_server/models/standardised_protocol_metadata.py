# SPDX-FileCopyrightText: 2020 PANGAEA (https://www.pangaea.de/)
#
# SPDX-License-Identifier: MIT

# coding: utf-8

from datetime import date, datetime  # noqa: F401

from fuji_server import util
from fuji_server.models.base_model_ import Model
from fuji_server.models.debug import Debug
from fuji_server.models.fair_result_common import FAIRResultCommon  # noqa: F401
from fuji_server.models.fair_result_common_score import FAIRResultCommonScore
from fuji_server.models.fair_result_evaluation_criterium import FAIRResultEvaluationCriterium
from fuji_server.models.standardised_protocol_output import StandardisedProtocolOutput


class StandardisedProtocolMetadata(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(
        self,
        output: StandardisedProtocolOutput | None = None,
        test_debug: Debug | None = None,
        id: int | None = None,
        metric_identifier: str | None = None,
        metric_name: str | None = None,
        metric_tests: dict[str, FAIRResultEvaluationCriterium] | None = None,
        test_status: str = "fail",
        score: FAIRResultCommonScore | None = None,
        maturity: int = 0,
    ):
        """StandardisedProtocolMetadata - a model defined in Swagger

        :param output: The output of this StandardisedProtocolMetadata.  # noqa: E501
        :type output: StandardisedProtocolOutput
        :param test_debug: The test_debug of this StandardisedProtocolMetadata.  # noqa: E501
        :type test_debug: Debug
        :param id: The id of this StandardisedProtocolMetadata.  # noqa: E501
        :type id: int
        :param metric_identifier: The metric_identifier of this StandardisedProtocolMetadata.  # noqa: E501
        :type metric_identifier: str
        :param metric_name: The metric_name of this StandardisedProtocolMetadata.  # noqa: E501
        :type metric_name: str
        :param metric_tests: The metric_tests of this StandardisedProtocolMetadata.  # noqa: E501
        :type metric_tests: Dict[str, FAIRResultEvaluationCriterium]
        :param test_status: The test_status of this StandardisedProtocolMetadata.  # noqa: E501
        :type test_status: str
        :param score: The score of this StandardisedProtocolMetadata.  # noqa: E501
        :type score: FAIRResultCommonScore
        :param maturity: The maturity of this StandardisedProtocolMetadata.  # noqa: E501
        :type maturity: int
        """
        self.swagger_types = {
            "output": StandardisedProtocolOutput,
            "test_debug": Debug,
            "id": int,
            "metric_identifier": str,
            "metric_name": str,
            "metric_tests": dict[str, FAIRResultEvaluationCriterium],
            "test_status": str,
            "score": FAIRResultCommonScore,
            "maturity": int,
        }

        self.attribute_map = {
            "output": "output",
            "test_debug": "test_debug",
            "id": "id",
            "metric_identifier": "metric_identifier",
            "metric_name": "metric_name",
            "metric_tests": "metric_tests",
            "test_status": "test_status",
            "score": "score",
            "maturity": "maturity",
        }
        self._output = output
        self._test_debug = test_debug
        self._id = id
        self._metric_identifier = metric_identifier
        self._metric_name = metric_name
        self._metric_tests = metric_tests
        self._test_status = test_status
        self._score = score
        self._maturity = maturity

    @classmethod
    def from_dict(cls, dikt) -> "StandardisedProtocolMetadata":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The StandardisedProtocolMetadata of this StandardisedProtocolMetadata.  # noqa: E501
        :rtype: StandardisedProtocolMetadata
        """
        return util.deserialize_model(dikt, cls)

    @property
    def output(self) -> StandardisedProtocolOutput:
        """Gets the output of this StandardisedProtocolMetadata.


        :return: The output of this StandardisedProtocolMetadata.
        :rtype: StandardisedProtocolOutput
        """
        return self._output

    @output.setter
    def output(self, output: StandardisedProtocolOutput):
        """Sets the output of this StandardisedProtocolMetadata.


        :param output: The output of this StandardisedProtocolMetadata.
        :type output: StandardisedProtocolOutput
        """

        self._output = output

    @property
    def test_debug(self) -> Debug:
        """Gets the test_debug of this StandardisedProtocolMetadata.


        :return: The test_debug of this StandardisedProtocolMetadata.
        :rtype: Debug
        """
        return self._test_debug

    @test_debug.setter
    def test_debug(self, test_debug: Debug):
        """Sets the test_debug of this StandardisedProtocolMetadata.


        :param test_debug: The test_debug of this StandardisedProtocolMetadata.
        :type test_debug: Debug
        """

        self._test_debug = test_debug

    @property
    def id(self) -> int:
        """Gets the id of this StandardisedProtocolMetadata.


        :return: The id of this StandardisedProtocolMetadata.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this StandardisedProtocolMetadata.


        :param id: The id of this StandardisedProtocolMetadata.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def metric_identifier(self) -> str:
        """Gets the metric_identifier of this StandardisedProtocolMetadata.


        :return: The metric_identifier of this StandardisedProtocolMetadata.
        :rtype: str
        """
        return self._metric_identifier

    @metric_identifier.setter
    def metric_identifier(self, metric_identifier: str):
        """Sets the metric_identifier of this StandardisedProtocolMetadata.


        :param metric_identifier: The metric_identifier of this StandardisedProtocolMetadata.
        :type metric_identifier: str
        """
        if metric_identifier is None:
            raise ValueError("Invalid value for `metric_identifier`, must not be `None`")

        self._metric_identifier = metric_identifier

    @property
    def metric_name(self) -> str:
        """Gets the metric_name of this StandardisedProtocolMetadata.


        :return: The metric_name of this StandardisedProtocolMetadata.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name: str):
        """Sets the metric_name of this StandardisedProtocolMetadata.


        :param metric_name: The metric_name of this StandardisedProtocolMetadata.
        :type metric_name: str
        """
        if metric_name is None:
            raise ValueError("Invalid value for `metric_name`, must not be `None`")

        self._metric_name = metric_name

    @property
    def metric_tests(self) -> dict[str, FAIRResultEvaluationCriterium]:
        """Gets the metric_tests of this StandardisedProtocolMetadata.


        :return: The metric_tests of this StandardisedProtocolMetadata.
        :rtype: Dict[str, FAIRResultEvaluationCriterium]
        """
        return self._metric_tests

    @metric_tests.setter
    def metric_tests(self, metric_tests: dict[str, FAIRResultEvaluationCriterium]):
        """Sets the metric_tests of this StandardisedProtocolMetadata.


        :param metric_tests: The metric_tests of this StandardisedProtocolMetadata.
        :type metric_tests: Dict[str, FAIRResultEvaluationCriterium]
        """

        self._metric_tests = metric_tests

    @property
    def test_status(self) -> str:
        """Gets the test_status of this StandardisedProtocolMetadata.


        :return: The test_status of this StandardisedProtocolMetadata.
        :rtype: str
        """
        return self._test_status

    @test_status.setter
    def test_status(self, test_status: str):
        """Sets the test_status of this StandardisedProtocolMetadata.


        :param test_status: The test_status of this StandardisedProtocolMetadata.
        :type test_status: str
        """
        allowed_values = ["pass", "fail", "indeterminate"]
        if test_status not in allowed_values:
            raise ValueError(f"Invalid value for `test_status` ({test_status}), must be one of {allowed_values}")

        self._test_status = test_status

    @property
    def score(self) -> FAIRResultCommonScore:
        """Gets the score of this StandardisedProtocolMetadata.


        :return: The score of this StandardisedProtocolMetadata.
        :rtype: FAIRResultCommonScore
        """
        return self._score

    @score.setter
    def score(self, score: FAIRResultCommonScore):
        """Sets the score of this StandardisedProtocolMetadata.


        :param score: The score of this StandardisedProtocolMetadata.
        :type score: FAIRResultCommonScore
        """
        if score is None:
            raise ValueError("Invalid value for `score`, must not be `None`")

        self._score = score

    @property
    def maturity(self) -> int:
        """Gets the maturity of this StandardisedProtocolMetadata.


        :return: The maturity of this StandardisedProtocolMetadata.
        :rtype: int
        """
        return self._maturity

    @maturity.setter
    def maturity(self, maturity: int):
        """Sets the maturity of this StandardisedProtocolMetadata.


        :param maturity: The maturity of this StandardisedProtocolMetadata.
        :type maturity: int
        """

        self._maturity = maturity
