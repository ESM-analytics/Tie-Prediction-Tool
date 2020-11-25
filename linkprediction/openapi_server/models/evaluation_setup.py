# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from linkprediction.openapi_server.models.base_model_ import Model
from linkprediction.openapi_server import util


class EvaluationSetup(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, random_seed=None, with_validation=None, train_sampling_ratio=None, test_sampling_ratio=None, ml_preprocessing=None):  # noqa: E501
        """EvaluationSetup - a model defined in OpenAPI

        :param random_seed: The random_seed of this EvaluationSetup.  # noqa: E501
        :type random_seed: int
        :param with_validation: The with_validation of this EvaluationSetup.  # noqa: E501
        :type with_validation: bool
        :param train_sampling_ratio: The train_sampling_ratio of this EvaluationSetup.  # noqa: E501
        :type train_sampling_ratio: float
        :param test_sampling_ratio: The test_sampling_ratio of this EvaluationSetup.  # noqa: E501
        :type test_sampling_ratio: float
        :param ml_preprocessing: The ml_preprocessing of this EvaluationSetup.  # noqa: E501
        :type ml_preprocessing: bool
        """
        self.openapi_types = {
            'random_seed': int,
            'with_validation': bool,
            'train_sampling_ratio': float,
            'test_sampling_ratio': float,
            'ml_preprocessing': bool
        }

        self.attribute_map = {
            'random_seed': 'random_seed',
            'with_validation': 'with_validation',
            'train_sampling_ratio': 'train_sampling_ratio',
            'test_sampling_ratio': 'test_sampling_ratio',
            'ml_preprocessing': 'ml_preprocessing'
        }

        self._random_seed = random_seed
        self._with_validation = with_validation
        self._train_sampling_ratio = train_sampling_ratio
        self._test_sampling_ratio = test_sampling_ratio
        self._ml_preprocessing = ml_preprocessing

    @classmethod
    def from_dict(cls, dikt) -> 'EvaluationSetup':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EvaluationSetup of this EvaluationSetup.  # noqa: E501
        :rtype: EvaluationSetup
        """
        return util.deserialize_model(dikt, cls)

    @property
    def random_seed(self):
        """Gets the random_seed of this EvaluationSetup.


        :return: The random_seed of this EvaluationSetup.
        :rtype: int
        """
        return self._random_seed

    @random_seed.setter
    def random_seed(self, random_seed):
        """Sets the random_seed of this EvaluationSetup.


        :param random_seed: The random_seed of this EvaluationSetup.
        :type random_seed: int
        """
        if random_seed is None:
            raise ValueError("Invalid value for `random_seed`, must not be `None`")  # noqa: E501

        self._random_seed = random_seed

    @property
    def with_validation(self):
        """Gets the with_validation of this EvaluationSetup.


        :return: The with_validation of this EvaluationSetup.
        :rtype: bool
        """
        return self._with_validation

    @with_validation.setter
    def with_validation(self, with_validation):
        """Sets the with_validation of this EvaluationSetup.


        :param with_validation: The with_validation of this EvaluationSetup.
        :type with_validation: bool
        """
        if with_validation is None:
            raise ValueError("Invalid value for `with_validation`, must not be `None`")  # noqa: E501

        self._with_validation = with_validation

    @property
    def train_sampling_ratio(self):
        """Gets the train_sampling_ratio of this EvaluationSetup.


        :return: The train_sampling_ratio of this EvaluationSetup.
        :rtype: float
        """
        return self._train_sampling_ratio

    @train_sampling_ratio.setter
    def train_sampling_ratio(self, train_sampling_ratio):
        """Sets the train_sampling_ratio of this EvaluationSetup.


        :param train_sampling_ratio: The train_sampling_ratio of this EvaluationSetup.
        :type train_sampling_ratio: float
        """
        if train_sampling_ratio is None:
            raise ValueError("Invalid value for `train_sampling_ratio`, must not be `None`")  # noqa: E501
        if train_sampling_ratio is not None and train_sampling_ratio > 1.0:  # noqa: E501
            raise ValueError("Invalid value for `train_sampling_ratio`, must be a value less than or equal to `1.0`")  # noqa: E501
        if train_sampling_ratio is not None and train_sampling_ratio < 0:  # noqa: E501
            raise ValueError("Invalid value for `train_sampling_ratio`, must be a value greater than or equal to `0`")  # noqa: E501

        self._train_sampling_ratio = train_sampling_ratio

    @property
    def test_sampling_ratio(self):
        """Gets the test_sampling_ratio of this EvaluationSetup.


        :return: The test_sampling_ratio of this EvaluationSetup.
        :rtype: float
        """
        return self._test_sampling_ratio

    @test_sampling_ratio.setter
    def test_sampling_ratio(self, test_sampling_ratio):
        """Sets the test_sampling_ratio of this EvaluationSetup.


        :param test_sampling_ratio: The test_sampling_ratio of this EvaluationSetup.
        :type test_sampling_ratio: float
        """
        if test_sampling_ratio is not None and test_sampling_ratio > 1.0:  # noqa: E501
            raise ValueError("Invalid value for `test_sampling_ratio`, must be a value less than or equal to `1.0`")  # noqa: E501
        if test_sampling_ratio is not None and test_sampling_ratio < 0:  # noqa: E501
            raise ValueError("Invalid value for `test_sampling_ratio`, must be a value greater than or equal to `0`")  # noqa: E501

        self._test_sampling_ratio = test_sampling_ratio

    @property
    def ml_preprocessing(self):
        """Gets the ml_preprocessing of this EvaluationSetup.


        :return: The ml_preprocessing of this EvaluationSetup.
        :rtype: bool
        """
        return self._ml_preprocessing

    @ml_preprocessing.setter
    def ml_preprocessing(self, ml_preprocessing):
        """Sets the ml_preprocessing of this EvaluationSetup.


        :param ml_preprocessing: The ml_preprocessing of this EvaluationSetup.
        :type ml_preprocessing: bool
        """
        if ml_preprocessing is None:
            raise ValueError("Invalid value for `ml_preprocessing`, must not be `None`")  # noqa: E501

        self._ml_preprocessing = ml_preprocessing