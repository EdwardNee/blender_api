import json
from typing import Tuple, List


class ModelObject(object):
    def __init__(self,
                 name,
                 translation: Tuple[float, float, float] = (0, 0, 0),
                 rotation: Tuple[float, float, float, float] = (0, 0, 0, 0),
                 scale: Tuple[float, float, float] = (0, 0, 0)
                 ) -> None:
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
    def __init__(self, listOfModels=None):
        if listOfModels is None:
            listOfModels = []
        self.listOfModels = listOfModels

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True,
                          indent=4)


def from_JSON_listmodels(jsonstr: str) -> List[ModelObject]:
    jsonobj = json.loads(jsonstr)
    result = [from_JSON_model_obj(json.dumps(e)) for e in jsonobj["listOfModels"]]
    return result
