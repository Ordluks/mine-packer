from mine_packer.versions.v1_17.object_model.datapack import Datapack
from mine_packer.versions.v1_17.object_model.namespace import Namespace


class ObjectModel:
    @staticmethod
    def create_datapack(name, description, namespaces=None):
        if namespaces is None:
            namespaces = []

        return Datapack(name, description, namespaces)

    @staticmethod
    def create_namespace(name):
        return Namespace(name)
