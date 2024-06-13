# Composter
A composter is a block that converts some biological material into bone meal. It also serves as a farmer villager's job site block.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Composting
	- 2.2 Changing profession
	- 2.3 Redstone component
	- 2.4 Hoppers
	- 2.5 Fuel
	- 2.6 Note blocks
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Trivia
- 8 Gallery
	- 8.1 Renders
		- 8.1.1 Java Edition
		- 8.1.2 Bedrock Edition
	- 8.2 Screenshots
- 9 References
- 10 External links

## Obtaining
### Breaking
Composters can be broken using any tool, though an axe is the fastest. The composter does not retain the compost inside; instead, it drops empty.

| Block     | Composter             |
|-----------|-----------------------|
| Hardness  | 0.6                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 0.9                   |
| Wooden    | 0.45                  |
| Stone     | 0.25                  |
| Iron      | 0.15                  |
| Diamond   | 0.15                  |
| Netherite | 0.1                   |
| Golden    | 0.1                   |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Composters generate in village farms. They can also generate in trail ruins.

### Crafting
| Ingredients    | Crafting recipe |
|----------------|-----------------|
| AnyWooden Slab |                 |

## Usage
Composters can be used to recycle a selection of food and plant items into bone meal. To do so, the player must use any of a selection of items on the composter. When an adjacent comparator is facing away from the composter, a comparator signal strength of up to 8 is emitted depending on the fullness of the block.

Composters appear to have an empty interior. As such, entities can enter and exit a composter through the top, but not the sides or bottom. The composter has a "floor", whose height depends on the fullness. When the composter is completely empty, this floor is slightly above the block below, and when it is completely full, there is a slight dip on top. In Bedrock Edition, when the composter’s fullness increases, any entities inside are pushed up accordingly.

### Composting
The composter can be filled with compost, which is done by adding compostable items to it. When successfully adding an item, a green particle () appears. The table below lists supported items, which have different levels of compost-ability. The higher the percentage of an item, the more likely it is for it to add another layer of compost. While the composter is empty, any compostable item can create the first layer of compost. Each layer of compost has a podzol-like appearance. When the composter reaches the 7th layer of compost, the compost changes appearance indicating that bone meal can be collected by using the composter a final time.

The following table shows the items that can be used in a composter, the percent chance for an item to add a level of compost, and the average number of items needed to fill a composter. Smaller pieces (individual pieces of wheat, melon slices, etc.) produce more compost than the blocks or other items that can be made from them. The exception is cookies, because each recipe produces 8 cookies, and together those give more than 3 times the compost.

Despite being plants, it is not possible to compost bamboo,[1] dead bushes,[2] poisonous potatoes[3] and chorus plant products.[4]. Meat and fish are also not compostable, unlike some other food items.

