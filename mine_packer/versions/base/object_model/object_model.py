from mine_packer.versions.base.object_model.datapack import Datapack
from mine_packer.versions.base.object_model.namespace import Namespace


class ObjectModel:
    @staticmethod
    def create_datapack(name, description, namespaces=[]):
        return Datapack(name, description, namespaces)

    @staticmethod
    def create_namespace(name: str, tags=[]):
        return Namespace(name, tags)
