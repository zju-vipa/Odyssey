# Sheep
Sheep are common passive mobs that supply wool and raw mutton and are found in many of the grassy biomes.

## Contents
- 1 Spawning
	- 1.1 Natural generation
- 2 Drops
	- 2.1 Breeding
	- 2.2 On death
	- 2.3 Shearing
- 3 Behavior
- 4 Dyeing
- 5 Easter eggs
- 6 Breeding
- 7 Sounds
- 8 Data values
	- 8.1 ID
	- 8.2 Entity data
- 9 Achievements
- 10 Advancements
- 11 History
	- 11.1 Prior colors
- 12 Issues
- 13 Gallery
	- 13.1 Renders
		- 13.1.1 Sheared
		- 13.1.2 Java Edition
		- 13.1.3 Bedrock Edition
		- 13.1.4 Jeb
	- 13.2 Screenshots
	- 13.3 In other media
- 14 References

## Spawning
When a sheep spawns, a color must be selected. A roll is performed with 100 numbers total. 5 numbers result in black sheep, 5 result in gray, 5 result in light gray, and 3 result in brown. That is a total of 18 out of the 100 numbers resulting in black, gray, light gray or brown sheep.

The remaining 82 numbers result in either white or pink sheep. When the roll lands on one of these 82 numbers, there is a 1/500 chance of the sheep being pink, otherwise it becomes white.

5% of sheep spawn as baby sheep.

| Color      | Chance         | Percent | Adult    | Baby    |
|------------|----------------|---------|----------|---------|
| Total      | -              | 100%    | 80%      | 20%     |
| White      | 82/100*499/500 | 81.84%  | 77.7442% | 4.0918% |
| Pink       | 82/100*1/500   | 0.164%  | 0.164%   | 0.0082% |
| Black      | 5/100          | 5%      | 4.75%    | 0.25%   |
| Gray       | 5/100          | 5%      | 4.75%    | 0.25%   |
| Light gray | 5/100          | 5%      | 4.75%    | 0.25%   |
| Brown      | 3/100          | 3%      | 2.85%    | 0.15%   |

If a sheep monster spawner is placed via /setblock, the sheep model spinning inside appears with one of the six naturally spawning colors. Independently from the displayed color, all six variants are able to spawn, the usual chances apply. To guarantee that sheep always spawn with the desired color, additional NBT tags can be applied to the monster spawner, utilizing the Color tag.

### Natural generation
In Java Edition, 4 sheep may spawn above grass blocks, at a light level of 9 or higher, even in snowy taigas.

In Bedrock Edition, 2 to 3 sheep spawn during the world generation on grass blocks at the surface at a light level of 7 or higher with at least a 2 block space above, except in snowy plains, ice spikes or wooded badlands. They later spawn individually on grassy biomes. 

Two sheep sometimes spawn in shepherd houses, butcher houses and animal pens in villages.

## Drops


### Breeding
Upon successful breeding, 1–7 is dropped.

### On death
| Item |                 | Roll Chance | Quantity (Roll Chance) |           |            |             |
|------|-----------------|-------------|------------------------|-----------|------------|-------------|
|      |                 |             | Default                | Looting I | Looting II | Looting III |
|      | Wool[d 1]       | 100%[d 2]   | 1                      | 1         | 1          | 1           |
|      | Raw Mutton[d 3] | 100%        | 1–2                    | 1–3       | 1–4        | 1–5         |


↑ Color of drop wool corresponds to color of sheep

↑ A sheared sheep does not drop wool.

↑ Dropped as cooked mutton if on fire when killed.


- 1–3 experience orbs if killed by a player or tamedwolf.

Killing a baby sheep yields no items nor experience.

### Shearing
When sheared, sheep give 1–3 wool and do not take any damage. This is not affected by Fortune or Looting.

