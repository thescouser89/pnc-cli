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


class BuildConfigurationAuditedRest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        BuildConfigurationAuditedRest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'rev': 'int',
            'name': 'str',
            'description': 'str',
            'build_script': 'str',
            'scm_repo_url': 'str',
            'scm_revision': 'str',
            'creation_time': 'datetime',
            'last_modification_time': 'datetime',
            'repositories': 'str',
            'project_id': 'int',
            'environment_id': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'rev': 'rev',
            'name': 'name',
            'description': 'description',
            'build_script': 'buildScript',
            'scm_repo_url': 'scmRepoURL',
            'scm_revision': 'scmRevision',
            'creation_time': 'creationTime',
            'last_modification_time': 'lastModificationTime',
            'repositories': 'repositories',
            'project_id': 'projectId',
            'environment_id': 'environmentId'
        }

        self._id = None
        self._rev = None
        self._name = None
        self._description = None
        self._build_script = None
        self._scm_repo_url = None
        self._scm_revision = None
        self._creation_time = None
        self._last_modification_time = None
        self._repositories = None
        self._project_id = None
        self._environment_id = None

    @property
    def id(self):
        """
        Gets the id of this BuildConfigurationAuditedRest.


        :return: The id of this BuildConfigurationAuditedRest.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BuildConfigurationAuditedRest.


        :param id: The id of this BuildConfigurationAuditedRest.
        :type: int
        """
        self._id = id

    @property
    def rev(self):
        """
        Gets the rev of this BuildConfigurationAuditedRest.


        :return: The rev of this BuildConfigurationAuditedRest.
        :rtype: int
        """
        return self._rev

    @rev.setter
    def rev(self, rev):
        """
        Sets the rev of this BuildConfigurationAuditedRest.


        :param rev: The rev of this BuildConfigurationAuditedRest.
        :type: int
        """
        self._rev = rev

    @property
    def name(self):
        """
        Gets the name of this BuildConfigurationAuditedRest.


        :return: The name of this BuildConfigurationAuditedRest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BuildConfigurationAuditedRest.


        :param name: The name of this BuildConfigurationAuditedRest.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this BuildConfigurationAuditedRest.


        :return: The description of this BuildConfigurationAuditedRest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this BuildConfigurationAuditedRest.


        :param description: The description of this BuildConfigurationAuditedRest.
        :type: str
        """
        self._description = description

    @property
    def build_script(self):
        """
        Gets the build_script of this BuildConfigurationAuditedRest.


        :return: The build_script of this BuildConfigurationAuditedRest.
        :rtype: str
        """
        return self._build_script

    @build_script.setter
    def build_script(self, build_script):
        """
        Sets the build_script of this BuildConfigurationAuditedRest.


        :param build_script: The build_script of this BuildConfigurationAuditedRest.
        :type: str
        """
        self._build_script = build_script

    @property
    def scm_repo_url(self):
        """
        Gets the scm_repo_url of this BuildConfigurationAuditedRest.


        :return: The scm_repo_url of this BuildConfigurationAuditedRest.
        :rtype: str
        """
        return self._scm_repo_url

    @scm_repo_url.setter
    def scm_repo_url(self, scm_repo_url):
        """
        Sets the scm_repo_url of this BuildConfigurationAuditedRest.


        :param scm_repo_url: The scm_repo_url of this BuildConfigurationAuditedRest.
        :type: str
        """
        self._scm_repo_url = scm_repo_url

    @property
    def scm_revision(self):
        """
        Gets the scm_revision of this BuildConfigurationAuditedRest.


        :return: The scm_revision of this BuildConfigurationAuditedRest.
        :rtype: str
        """
        return self._scm_revision

    @scm_revision.setter
    def scm_revision(self, scm_revision):
        """
        Sets the scm_revision of this BuildConfigurationAuditedRest.


        :param scm_revision: The scm_revision of this BuildConfigurationAuditedRest.
        :type: str
        """
        self._scm_revision = scm_revision

    @property
    def creation_time(self):
        """
        Gets the creation_time of this BuildConfigurationAuditedRest.


        :return: The creation_time of this BuildConfigurationAuditedRest.
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """
        Sets the creation_time of this BuildConfigurationAuditedRest.


        :param creation_time: The creation_time of this BuildConfigurationAuditedRest.
        :type: datetime
        """
        self._creation_time = creation_time

    @property
    def last_modification_time(self):
        """
        Gets the last_modification_time of this BuildConfigurationAuditedRest.


        :return: The last_modification_time of this BuildConfigurationAuditedRest.
        :rtype: datetime
        """
        return self._last_modification_time

    @last_modification_time.setter
    def last_modification_time(self, last_modification_time):
        """
        Sets the last_modification_time of this BuildConfigurationAuditedRest.


        :param last_modification_time: The last_modification_time of this BuildConfigurationAuditedRest.
        :type: datetime
        """
        self._last_modification_time = last_modification_time

    @property
    def repositories(self):
        """
        Gets the repositories of this BuildConfigurationAuditedRest.


        :return: The repositories of this BuildConfigurationAuditedRest.
        :rtype: str
        """
        return self._repositories

    @repositories.setter
    def repositories(self, repositories):
        """
        Sets the repositories of this BuildConfigurationAuditedRest.


        :param repositories: The repositories of this BuildConfigurationAuditedRest.
        :type: str
        """
        self._repositories = repositories

    @property
    def project_id(self):
        """
        Gets the project_id of this BuildConfigurationAuditedRest.


        :return: The project_id of this BuildConfigurationAuditedRest.
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this BuildConfigurationAuditedRest.


        :param project_id: The project_id of this BuildConfigurationAuditedRest.
        :type: int
        """
        self._project_id = project_id

    @property
    def environment_id(self):
        """
        Gets the environment_id of this BuildConfigurationAuditedRest.


        :return: The environment_id of this BuildConfigurationAuditedRest.
        :rtype: int
        """
        return self._environment_id

    @environment_id.setter
    def environment_id(self, environment_id):
        """
        Sets the environment_id of this BuildConfigurationAuditedRest.


        :param environment_id: The environment_id of this BuildConfigurationAuditedRest.
        :type: int
        """
        self._environment_id = environment_id

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
