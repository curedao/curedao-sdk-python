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
    from openapi_client.model.tracking_reminder_notification_action import TrackingReminderNotificationAction
    from openapi_client.model.tracking_reminder_notification_track_all_action import TrackingReminderNotificationTrackAllAction
    from openapi_client.model.unit import Unit
    globals()['Card'] = Card
    globals()['TrackingReminderNotificationAction'] = TrackingReminderNotificationAction
    globals()['TrackingReminderNotificationTrackAllAction'] = TrackingReminderNotificationTrackAllAction
    globals()['Unit'] = Unit


class TrackingReminderNotification(ModelNormal):
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
        ('combination_operation',): {
            'MEAN': "MEAN",
            'SUM': "SUM",
        },
        ('variable_category_name',): {
            'ACTIVITY': "Activity",
            'BOOKS': "Books",
            'CAUSES_OF_ILLNESS': "Causes of Illness",
            'COGNITIVE_PERFORMANCE': "Cognitive Performance",
            'CONDITIONS': "Conditions",
            'EMOTIONS': "Emotions",
            'ENVIRONMENT': "Environment",
            'FOODS': "Foods",
            'GOALS': "Goals",
            'LOCATIONS': "Locations",
            'MISCELLANEOUS': "Miscellaneous",
            'MOVIES_AND_TV': "Movies and TV",
            'MUSIC': "Music",
            'NUTRIENTS': "Nutrients",
            'PAYMENTS': "Payments",
            'PHYSICAL_ACTIVITIES': "Physical Activities",
            'PHYSIQUE': "Physique",
            'SLEEP': "Sleep",
            'SOCIAL_INTERACTIONS': "Social Interactions",
            'SOFTWARE': "Software",
            'SYMPTOMS': "Symptoms",
            'TREATMENTS': "Treatments",
            'VITAL_SIGNS': "Vital Signs",
        },
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
            'action_array': ([TrackingReminderNotificationAction],),  # noqa: E501
            'available_units': ([Unit],),  # noqa: E501
            'filling_value': (int,),  # noqa: E501
            'id': (int,),  # noqa: E501
            'track_all_actions': ([TrackingReminderNotificationTrackAllAction],),  # noqa: E501
            'best_study_link': (str,),  # noqa: E501
            'best_study_card': (Card,),  # noqa: E501
            'best_user_study_link': (str,),  # noqa: E501
            'best_user_study_card': (Card,),  # noqa: E501
            'best_population_study_link': (str,),  # noqa: E501
            'best_population_study_card': (Card,),  # noqa: E501
            'optimal_value_message': (str,),  # noqa: E501
            'common_optimal_value_message': (str,),  # noqa: E501
            'user_optimal_value_message': (str,),  # noqa: E501
            'card': (Card,),  # noqa: E501
            'client_id': (str,),  # noqa: E501
            'combination_operation': (str,),  # noqa: E501
            'created_at': (str,),  # noqa: E501
            'display_name': (str,),  # noqa: E501
            'modified_value': (float,),  # noqa: E501
            'unit_abbreviated_name': (str,),  # noqa: E501
            'unit_category_id': (int,),  # noqa: E501
            'unit_category_name': (str,),  # noqa: E501
            'unit_id': (int,),  # noqa: E501
            'unit_name': (str,),  # noqa: E501
            'default_value': (float,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'email': (bool,),  # noqa: E501
            'icon_icon': (str,),  # noqa: E501
            'image_url': (str,),  # noqa: E501
            'input_type': (str,),  # noqa: E501
            'ion_icon': (str,),  # noqa: E501
            'last_value': (float,),  # noqa: E501
            'manual_tracking': (bool,),  # noqa: E501
            'maximum_allowed_value': (int,),  # noqa: E501
            'minimum_allowed_value': (int,),  # noqa: E501
            'most_common_value': (float,),  # noqa: E501
            'notification_bar': (bool,),  # noqa: E501
            'notified_at': (str,),  # noqa: E501
            'number_of_unique_values': (int,),  # noqa: E501
            'outcome': (bool,),  # noqa: E501
            'png_path': (str,),  # noqa: E501
            'png_url': (str,),  # noqa: E501
            'pop_up': (bool,),  # noqa: E501
            'product_url': (str,),  # noqa: E501
            'question': (str,),  # noqa: E501
            'long_question': (str,),  # noqa: E501
            'reminder_end_time': (str,),  # noqa: E501
            'reminder_frequency': (int,),  # noqa: E501
            'reminder_sound': (str,),  # noqa: E501
            'reminder_start_time': (str,),  # noqa: E501
            'reminder_time': (str,),  # noqa: E501
            'second_most_common_value': (float,),  # noqa: E501
            'second_to_last_value': (float,),  # noqa: E501
            'sms': (bool,),  # noqa: E501
            'svg_url': (str,),  # noqa: E501
            'third_most_common_value': (float,),  # noqa: E501
            'third_to_last_value': (float,),  # noqa: E501
            'title': (str,),  # noqa: E501
            'total': (float,),  # noqa: E501
            'tracking_reminder_id': (int,),  # noqa: E501
            'tracking_reminder_image_url': (str,),  # noqa: E501
            'tracking_reminder_notification_id': (int,),  # noqa: E501
            'tracking_reminder_notification_time': (str,),  # noqa: E501
            'tracking_reminder_notification_time_epoch': (int,),  # noqa: E501
            'tracking_reminder_notification_time_local': (str,),  # noqa: E501
            'tracking_reminder_notification_time_local_human_string': (str,),  # noqa: E501
            'updated_at': (str,),  # noqa: E501
            'user_id': (int,),  # noqa: E501
            'user_variable_unit_abbreviated_name': (str,),  # noqa: E501
            'user_variable_unit_category_id': (int,),  # noqa: E501
            'user_variable_unit_category_name': (str,),  # noqa: E501
            'user_variable_unit_id': (int,),  # noqa: E501
            'user_variable_unit_name': (str,),  # noqa: E501
            'user_variable_variable_category_id': (int,),  # noqa: E501
            'user_variable_variable_category_name': (str,),  # noqa: E501
            'valence': (str,),  # noqa: E501
            'variable_category_id': (int,),  # noqa: E501
            'variable_category_image_url': (str,),  # noqa: E501
            'variable_category_name': (str,),  # noqa: E501
            'variable_id': (int,),  # noqa: E501
            'variable_image_url': (str,),  # noqa: E501
            'variable_name': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'action_array': 'actionArray',  # noqa: E501
        'available_units': 'availableUnits',  # noqa: E501
        'filling_value': 'fillingValue',  # noqa: E501
        'id': 'id',  # noqa: E501
        'track_all_actions': 'trackAllActions',  # noqa: E501
        'best_study_link': 'bestStudyLink',  # noqa: E501
        'best_study_card': 'bestStudyCard',  # noqa: E501
        'best_user_study_link': 'bestUserStudyLink',  # noqa: E501
        'best_user_study_card': 'bestUserStudyCard',  # noqa: E501
        'best_population_study_link': 'bestPopulationStudyLink',  # noqa: E501
        'best_population_study_card': 'bestPopulationStudyCard',  # noqa: E501
        'optimal_value_message': 'optimalValueMessage',  # noqa: E501
        'common_optimal_value_message': 'commonOptimalValueMessage',  # noqa: E501
        'user_optimal_value_message': 'userOptimalValueMessage',  # noqa: E501
        'card': 'card',  # noqa: E501
        'client_id': 'clientId',  # noqa: E501
        'combination_operation': 'combinationOperation',  # noqa: E501
        'created_at': 'createdAt',  # noqa: E501
        'display_name': 'displayName',  # noqa: E501
        'modified_value': 'modifiedValue',  # noqa: E501
        'unit_abbreviated_name': 'unitAbbreviatedName',  # noqa: E501
        'unit_category_id': 'unitCategoryId',  # noqa: E501
        'unit_category_name': 'unitCategoryName',  # noqa: E501
        'unit_id': 'unitId',  # noqa: E501
        'unit_name': 'unitName',  # noqa: E501
        'default_value': 'defaultValue',  # noqa: E501
        'description': 'description',  # noqa: E501
        'email': 'email',  # noqa: E501
        'icon_icon': 'iconIcon',  # noqa: E501
        'image_url': 'imageUrl',  # noqa: E501
        'input_type': 'inputType',  # noqa: E501
        'ion_icon': 'ionIcon',  # noqa: E501
        'last_value': 'lastValue',  # noqa: E501
        'manual_tracking': 'manualTracking',  # noqa: E501
        'maximum_allowed_value': 'maximumAllowedValue',  # noqa: E501
        'minimum_allowed_value': 'minimumAllowedValue',  # noqa: E501
        'most_common_value': 'mostCommonValue',  # noqa: E501
        'notification_bar': 'notificationBar',  # noqa: E501
        'notified_at': 'notifiedAt',  # noqa: E501
        'number_of_unique_values': 'numberOfUniqueValues',  # noqa: E501
        'outcome': 'outcome',  # noqa: E501
        'png_path': 'pngPath',  # noqa: E501
        'png_url': 'pngUrl',  # noqa: E501
        'pop_up': 'popUp',  # noqa: E501
        'product_url': 'productUrl',  # noqa: E501
        'question': 'question',  # noqa: E501
        'long_question': 'longQuestion',  # noqa: E501
        'reminder_end_time': 'reminderEndTime',  # noqa: E501
        'reminder_frequency': 'reminderFrequency',  # noqa: E501
        'reminder_sound': 'reminderSound',  # noqa: E501
        'reminder_start_time': 'reminderStartTime',  # noqa: E501
        'reminder_time': 'reminderTime',  # noqa: E501
        'second_most_common_value': 'secondMostCommonValue',  # noqa: E501
        'second_to_last_value': 'secondToLastValue',  # noqa: E501
        'sms': 'sms',  # noqa: E501
        'svg_url': 'svgUrl',  # noqa: E501
        'third_most_common_value': 'thirdMostCommonValue',  # noqa: E501
        'third_to_last_value': 'thirdToLastValue',  # noqa: E501
        'title': 'title',  # noqa: E501
        'total': 'total',  # noqa: E501
        'tracking_reminder_id': 'trackingReminderId',  # noqa: E501
        'tracking_reminder_image_url': 'trackingReminderImageUrl',  # noqa: E501
        'tracking_reminder_notification_id': 'trackingReminderNotificationId',  # noqa: E501
        'tracking_reminder_notification_time': 'trackingReminderNotificationTime',  # noqa: E501
        'tracking_reminder_notification_time_epoch': 'trackingReminderNotificationTimeEpoch',  # noqa: E501
        'tracking_reminder_notification_time_local': 'trackingReminderNotificationTimeLocal',  # noqa: E501
        'tracking_reminder_notification_time_local_human_string': 'trackingReminderNotificationTimeLocalHumanString',  # noqa: E501
        'updated_at': 'updatedAt',  # noqa: E501
        'user_id': 'userId',  # noqa: E501
        'user_variable_unit_abbreviated_name': 'userVariableUnitAbbreviatedName',  # noqa: E501
        'user_variable_unit_category_id': 'userVariableUnitCategoryId',  # noqa: E501
        'user_variable_unit_category_name': 'userVariableUnitCategoryName',  # noqa: E501
        'user_variable_unit_id': 'userVariableUnitId',  # noqa: E501
        'user_variable_unit_name': 'userVariableUnitName',  # noqa: E501
        'user_variable_variable_category_id': 'userVariableVariableCategoryId',  # noqa: E501
        'user_variable_variable_category_name': 'userVariableVariableCategoryName',  # noqa: E501
        'valence': 'valence',  # noqa: E501
        'variable_category_id': 'variableCategoryId',  # noqa: E501
        'variable_category_image_url': 'variableCategoryImageUrl',  # noqa: E501
        'variable_category_name': 'variableCategoryName',  # noqa: E501
        'variable_id': 'variableId',  # noqa: E501
        'variable_image_url': 'variableImageUrl',  # noqa: E501
        'variable_name': 'variableName',  # noqa: E501
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
    def __init__(self, action_array, available_units, filling_value, id, track_all_actions, *args, **kwargs):  # noqa: E501
        """TrackingReminderNotification - a model defined in OpenAPI

        Args:
            action_array ([TrackingReminderNotificationAction]):
            available_units ([Unit]):
            filling_value (int): Ex: 0
            id (int): id for the specific PENDING tracking remidner
            track_all_actions ([TrackingReminderNotificationTrackAllAction]):

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
            best_study_link (str): Link to study comparing variable with strongest relationship for user or population. [optional]  # noqa: E501
            best_study_card (Card): [optional]  # noqa: E501
            best_user_study_link (str): Link to study comparing variable with strongest relationship for user. [optional]  # noqa: E501
            best_user_study_card (Card): [optional]  # noqa: E501
            best_population_study_link (str): Link to study comparing variable with strongest relationship for population. [optional]  # noqa: E501
            best_population_study_card (Card): [optional]  # noqa: E501
            optimal_value_message (str): Description of relationship with variable with strongest relationship for user or population. [optional]  # noqa: E501
            common_optimal_value_message (str): Description of relationship with variable with strongest relationship for population. [optional]  # noqa: E501
            user_optimal_value_message (str): Description of relationship with variable with strongest relationship for user. [optional]  # noqa: E501
            card (Card): [optional]  # noqa: E501
            client_id (str): Your CureDAO client id can be obtained by creating an app at https://builder.quantimo.do. [optional]  # noqa: E501
            combination_operation (str): The way multiple measurements are aggregated over time. [optional]  # noqa: E501
            created_at (str): Ex: 2017-07-29 20:49:54 UTC ISO 8601 YYYY-MM-DDThh:mm:ss. [optional]  # noqa: E501
            display_name (str): Ex: Trader Joe's Bedtime Tea. [optional]  # noqa: E501
            modified_value (float): Is the user specified default value or falls back to the last value in user unit. Good for initializing input fields. Unit: User-specified or common.. [optional]  # noqa: E501
            unit_abbreviated_name (str): Ex: /5. [optional]  # noqa: E501
            unit_category_id (int): Ex: 5. [optional]  # noqa: E501
            unit_category_name (str): Ex: Rating. [optional]  # noqa: E501
            unit_id (int): Ex: 10. [optional]  # noqa: E501
            unit_name (str): Ex: 1 to 5 Rating. [optional]  # noqa: E501
            default_value (float): Default value to use for the measurement when tracking. [optional]  # noqa: E501
            description (str): Valence indicates what type of buttons should be used when recording measurements for this variable. positive - Face buttons with the happiest face equating to a 5/5 rating where higher is better like Overall Mood. negative - Face buttons with happiest face equating to a 1/5 rating where lower is better like Headache Severity. numeric - Just 1 to 5 numeric buttons for neutral variables. . [optional]  # noqa: E501
            email (bool): True if the reminders should be delivered via email. [optional]  # noqa: E501
            icon_icon (str): Ex: ion-sad-outline. [optional]  # noqa: E501
            image_url (str): Ex: https://rximage.nlm.nih.gov/image/images/gallery/original/55111-0129-60_RXNAVIMAGE10_B051D81E.jpg. [optional]  # noqa: E501
            input_type (str): Ex: happiestFaceIsFive. [optional]  # noqa: E501
            ion_icon (str): Ex: ion-happy-outline. [optional]  # noqa: E501
            last_value (float): Ex: 3. [optional]  # noqa: E501
            manual_tracking (bool): True if this variable is normally tracked via manual user input rather than automatic imports. [optional]  # noqa: E501
            maximum_allowed_value (int): Ex: 5. [optional]  # noqa: E501
            minimum_allowed_value (int): Ex: 1. [optional]  # noqa: E501
            most_common_value (float): Ex: 3. [optional]  # noqa: E501
            notification_bar (bool): True if the reminders should appear in the notification bar. [optional]  # noqa: E501
            notified_at (str): Ex: UTC ISO 8601 YYYY-MM-DDThh:mm:ss. [optional]  # noqa: E501
            number_of_unique_values (int): Ex: 5. [optional]  # noqa: E501
            outcome (bool): Indicates whether or not the variable is usually an outcome of interest such as a symptom or emotion. [optional]  # noqa: E501
            png_path (str): Ex: img/variable_categories/emotions.png. [optional]  # noqa: E501
            png_url (str): Ex: https://app.curedao.org/img/variable_categories/emotions.png. [optional]  # noqa: E501
            pop_up (bool): True if the reminders should appear as a popup notification. [optional]  # noqa: E501
            product_url (str): Link to associated product for purchase. [optional]  # noqa: E501
            question (str): Ex: How is your overall mood?. [optional]  # noqa: E501
            long_question (str): Ex: How is your overall mood on a scale of 1 to 5??. [optional]  # noqa: E501
            reminder_end_time (str): Ex: 01-01-2018. [optional]  # noqa: E501
            reminder_frequency (int): How often user should be reminded in seconds. Ex: 86400. [optional]  # noqa: E501
            reminder_sound (str): String identifier for the sound to accompany the reminder. [optional]  # noqa: E501
            reminder_start_time (str): Earliest time of day at which reminders should appear in UTC HH:MM:SS format. [optional]  # noqa: E501
            reminder_time (str): UTC ISO 8601 YYYY-MM-DDThh:mm:ss timestamp for the specific time the variable should be tracked in UTC.  This will be used for the measurement startTime if the track endpoint is used.. [optional]  # noqa: E501
            second_most_common_value (float): Ex: 4. [optional]  # noqa: E501
            second_to_last_value (float): Ex: 1. [optional]  # noqa: E501
            sms (bool): True if the reminders should be delivered via SMS. [optional]  # noqa: E501
            svg_url (str): Ex: https://app.curedao.org/img/variable_categories/emotions.svg. [optional]  # noqa: E501
            third_most_common_value (float): Ex: 2. [optional]  # noqa: E501
            third_to_last_value (float): Ex: 2. [optional]  # noqa: E501
            title (str): Ex: Rate Overall Mood. [optional]  # noqa: E501
            total (float): Ex: 3. [optional]  # noqa: E501
            tracking_reminder_id (int): id for the repeating tracking remidner. [optional]  # noqa: E501
            tracking_reminder_image_url (str): Ex: https://rximage.nlm.nih.gov/image/images/gallery/original/55111-0129-60_RXNAVIMAGE10_B051D81E.jpg. [optional]  # noqa: E501
            tracking_reminder_notification_id (int): Ex: 5072482. [optional]  # noqa: E501
            tracking_reminder_notification_time (str): UTC ISO 8601 YYYY-MM-DDThh:mm:ss timestamp for the specific time the variable should be tracked in UTC.  This will be used for the measurement startTime if the track endpoint is used.. [optional]  # noqa: E501
            tracking_reminder_notification_time_epoch (int): Ex: 1501534124. [optional]  # noqa: E501
            tracking_reminder_notification_time_local (str): Ex: 15:48:44. [optional]  # noqa: E501
            tracking_reminder_notification_time_local_human_string (str): Ex: 8PM Sun, May 1. [optional]  # noqa: E501
            updated_at (str): When the record in the database was last updated. Use UTC ISO 8601 YYYY-MM-DDThh:mm:ss  datetime format. Time zone should be UTC and not local.. [optional]  # noqa: E501
            user_id (int): ID of User. [optional]  # noqa: E501
            user_variable_unit_abbreviated_name (str): Ex: /5. [optional]  # noqa: E501
            user_variable_unit_category_id (int): Ex: 5. [optional]  # noqa: E501
            user_variable_unit_category_name (str): Ex: Rating. [optional]  # noqa: E501
            user_variable_unit_id (int): Ex: 10. [optional]  # noqa: E501
            user_variable_unit_name (str): Ex: 1 to 5 Rating. [optional]  # noqa: E501
            user_variable_variable_category_id (int): Ex: 1. [optional]  # noqa: E501
            user_variable_variable_category_name (str): Ex: Emotions. [optional]  # noqa: E501
            valence (str): Valence indicates what type of buttons should be used when recording measurements for this variable. positive - Face buttons with the happiest face equating to a 5/5 rating where higher is better like Overall Mood. negative - Face buttons with happiest face equating to a 1/5 rating where lower is better like Headache Severity. numeric - Just 1 to 5 numeric buttons for neutral variables. . [optional]  # noqa: E501
            variable_category_id (int): Ex: 1. [optional]  # noqa: E501
            variable_category_image_url (str): Ex: https://static.quantimo.do/img/variable_categories/theatre_mask-96.png. [optional]  # noqa: E501
            variable_category_name (str): Ex: Emotions, Treatments, Symptoms.... [optional]  # noqa: E501
            variable_id (int): Id for the variable to be tracked. [optional]  # noqa: E501
            variable_image_url (str): Ex: https://image.png. [optional]  # noqa: E501
            variable_name (str): Name of the variable to be used when sending measurements. [optional]  # noqa: E501
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

        self.action_array = action_array
        self.available_units = available_units
        self.filling_value = filling_value
        self.id = id
        self.track_all_actions = track_all_actions
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
