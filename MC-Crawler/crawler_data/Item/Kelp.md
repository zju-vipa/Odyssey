# Kelp
Kelp is an underwater algae that generates in most oceans.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Trading
- 2 Usage
	- 2.1 Cooking ingredient
	- 2.2 Composting
	- 2.3 Growth mechanics
	- 2.4 Farming
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
- 9 References
- 10 External links

## Obtaining
### Breaking
Kelp can be mined instantly with any tool or with the player's fist. Removing water from the kelp block destroys the kelp. Breaking one part of a kelp stalk destroys all kelp blocks above it. Each block drops a kelp item.

| Block    | Kelp                |
|----------|---------------------|
| Hardness | 0                   |
|          | Breakingtime (secs) |
| Default  | 0.05                |

### Natural generation
Kelp naturally generates in any ocean biomes (except in frozen, deep frozen and warm), near and around seagrass. Each chunk has 1⁄18 chance to generate a vegetation of kelp.


### Trading
Kelp can be bought from wandering traders for 3 emeralds.

## Usage
Kelp can be placed underwater by hand, or anywhere by the use of commands such as /setblock. Placing it by hand gives it a random age value between 0 and 24. Kelp can be placed only in water source blocks or downward-flowing water, not horizontally flowing water.

When placed in downward-flowing water, the kelp becomes waterlogged, transforming the flowing water into a water source block,[1] which is useful for faster bubble column elevator creation.

Any building block can be placed on top of a kelp plant, which is useful for building structures over a deep ocean without needing to build from the ocean floor (see also lily pad).

### Cooking ingredient
| Name       | Ingredients  | Smelting recipe |
|------------|--------------|-----------------|
| Dried Kelp | Kelp+Anyfuel | 0.1             |

### Composting
Placing kelp into a composter has a 30% chance of raising the compost level by 1.

### Growth mechanics
Kelp can be planted on a broad variety of blocks. It grows underwater if it has either a source block of water or, in Java Edition, flowing water above it.[2] Neither players nor dispensers can remove the water source block that kelp grows in without breaking the kelp first.

Kelp does not require any light level to grow. Kelp also grows without having sky access. Bone meal can be used to grow kelp by 1 block on each use.

When kelp is planted, it is generated with a randomly chosen age value, which can be checked when pressing F3‌[Java Edition  only]. The age value of a newly planted kelp plant varies randomly from 0 to 24. Each time the kelp grows in height by one block, the newly generated top of the kelp plant increases its age by 1. When the top block of the kelp plant reaches an age of 25, it stops growing. This means that kelp can naturally grow to a height between 2 (if the first kelp plant had an age of 24) and 26 blocks (if the first kelp plant had an age of 0). 

When a kelp plant block is broken, the age of the kelp plant block underneath is randomized to a value from 0 to 24 and the kelp continues growing until it reaches age 25. It is possible to use this mechanic to cultivate a kelp plant to increase its growth height beyond its natural maximum height of 26 blocks. This can be done by breaking the top-most block of the kelp plant each time it reaches age 25. A kelp plant cultivated by a player in this way repeatedly grows until it reaches the water surface.

Each time it receives a random tick, kelp has a 14% chance of growing. At default random tick speed (3), each plant grows on average every 9752 game ticks (487.6 seconds).

If shears are used on the topmost block of kelp, that block automatically sets its age value to 25 and stops growing.‌[Java Edition  only]

### Farming
Main article: Tutorials/Kelp farming
Kelp farming is similar to farming sugar cane, although kelp must be placed underwater. Automation of harvest is easier because items float up in water.

## Data values
### ID
Java Edition:

| Name       | Identifier | Form         | Translation key            |
|------------|------------|--------------|----------------------------|
| Kelp       | kelp       | Block & Item | block.minecraft.kelp       |
| Kelp Plant | kelp_plant | Block        | block.minecraft.kelp_plant |

Bedrock Edition:

| Kelp  | Identifier | Numeric ID | Form                         | Item ID[i 1] | Translation key |
|-------|------------|------------|------------------------------|--------------|-----------------|
| Item  | kelp       | 382        | Item                         | —            | item.kelp.name  |
| Block | kelp       | 393        | Block & Ungiveable Item[i 2] | item.kelp    | —               |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Unavailable with /give command


### Block states
See also: Block states

Java Edition:
Top kelp block:

| Name | Default value | Allowed values                             | Description                                                                                                                                                                                       |
|------|---------------|--------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| age  | 0             | 012345678910111213141516171819202122232425 | A freshly planted kelp starts with a random age between 0 and 24.Below age 25, a kelp may try go grow more kelp above it with the same age value incremented by one.Kelp stops growing at age 25. |

Bedrock Edition:

| Name     | Metadata Bits | Default value | Allowed values         | Values forMetadata Bits | Description                                                                                |
|----------|---------------|---------------|------------------------|-------------------------|--------------------------------------------------------------------------------------------|
| kelp_age | 0x10x20x40x8  | 0             | 0123456789101112131415 | 0123456789101112131415  | The age of the kelp. The kelp renders as a non-top piece if there's another kelp above it. |
|          |               |               | 16171819202122232425   | Unsupported             | Unused                                                                                     |



