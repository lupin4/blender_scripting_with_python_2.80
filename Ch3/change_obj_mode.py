import bpy

bpy.ops.object.mode_set(mode = 'OBJECT')
cube = bpy.context.scene.objects['Cube']
bpy.context.view_layer.objects.active = cube
cube.select_set(True)
bpy.ops.object.mode_set(mode = 'EDIT')
bpy.context.view_layer.update()
