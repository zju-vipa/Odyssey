# Dark Prismarine
Dark prismarine is a dark cyan block, with a tight grid pattern; variant of prismarine.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Conduit power
	- 2.2 Crafting ingredient
	- 2.3 Stonecutting
	- 2.4 Note blocks
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 Achievements
- 6 Video
- 7 History
- 8 Issues
- 9 References

## Obtaining
### Breaking
Dark prismarine only drops itself when mined with a pickaxe. If mined by any other tool, it drops nothing.

| Block     | Dark Prismarine       |
|-----------|-----------------------|
| Hardness  | 1.5                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 7.5                   |
| Wooden    | 1.15                  |
| Stone     | 0.6                   |
| Iron      | 0.4                   |
| Diamond   | 0.3                   |
| Netherite | 0.25                  |
| Golden    | 0.2                   |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Dark prismarine naturally generate as the main blocks making up ocean monuments. Dark prismarine encases the 8 gold blocks of the dungeon, and appears in fewer decorative features, compared to the other variants of prismarine. 

### Crafting
| Name            | Ingredients                     | Crafting recipe | Description                                      |
|-----------------|---------------------------------|-----------------|--------------------------------------------------|
| Dark Prismarine | Prismarine Shard+<br/>Black Dye |                 |                                                  |
| Dark Prismarine | Prismarine Shard+<br/>Ink Sac   |                 | ‌[Bedrock Edition and Minecraft Education  only] |

## Usage
### Conduit power
Main article: Conduit
Dark prismarine can be used to activate a conduit by building a structure around it. By doing this, the conduit emits the Conduit Power effect in a certain radius, depending on how many blocks are used to power it. Other two variants of prismarine and sea lanterns can also be used for this purpose.

### Crafting ingredient
| Name                   | Ingredients     | Crafting recipe |
|------------------------|-----------------|-----------------|
| Dark Prismarine Slab   | Dark Prismarine | 6               |
| Dark Prismarine Stairs | Dark Prismarine | 4               |

### Stonecutting
| Name                   | Ingredients     | Cutting recipe |
|------------------------|-----------------|----------------|
| Dark Prismarine Slab   | Dark Prismarine | 2              |
| Dark Prismarine Stairs | Dark Prismarine |                |

### Note blocks
Dark prismarine can be placed under note blocks to produce "bass drum" sound.

## Data values
### ID
Java Edition:

| Name            | Identifier        | Form         | Translation key                   |
|-----------------|-------------------|--------------|-----------------------------------|
| Dark Prismarine | `dark_prismarine` | Block & Item | `block.minecraft.dark_prismarine` |

Bedrock Edition:

| Name            | Identifier   | Numeric ID | Form                       | Item ID[i 1]   | Translation key             |
|-----------------|--------------|------------|----------------------------|----------------|-----------------------------|
| Dark Prismarine | `prismarine` | `168`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.prismarine.dark.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Bedrock Edition:

| Name                  | Metadata Bits   | Default value | Allowed values | Values forMetadata Bits | Description       |
|-----------------------|-----------------|---------------|----------------|-------------------------|-------------------|
| prismarine_block_type | `0x1`<br/>`0x2` | `default`     | `bricks`       | `2`                     | Prismarine Bricks |
|                       |                 |               | `dark`         | `1`                     | Dark Prismarine   |
|                       |                 |               | `default`      | `0`                     | Prismarine        |



