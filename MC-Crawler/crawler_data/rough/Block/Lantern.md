# Lantern
Lanterns are blocks that emit light.

There is a green variant of the lantern that appeared in Minecraft Live 2023. Its function is unknown.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
	- 1.4 Trading
- 2 Usage
	- 2.1 Light
- 3 Sounds
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

## Obtaining
### Breaking
When broken with a pickaxe, a lantern drops itself. When broken without a pickaxe, it drops nothing. A lantern always drops if its supporting block is removed.

| Block     | Lantern               |
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
Lanterns can generate as lamps or lamp posts above farms and on some buildings in snowy tundra villages and in bastion remnants.

### Crafting
| Ingredients            | Crafting recipe |
|------------------------|-----------------|
| Iron Nugget+<br/>Torch |                 |

### Trading
Apprentice-level librarian villagers have a 50%‌[Bedrock Edition  only] or 66.7%‌[Java Edition  only] chance of selling a lantern for an emerald as part of their trades.

## Usage
Lanterns can be placed on the top or bottom surfaces of most solid blocks, although some require sneaking. More information can be found at Opacity/Placement.

When placed below a block the lantern appears to hang. They connect to chains seamlessly.

Lanterns can be placed (if a support platform is presented) or hanging (if a ceiling block is presented). The type of the block (solid, opaque, transparent, etc... given the block has top/bottom solid surface) does not affect the ability to hang of a lantern, similar to torches. Press use on the targeted block or a block adjacent to the air block the lantern is going to occupy to place it. If the latter is used and both the support/ceiling block is presented:

- Press use on the upper half of the adjacent block to "hang" the lantern up.
- Press use on the lower half of the adjacent block to "place" the lantern down.

If the object the lantern is placed on receives a block update that does not support the placement of the lantern, it is removed and dropped as an item (e.g: lantern is on a trapdoor and the trapdoor is flipped).

### Light
The lantern is among the most luminous of light sources, emitting a light level of 15. Lanterns also melt snow layers within 2 blocks and ice within 3 blocks (taxicab distance).

## Data values
### ID
Java Edition:

| Name    | Identifier | Form         | Block tags | Item tags | Translation key           |
|---------|------------|--------------|------------|-----------|---------------------------|
| Lantern | `lantern`  | Block & Item | None       | None      | `block.minecraft.lantern` |

Bedrock Edition:

| Name    | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key     |
|---------|------------|------------|----------------------------|----------------|---------------------|
| Lantern | `lantern`  | `463`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.lantern.name` |

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



