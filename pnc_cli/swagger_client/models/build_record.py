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


class BuildRecord(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        BuildRecord - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'latest_build_configuration': 'BuildConfiguration',
            'build_configuration_audited': 'BuildConfigurationAudited',
            'build_content_id': 'str',
            'submit_time': 'datetime',
            'start_time': 'datetime',
            'end_time': 'datetime',
            'user': 'User',
            'build_log': 'str',
            'status': 'str',
            'built_artifacts': 'list[Artifact]',
            'dependencies': 'list[Artifact]',
            'build_driver_id': 'str',
            'system_image': 'BuildEnvironment',
            'build_record_sets': 'list[BuildRecordSet]',
            'build_config_set_record': 'BuildConfigSetRecord',
            'external_archive_id': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'latest_build_configuration': 'latestBuildConfiguration',
            'build_configuration_audited': 'buildConfigurationAudited',
            'build_content_id': 'buildContentId',
            'submit_time': 'submitTime',
            'start_time': 'startTime',
            'end_time': 'endTime',
            'user': 'user',
            'build_log': 'buildLog',
            'status': 'status',
            'built_artifacts': 'builtArtifacts',
            'dependencies': 'dependencies',
            'build_driver_id': 'buildDriverId',
            'system_image': 'systemImage',
            'build_record_sets': 'buildRecordSets',
            'build_config_set_record': 'buildConfigSetRecord',
            'external_archive_id': 'externalArchiveId'
        }

        self._id = None
        self._latest_build_configuration = None
        self._build_configuration_audited = None
        self._build_content_id = None
        self._submit_time = None
        self._start_time = None
        self._end_time = None
        self._user = None
        self._build_log = None
        self._status = None
        self._built_artifacts = None
        self._dependencies = None
        self._build_driver_id = None
        self._system_image = None
        self._build_record_sets = None
        self._build_config_set_record = None
        self._external_archive_id = None

    @property
    def id(self):
        """
        Gets the id of this BuildRecord.


        :return: The id of this BuildRecord.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BuildRecord.


        :param id: The id of this BuildRecord.
        :type: int
        """
        self._id = id

    @property
    def latest_build_configuration(self):
        """
        Gets the latest_build_configuration of this BuildRecord.


        :return: The latest_build_configuration of this BuildRecord.
        :rtype: BuildConfiguration
        """
        return self._latest_build_configuration

    @latest_build_configuration.setter
    def latest_build_configuration(self, latest_build_configuration):
        """
        Sets the latest_build_configuration of this BuildRecord.


        :param latest_build_configuration: The latest_build_configuration of this BuildRecord.
        :type: BuildConfiguration
        """
        self._latest_build_configuration = latest_build_configuration

    @property
    def build_configuration_audited(self):
        """
        Gets the build_configuration_audited of this BuildRecord.


        :return: The build_configuration_audited of this BuildRecord.
        :rtype: BuildConfigurationAudited
        """
        return self._build_configuration_audited

    @build_configuration_audited.setter
    def build_configuration_audited(self, build_configuration_audited):
        """
        Sets the build_configuration_audited of this BuildRecord.


        :param build_configuration_audited: The build_configuration_audited of this BuildRecord.
        :type: BuildConfigurationAudited
        """
        self._build_configuration_audited = build_configuration_audited

    @property
    def build_content_id(self):
        """
        Gets the build_content_id of this BuildRecord.


        :return: The build_content_id of this BuildRecord.
        :rtype: str
        """
        return self._build_content_id

    @build_content_id.setter
    def build_content_id(self, build_content_id):
        """
        Sets the build_content_id of this BuildRecord.


        :param build_content_id: The build_content_id of this BuildRecord.
        :type: str
        """
        self._build_content_id = build_content_id

    @property
    def submit_time(self):
        """
        Gets the submit_time of this BuildRecord.


        :return: The submit_time of this BuildRecord.
        :rtype: datetime
        """
        return self._submit_time

    @submit_time.setter
    def submit_time(self, submit_time):
        """
        Sets the submit_time of this BuildRecord.


        :param submit_time: The submit_time of this BuildRecord.
        :type: datetime
        """
        self._submit_time = submit_time

    @property
    def start_time(self):
        """
        Gets the start_time of this BuildRecord.


        :return: The start_time of this BuildRecord.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this BuildRecord.


        :param start_time: The start_time of this BuildRecord.
        :type: datetime
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """
        Gets the end_time of this BuildRecord.


        :return: The end_time of this BuildRecord.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this BuildRecord.


        :param end_time: The end_time of this BuildRecord.
        :type: datetime
        """
        self._end_time = end_time

    @property
    def user(self):
        """
        Gets the user of this BuildRecord.


        :return: The user of this BuildRecord.
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this BuildRecord.


        :param user: The user of this BuildRecord.
        :type: User
        """
        self._user = user

    @property
    def build_log(self):
        """
        Gets the build_log of this BuildRecord.


        :return: The build_log of this BuildRecord.
        :rtype: str
        """
        return self._build_log

    @build_log.setter
    def build_log(self, build_log):
        """
        Sets the build_log of this BuildRecord.


        :param build_log: The build_log of this BuildRecord.
        :type: str
        """
        self._build_log = build_log

    @property
    def status(self):
        """
        Gets the status of this BuildRecord.


        :return: The status of this BuildRecord.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this BuildRecord.


        :param status: The status of this BuildRecord.
        :type: str
        """
        allowed_values = ["SUCCESS", "FAILED", "UNSTABLE", "BUILDING", "ABORTED", "CANCELLED", "SYSTEM_ERROR", "UNKNOWN"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status`, must be one of {0}"
                .format(allowed_values)
            )
        self._status = status

    @property
    def built_artifacts(self):
        """
        Gets the built_artifacts of this BuildRecord.


        :return: The built_artifacts of this BuildRecord.
        :rtype: list[Artifact]
        """
        return self._built_artifacts

    @built_artifacts.setter
    def built_artifacts(self, built_artifacts):
        """
        Sets the built_artifacts of this BuildRecord.


        :param built_artifacts: The built_artifacts of this BuildRecord.
        :type: list[Artifact]
        """
        self._built_artifacts = built_artifacts

    @property
    def dependencies(self):
        """
        Gets the dependencies of this BuildRecord.


        :return: The dependencies of this BuildRecord.
        :rtype: list[Artifact]
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """
        Sets the dependencies of this BuildRecord.


        :param dependencies: The dependencies of this BuildRecord.
        :type: list[Artifact]
        """
        self._dependencies = dependencies

    @property
    def build_driver_id(self):
        """
        Gets the build_driver_id of this BuildRecord.


        :return: The build_driver_id of this BuildRecord.
        :rtype: str
        """
        return self._build_driver_id

    @build_driver_id.setter
    def build_driver_id(self, build_driver_id):
        """
        Sets the build_driver_id of this BuildRecord.


        :param build_driver_id: The build_driver_id of this BuildRecord.
        :type: str
        """
        self._build_driver_id = build_driver_id

    @property
    def system_image(self):
        """
        Gets the system_image of this BuildRecord.


        :return: The system_image of this BuildRecord.
        :rtype: BuildEnvironment
        """
        return self._system_image

    @system_image.setter
    def system_image(self, system_image):
        """
        Sets the system_image of this BuildRecord.


        :param system_image: The system_image of this BuildRecord.
        :type: BuildEnvironment
        """
        self._system_image = system_image

    @property
    def build_record_sets(self):
        """
        Gets the build_record_sets of this BuildRecord.


        :return: The build_record_sets of this BuildRecord.
        :rtype: list[BuildRecordSet]
        """
        return self._build_record_sets

    @build_record_sets.setter
    def build_record_sets(self, build_record_sets):
        """
        Sets the build_record_sets of this BuildRecord.


        :param build_record_sets: The build_record_sets of this BuildRecord.
        :type: list[BuildRecordSet]
        """
        self._build_record_sets = build_record_sets

    @property
    def build_config_set_record(self):
        """
        Gets the build_config_set_record of this BuildRecord.


        :return: The build_config_set_record of this BuildRecord.
        :rtype: BuildConfigSetRecord
        """
        return self._build_config_set_record

    @build_config_set_record.setter
    def build_config_set_record(self, build_config_set_record):
        """
        Sets the build_config_set_record of this BuildRecord.


        :param build_config_set_record: The build_config_set_record of this BuildRecord.
        :type: BuildConfigSetRecord
        """
        self._build_config_set_record = build_config_set_record

    @property
    def external_archive_id(self):
        """
        Gets the external_archive_id of this BuildRecord.


        :return: The external_archive_id of this BuildRecord.
        :rtype: int
        """
        return self._external_archive_id

    @external_archive_id.setter
    def external_archive_id(self, external_archive_id):
        """
        Sets the external_archive_id of this BuildRecord.


        :param external_archive_id: The external_archive_id of this BuildRecord.
        :type: int
        """
        self._external_archive_id = external_archive_id

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
                result[attr] = str(value)
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
