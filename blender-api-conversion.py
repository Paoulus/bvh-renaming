import sys

import bpy

argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "—"
bvh_in = argv[0]
fbx_out = argv[1]

# TO RUN:
# <blender.exe-path> -b --python blender-api-conversion.py -- <path-to-source-bvh> <path-to-dest-fbx>

# Import the BVH file
# See http://www.blender.org/documentation/blender_python_api_2_60_0/bpy.ops.import_anim.html
bpy.ops.import_anim.bvh(filepath = bvh_in, filter_glob = "*.bvh", global_scale = 1, frame_start = 1, use_fps_scale = False, use_cyclic = False, rotate_mode = 'NATIVE', axis_forward = '-Z',
                        axis_up = 'Y')

# Export as FBX 
# See http://www.blender.org/documentation/blender_python_api_2_62_1/bpy.ops.export_scene.html
# bpy.ops.export_scene.fbx(filepath = fbx_out, axis_forward = '-Z', axis_up = 'Y', use_anim = True, use_selection = True, use_default_take = False)
bpy.ops.export_scene.fbx(filepath = fbx_out, axis_forward = '-Z', axis_up = 'Y', use_selection = True, bake_anim = True)
