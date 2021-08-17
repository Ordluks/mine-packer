class Namespace:
    def __init__(self, name: str, tags=[]):
        self.name = name
        self.__tags = tags

    def get_tags(self):
        return self.__tags
