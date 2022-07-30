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
    from openapi_client.model.authorized_clients import AuthorizedClients
    from openapi_client.model.card import Card
    globals()['AuthorizedClients'] = AuthorizedClients
    globals()['Card'] = Card


class User(ModelNormal):
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
            'access_token': (str,),  # noqa: E501
            'administrator': (bool,),  # noqa: E501
            'display_name': (str,),  # noqa: E501
            'email': (str,),  # noqa: E501
            'id': (int,),  # noqa: E501
            'login_name': (str,),  # noqa: E501
            'access_token_expires': (str,),  # noqa: E501
            'access_token_expires_at_milliseconds': (int,),  # noqa: E501
            'authorized_clients': (AuthorizedClients,),  # noqa: E501
            'avatar': (str,),  # noqa: E501
            'avatar_image': (str,),  # noqa: E501
            'capabilities': (str,),  # noqa: E501
            'card': (Card,),  # noqa: E501
            'client_id': (str,),  # noqa: E501
            'client_user_id': (str,),  # noqa: E501
            'combine_notifications': (bool,),  # noqa: E501
            'created_at': (str,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'earliest_reminder_time': (str,),  # noqa: E501
            'first_name': (str,),  # noqa: E501
            'get_preview_builds': (bool,),  # noqa: E501
            'has_android_app': (bool,),  # noqa: E501
            'has_chrome_extension': (bool,),  # noqa: E501
            'has_ios_app': (bool,),  # noqa: E501
            'last_active': (str,),  # noqa: E501
            'last_four': (str,),  # noqa: E501
            'last_name': (str,),  # noqa: E501
            'last_sms_tracking_reminder_notification_id': (str,),  # noqa: E501
            'latest_reminder_time': (str,),  # noqa: E501
            'password': (str,),  # noqa: E501
            'phone_number': (str,),  # noqa: E501
            'phone_verification_code': (str,),  # noqa: E501
            'primary_outcome_variable_id': (int,),  # noqa: E501
            'primary_outcome_variable_name': (str,),  # noqa: E501
            'push_notifications_enabled': (bool,),  # noqa: E501
            'refresh_token': (str,),  # noqa: E501
            'roles': (str,),  # noqa: E501
            'send_predictor_emails': (bool,),  # noqa: E501
            'send_reminder_notification_emails': (bool,),  # noqa: E501
            'share_all_data': (bool,),  # noqa: E501
            'sms_notifications_enabled': (bool,),  # noqa: E501
            'stripe_active': (bool,),  # noqa: E501
            'stripe_id': (str,),  # noqa: E501
            'stripe_plan': (str,),  # noqa: E501
            'stripe_subscription': (str,),  # noqa: E501
            'subscription_ends_at': (str,),  # noqa: E501
            'subscription_provider': (str,),  # noqa: E501
            'time_zone_offset': (int,),  # noqa: E501
            'track_location': (bool,),  # noqa: E501
            'updated_at': (str,),  # noqa: E501
            'user_registered': (str,),  # noqa: E501
            'user_url': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'access_token': 'accessToken',  # noqa: E501
        'administrator': 'administrator',  # noqa: E501
        'display_name': 'displayName',  # noqa: E501
        'email': 'email',  # noqa: E501
        'id': 'id',  # noqa: E501
        'login_name': 'loginName',  # noqa: E501
        'access_token_expires': 'accessTokenExpires',  # noqa: E501
        'access_token_expires_at_milliseconds': 'accessTokenExpiresAtMilliseconds',  # noqa: E501
        'authorized_clients': 'authorizedClients',  # noqa: E501
        'avatar': 'avatar',  # noqa: E501
        'avatar_image': 'avatarImage',  # noqa: E501
        'capabilities': 'capabilities',  # noqa: E501
        'card': 'card',  # noqa: E501
        'client_id': 'clientId',  # noqa: E501
        'client_user_id': 'clientUserId',  # noqa: E501
        'combine_notifications': 'combineNotifications',  # noqa: E501
        'created_at': 'createdAt',  # noqa: E501
        'description': 'description',  # noqa: E501
        'earliest_reminder_time': 'earliestReminderTime',  # noqa: E501
        'first_name': 'firstName',  # noqa: E501
        'get_preview_builds': 'getPreviewBuilds',  # noqa: E501
        'has_android_app': 'hasAndroidApp',  # noqa: E501
        'has_chrome_extension': 'hasChromeExtension',  # noqa: E501
        'has_ios_app': 'hasIosApp',  # noqa: E501
        'last_active': 'lastActive',  # noqa: E501
        'last_four': 'lastFour',  # noqa: E501
        'last_name': 'lastName',  # noqa: E501
        'last_sms_tracking_reminder_notification_id': 'lastSmsTrackingReminderNotificationId',  # noqa: E501
        'latest_reminder_time': 'latestReminderTime',  # noqa: E501
        'password': 'password',  # noqa: E501
        'phone_number': 'phoneNumber',  # noqa: E501
        'phone_verification_code': 'phoneVerificationCode',  # noqa: E501
        'primary_outcome_variable_id': 'primaryOutcomeVariableId',  # noqa: E501
        'primary_outcome_variable_name': 'primaryOutcomeVariableName',  # noqa: E501
        'push_notifications_enabled': 'pushNotificationsEnabled',  # noqa: E501
        'refresh_token': 'refreshToken',  # noqa: E501
        'roles': 'roles',  # noqa: E501
        'send_predictor_emails': 'sendPredictorEmails',  # noqa: E501
        'send_reminder_notification_emails': 'sendReminderNotificationEmails',  # noqa: E501
        'share_all_data': 'shareAllData',  # noqa: E501
        'sms_notifications_enabled': 'smsNotificationsEnabled',  # noqa: E501
        'stripe_active': 'stripeActive',  # noqa: E501
        'stripe_id': 'stripeId',  # noqa: E501
        'stripe_plan': 'stripePlan',  # noqa: E501
        'stripe_subscription': 'stripeSubscription',  # noqa: E501
        'subscription_ends_at': 'subscriptionEndsAt',  # noqa: E501
        'subscription_provider': 'subscriptionProvider',  # noqa: E501
        'time_zone_offset': 'timeZoneOffset',  # noqa: E501
        'track_location': 'trackLocation',  # noqa: E501
        'updated_at': 'updatedAt',  # noqa: E501
        'user_registered': 'userRegistered',  # noqa: E501
        'user_url': 'userUrl',  # noqa: E501
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
    def __init__(self, access_token, administrator, display_name, email, id, login_name, *args, **kwargs):  # noqa: E501
        """User - a model defined in OpenAPI

        Args:
            access_token (str): User access token
            administrator (bool): Is user administrator
            display_name (str): User display name
            email (str): User email
            id (int): User id
            login_name (str): User login name

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
            access_token_expires (str): Ex: 2018-08-08 02:41:19. [optional]  # noqa: E501
            access_token_expires_at_milliseconds (int): Ex: 1533696079000. [optional]  # noqa: E501
            authorized_clients (AuthorizedClients): [optional]  # noqa: E501
            avatar (str): Ex: https://lh6.googleusercontent.com/-BHr4hyUWqZU/AAAAAAAAAAI/AAAAAAAIG28/2Lv0en738II/photo.jpg?sz=50. [optional]  # noqa: E501
            avatar_image (str): Ex: https://lh6.googleusercontent.com/-BHr4hyUWqZU/AAAAAAAAAAI/AAAAAAAIG28/2Lv0en738II/photo.jpg?sz=50. [optional]  # noqa: E501
            capabilities (str): Ex: a:1:{s:13:\"administrator\";b:1;}. [optional]  # noqa: E501
            card (Card): [optional]  # noqa: E501
            client_id (str): Ex: curedao. [optional]  # noqa: E501
            client_user_id (str): Ex: 118444693184829555362. [optional]  # noqa: E501
            combine_notifications (bool): Ex: 1. [optional]  # noqa: E501
            created_at (str): When the record was first created. Use UTC ISO 8601 YYYY-MM-DDThh:mm:ss datetime format. [optional]  # noqa: E501
            description (str): Your bio will be displayed on your published studies. [optional]  # noqa: E501
            earliest_reminder_time (str): Earliest time user should get notifications. Ex: 05:00:00. [optional]  # noqa: E501
            first_name (str): Ex: Mike. [optional]  # noqa: E501
            get_preview_builds (bool): Ex: false. [optional]  # noqa: E501
            has_android_app (bool): Ex: false. [optional]  # noqa: E501
            has_chrome_extension (bool): Ex: false. [optional]  # noqa: E501
            has_ios_app (bool): Ex: false. [optional]  # noqa: E501
            last_active (str): Ex: Date the user last logged in. [optional]  # noqa: E501
            last_four (str): Ex: 2009. [optional]  # noqa: E501
            last_name (str): Ex: Sinn. [optional]  # noqa: E501
            last_sms_tracking_reminder_notification_id (str): Ex: 1. [optional]  # noqa: E501
            latest_reminder_time (str): Latest time user should get notifications. Ex: 23:00:00. [optional]  # noqa: E501
            password (str): Ex: PASSWORD. [optional]  # noqa: E501
            phone_number (str): Ex: 618-391-0002. [optional]  # noqa: E501
            phone_verification_code (str): Ex: 1234. [optional]  # noqa: E501
            primary_outcome_variable_id (int): A good primary outcome variable is something that you want to improve and that changes inexplicably. For instance, if you have anxiety, back pain or arthritis which is worse on some days than others, these would be good candidates for primary outcome variables.  Recording their severity and potential factors will help you identify hidden factors exacerbating or improving them. . [optional]  # noqa: E501
            primary_outcome_variable_name (str): A good primary outcome variable is something that you want to improve and that changes inexplicably. For instance, if you have anxiety, back pain or arthritis which is worse on some days than others, these would be good candidates for primary outcome variables.  Recording their severity and potential factors will help you identify hidden factors exacerbating or improving them. . [optional]  # noqa: E501
            push_notifications_enabled (bool): Ex: 1. [optional]  # noqa: E501
            refresh_token (str): See https://oauth.net/2/grant-types/refresh-token/. [optional]  # noqa: E501
            roles (str): Ex: [\"admin\"]. [optional]  # noqa: E501
            send_predictor_emails (bool): Ex: 1. [optional]  # noqa: E501
            send_reminder_notification_emails (bool): Ex: 1. [optional]  # noqa: E501
            share_all_data (bool): Share all studies, charts, and measurement data with all other users. [optional]  # noqa: E501
            sms_notifications_enabled (bool): Ex: false. [optional]  # noqa: E501
            stripe_active (bool): Ex: 1. [optional]  # noqa: E501
            stripe_id (str): Ex: cus_A8CEmcvl8jwLhV. [optional]  # noqa: E501
            stripe_plan (str): Ex: monthly7. [optional]  # noqa: E501
            stripe_subscription (str): Ex: sub_ANTx3nOE7nzjQf. [optional]  # noqa: E501
            subscription_ends_at (str): UTC ISO 8601 YYYY-MM-DDThh:mm:ss. [optional]  # noqa: E501
            subscription_provider (str): Ex: google. [optional]  # noqa: E501
            time_zone_offset (int): Ex: 300. [optional]  # noqa: E501
            track_location (bool): Ex: 1. [optional]  # noqa: E501
            updated_at (str): When the record in the database was last updated. Use UTC ISO 8601 YYYY-MM-DDThh:mm:ss datetime format. [optional]  # noqa: E501
            user_registered (str): Ex: 2013-12-03 15:25:13 UTC ISO 8601 YYYY-MM-DDThh:mm:ss. [optional]  # noqa: E501
            user_url (str): Ex: https://plus.google.com/+MikeSinn. [optional]  # noqa: E501
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

        self.access_token = access_token
        self.administrator = administrator
        self.display_name = display_name
        self.email = email
        self.id = id
        self.login_name = login_name
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)