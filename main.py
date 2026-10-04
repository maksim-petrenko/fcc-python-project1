# https://www.freecodecamp.org/
# Curriculum: Python Certification
# Project: Build a User Configuration Manager
# Copyright (C) 2026 Maksim Petrenko


# Constants
ADD_SUCCESS = "Setting '{}' added with value '{}' successfully!"
ADD_FAILURE = "\
Setting '{}' already exists! Cannot add a new setting with this name."
UPDATE_SUCCESS = "Setting '{}' updated to '{}' successfully!"
UPDATE_FAILURE = "\
Setting '{}' does not exist! Cannot update a non-existing setting."
DELETE_SUCCESS = "Setting '{}' deleted successfully!"
DELETE_FAILURE = "Setting not found!"
VIEW_SUCCESS = "Current User Settings:\n"
VIEW_FAILURE = "No settings available."

# TEST
test_settings = {"theme": "dark", "notifications": "enabled", "volume": "high"}


########################################################################
# Functions

def add_setting(settings: dict, items: tuple) -> str:
    key = items[0].lower()
    value = items[1].lower()
    if key in settings:
        return ADD_FAILURE.format(key)
    else:
        settings[key] = value
        return ADD_SUCCESS.format(key, value)


def update_setting(settings: dict, items: tuple) -> str:
    key = items[0].lower()
    value = items[1].lower()
    if key in settings:
        settings[key] = value
        return UPDATE_SUCCESS.format(key, value)
    else:
        return UPDATE_FAILURE.format(key)


def delete_setting(settings: dict, key: str) -> str:
    key = key.lower()
    if key in settings:
        del settings[key]
        return DELETE_SUCCESS.format(key)
    else:
        return DELETE_FAILURE


def view_settings(settings: dict) -> str:
    if not settings:
        return VIEW_FAILURE
    else:
        result = VIEW_SUCCESS
        for key in settings:
            result += "{}: {}\n".format(key.capitalize(), settings[key])
        return result
