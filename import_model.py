import bpy
import sys
import os

def import_fbx(filepath):
    bpy.ops.import_scene.fbx(filepath=filepath)

def import_dae(filepath):
    bpy.ops.wm.collada_import(filepath=filepath)

def import_obj(filepath):
    bpy.ops.import_scene.obj(filepath=filepath)

def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

import_function_map = {
    '.fbx': import_fbx,
    '.dae': import_dae,
    '.obj': import_obj,
}

def import_file(path):
    extension = os.path.splitext(path)[1].lower()

    # Attempt to import the file based on its extension
    if extension in import_function_map:
        import_function_map[extension](path)
    else:
        # Inform the user about the unsupported filetype and display the actual extension
        print(f"Unsupported filetype: '{extension}'. Supported types are .fbx, .dae, .obj")

def main():
    clear_scene()
    # The file path is the last argument in sys.argv
    import_file(sys.argv[-1])

if __name__ == "__main__":
    main()


