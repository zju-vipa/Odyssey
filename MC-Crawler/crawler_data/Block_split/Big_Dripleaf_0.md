# Big Dripleaf
A big dripleaf is a plant that generates within lush caves. Its leaf is a temporary platform; when stood on, it tilts down and drops its burden, resetting a few seconds later.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Post-generation
- 2 Usage
	- 2.1 Placement
	- 2.2 Growth
	- 2.3 Composting
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
	- 8.3 Concept artwork
- 9 References

## Obtaining
### Breaking
Big dripleaves can be obtained with any tool, but an axe is the most efficient. It also breaks when pushed with a piston or sticky piston. Breaking it at any spot on the plant causes the entire plant to collapse. 

Destroying a big dripleaf plant drops one big dripleaf for each stem block and the leaf.

| Block     | Big Dripleaf          |
|-----------|-----------------------|
| Hardness  | 0.1                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 0.15                  |
| Wooden    | 0.1                   |
| Stone     | 0.05                  |
| Iron      | 0.05                  |
| Diamond   | 0.05                  |
| Netherite | 0.05                  |
| Golden    | 0.05                  |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Natural generation
Big dripleaves naturally generate within lush caves biome.


### Post-generation
Bone meal can be used on a small dripleaf plant to turn it into a big dripleaf up to 5 blocks tall, as long as there is enough open space above it. Using bone meal on a big dripleaf plant makes it one block taller, creating an extra stem block (see #Growth).

## Usage
Big dripleaves consist of any number of non-solid stem blocks atop of each other and a single leaf as the uppermost block, which can be stood on by any entity like a normal block for 1 second (20 game ticks). After this time, it tilts down, becoming lower than a block and giving a player warning that it is about to collapse. After a few ticks, it tilts down and becomes temporarily non-solid. When the leaf is powered by redstone, it does not tilt or collapse, however. Powering the stem has no effect.

One-block tall big dripleaves can be used to make the player crawl.‌[Java Edition  only] If a player is standing inside a big dripleaf when it is fully tilted, and the dripleaf returns to the untilted position, the player is left crawling underneath the leaf.

When directly hit with any projectile, the leaf immediately becomes temporarily non-solid. This cannot be prevented by powering it with redstone.

Frogs enjoy jumping on big dripleaves, although the dripleaf tilts down and drops the frog.

### Placement
Big dripleaves can be placed only on top of clay, coarse dirt, dirt, farmland, grass blocks, moss blocks, mycelium, podzol, rooted dirt, and mud. It is always one block tall when placed.

### Growth
Using bone meal on a big dripleaf makes it grow 1 block taller, unless there is a block above the leaf other than air or water. Unlike most plants, dripleaf does not grow by itself: bone meal must be applied for growth to occur.

### Composting
Placing a big dripleaf into a composter has a 65% chance of raising the compost level by 1.

## Data values
### ID
Java Edition:

| Name              | Identifier        | Form         | Block tags              | Translation key                   |
|-------------------|-------------------|--------------|-------------------------|-----------------------------------|
| Big Dripleaf      | big_dripleaf      | Block & Item | lush_plants_replaceable | block.minecraft.big_dripleaf      |
| Big Dripleaf Stem | big_dripleaf_stem | Block        | lush_plants_replaceable | block.minecraft.big_dripleaf_stem |

Bedrock Edition:

| Name         | Identifier   | Numeric ID | Form                       | Item ID[i 1]   | Translation key        |
|--------------|--------------|------------|----------------------------|----------------|------------------------|
| Big Dripleaf | big_dripleaf | 578        | Block & Giveable Item[i 2] | Identical[i 3] | tile.big_dripleaf.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:

Leaf:

| Name        | Default value | Allowed values          | Description                                                                                                               |
|-------------|---------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------|
| facing      | north         | eastnorthsouthwest      | The direction the big dripleaf is facing.The opposite from the direction the player faces while placing the big dripleaf. |
| tilt        | none          | fullnonepartialunstable | How far this big dripleaf is tilted.                                                                                      |
| waterlogged | false         | falsetrue               | Whether there is water in the same place as this big dripleaf.                                                            |

Stem:

| Name        | Default value | Allowed values     | Description                                                         |
|-------------|---------------|--------------------|---------------------------------------------------------------------|
| facing      | north         | eastnorthsouthwest | The direction the big dripleaf stem is facing.                      |
| waterlogged | false         | falsetrue          | Whether there is water in the same place as this big dripleaf stem. |


Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                    | Values forMetadata Bits | Description                                                                                                               |
|------------------------------|---------------|---------------|-----------------------------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------|
| big_dripleaf_head            | Not Supported | 1             | 01                                | Unsupported             | Whether this is the leaf part or the stem part of big dripleaf.                                                           |
| big_dripleaf_tilt            | Not Supported | none          | noneunstablepartial_tiltfull_tilt | Unsupported             | How far this big dripleaf is tilted.                                                                                      |
| minecraft:cardinal_direction | Not Supported | south         | eastnorthsouthwest                | Unsupported             | The direction the big dripleaf is facing.The opposite from the direction the player faces while placing the big dripleaf. |




