# Copyright Epic Games, Inc. All Rights Reserved.

import bpy
import os
import importlib
from . import operators, properties, constants
from .dependencies import remote_execution, unreal
from .ui import header_menu, addon_preferences, file_browser, dialog, panel
from .core import formatting, validations, settings, utilities, export, ingest, extension, io

modules = [
    export,
    ingest,
    settings,
    unreal,
    utilities,
    formatting,
    validations,
    dialog,
    file_browser,
    operators,
    properties,
    constants,
    remote_execution,
    addon_preferences,
    extension,
    io.fbx_b3,
    io.fbx_b4
]


def register():
    """
    Registers the addon classes when the addon is enabled.
    """
    # reload the submodules
    if os.environ.get('SEND2UE_DEV'):
        for module in modules:
            importlib.reload(module)
    try:
        properties.register()
        operators.register()
        header_menu.register()
        addon_preferences.register()
        panel.register()
    except RuntimeError as error:
        print(error)
    bpy.app.handlers.load_post.append(bpy.app.handlers.persistent(utilities.setup_project))
    bpy.app.timers.register(utilities.addon_enabled, first_interval=0.1)


def unregister():
    """
    Unregisters the addon classes when the addon is disabled.
    """
    if utilities.setup_project in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.remove(utilities.setup_project)
    try:
        header_menu.remove_parent_menu()
        header_menu.unregister()
        addon_preferences.unregister()
        panel.unregister()
        operators.unregister()
        properties.unregister()
    except RuntimeError as error:
        print(error)
    utilities.remove_temp_data()
