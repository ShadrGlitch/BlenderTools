# Copyright Epic Games, Inc. All Rights Reserved.
import bpy
from ..constants import ToolInfo, Extensions

class SEND2UE_PT_Export(bpy.types.Panel):
    bl_label = "Export"
    bl_idname = "SEND2UE_PT_Export"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Send 2 UE"

    def draw(self, context):
        layout = self.layout
        layout.operator('wm.send2ue', text="Push Assets")
        layout.operator('wm.import_asset', text="Import Asset")
        layout.operator('wm.settings_dialog', text="Settings")


class SEND2UE_PT_Utilities(bpy.types.Panel):
    bl_label = "Utilities"
    bl_idname = "SEND2UE_PT_Utilities"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Send 2 UE"

    def draw(self, context):
        layout = self.layout
        layout.operator('send2ue.create_predefined_collections', text="Create Predefined Collections")
        layout.operator('send2ue.start_rpc_servers', text="Start RPC Servers")
        operator_namespace = getattr(bpy.ops, ToolInfo.NAME.value, None)
        if operator_namespace:
            for namespace in dir(operator_namespace):
                if namespace.startswith(f'{Extensions.NAME}_'):
                    layout.operator(f'{ToolInfo.NAME.value}.{namespace}')

classes = [
    SEND2UE_PT_Export,
    SEND2UE_PT_Utilities
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
