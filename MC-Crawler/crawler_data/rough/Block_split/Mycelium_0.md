# Mycelium
Mycelium is a particularly rare variant of dirt that is found naturally only in mushroom fields biomes. It has a particle effect that resembles tiny spores being released constantly from the surface.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Mob loot
- 2 Usage
	- 2.1 Spread
	- 2.2 Dirt path
	- 2.3 Effect on plants
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
	- 8.1 Screenshots
- 9 See also
- 10 References
- 11 External links

## Obtaining
### Breaking
Mycelium can be obtained by mining it using a tool with the Silk Touch enchantment. If mined with any other tool or by hand, it drops dirt. A shovel is the fastest tool to collect it.

| Block     | Mycelium              |
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
Mycelium generates in mushroom fields biomes in abundance.


### Mob loot
Endermen can pick up mycelium blocks, and drop the block they are holding if killed.

## Usage
### Spread
A mycelium block can spread to any dirt block within one space above, one sideways, or three down. The mycelium needs light level 9+ above it, while the dirt needs light level 4+ above it, and must not be covered by any light-impeding block or any opaque block. Mycelium reverts to dirt when covered by one of the light-impeding blocks above, and the light level at that block is below 4. The death and spread behaviors are checked when a random tick lands on the block.

If there is a plant on a dirt block when mycelium spreads to it, the plant pops out and drops as an item.

### Dirt path
Mycelium can be turned into a dirt path by using any type of shovel on it.

### Effect on plants
- Mushroomsandfunguscan remain on mycelium blocks in any light level, unlike the situation on other blocks, where mushrooms are broken (dropping as items) during block updates in high light.
- Huge mushroomscan grow on mycelium, just as they can grow ondirt,grass, orpodzol.
- Mycelium cannot be tilled with ahoeto makefarmland.[1]
	- However, it can first be converted to dirt path using a shovel, then tilled with a hoe to create farmland.

## Data values
### ID
Java Edition:

| Name     | Identifier | Form         | Block tags                                                                                                                                                    | Translation key            |
|----------|------------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|
| Mycelium | `mycelium` | Block & Item | `bamboo_plantable_on`<br/>`enderman_holdable`<br/>`mushroom_grow_block`<br/>`moss_replaceable`<br/>`lush_ground_replaceable`<br/>`mineable/shovel`<br/>`dirt` | `block.minecraft.mycelium` |

Bedrock Edition:

| Name     | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key      |
|----------|------------|------------|----------------------------|----------------|----------------------|
| Mycelium | `mycelium` | `110`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.mycelium.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name  | Default value | Allowed values     | Description                                                                                                      |
|-------|---------------|--------------------|------------------------------------------------------------------------------------------------------------------|
| snowy | `false`       | `false`<br/>`true` | If true, the block uses a snowy side and top texture.<br/>In-game, this is true when asnow blockorsnowis on top. |


