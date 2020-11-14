# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from linkprediction.openapi_server.models.base_model_ import Model
from linkprediction.openapi_server import util


class PredictionState(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, state=None):  # noqa: E501
        """PredictionState - a model defined in OpenAPI

        :param state: The state of this PredictionState.  # noqa: E501
        :type state: str
        """
        self.openapi_types = {
            'state': str
        }

        self.attribute_map = {
            'state': 'state'
        }

        self._state = state

    @classmethod
    def from_dict(cls, dikt) -> 'PredictionState':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PredictionState of this PredictionState.  # noqa: E501
        :rtype: PredictionState
        """
        return util.deserialize_model(dikt, cls)

    @property
    def state(self):
        """Gets the state of this PredictionState.


        :return: The state of this PredictionState.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PredictionState.


        :param state: The state of this PredictionState.
        :type state: str
        """
        allowed_values = ["Start", "Abort"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state
