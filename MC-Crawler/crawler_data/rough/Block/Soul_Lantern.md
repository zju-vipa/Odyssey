# Soul Lantern
Soul lanterns are blocks that emit light. They are a variant of the lantern crafted from soul torches.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Light
	- 2.2 Piglins
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 See also
- 8 References

## Obtaining
### Breaking
When broken with a pickaxe, a lantern drops itself. When broken without a pickaxe, it drops nothing. A lantern always drops if its supporting block is removed.

| Block     | Soul Lantern          |
|-----------|-----------------------|
| Hardness  | 3.5                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 17.5                  |
| Wooden    | 2.65                  |
| Stone     | 1.35                  |
| Iron      | 0.9                   |
| Diamond   | 0.7                   |
| Netherite | 0.6                   |
| Golden    | 0.45                  |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Soul lanterns can generate in ancient cities.

### Crafting
| Ingredients                 | Crafting recipe |
|-----------------------------|-----------------|
| Iron Nugget+<br/>Soul Torch |                 |

## Usage
Soul lanterns can be placed on the top or bottom surfaces of most solid blocks, although some require sneaking. More information can be found at Opacity/Placement.

When placed below a block the soul lantern appears to hang. They connect to chains seamlessly.

Soul lanterns can be placed (if a support platform is presented) or hanging (if a ceiling block is presented). The type of the block (solid, opaque, transparent, etc... given the block has top/bottom solid surface) does not affect the ability to hang of a soul lantern, similar to torches. Press use on the targeted block or a block adjacent to the air block the soul lantern is going to occupy to place it. If the latter is used and both the support/ceiling block is presented:

- Press use on the upper half of the adjacent block to "hang" the soul lantern up.
- Press use on the lower half of the adjacent block to "place" the soul lantern down.

If the object the soul lantern is placed on receives a block update that does not support the placement of the soul lantern, it is removed and dropped as an item (e.g: soul lantern on a trapdoor and the trapdoor is flipped).

### Light
The soul lantern emits a light level of 10. Due to their lower light level, soul lanterns do not melt snow or ice.

### Piglins
Soul lanterns repel piglins.

## Data values
### ID
Java Edition:

| Name         | Identifier     | Form         | Block tags          | Item tags           | Translation key                |
|--------------|----------------|--------------|---------------------|---------------------|--------------------------------|
| Soul Lantern | `soul_lantern` | Block & Item | `piglin_repellents` | `piglin_repellents` | `block.minecraft.soul_lantern` |

Bedrock Edition:

| Name         | Identifier     | Numeric ID | Form                       | Item ID[i 1]   | Translation key          |
|--------------|----------------|------------|----------------------------|----------------|--------------------------|
| Soul Lantern | `soul_lantern` | `524`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.soul_lantern.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values     | Description                                                     |
|-------------|---------------|--------------------|-----------------------------------------------------------------|
| hanging     | `false`       | `false`<br/>`true` | If the lantern is hanging from a block.                         |
| waterlogged | `false`       | `false`<br/>`true` | Whether or not there's water in the same place as this lantern. |

Bedrock Edition:

| Name    | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                             |
|---------|---------------|---------------|--------------------|-------------------------|-----------------------------------------|
| hanging | `0x1`         | `false`       | `false`<br/>`true` | `0`<br/>`1`             | If the lantern is hanging from a block. |



