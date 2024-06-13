# Sweet Berries
Sweet berries are a food item obtained from sweet berry bushes and are used to plant them.

## Contents
- 1 Obtaining
	- 1.1 Natural generation
	- 1.2 Breaking
	- 1.3 Harvesting
	- 1.4 Chest loot
- 2 Usage
	- 2.1 Placement
	- 2.2 Growth
	- 2.3 Food
	- 2.4 Composting
	- 2.5 Breeding
	- 2.6 Trading
	- 2.7 Entity movement
	- 2.8 Bees
- 3 Sounds
	- 3.1 Generic
		- 3.1.1 Block
		- 3.1.2 Item
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 Advancements
- 6 History
	- 6.1 Sweet berry bush "item"
		- 6.1.1 Appearances
		- 6.1.2 Names
- 7 Issues
- 8 Trivia
- 9 Gallery
	- 9.1 Screenshots
- 10 References
- 11 External links

## Obtaining
### Natural generation
Berry bushes commonly generate in taiga and snowy taiga biomes. Each chunk has a 1⁄12 chance to generate sweet berry bushes in random patches. In Java Edition, they also generate in both old growth pine taiga and old growth spruce taiga biomes.


### Breaking
See also: Fortune § Discrete random

Sweet berry bushes can be mined instantly with any tool or by hand. A mature sweet berry bush yields 2–3 sweet berries. On its third growth stage, it yields 1–2 sweet berries. Each level of Fortune can increase the amount of drops by 1.

### Harvesting
Sweet berries can be collected from a sweet berry bush by pressing the use control on it, yielding 1–2 sweet berries in its third growth stage, and 2–3 sweet berries in its final growth stage. After dropping the berries on the ground, the sweet berry bush reverts to its first growth stage. 

### Chest loot
| Item          | Structure | Container         | Quantity | Chance       |
|---------------|-----------|-------------------|----------|--------------|
|               |           |                   |          | Java Edition |
| Sweet Berries | Village   | Taiga house chest | 1–7      | 40.6%        |

## Usage
### Placement
Placing sweet berries on a grass block, dirt, coarse dirt, rooted dirt, farmland, podzol, mycelium, moss block, mud, or muddy mangrove roots creates a small sweet berry bush that eventually becomes a fully grown sweet berry bush.

### Growth
A sweet berry bush grows through four stages after it is planted. Its first growth stage is a small bush without any berries. It becomes a grown plant in its second stage, and produces berries in its third and fourth growth stage. The bush needs to be in light level 9 or greater to grow. Using bone meal on it increases its growth stage by one, and at full maturity, ejects the sweet berry item. The bush can be placed on a 1 block high space, but it cannot grow with a full, non-transparent block immediately above it.

### Food
To eat sweet berries, press and hold use while it is selected in the hotbar. Eating one restores 2 () hunger and 0.4‌[JE  only] / 1.2‌[BE  only] hunger saturation.

### Composting
Placing sweet berries into a composter has a 30% chance of raising the compost level by 1.

### Breeding
Sweet berries can be fed to foxes to breed them. Foxes are similar to cats when being fed as a wild animal; a sudden movement by the player may cause the fox to flee even if the player holds sweet berries. A baby fox bred by a player trusts the player and does not flee.

### Trading
Master-level butcher villagers offer to buy 10 sweet berries for an emerald.

### Entity movement
A sweet berry bush (at any stage) slows down all entities (except items) passing through it. At stage 1 and higher, it causes damage. Foxes are immune to both characteristics, however. Sweet berry bushes deal 1 damage every 0.5 seconds, only if the entity is moving in the hitbox of the bush. Entities that move through sweet berry bushes slow down to about 34.05% of their normal speed, similar to how a cobweb slows down mobs to 15% of normal speed. This makes it impossible to jump a full block while inside the bush.

Mobs at standard block height in a minecart are not damaged when the minecart is pushed through sweet berries. Players in a sweet berry bush take no damage except from horizontal movement, but are unable to jump out of the bush, similar to a cobweb.

### Bees
Bees do not pollinate sweet berry bushes.

## Data values
### ID
Java Edition:

| Name             | Identifier       | Form  | Block tags                          | Item tags | Translation key                  |
|------------------|------------------|-------|-------------------------------------|-----------|----------------------------------|
| Sweet Berry Bush | sweet_berry_bush | Block | azalea_log_replaceablebee_growables | —         | block.minecraft.sweet_berry_bush |
| Sweet Berries    | sweet_berries    | Item  | —                                   | fox_food  | item.minecraft.sweet_berries     |

Bedrock Edition:

| Name             | Identifier       | Numeric ID | Form                         | Item ID[i 1]   | Translation key            |
|------------------|------------------|------------|------------------------------|----------------|----------------------------|
| Sweet Berry Bush | sweet_berry_bush | 462        | Block & Ungiveable Item[i 2] | Identical[i 3] | tile.sweet_berry_bush.name |
| Sweet Berries    | sweet_berries    | 287        | Item                         | —              | item.sweet_berries.name    |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Unavailable with /give command

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:

| Name | Default value | Allowed values | Description                                                                  |
|------|---------------|----------------|------------------------------------------------------------------------------|
| age  | 0             | 0              | Young plant                                                                  |
|      |               | 1              | No berries                                                                   |
|      |               | 2              | Some berries,usingthe bush gives 1–2sweet berriesand sets the age back to 1. |
|      |               | 3              | Full berries,usingthe bush gives 2–3sweet berriesand sets the age back to 1. |

Bedrock Edition:

| Name   | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                                                     |
|--------|---------------|---------------|----------------|-------------------------|---------------------------------------------------------------------------------|
| growth | 0x1           | 0             | 0              | 0                       | Young plant                                                                     |
|        |               |               | 1              | 1                       | No berries                                                                      |
|        |               |               | 2              | 2                       | Some berries,usingthe bush gives 1–2sweet berriesand sets the growth back to 2. |
|        |               |               | 3              | 3                       | Full berries,usingthe bush gives 2–3sweet berriesand sets the growth back to 2. |



