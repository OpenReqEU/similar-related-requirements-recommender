# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from application.models.base_model_ import Model
from application.util import util


class Requirement(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, title: str=None, description: str=None, predict: bool=False):  # noqa: E501
        """Requirement - a model defined in Swagger

        :param id: The id of this Requirement.  # noqa: E501
        :type id: int
        :param title: The title of this Requirement.  # noqa: E501
        :type title: str
        :param description: The description of this Requirement.  # noqa: E501
        :type description: str
        :param predict: The predict attribute of this Requirement.  # noqa: E501
        :type predict: bool
        :param predictions: The predicted similar requirements of this Requirement.  # noqa: E501
        :type predictions: List[int]
        """
        self.swagger_types = {
            'id': int,
            'title': str,
            'description': str,
            'predict': bool,
            'predictions': list
        }

        self.attribute_map = {
            'id': 'id',
            'title': 'title',
            'description': 'description',
            'predict': 'predict',
            'predictions': 'predictions'
        }

        self._id = id
        self._title = title
        self._description = description
        self._predict = predict
        self._predictions = []

    @classmethod
    def from_dict(cls, dikt) -> 'Requirement':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Requirement of this Requirement.  # noqa: E501
        :rtype: Requirement
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Requirement.


        :return: The id of this Requirement.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Requirement.


        :param id: The id of this Requirement.
        :type id: int
        """

        self._id = id

    @property
    def title(self) -> str:
        """Gets the title of this Requirement.


        :return: The title of this Requirement.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this Requirement.


        :param title: The title of this Requirement.
        :type title: str
        """

        self._title = title

    @property
    def description(self) -> str:
        """Gets the description of this Requirement.


        :return: The description of this Requirement.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Requirement.


        :param description: The description of this Requirement.
        :type description: str
        """

        self._description = description

    @property
    def predict(self) -> bool:
        """Gets the predict attribute of this Requirement.


        :return: The predict attribute of this Requirement.
        :rtype: bool
        """
        return self._predict

    @predict.setter
    def predict(self, predict: bool):
        """Sets the predict attribute of this Requirement.


        :param predict: The predict attribute of this Requirement.
        :type predict: bool
        """

        self._predict = predict

    @property
    def predictions(self) -> []:
        """Gets the predictions of this Requirement.


        :return: The predictions of this Requirement.
        :rtype: List[Requirement]
        """
        return self._predictions

    @predictions.setter
    def predictions(self, predictions: list):
        """Sets the predict attribute of this Requirement.


        :param predictions: The predictions similar requirements list attribute of this Requirement.
        :type predictions: List[int]
        """

        self._predictions = predictions