# Weeping Vines
Weeping vines are climbable downwards-growing vegetation blocks found in the Nether in crimson forests.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Post-generation
- 2 Usage
	- 2.1 Climbing
	- 2.2 Composting
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Screenshots
- 8 See also

## Obtaining
### Breaking
Weeping vines are broken instantly using any tool. They have a 33% chance to drop a single weeping vine when broken, increased to 55% with Fortune I, 77% with Fortune II, and 100% with Fortune III. They always drop a single weeping vine when broken with shears or a tool enchanted with Silk Touch. Any segments left unsupported from above break with a 33% drop chance, regardless of tool used. Accordingly, weeping vines are best harvested from the bottom.

| Block    | Weeping Vines[note 1] |
|----------|-----------------------|
| Hardness | 0                     |
|          | Breakingtime (secs)   |
| Default  | 0.05                  |

1. ↑These blocks have a 1⁄3 chance of dropping themselves.

### Natural generation
Weeping vines generate naturally inside crevices within the ceilings, or on huge crimson fungi in the crimson forest biome.


### Post-generation
A huge fungus grown by using bone meal on a crimson fungus generates weeping vines growing on it.

Each random tick, weeping vines have a 10% chance of growing one block downward. At default random tick speed, each fungus grows approximately every 13653 game ticks (11.3775 minutes). Weeping vines stop growing once they reach the ground or when the block reaches an age block state of 25, whichever is first.

Bone meal can be used to extend weeping vines and can be used anywhere in the chain to extend the whole chain. This can be useful for getting down from a high place in the nether. 

## Usage
Weeping vines can be placed on, and grow from, the bottom of a block. The top-most vine block always has a starting age value of 0, which increments every time the block grows. If the bottom-most vine block has an age below 25, it continues to grow provided that there is free space below the vine. When the vine does grow, a new vine block with an incremented age value is placed beneath it.

Weeping vines stop growing if shears are used on the tip.‌‌[Java Edition  only]

### Climbing
Weeping vines can be climbed by standing in them and holding the jump key. If there is a solid block behind the weeping vines, the walk forwards key can also be used.

### Composting
Weeping vines can also be used on a composter, with a 50% chance to raise the compost level by 1.

## Data values
### ID
Java Edition:

| Name                | Identifier            | Form         | Block tags  | Translation key                       |
|---------------------|-----------------------|--------------|-------------|---------------------------------------|
| Weeping Vines       | `weeping_vines`       | Block & Item | `climbable` | `block.minecraft.weeping_vines`       |
| Weeping Vines Plant | `weeping_vines_plant` | Block        | `climbable` | `block.minecraft.weeping_vines_plant` |

Bedrock Edition:

| Name          | Identifier      | Numeric ID | Form                       | Item ID[i 1]   | Translation key           |
|---------------|-----------------|------------|----------------------------|----------------|---------------------------|
| Weeping Vines | `weeping_vines` | `486`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.weeping_vines.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
Java Edition
Weeping Vines:

| Name | Default value | Allowed values                                                                                                                                                                                                              | Description                                        |
|------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| age  | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15`<br/>`16`<br/>`17`<br/>`18`<br/>`19`<br/>`20`<br/>`21`<br/>`22`<br/>`23`<br/>`24`<br/>`25` | Increments for every block the weeping vine grows. |

Bedrock Edition

| Name              | Metadata Bits                                  | Default value | Allowed values                                                                                                                                                                                                              | Values forMetadata Bits                                                                                                                                                                                                     | Description                                        |
|-------------------|------------------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| weeping_vines_age | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8`<br/>`0x10` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15`<br/>`16`<br/>`17`<br/>`18`<br/>`19`<br/>`20`<br/>`21`<br/>`22`<br/>`23`<br/>`24`<br/>`25` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15`<br/>`16`<br/>`17`<br/>`18`<br/>`19`<br/>`20`<br/>`21`<br/>`22`<br/>`23`<br/>`24`<br/>`25` | Increments for every block the weeping vine grows. |



