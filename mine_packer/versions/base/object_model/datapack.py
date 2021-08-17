from mine_packer.versions.base.object_model.namespace import Namespace


class Datapack:
    def __init__(self, name, description, namespaces=[]):
        self.name = name
        self.description = description
        self.__namespaces = namespaces

    def add_namespace(self, namespace):
        self.__namespaces.append(namespace)

    def get_namespaces(self):
        return self.__namespaces
