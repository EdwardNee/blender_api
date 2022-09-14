from blender_utils.blender_utils import *
from blender_utils.model_object import *


def process_object(model_object: ModelObject) -> None:
    path = model_object.name  # TODO find path to model in server folder.
    add_to_scene(path)


def process_coordinates(model_object: ModelObject) -> None:
    obj = is_on_scene(model_object.name)
    set_rotation(obj, model_object.rotation)
    set_translation(obj, model_object.translation)
    set_scale(obj, model_object.scale)


def start(list_models: str) -> None:
    model_objects = from_JSON_listmodels(list_models)
    for obj in model_objects:
        process_object(obj)
        process_coordinates(obj)
    remove_object("Cube")


def end(path_to_save: str) -> None:
    export_scene(path_to_save)


if __name__ == '__main__':
    # start(jsonString)
    # end(pathToFileToExport)
    pass
