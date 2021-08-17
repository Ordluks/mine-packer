from mine_packer.versions.base.game_register.game_register import GameRegister
from mine_packer.versions.base.object_model.object_model import ObjectModel
from mine_packer.versions.base.builder.builder import Builder


class BaseVersion:
    build_config = None
    register_data = None

    def __init__(self):
        self.game_register = GameRegister(self.register_data)
        self.object_model = ObjectModel()
        self.builder = Builder(self.build_config)
