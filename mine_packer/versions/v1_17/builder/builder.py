import os, json


class Builder:
    def __init__(self, config):
        self.__build_config = config

    def build(self, pack):
        output_dir = 'build'

        path_datapack = os.path.join(output_dir, pack.name)
        path_mcmeta = os.path.join(path_datapack, 'pack.mcmeta')
        path_namespaces = os.path.join(path_datapack, 'data')

        self.make_directory(path_datapack)

        # create mcmeta
        mcmeta = {
            'pack': {
                'description': pack.description,
                'pack_format': self.__build_config['pack_format']
            }
        }

        mcmeta_text = json.dumps(mcmeta)
        open(path_mcmeta, 'w').write(mcmeta_text)

        # create namespaces
        self.make_directory(path_namespaces)

        namespaces = pack.get_namespaces()
        for i in range(len(namespaces)):
            namespace = namespaces[i]
            self.make_directory(os.path.join(path_namespaces, namespace.name))

    @staticmethod
    def make_directory(path):
        if not os.path.exists(path):
            os.makedirs(path)
