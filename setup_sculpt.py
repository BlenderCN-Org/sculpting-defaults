bl_info = {
    "name": "Setup Good Defaults for Scultping",
    "description": "Set several defaults for sculpting from the basic startup file. Based on YanSculpts suggestions",
    "author": "Johnny Matthews",
    "version": (0, 0, 1),
    "blender": (2, 79, 0),
    "location": "View3d > View > Setup YanSculpts Defaults",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "View3d"
}


import bpy


def setup(context):
    bpy.ops.view3d.snap_cursor_to_center()
    bpy.ops.mesh.primitive_uv_sphere_add(size=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.context.space_data.use_matcap = True
    bpy.context.space_data.matcap_icon = '06'
    bpy.context.space_data.fx_settings.use_ssao = True
    bpy.context.space_data.lens = 100    
    bpy.data.brushes["Grab"].strength = 0.1
    
    points = bpy.data.brushes["Scrape/Peaks"].curve.curves[0].points
    while len(points) > 2:
        points.remove(points[1])            
    points[0].location = [0,1]
    points[1].location = [1,1]
    bpy.data.brushes["Scrape/Peaks"].curve.update()
      
    return {'FINISHED'}

from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator

class SetupSculpting(Operator):
    bl_idname = "setup.sculptingdefaults"  
    bl_label = "Setup Good Sculpting Defaults"

    def execute(self, context):
        return setup(context)

def menu_func_import(self, context):
    self.layout.operator(SetupSculpting.bl_idname, text="Setup YanSculpts Defaults")


def register():
    bpy.utils.register_class(SetupSculpting)
    bpy.types.VIEW3D_MT_view.append(menu_func_import)


def unregister():
    bpy.utils.unregister_class(SetupSculpting)
    bpy.types.VIEW3D_MT_view.remove(menu_func_import)


if __name__ == "__main__":
    register()
