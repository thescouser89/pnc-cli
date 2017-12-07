# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from datetime import datetime
from pprint import pformat
from six import iteritems


class ArtifactImportError(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ArtifactImportError - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'artifact_id': 'int',
            'error_message': 'str'
        }

        self.attribute_map = {
            'artifact_id': 'artifactId',
            'error_message': 'errorMessage'
        }

        self._artifact_id = None
        self._error_message = None

    @property
    def artifact_id(self):
        """
        Gets the artifact_id of this ArtifactImportError.


        :return: The artifact_id of this ArtifactImportError.
        :rtype: int
        """
        return self._artifact_id

    @artifact_id.setter
    def artifact_id(self, artifact_id):
        """
        Sets the artifact_id of this ArtifactImportError.


        :param artifact_id: The artifact_id of this ArtifactImportError.
        :type: int
        """
        self._artifact_id = artifact_id

    @property
    def error_message(self):
        """
        Gets the error_message of this ArtifactImportError.


        :return: The error_message of this ArtifactImportError.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this ArtifactImportError.


        :param error_message: The error_message of this ArtifactImportError.
        :type: str
        """
        self._error_message = error_message

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
	    elif isinstance(value, datetime):
		result[attr] = str(value.date())
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()
