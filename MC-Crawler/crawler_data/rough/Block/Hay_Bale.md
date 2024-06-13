# Hay Bale
Hay bales are storage blocks equivalent to nine pieces of wheat. They are used as a crafting ingredient, to feed llamas and all horse variants, reduce fall damage, and extend campfire smoke.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Food
	- 2.3 Animals
		- 2.3.1 Breeding
	- 2.4 Falling
	- 2.5 Campfires
	- 2.6 Composting
	- 2.7 Placement
	- 2.8 Note blocks
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Renders
	- 7.2 Screenshots
- 8 References
- 9 External links

## Obtaining
### Breaking
Hay bales can be mined using any tool, but a hoe speeds up the process.

| Block     | Hay Bale              |
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
Hay bales often generate as pile (and in some houses, animal pens, farms, or meeting points) scattered around in villages located in plains, and less commonly in savanna and desert villages. They also can generate under some campfires in taiga villages and as a part of targets/scarecrows in pillager outposts.


### Crafting
| Ingredients | Crafting recipe |
|-------------|-----------------|
| Wheat       |                 |

## Usage
Hay bales can be used as compact storage of wheat.

### Crafting ingredient
| Name   | Ingredients                 | Crafting recipe |
|--------|-----------------------------|-----------------|
| Target | Redstone Dust+<br/>Hay Bale |                 |
| Wheat  | Hay Bale                    | 9               |

### Food
Although players cannot eat hay bales, hay bales serve as a compact wheat supply for crafting food items during long periods away from other food sources. A full stack of 64 hay bales is equivalent to 192 loaves of bread in a single inventory slot.

### Animals
Hay bales can be fed to donkeys, horses, llamas, or mules to heal up to 10 hearts. They are an effective method to heal horses if the player wants to heal them in a short period of time. They also speed up the growth of foals by three minutes and baby llamas by 90 seconds.

#### Breeding
Hay bales can be used both to lead and breed llamas.

### Falling
Falling onto a hay bale reduces the fall damage by 80%, meaning whatever falls on a hay bale takes 20% of the normal fall damage.

Below are some example damages a player receives falling on a hay bale (assuming no enchantments and/or status effects that reduce fall damage).

| Fall height    | Fall damage |
|----------------|-------------|
| 4-8 blocks     | 1           |
| 9-13 blocks    | 2           |
| 95-100 blocks  | 19× 9.5     |
| 101-103 blocks | 20× 10      |
| 115-120 blocks | 23× 11.5    |

Thus, it is possible to fall onto a hay bale and survive a 100 block drop (starting with full health) or even a 120 block fall (starting with full health plus 2 Absorption hearts).

### Campfires
Placing a hay bale under a campfire makes it a signal fire, increasing the height to which its smoke particles can rise from 10 blocks to 25 blocks.

### Composting
Placing a hay bale into a composter has an 85% chance of raising the compost level by 1. Composting with hay bales is very inefficient, as the hay bale's chance to be composted is only slightly higher than wheat. For example, 900 wheat could be composted to yield 834⁄7 bone meal on average, but if crafted into 100 hay bales, they would only yield 121⁄7 bone meal on average

### Placement
Seen here alongside logs, bone blocks, quartz pillars, and purpur pillars, hay bales can be pointed in multiple directions.
Hay bales can be placed pointing in all three spatial dimensions, in the same way as a log is placed. However, there is no "six-sided" variant like that of the wood block.

### Note blocks
Hay bale can be placed under note blocks to produce banjo sounds.

## Data values
### ID
Java Edition:

| Name     | Identifier  | Form         | Translation key             |
|----------|-------------|--------------|-----------------------------|
| Hay Bale | `hay_block` | Block & Item | `block.minecraft.hay_block` |

Bedrock Edition:

| Name     | Identifier  | Numeric ID | Form                       | Item ID[i 1]   | Translation key       |
|----------|-------------|------------|----------------------------|----------------|-----------------------|
| Hay Bale | `hay_block` | `170`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.hay_block.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name | Default value | Allowed values | Description                            |
|------|---------------|----------------|----------------------------------------|
| axis | `y`           | `x`            | The hay block is oriented east–west.   |
|      |               | `y`            | The hay block is oriented vertically.  |
|      |               | `z`            | The hay block is oriented north–south. |

Bedrock Edition:

| Name        | Metadata Bits   | Default value | Allowed values              | Values forMetadata Bits     | Description                                |
|-------------|-----------------|---------------|-----------------------------|-----------------------------|--------------------------------------------|
| pillar_axis | `0x4`<br/>`0x8` | `y`           | `x`<br/>`y`<br/>`z`         | `1`<br/>`0`<br/>`2`         | The axis along which the block is oriented |
| deprecated  | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`1`<br/>`2`<br/>`3` | Unused, has no effect in game.             |



