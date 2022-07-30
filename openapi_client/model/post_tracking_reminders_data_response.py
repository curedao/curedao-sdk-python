"""
    CureDAO Unified Health API

    A platform for participant-centered research and personal data exploration  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

import nulltype  # noqa: F401

from openapi_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from openapi_client.model.card import Card
    from openapi_client.model.error_response import ErrorResponse
    from openapi_client.model.tracking_reminder import TrackingReminder
    from openapi_client.model.tracking_reminder_notification import TrackingReminderNotification
    from openapi_client.model.variable import Variable
    globals()['Card'] = Card
    globals()['ErrorResponse'] = ErrorResponse
    globals()['TrackingReminder'] = TrackingReminder
    globals()['TrackingReminderNotification'] = TrackingReminderNotification
    globals()['Variable'] = Variable


class PostTrackingRemindersDataResponse(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'tracking_reminder_notifications': ([TrackingReminderNotification],),  # noqa: E501
            'tracking_reminders': ([TrackingReminder],),  # noqa: E501
            'user_variables': ([Variable],),  # noqa: E501
            'description': (str,),  # noqa: E501
            'summary': (str,),  # noqa: E501
            'errors': ([ErrorResponse],),  # noqa: E501
            'status': (str,),  # noqa: E501
            'success': (bool,),  # noqa: E501
            'code': (float,),  # noqa: E501
            'link': (str,),  # noqa: E501
            'card': (Card,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'tracking_reminder_notifications': 'trackingReminderNotifications',  # noqa: E501
        'tracking_reminders': 'trackingReminders',  # noqa: E501
        'user_variables': 'userVariables',  # noqa: E501
        'description': 'description',  # noqa: E501
        'summary': 'summary',  # noqa: E501
        'errors': 'errors',  # noqa: E501
        'status': 'status',  # noqa: E501
        'success': 'success',  # noqa: E501
        'code': 'code',  # noqa: E501
        'link': 'link',  # noqa: E501
        'card': 'card',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """PostTrackingRemindersDataResponse - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            tracking_reminder_notifications ([TrackingReminderNotification]): [optional]  # noqa: E501
            tracking_reminders ([TrackingReminder]): [optional]  # noqa: E501
            user_variables ([Variable]): [optional]  # noqa: E501
            description (str): Can be used as body of help info popup. [optional]  # noqa: E501
            summary (str): Can be used as title in help info popup. [optional]  # noqa: E501
            errors ([ErrorResponse]): Array of error objects with message property. [optional]  # noqa: E501
            status (str): ex. OK or ERROR. [optional]  # noqa: E501
            success (bool): true or false. [optional]  # noqa: E501
            code (float): Response code such as 200. [optional]  # noqa: E501
            link (str): A super neat url you might want to share with your users!. [optional]  # noqa: E501
            card (Card): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