## Behavior
Sheep wander aimlessly and individually or in small flocks of two to four. Sheep avoid cliffs and hazardous areas if it warrants damage. Sheep emit hoarse bleats in mostly random patterns and especially when attacked. If harmed, sheep flee for a few seconds, but make no special attempt to avoid wolves.

Sheep are nonchalant to players or other mobs, but follow a player holding wheat within a six blocks radius.

Adult sheep cannot fit through a gap if the 90-degree intersection of two fences is removed whereas the player and most other mobs can get through easily.


Sheep graze short grass (but not tall grass), making it disappear, and grass blocks, changing them into dirt blocks. In Bedrock Edition, they can also eat ferns. Baby sheep graze grass much more often than adults and mature 1 minute faster when grazing. Sheep can eat grass through blocks that are less than a full block thick, including extremities such as honey blocks, as well as from inside minecarts. A sheared sheep regrows its wool after grazing. Therefore, if no grass is available, a sheep cannot regrow its wool after being sheared. If an adult sheep has the opportunity, the chance of eating grass is 1⁄1000 every other game tick (1⁄50 for baby sheep). If /gamerule mobGriefing is set to false, grass blocks remain, but the sheep still regrow their wool.[1]


## Dyeing
Sheep's wool can be dyed by pressing the use key or the interact button while holding any dye. Sheared sheep cannot be dyed until their wool grows back after eating a grass block. Dyeing changes the color of the sheep's wool permanently or until the sheep is dyed again. The new wool colors will be inherited by baby sheep.

If a sheep is dyed and then sheared, it retains its new dyed wool color after the wool regrows. In Java Edition, the wool patches that are seen on a sheared sheep always appear white regardless of their actual color.[2]

## Easter eggs
See also: Easter eggs § Naming_mobs

An evoker can change a sheep's wool color if the evoker isn't engaged in combat and /gamerule mobGriefing is set to true. Then it can change the wool color of any blue sheep within 16 blocks to red. It signals the spell by producing orange color particles () and making a "wololo" sound. This is a reference to the priest unit of the 1997 game Age of Empires.

A sheep named “jeb_”.
If a sheep is named jeb_, its wool cycles through all dye colors in a similar manner to prismarine. This is purely a visual effect. A sheep named jeb_ can still be dyed without changing the rainbow effect, and any wool obtained from one of these sheep has the most recent color as if the sheep was not named.


## Breeding
An example of how a bred sheep inherits a mixture of its parents' colors when possible.
See also: Breeding

Sheep can be bred using wheat, after which they spawn a baby sheep. They cannot breed for five minutes after the baby sheep appears.

In Java Edition, if the parents have compatible wool colors (meaning that the corresponding dye items could be combined into a third dye color), the resulting baby sheep inherits a mix of their colors (e.g., blue sheep + white sheep = light blue baby sheep).
If the dye colors cannot normally be mixed, and also always in Bedrock Edition, the baby sheep spawns with the same color as one of the parents, chosen randomly, regardless of whether one or both parents have been sheared.

The 20-minute growth of baby sheep can be slightly accelerated using wheat. Each use takes 10% off the remaining time to grow up. It can also accelerate its own growth by eating grass.


## Data values
### ID
Java Edition:

| Name  | Identifier | Translation key        |
|-------|------------|------------------------|
| Sheep | sheep      | entity.minecraft.sheep |

Bedrock Edition:

| Name  | Identifier | Numeric ID | Translation key   |
|-------|------------|------------|-------------------|
| Sheep | sheep      | 13         | entity.sheep.name |

### Entity data
Sheep have entity data associated with them that contain various properties.

Bedrock Edition: 

See Bedrock Edition level format/Entity format.
Java Edition:

Main article: Entity format

 Entity data
Additional fields for mobs that can breed
Tags common to all entities
Tags common to all mobs
 Color: The color of the sheep. Default is 0.
 Sheared: 1 or 0 (true/false) - true if the sheep has been shorn.


Sheep color
Main article: Sheep/DV[edit]

