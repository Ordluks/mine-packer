# Mine Packer
Built datapacks for Minecraft easily! You do not need for create difficult file structure of your datapack.
Mine Packer intended for make datapack development easier.

## Datapack
More about Minecraft's datapacks - https://minecraft.fandom.com/wiki/Data_Pack

## Namespaces
Namespce can contain mcfunctions, loot tables, advancements, recipes, tags. More info - https://minecraft.fandom.com/wiki/Tutorials/Creating_a_data_pack#Naming

### Creating datapack example
```python
import mine_packer


# init mine packer for selected version of Minecraft
mine_packer.mp_init('1.17')

# create namespaces
namespace1 = mp.object_model.create_namespace('namespace1')
namespace2 = mp.object_model.create_namespace('namespace2')

# create datapack whis your namespaces
datapack = mp.object_model.create_datapack('Datapack name', 'Datapack description', [
  namespace1,
  namespace2
])
```
