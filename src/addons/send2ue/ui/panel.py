# Copyright Epic Games, Inc. All Rights Reserved.
import bpy
from ..constants import ToolInfo, Extensions

class SEND2UE_PT_NPanel(bpy.types.Panel):
    bl_label = "Send 2 UE"
    bl_idname = "SEND2UE_PT_NPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Send 2 UE"

    def draw(self, context):
        layout = self.layout
        # Export section
        layout.label(text="Export")
        layout.operator('wm.send2ue', text="Send to Unreal")
        layout.operator('wm.settings_dialog', text="Settings")
        # Import section
        layout.separator()
        layout.label(text="Import")
        layout.operator('wm.import_asset', text="Import Asset")
        # Utilities section
        layout.separator()
        layout.label(text="Utilities")
        layout.operator('send2ue.create_predefined_collections', text="Create Predefined Collections")
        layout.operator('send2ue.start_rpc_servers', text="Start RPC Servers")
        # Dynamic extension operators (if any)
        operator_namespace = getattr(bpy.ops, ToolInfo.NAME.value, None)
        if operator_namespace:
            for namespace in dir(operator_namespace):
                if namespace.startswith(f'{Extensions.NAME}_'):
                    layout.operator(f'{ToolInfo.NAME.value}.{namespace}')

def register():
    bpy.utils.register_class(SEND2UE_PT_NPanel)

def unregister():
    bpy.utils.unregister_class(SEND2UE_PT_NPanel)
