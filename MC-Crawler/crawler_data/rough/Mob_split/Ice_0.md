# Ice
Ice is a translucent solid block. It can slide entities using all methods of transportation (excluding minecarts).

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Post-generation
		- 1.3.1 Snowy biomes
		- 1.3.2 Ice bomb
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Speed
		- 2.2.1 Boat highway
	- 2.3 Creating water
- 3 Sounds
- 4 Data values
	- 4.1 ID
- 5 History
- 6 Issues
- 7 Trivia
- 8 Gallery
	- 8.1 Screenshots
- 9 See also
- 10 References
- 11 External links

## Obtaining
### Breaking
Ice can be easily destroyed without tools, but the use of a pickaxe speeds up the process. It can be broken instantly with Efficiency III on a diamond pickaxe. However, the block drops only when using a tool enchanted with Silk Touch. If mined without Silk Touch, the block drops nothing, and instead is replaced with water if there is a block under the ice block.

| Block     | Ice                   |
|-----------|-----------------------|
| Hardness  | 0.5                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 0.75                  |
| Wooden    | 0.4                   |
| Stone     | 0.2                   |
| Iron      | 0.15                  |
| Diamond   | 0.1                   |
| Netherite | 0.1                   |
| Golden    | 0.1                   |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Ice can be found naturally as part of the landscape in snowy biomes from rivers, and oceans. It can also be found in igloos‌[Java Edition  only], ice spikes, icebergs, snowy slopes, also on landscape of frozen peaks biomes. They also generate in ancient cities.


### Post-generation
#### Snowy biomes
See also: Ice farming

Water source blocks in a snowy biome eventually freeze into ice if exposed to the sky from directly above, the block light level inside the water block is less than 10, and there is at least one horizontally adjacent non-water (and non-waterlogged) block. This can happen at any time of day, and in any weather condition.

Water also freezes into ice in cold biomes, as long as the altitude is high enough for snowfall.

Ice formation occurs as part of chunk ticking, so it requires that a player is nearby similar to crop growth or grass spreading. The speed of ice formation is affected by the game rule randomTickSpeed.

#### Ice bomb

  

This feature is exclusive to  Bedrock Edition and  Minecraft Education. 


When an ice bomb is thrown into water, it transforms the water in a 3×3×3 cube centered around the projectile into ice. This works for source water or flowing water upon hit.

## Usage
### Crafting ingredient
| Name       | Ingredients | Crafting recipe |
|------------|-------------|-----------------|
| Packed Ice | Ice         |                 |

Despite being created by a 3×3 recipe, packed ice is not a storage block, because it cannot be crafted back into ice. The same applies to the next tier of compression, blue ice.

### Speed
Ice is slightly slippery, causing entities (excluding minecarts[1]) to slide, including items. This allows for increased speed of items in water currents, by placing ice blocks under the water current. Items already travel at high speeds in water currents because they float, so ice block water streams are less necessary for item transportation.

A player who sprints and jumps repeatedly on ice travels faster than on any other block type. The player can travel even faster if they sprint and spam jump in a 2-block-high corridor with ice on the floor, allowing the player to accelerate to extremely high speeds, although this will cost them a lot of hunger.

In Java Edition, when a non-full block is placed on top of ice, the block has the same "slipperiness" as the ice below it.[2]

#### Boat highway
Like other entities, boats travel extremely quickly on ice/blue ice, where it can reach a speed of 40-72 m/s, much faster than the 8 m/s speed on water.[3] More beneficially, unlike water, ice can be placed in the Nether, allowing players to construct boat highways made of ice/blue ice in the dimension, to make use of the 1:8 distance travel ratio, and travel at an equivalent speed up to 320-580 m/s (720-1300 mph) between locations in the Overworld.

### Creating water
Ice can be used to create water either by its melting or being broken. If there is a non-air block directly underneath the ice block, the ice becomes a water source block when broken. 

Ice also melts into water if the block light level immediately next to it on any side is higher than 11. Sky light level is ignored, therefore ice does not melt from sunlight. In  Minecraft Education and Bedrock Edition, ice also melts when near a heat block, though heat blocks do not produce light. 

Compared to water buckets, ice has the benefit of being able to stack in the inventory. Therefore, carrying ice instead of water buckets can be much more convenient, if the player wants to create a lot of water sources.

If ice melts or is broken in the Nether, no water is produced (it sublimates).

## Data values
### ID
Java Edition:

| Name | Identifier | Form         | Block tags                                              | Translation key       |
|------|------------|--------------|---------------------------------------------------------|-----------------------|
| Ice  | `ice`      | Block & Item | `ice`<br/>`mineable/pickaxe`<br/>`geode_invalid_blocks` | `block.minecraft.ice` |

Bedrock Edition:

| Name | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key |
|------|------------|------------|----------------------------|----------------|-----------------|
| Ice  | `ice`      | `79`       | Block & Giveable Item[i 2] | Identical[i 3] | `tile.ice.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.


