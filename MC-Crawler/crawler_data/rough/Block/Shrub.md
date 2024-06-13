# Shrub
The shrub is an unused dead bush-looking variant of short grass that does not generate naturally. It currently only exists in Legacy Console Edition, where it can be obtained from the Creative inventory. The shrub used to exist in Java Edition, but it was removed in 17w47a.

In Bedrock Edition, it is named fern instead and takes the appearance of short grass. It can be obtained or placed only via commands.‌[until BE 1.21.0]

## Contents
- 1 Obtaining
	- 1.1 Breaking
- 2 Appearance
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block data
	- 4.3 Block states
- 5 History
	- 5.1 Data history
- 6 Issues
- 7 Trivia
- 8 Gallery
	- 8.1 Renders
		- 8.1.1 Java Edition
		- 8.1.2 Bedrock Edition
	- 8.2 Screenshots

## Obtaining
### Breaking
When broken normally, shrubs have a 1⁄8 chance of dropping wheat seeds, due to being a type of grass. This drop rate is affected by Fortune like normal grass as well. Shrubs can be obtained as an item using shears.

## Appearance

  

This section is missing information about biome-dependent colors. 
Please expand the section to include this information. Further details may exist on the talk page.


Shrubs placed in an intersection between a taiga, a dark forest and a desert in Legacy Console Edition.
In Java Edition, the shrub uses the texture of dead bushes. The only visual difference between the shrub and the dead bush is that the shrub appears randomly off-centered and sunk into the ground, like short grass and ferns.

In Legacy Console Edition, shrubs appear similar to Java Edition, but they change color based on the biome they are placed in, similar to the green shrub.

In Bedrock Edition, the "fern" uses the texture of short grass.

## Data values
### ID
Java Edition (until 17w47a):

| Name  | Identifier  | Numeric ID | Translation key             |
|-------|-------------|------------|-----------------------------|
| Shrub | `tallgrass` | `31`       | `tile.tallgrass.shrub.name` |

Bedrock Edition (until preview 1.21.0.20):

| Name | Identifier  | Numeric ID | Translation key            |
|------|-------------|------------|----------------------------|
| Fern | `tallgrass` | `31`       | `tile.tallgrass.fern.name` |

### Block data
See also: Data values

|  | DV | Description                                                                                |
|--|----|--------------------------------------------------------------------------------------------|
|  | 0  | Shrub(identical in appearance to block dead bush when placed, but acts like grass or fern) |
|  | 1  | Grass                                                                                      |
|  | 2  | Fern                                                                                       |
|  | 3  | Grass(identical to the shrub, but colors are affected by biome)                            |



### Block states
See also: Block states

Java Edition:
| Name | Default value | Allowed values | Description |
|------|---------------|----------------|-------------|
| type | `?`           | `dead_bush`    | Shrub       |
|      |               | `fern`         | Fern        |
|      |               | `tall_grass`   | Tall Grass  |

Bedrock Edition:
| Name            | Metadata Bits   | Default value | Allowed values | Values forMetadata Bits | Description                                         |
|-----------------|-----------------|---------------|----------------|-------------------------|-----------------------------------------------------|
| tall_grass_type | `0x1`<br/>`0x2` | `default`     | `default`      | `0`                     | Fern(Unused variant which looks identical to grass) |
|                 |                 |               | `tall`         | `1`                     | Grass                                               |
|                 |                 |               | `fern`         | `2`                     | Fern                                                |
|                 |                 |               | `snow`         | `3`                     | Fern (Unused variant which looks identical to fern) |



