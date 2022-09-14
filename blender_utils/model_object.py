import json


class ModelObject(object):
    def __init__(self, name, translation=None, rotation=None,
                 scale=None) -> None:
        if scale is None:
            scale = [1, 1, 1]
        if translation is None:
            translation = [0, 0, 0]
        if rotation is None:
            rotation = [1, 0, 0, 0]
        self.name = name
        self.translation = translation
        self.rotation = rotation
        self.scale = scale

    def toJSON(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


def from_JSON_model_obj(string_obj: str) -> ModelObject:
    return json.loads(string_obj, object_hook=lambda d: ModelObject(**d))


class JsonObj(object):
    def __init__(self, pole_name=None, list_models=None):
        if list_models is None:
            list_models = []
        if pole_name is None:
            pole_name = ""
        self.list_models = list_models
        self.pole_name = pole_name

    def toJSON(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True,
                          indent=4)


def from_JSON_listmodels(jsonstr: str) -> JsonObj:
    jsonobj = json.loads(jsonstr)
    result = [from_JSON_model_obj(json.dumps(e)) for e in
              jsonobj["list_models"]]

    return JsonObj(jsonobj["pole_name"], result)
