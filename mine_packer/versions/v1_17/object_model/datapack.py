from mine_packer.versions.v1_17.object_model.namespace import Namespace


class Datapack:
    __namespaces = []

    def __init__(self, name, description, namespaces=None):
        if namespaces is None:
            namespaces = []

        self.__namespaces = namespaces
        self.name = name
        self.description = description

    def add_namespace(self, namespace):
        self.__namespaces.append(namespace)
