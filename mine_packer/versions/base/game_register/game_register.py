import json
from mine_packer.versions.base.game_register.content_types import ContentTypes
from mine_packer.versions.base.game_register.game_content import GameContent


class GameRegister:
    def __init__(self, register_data):
        if register_data is None:
            return

        register_data = json.loads(register_data)

        self.content_types = ContentTypes()

        # items to register
        items = register_data['item']['entries']
        self.items = {}

        for key in items:
            protocol_id = items[key]['protocol_id']
            name = key
            self.items[key] = GameContent(protocol_id, name, self.content_types.item)

        # blocks
        blocks = register_data['block']['entries']
        self.blocks = {}

        for key in blocks:
            protocol_id = blocks[key]['protocol_id']
            name = key
            self.blocks[key] = GameContent(protocol_id, name, self.content_types.block)

        # fluids
        fluids = register_data['fluid']['entries']
        self.fluids = {}

        for key in fluids:
            protocol_id = fluids[key]['protocol_id']
            name = key
            self.fluids[key] = GameContent(protocol_id, name, self.content_types.fluid)

        # entities
        entities = register_data['entity_type']['entries']
        self.entities = {}

        for key in entities:
            protocol_id = entities[key]['protocol_id']
            name = key
            self.entities[key] = GameContent(protocol_id, name, self.content_types.entity)
