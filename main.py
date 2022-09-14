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


def start(model_objects: List[ModelObject]) -> None:
    for obj in model_objects:
        process_object(obj)
        process_coordinates(obj)
    remove_object("Cube")


def end(path_to_save: str) -> None:
    export_scene(path_to_save)


if __name__ == '__main__':
    list_models = ""  # TODO Json string
    json_object = from_JSON_listmodels(list_models)
    start(json_object.list_models)
    # end(pathToFileToExport + "\\" + json_object.pole_name) #TODO pathToFileToExport dir with exported files
    pass
