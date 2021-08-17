from mine_packer.versions.base import BaseVersion

from mine_packer.versions.v1_17.game_register.register_data import data


class Version(BaseVersion):
    build_config = {
        'pack_format': 7
    }
    register_data = data
