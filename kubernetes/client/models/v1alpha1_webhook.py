# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.13.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1alpha1Webhook(object):
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
        'client_config': 'V1alpha1WebhookClientConfig',
        'throttle': 'V1alpha1WebhookThrottleConfig'
    }

    attribute_map = {
        'client_config': 'clientConfig',
        'throttle': 'throttle'
    }

    def __init__(self, client_config=None, throttle=None):
        """
        V1alpha1Webhook - a model defined in Swagger
        """

        self._client_config = None
        self._throttle = None
        self.discriminator = None

        self.client_config = client_config
        if throttle is not None:
          self.throttle = throttle

    @property
    def client_config(self):
        """
        Gets the client_config of this V1alpha1Webhook.
        ClientConfig holds the connection parameters for the webhook required

        :return: The client_config of this V1alpha1Webhook.
        :rtype: V1alpha1WebhookClientConfig
        """
        return self._client_config

    @client_config.setter
    def client_config(self, client_config):
        """
        Sets the client_config of this V1alpha1Webhook.
        ClientConfig holds the connection parameters for the webhook required

        :param client_config: The client_config of this V1alpha1Webhook.
        :type: V1alpha1WebhookClientConfig
        """
        if client_config is None:
            raise ValueError("Invalid value for `client_config`, must not be `None`")

        self._client_config = client_config

    @property
    def throttle(self):
        """
        Gets the throttle of this V1alpha1Webhook.
        Throttle holds the options for throttling the webhook

        :return: The throttle of this V1alpha1Webhook.
        :rtype: V1alpha1WebhookThrottleConfig
        """
        return self._throttle

    @throttle.setter
    def throttle(self, throttle):
        """
        Sets the throttle of this V1alpha1Webhook.
        Throttle holds the options for throttling the webhook

        :param throttle: The throttle of this V1alpha1Webhook.
        :type: V1alpha1WebhookThrottleConfig
        """

        self._throttle = throttle

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
        if not isinstance(other, V1alpha1Webhook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
