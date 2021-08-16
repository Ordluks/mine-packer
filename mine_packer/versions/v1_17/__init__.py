from mine_packer.versions.v1_17.game_register.game_register import GameRegister
from mine_packer.versions.v1_17.object_model.object_model import ObjectModel


class Version:
    build_config = {
        'pack_format': 7
    }
    game_register = GameRegister()
    object_model = ObjectModel()
