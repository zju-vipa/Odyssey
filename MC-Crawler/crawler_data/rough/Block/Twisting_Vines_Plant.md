# Twisting Vines
Twisting vines are climbable upward-growing vegetation blocks found in the Nether in warped forests. 

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
- 7 Trivia
- 8 Gallery
	- 8.1 Renders
	- 8.2 Screenshots
- 9 References

## Obtaining
### Breaking
Twisting vines can be obtained with any tools. They are broken instantly using any tool. They have a 33% chance to drop a single twisting vine when broken, increased to 55% with Fortune I, 77% with Fortune II, and 100% with Fortune III (or higher). They always drop a single twisting vine when broken with shears or with a tool enchanted with Silk Touch.  Any segments left unsupported from below break with a 33% drop chance, regardless of tool used. Accordingly, twisting vines are best harvested from the top.

| Block    | Twisting Vines[note 1] |
|----------|------------------------|
| Hardness | 0                      |
|          | Breakingtime (secs)    |
| Default  | 0.05                   |

1. ↑These blocks have a 1⁄3 chance of dropping themselves.

### Natural generation
Twisting vines generate naturally in the warped forest biome, either on the ground, or on warped huge fungus structures, and can be found only in the Nether.


### Post-generation
Applying bone meal on warped nylium occasionally creates 1-block tall twisting vines on any nylium or netherrack nearby.

Just like weeping vines, twisting vines have a 10% chance of growing one block each random tick. Unlike weeping vines, however, twisting vines grow upward. At default random tick speed, each fungus grows approximately every 13653 game ticks (11.3775 minutes). Twisting vines stop growing once they reach the ceiling or when the block reaches an age block state of 25, whichever is first.

## Usage
Twisting vines can be placed on any block except for transparent blocks (e.g. leaves and fences), and automatically begin to grow. Twisting vines can also be used similarly to a water bucket, as it can prevent fall damage. Applying bone meal to any block of twisting vines causes it to grow immediately. It occasionally spawns if bone meal is used on warped nylium found in warped forest floors.

Twisting vines stop growing if shears are used on the tip.‌‌[Java Edition  only]

### Climbing
Twisting vines can be climbed by standing inside and holding the jump key. If there is a solid block behind the twisting vines, the walk forward key can also be used.

### Composting
Twisting vines also have a 50% chance of raising the compost level by 1 if placed in a composter.

## Data values
### ID
Java Edition:

| Name                 | Identifier             | Form         | Block tags  | Translation key                        |
|----------------------|------------------------|--------------|-------------|----------------------------------------|
| Twisting Vines       | `twisting_vines`       | Block & Item | `climbable` | `block.minecraft.twisting_vines`       |
| Twisting Vines Plant | `twisting_vines_plant` | Block        | `climbable` | `block.minecraft.twisting_vines_plant` |

Bedrock Edition:

| Name           | Identifier       | Numeric ID | Form                       | Item ID[i 1]   | Translation key            |
|----------------|------------------|------------|----------------------------|----------------|----------------------------|
| Twisting Vines | `twisting_vines` | `542`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.twisting_vines.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
Java Edition
Twisting Vines:

| Name | Default value | Allowed values                                                                                                                                                                                                              | Description                                         |
|------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| age  | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15`<br/>`16`<br/>`17`<br/>`18`<br/>`19`<br/>`20`<br/>`21`<br/>`22`<br/>`23`<br/>`24`<br/>`25` | Increments for every block the twisting vine grows. |

Bedrock Edition

| Name               | Metadata Bits                                  | Default value | Allowed values                                                                                                                                                                                                              | Values forMetadata Bits                                                                                                                                                                                                     | Description                                         |
|--------------------|------------------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| twisting_vines_age | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8`<br/>`0x10` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15`<br/>`16`<br/>`17`<br/>`18`<br/>`19`<br/>`20`<br/>`21`<br/>`22`<br/>`23`<br/>`24`<br/>`25` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15`<br/>`16`<br/>`17`<br/>`18`<br/>`19`<br/>`20`<br/>`21`<br/>`22`<br/>`23`<br/>`24`<br/>`25` | Increments for every block the twisting vine grows. |



