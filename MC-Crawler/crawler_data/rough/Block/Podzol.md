# Podzol
Podzol is a dirt-type block that naturally blankets the surface of the old growth taiga and bamboo jungles, along with their respective variants. Grass blocks and mycelium cannot spread to this block.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Mob loot
	- 1.4 Trading
	- 1.5 Post-generation
- 2 Usage
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
	- 5.1 Data history
- 6 Issues
- 7 Trivia
- 8 Gallery
	- 8.1 Screenshots
- 9 See also
- 10 References
- 11 External links

## Obtaining
### Breaking
Podzol can be broken using any tool or by hand, but the shovel is the quickest. It can be obtained using a tool with Silk Touch, otherwise it drops dirt instead. 

| Block     | Podzol                |
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
Podzol generates only in old growth taiga, bamboo jungle biomes and in trial chambers surrounding the bogged and the cave spider trial spawners.‌[upcoming: JE 1.21 & BE 1.21.0]


### Mob loot
The pattern in which large spruce trees replace blocks with podzol as it grows.
Endermen can pick up podzol blocks, and drop it if holding it when killed.

### Trading
Wandering traders have 1⁄6 chance to sell 3 podzol for 3 emeralds.

The maximum reach of podzol that can spawn from a mega spruce tree.
### Post-generation
See also: Dirt § Renewable acquisition

Podzol replaces grass blocks, dirt, mycelium, coarse dirt, rooted dirt, moss block, muddy mangrove roots, and mud‌[Java Edition  only][1] around a large spruce tree when it is grown from 4 saplings arranged in a square. The pattern of the podzol reaches at most 6 blocks in the eastern and southern (positive X and Z) directions, and 5 blocks in the western and northern directions.

In Java Edition, since podzol can be converted from moss blocks, and moss can be grown on renewable stone, dirt can be renewably created as long as there is access to water, lava, moss, spruce saplings and bone meal. This is especially useful on maps where dirt is limited.

## Usage
Like mycelium, podzol allows mushrooms to be placed on it no matter the light level, which allows the growth of huge mushrooms. Saplings, all kinds of flowers, and sugar cane can be placed on it normally. A podzol block can be turned into a dirt path by pressing use on it with any type of shovel, but it cannot be tilled with a hoe to make farmland.[2] However, the player can first use the shovel on the podzol to turn it into dirt path, then use the hoe on the dirt path to turn it into farmland.

Unlike other similar blocks, podzol never spreads to dirt blocks, and it does not become dirt if a solid block is placed on top of it, no matter how long the block remains on top of it. Additionally, neither grass nor mycelium can spread to podzol.

## Data values
### ID
Java Edition:

| Name   | Identifier | Form         | Block tags                                                                                                                                                                                                    | Translation key          |
|--------|------------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|
| Podzol | `podzol`   | Block & Item | `bamboo_plantable_on`<br/>`enderman_holdable`<br/>`mushroom_grow_block`<br/>`valid_spawn`<br/>`moss_replaceable`<br/>`lush_ground_replaceable`<br/>`mineable/shovel`<br/>`dirt`<br/>`#sniffer_diggable_block` | `block.minecraft.podzol` |

Bedrock Edition:

| Name   | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key    |
|--------|------------|------------|----------------------------|----------------|--------------------|
| Podzol | `podzol`   | `243`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.podzol.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states


Java Edition:

| Name  | Default value | Allowed values     | Description                                                                                                      |
|-------|---------------|--------------------|------------------------------------------------------------------------------------------------------------------|
| snowy | `false`       | `false`<br/>`true` | If true, the block uses a snowy side and top texture.<br/>In-game, this is true when asnow blockorsnowis on top. |

