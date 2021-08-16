from mine_packer.versions import *

LAST_MC_VER = '1.17'

MinePacker = {
    '1.17': lambda: v1_17.Version()
}

game_register = None
object_model = None


def mp_init(minecraft_version=LAST_MC_VER):
    mp = MinePacker[LAST_MC_VER]()

    global game_register
    game_register = mp.game_register

    global object_model
    object_model = mp.object_model
