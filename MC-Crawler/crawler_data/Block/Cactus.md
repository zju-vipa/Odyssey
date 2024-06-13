# Cactus
A cactus is a plant block that generates in deserts and badlands and causes damage.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Mob loot
	- 1.4 Chest loot
	- 1.5 Trading
- 2 Usage
	- 2.1 Farming
	- 2.2 Smelting ingredient
	- 2.3 Breeding
	- 2.4 Composting
- 3 Sounds
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
A cactus can be mined by hand without taking damage. The tool used to mine the cactus does not affect mining speed.[1]

| Block    | Cactus              |
|----------|---------------------|
| Hardness | 0.4                 |
|          | Breakingtime (secs) |
| Default  | 0.6                 |

When the spot a cactus is placed in becomes unsuitable, such as when a solid block is placed next to it or its supporting block is removed, the cactus block uproots and drops as an item. 

A cactus also removes and drops itself as an item if a piston tries to push it, or moves a block into its space. Trying to pull it with a sticky piston does nothing. 

Using a sign on the side of a cactus causes both the sign and the cactus to drop as items.

### Natural generation
Cacti naturally occur in desert and badlands biomes (twice more common in desert than in badlands). They generate as one (11⁄18 chance), two (5⁄18 chance), or three (2⁄18 chance) blocks tall. Rarely taller cacti can be found if generation chooses to generate another on top of one already generated (although not as commonly as sugar cane).

A potted cactus can also be found in an igloo with a basement.
Potted cacti and 3 block cactus can also be found in some desert village buildings.


### Mob loot
Endermen can pick up cacti. When they die, they drop the cacti they're holding.

### Chest loot
| Item   | Structure   | Container          | Quantity | Chance          |
|--------|-------------|--------------------|----------|-----------------|
|        |             |                    |          | Java Edition    |
| Cactus | Village     | Desert house chest | 1–4      | 80.6%           |
|        |             |                    |          | Bedrock Edition |
| Cactus | Bonus Chest | Chest              | 1–2      | 60%             |
|        | Village     | Desert house chest | 1–4      | 80.6%           |

### Trading
Wandering traders can sell a cactus for three emeralds.

## Usage
A cactus block may be placed only on sand, red sand, suspicious sand, or another cactus block. A cactus breaks itself (and drops as an item) if any block with a solid material, or lava, occupies any of the 4 horizontally adjacent blocks. It also breaks if on the sand and the block above is water or lava.

When any entity, including players and mobs, touches a cactus, 1 damage is taken every 0.5 seconds. Damage from touching a cactus is reduced by armor, but touching it also damages the armor. Mobs do not avoid cacti when they pathfind.

A cactus destroys any item that come into contact with it, including other cactus in item form. Falling blocks such as sand and gravel are not destroyed when falling onto cactus; instead, they are transformed into item form (as happens when it falls into any block with a hitbox that has a height less than 1, such as slabs). The item created in this case is sometimes (though not always) destroyed by the cactus. The conversion to an item applies even when the falling block is a cactus (which is possible with /summon).

When a minecart hits a cactus block, the minecart drops as an item and is often destroyed, although a hopper can pick it up faster.

A cactus can also be placed in a flower pot, where it is rendered harmless.

A cactus (excluding its spikes) is 7⁄8 of a block in width (the same as chests) and a full block in height, however the collision box is 15⁄16 of a block high.

### Farming
Main article: Tutorials/Cactus farming
Cacti naturally grow to a height of three blocks, adding a block of height when the top cactus block has received 16 random ticks (i.e. on average every 18 minutes, but the actual rate can vary widely). Bone meal does not work on cacti to speed their growth.[2] A cactus does not need light to grow and is non-flammable. If a cactus has space directly above it, it grows even if the newly-grown block would immediately break due to adjacent blocks.

### Smelting ingredient
| Name      | Ingredients    | Smelting recipe | Description              |
|-----------|----------------|-----------------|--------------------------|
| Green Dye | Cactus+Anyfuel | 1               | ‌[Java Edition  only][3] |
| Green Dye | Cactus+Anyfuel | 0.2             | ‌[Bedrock Edition  only] |

### Breeding
Cacti can be used to breed camels and reduce the remaining growth duration of baby camels by 10%. Camels also follow a player holding a cactus.

### Composting
Placing a cactus into a composter has a 50% chance of raising the compost level by 1.

## Data values
### ID
Java Edition:

| Name   | Identifier | Form         | Block tags        | Translation key        |
|--------|------------|--------------|-------------------|------------------------|
| Cactus | cactus     | Block & Item | enderman_holdable | block.minecraft.cactus |

Bedrock Edition:

| Name   | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key  |
|--------|------------|------------|----------------------------|----------------|------------------|
| Cactus | cactus     | 81         | Block & Giveable Item[i 2] | Identical[i 3] | tile.cactus.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition

| Name | Default value | Allowed values         | Description                                                                                                                                                                                              |
|------|---------------|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| age  | 0             | 0123456789101112131415 | A freshly-planted cactus – and a cactus that has just grown cactus above it – each have an age of 0.The age is incremented at random intervals.At age 15, a cactus may try to grow more cactus above it. |

Bedrock Edition

| Name | Metadata Bits | Default value | Allowed values         | Values forMetadata Bits | Description                                                                                                                                                                                              |
|------|---------------|---------------|------------------------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| age  | 0x10x20x40x8  | 0             | 0123456789101112131415 | 0123456789101112131415  | A freshly-planted cactus – and a cactus that has just grown cactus above it – each have an age of 0.The age is incremented at random intervals.At age 15, a cactus may try to grow more cactus above it. |



