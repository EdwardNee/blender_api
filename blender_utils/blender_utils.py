from typing import Tuple

import bpy
from bpy.types import Object
from mathutils import Quaternion, Vector


def add_to_scene(filepath: str) -> None:
    bpy.ops.import_scene.gltf(filepath=filepath)


def export_scene(to_file: str) -> None:
    bpy.ops.export_scene.gltf(filepath=to_file, export_format="GLB")


def remove_object(object_name: str) -> None:
    # Deselect the objects
    bpy.ops.object.select_all(action="DESELECT")

    # bpy.data.objects[object_name].select = True #2.7
    bpy.data.objects[object_name].select_set(True)  # 2.8
    bpy.ops.object.delete()


def is_on_scene(object_name: str) -> Object:
    obj = bpy.context.scene.objects.get(object_name)
    return obj


def set_rotation(obj_scene: Object, rotation: Tuple[float, float, float, float]) -> None:
    if not obj_scene:
        return
    obj_scene.rotation = Vector(rotation)


def set_translation(obj_scene: Object, position: Tuple[float, float, float]) -> None:
    if not obj_scene:
        return
    obj_scene.location = Vector(position)


def set_scale(obj_scene: Object, scale: Tuple[float, float, float]) -> None:
    if not obj_scene:
        return
    obj_scene.scale = Vector(scale)
