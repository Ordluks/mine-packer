from mine_packer.versions import *


def __not_init():
    print('Mine Packer is not init')


LAST_MC_VER = '1.17'

MinePacker = {
    '1.17': lambda: v1_17.Version()
}

game_register = base.GameRegister(None)

object_model = base.ObjectModel()
object_model.create_datapack = __not_init
object_model.create_namespace = __not_init

builder = base.Builder(None)


def mp_init(minecraft_version=LAST_MC_VER):
    mp = MinePacker[minecraft_version]()

    global game_register
    game_register = mp.game_register

    global object_model
    object_model = mp.object_model

    global builder
    builder = mp.builder
