# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from datetime import datetime
from pprint import pformat
from six import iteritems
import re


class RepositoryManagerResultRest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'built_artifacts': 'list[ArtifactRest]',
        'dependencies': 'list[ArtifactRest]',
        'build_content_id': 'str',
        'log': 'str',
        'completion_status': 'str'
    }

    attribute_map = {
        'built_artifacts': 'builtArtifacts',
        'dependencies': 'dependencies',
        'build_content_id': 'buildContentId',
        'log': 'log',
        'completion_status': 'completionStatus'
    }

    def __init__(self, built_artifacts=None, dependencies=None, build_content_id=None, log=None, completion_status=None):
        """
        RepositoryManagerResultRest - a model defined in Swagger
        """

        self._built_artifacts = None
        self._dependencies = None
        self._build_content_id = None
        self._log = None
        self._completion_status = None

        if built_artifacts is not None:
          self.built_artifacts = built_artifacts
        if dependencies is not None:
          self.dependencies = dependencies
        if build_content_id is not None:
          self.build_content_id = build_content_id
        if log is not None:
          self.log = log
        if completion_status is not None:
          self.completion_status = completion_status

    @property
    def built_artifacts(self):
        """
        Gets the built_artifacts of this RepositoryManagerResultRest.

        :return: The built_artifacts of this RepositoryManagerResultRest.
        :rtype: list[ArtifactRest]
        """
        return self._built_artifacts

    @built_artifacts.setter
    def built_artifacts(self, built_artifacts):
        """
        Sets the built_artifacts of this RepositoryManagerResultRest.

        :param built_artifacts: The built_artifacts of this RepositoryManagerResultRest.
        :type: list[ArtifactRest]
        """

        self._built_artifacts = built_artifacts

    @property
    def dependencies(self):
        """
        Gets the dependencies of this RepositoryManagerResultRest.

        :return: The dependencies of this RepositoryManagerResultRest.
        :rtype: list[ArtifactRest]
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """
        Sets the dependencies of this RepositoryManagerResultRest.

        :param dependencies: The dependencies of this RepositoryManagerResultRest.
        :type: list[ArtifactRest]
        """

        self._dependencies = dependencies

    @property
    def build_content_id(self):
        """
        Gets the build_content_id of this RepositoryManagerResultRest.

        :return: The build_content_id of this RepositoryManagerResultRest.
        :rtype: str
        """
        return self._build_content_id

    @build_content_id.setter
    def build_content_id(self, build_content_id):
        """
        Sets the build_content_id of this RepositoryManagerResultRest.

        :param build_content_id: The build_content_id of this RepositoryManagerResultRest.
        :type: str
        """

        self._build_content_id = build_content_id

    @property
    def log(self):
        """
        Gets the log of this RepositoryManagerResultRest.

        :return: The log of this RepositoryManagerResultRest.
        :rtype: str
        """
        return self._log

    @log.setter
    def log(self, log):
        """
        Sets the log of this RepositoryManagerResultRest.

        :param log: The log of this RepositoryManagerResultRest.
        :type: str
        """

        self._log = log

    @property
    def completion_status(self):
        """
        Gets the completion_status of this RepositoryManagerResultRest.

        :return: The completion_status of this RepositoryManagerResultRest.
        :rtype: str
        """
        return self._completion_status

    @completion_status.setter
    def completion_status(self, completion_status):
        """
        Sets the completion_status of this RepositoryManagerResultRest.

        :param completion_status: The completion_status of this RepositoryManagerResultRest.
        :type: str
        """
        allowed_values = ["SUCCESS", "NO_REBUILD_REQUIRED", "FAILED", "CANCELLED", "TIMED_OUT", "SYSTEM_ERROR"]
        if completion_status not in allowed_values:
            raise ValueError(
                "Invalid value for `completion_status` ({0}), must be one of {1}"
                .format(completion_status, allowed_values)
            )

        self._completion_status = completion_status

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
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
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

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, RepositoryManagerResultRest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other