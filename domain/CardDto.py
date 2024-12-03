import json


class CardDto:
    def __init__(self, id, native, foreign, tags=None):
        if tags is None:
            tags = []
        self.id = id
        self.native = native
        self.foreign = foreign
        self.tags = tags

    def toJson(self):
        return json.dumps(self.__dict__)
