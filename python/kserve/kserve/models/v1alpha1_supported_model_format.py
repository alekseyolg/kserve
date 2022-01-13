# Copyright 2021 The KServe Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8

"""
    KServe

    Python SDK for KServe  # noqa: E501

    The version of the OpenAPI document: v0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kserve.configuration import Configuration


class V1alpha1SupportedModelFormat(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'auto_select': 'bool',
        'name': 'str',
        'version': 'str'
    }

    attribute_map = {
        'auto_select': 'autoSelect',
        'name': 'name',
        'version': 'version'
    }

    def __init__(self, auto_select=None, name='', version=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1SupportedModelFormat - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._auto_select = None
        self._name = None
        self._version = None
        self.discriminator = None

        if auto_select is not None:
            self.auto_select = auto_select
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version

    @property
    def auto_select(self):
        """Gets the auto_select of this V1alpha1SupportedModelFormat.  # noqa: E501

        Set to true to allow the ServingRuntime to be used for automatic model placement if this model format is specified with no explicit runtime.  # noqa: E501

        :return: The auto_select of this V1alpha1SupportedModelFormat.  # noqa: E501
        :rtype: bool
        """
        return self._auto_select

    @auto_select.setter
    def auto_select(self, auto_select):
        """Sets the auto_select of this V1alpha1SupportedModelFormat.

        Set to true to allow the ServingRuntime to be used for automatic model placement if this model format is specified with no explicit runtime.  # noqa: E501

        :param auto_select: The auto_select of this V1alpha1SupportedModelFormat.  # noqa: E501
        :type: bool
        """

        self._auto_select = auto_select

    @property
    def name(self):
        """Gets the name of this V1alpha1SupportedModelFormat.  # noqa: E501

        Name of the model format.  # noqa: E501

        :return: The name of this V1alpha1SupportedModelFormat.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1alpha1SupportedModelFormat.

        Name of the model format.  # noqa: E501

        :param name: The name of this V1alpha1SupportedModelFormat.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def version(self):
        """Gets the version of this V1alpha1SupportedModelFormat.  # noqa: E501

        Version of the model format. Used in validating that a predictor is supported by a runtime. Can be \"major\", \"major.minor\" or \"major.minor.patch\".  # noqa: E501

        :return: The version of this V1alpha1SupportedModelFormat.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this V1alpha1SupportedModelFormat.

        Version of the model format. Used in validating that a predictor is supported by a runtime. Can be \"major\", \"major.minor\" or \"major.minor.patch\".  # noqa: E501

        :param version: The version of this V1alpha1SupportedModelFormat.  # noqa: E501
        :type: str
        """

        self._version = version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1alpha1SupportedModelFormat):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1SupportedModelFormat):
            return True

        return self.to_dict() != other.to_dict()