import json
from mine_packer.versions.v1_17.content_types import __ContentTypes as ContentTypes
from mine_packer.versions.v1_17.game_content import __GameContent as GameContent


class GameRegister:
    def __init__(self):
        register_file = open('mine_packer/versions/v1_17/register.json', 'r')
        register_data = json.loads(register_file.read().replace('minecraft:', ''))

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