| Composting chance (per item)                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                            |                           |                                             |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|---------------------------------------------|
| 30%                                                                                                                                                                                                                                                                                                                                                                   | 50%                                                                                                                                                                                          | 65%                                                                                                                                                                                                                                                                                                                                                       | 85%                                                                                                                                                                        | 100%                      |                                             |
|                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                            |                           | Items                                       |
| Beetroot Seeds<br/>Dried Kelp<br/>Glow Berries<br/>Grass Block‌[BE  only]<br/>Hanging Roots<br/>Mangrove Propagule<br/>Mangrove Roots<br/>Kelp<br/>Leaves<br/>Melon Seeds<br/>Moss Carpet<br/>Pink Petals<br/>Pitcher Pod<br/>Pumpkin Seeds<br/>Saplings<br/>Seagrass<br/>Short Grass<br/>Small Dripleaf<br/>Sweet Berries<br/>Torchflower Seeds<br/>Wheat Seeds<br/> | Cactus<br/>Dried Kelp Block<br/>Flowering Azalea Leaves<br/>Glow Lichen<br/>Melon Slice<br/>Nether Sprouts<br/>Sugar Cane<br/>Tall Grass<br/>Twisting Vines<br/>Vines<br/>Weeping Vines<br/> | Apple<br/>Azalea<br/>Beetroot<br/>Big Dripleaf<br/>Carrot<br/>Cocoa Beans<br/>Fern<br/>Flowers<br/>Fungus<br/>Large Fern<br/>Lily Pad<br/>Melon<br/>Moss Block<br/>Mushrooms<br/>Mushroom Stem<br/>Nether Wart<br/>Potato<br/>Pumpkins<br/>Crimson Roots<br/>Warped Roots<br/>Sea Pickle<br/>Shroomlight<br/>Spore Blossom<br/>Wheat<br/>Wither Rose<br/> | Baked Potato<br/>Bread<br/>Cookie<br/>Flowering Azalea<br/>Hay Bale<br/>Mushroom Blocks<br/>Nether Wart Block<br/>Pitcher Plant<br/>Torchflower<br/>Warped Wart Block<br/> | Cake<br/>Pumpkin Pie<br/> |                                             |
|                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                            |                           | Average number of items to complete compost |
| 23.33                                                                                                                                                                                                                                                                                                                                                                 | 14.00                                                                                                                                                                                        | 10.77                                                                                                                                                                                                                                                                                                                                                     | 8.24                                                                                                                                                                       | 7.00                      |                                             |
|                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                            |                           | Average compost yield (per stack)           |
| 2.74                                                                                                                                                                                                                                                                                                                                                                  | 4.57                                                                                                                                                                                         | 5.94                                                                                                                                                                                                                                                                                                                                                      | 7.77                                                                                                                                                                       | 9.14                      |                                             |

### Changing profession
If a village has a composter that has not been claimed by a villager, any resident villager who has not already chosen a job site block has a chance to change their profession to farmer.

### Redstone component
See also: Redstone circuit

A composter can act as a power source for a redstone comparator. With a composter behind it (either directly, or separated by an unpowered solid block), a comparator outputs a signal strength between 0 and 8, proportional to how full the composter is: 0 for empty, 1 for 1⁄7 full, 2 for 2⁄7 full, and so on to 6. 7 is for completely full but the bone meal is not ready to collect, and 8 for completely full and the bone meal is ready to collect. However, if there is a block between the composter and comparator, the comparator does not immediately update.

### Hoppers
Composters can interact with hoppers. A hopper directly below a composter pulls bone meal from it. A hopper or dropper facing downward directly above a composter pushes items into it. See Hopper § Redstone component for more details.

Hoppers cannot interact with the sides of a composter.

Composters are also often placed on top of hoppers when they don't need to suck items in from the world. This is because hoppers with containers on top of them don't look for item entities around them and the composter is the container with the least amount of information stored so this helps reducing lag.

### Fuel
A composter can be used as fuel in a furnace to smelt 1.5 items.

### Note blocks
Composters can be placed under note blocks to produce "bass" sounds.

## Data values
### ID
Java Edition:

| Name      | Identifier  | Form         | Translation key             |
|-----------|-------------|--------------|-----------------------------|
| Composter | `composter` | Block & Item | `block.minecraft.composter` |

Bedrock Edition:

| Name      | Identifier  | Numeric ID | Form                       | Item ID[i 1]   | Translation key       |
|-----------|-------------|------------|----------------------------|----------------|-----------------------|
| Composter | `composter` | `468`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.composter.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
** Composter with different compost levels **
- 
- 
- 
- 
- 
- 
- 
- 
- 

Java Edition:

| Name  | Default value | Allowed values                                                      | Description                                                            |
|-------|---------------|---------------------------------------------------------------------|------------------------------------------------------------------------|
| level | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8` | When at level 8, bone meal is able to be collected from the composter. |

Bedrock Edition:

| Name                 | Metadata Bits                       | Default value | Allowed values                                                      | Values forMetadata Bits                                             | Description                                                            |
|----------------------|-------------------------------------|---------------|---------------------------------------------------------------------|---------------------------------------------------------------------|------------------------------------------------------------------------|
| composter_fill_level | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8` | When at level 8, bone meal is able to be collected from the composter. |



