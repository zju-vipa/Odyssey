# Tadpole
A tadpole is a bucketable aquatic baby passive mob hatched from frogspawn. They mature into one of the three frog variants depending on the biome in which they mature.

## Contents
- 1 Spawning
- 2 Drops
- 3 Behavior
- 4 Sounds
- 5 Data values
	- 5.1 ID
	- 5.2 Entity data
- 6 Achievements
- 7 Advancements
- 8 History
- 9 Issues
- 10 Gallery
	- 10.1 Screenshots
	- 10.2 In other media
- 11 References
- 12 External links

## Spawning
Tadpoles hatch from frogspawn in groups of 2-5.

## Drops
As with other baby animals, tadpoles do not drop any items or experience on death.

## Behavior
Tadpoles swim aimlessly in water. On land, they flop around like fish and seek out nearest water. They die in less than 20 seconds after being out of water. 

Unlike frogs, tadpoles are hunted by axolotls.

Tadpoles follow a player that is holding a slimeball.

A player can pick up a tadpole with a bucket of water.

A tadpole grows up into one of the variants of a frog depending on the tadpole's location, as shown on the table below. Tadpoles take one Minecraft day to grow up (20 minutes). Its growth may be accelerated by feeding it slimeballs. Each use reduces the remaining growth duration by 10%.

| Variants |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                   |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          | Temperate                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Cold                                                                                                                                                                                                                                                                                                                                                                                     | Warm                                                                                                                                                                                                                                                                                                                                                                                              |
| Biomes   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                   |
|          | River<br/>Beach<br/>Taiga<br/>Old Growth Pine Taiga<br/>Old Growth Spruce Taiga<br/>Birch Forest<br/>Old Growth Birch Forest<br/>Dark Forest<br/>Forest<br/>Flower Forest<br/>Mushroom Fields<br/>Meadow<br/>Plains<br/>Sunflower Plains<br/>Swamp[n 1]<br/>Windswept Hills<br/>Windswept Gravelly Hills<br/>Windswept Forest<br/>Ocean<br/>Dripstone Caves<br/>Lush Caves<br/>Stony Shore<br/>Stony Peaks‌[JE  only]<br/>Cold Ocean‌[JE  only]<br/>Deep Cold Ocean‌[JE  only]<br/>Lukewarm Ocean‌[JE  only]<br/>Deep Lukewarm Ocean‌[JE  only]<br/>The Void‌[JE  only] | Frozen River<br/>Snowy Beach<br/>Grove<br/>Frozen Peaks<br/>Jagged Peaks<br/>Snowy Plains<br/>Ice Spikes<br/>Snowy Slopes<br/>Snowy Taiga<br/>Frozen Ocean<br/>Deep Frozen Ocean<br/>The End<br/>Deep Dark<br/>End Barrens‌[JE  only]<br/>End Highlands‌[JE  only]<br/>End Midlands‌[JE  only]<br/>Small End Islands‌[JE  only]<br/>Cold Ocean‌[BE  only]<br/>Deep Cold Ocean‌[BE  only] | Jungle<br/>Bamboo Jungle<br/>Sparse Jungle<br/>Badlands<br/>Eroded Badlands<br/>Wooded Badlands<br/>Desert<br/>Savanna<br/>Savanna Plateau<br/>Windswept Savanna<br/>Warm Ocean<br/>Mangrove Swamp[n 1]<br/>Basalt Deltas<br/>Crimson Forest<br/>Nether Wastes<br/>Soul Sand Valley<br/>Warped Forest<br/>Stony Peaks‌[BE  only]<br/>Lukewarm Ocean‌[BE  only]<br/>Deep Lukewarm Ocean‌[BE  only] |

** Notes **
1. ↑ a bFrogs spawn naturally in this biome.

## Data values
### ID
Java Edition:

| Name    | Identifier | Entity tags                                                                                                                   | Translation key            |
|---------|------------|-------------------------------------------------------------------------------------------------------------------------------|----------------------------|
| Tadpole | `tadpole`  | `aquatic`<br/>`axolotl_hunt_targets`<br/>`can_breathe_under_water`<br/>`not_scary_for_pufferfish`<br/>`sensitive_to_impaling` | `entity.minecraft.tadpole` |

Bedrock Edition:

| Name    | Identifier | Numeric ID | Translation key       |
|---------|------------|------------|-----------------------|
| Tadpole | `tadpole`  | `133`      | `entity.tadpole.name` |

### Entity data
Tadpoles have entity data associated with them that contain various properties.

Java Edition:

Main article: Entity format
- Entity data
	- 
	- Tags common to all entities
	- 
	- Tags common to all mobs
	- Age: Represents the age of the tadpole in ticks. When greater than or equal to 24000 game ticks (20 minutes), the tadpole grows up to a frog.
	- FromBucket: 1 or 0 (true/false) - Whether the tadpole had ever been released from a bucket.

