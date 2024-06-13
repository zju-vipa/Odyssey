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

| Variants                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Temperate                                                                                                                                                                                                                                                                                                                                                                                                                        | Cold                                                                                                                                                                                                                                                                                           | Warm                                                                                                                                                                                                                                                                                               |
| Biomes                                                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                    |
| RiverBeachTaigaOld Growth Pine TaigaOld Growth Spruce TaigaBirch ForestOld Growth Birch ForestDark ForestForestFlower ForestMushroom FieldsMeadowPlainsSunflower PlainsSwamp[n 1]Windswept HillsWindswept Gravelly HillsWindswept ForestOceanDripstone CavesLush CavesStony ShoreStony Peaks‌[JE  only]Cold Ocean‌[JE  only]Deep Cold Ocean‌[JE  only]Lukewarm Ocean‌[JE  only]Deep Lukewarm Ocean‌[JE  only]The Void‌[JE  only] | Frozen RiverSnowy BeachGroveFrozen PeaksJagged PeaksSnowy PlainsIce SpikesSnowy SlopesSnowy TaigaFrozen OceanDeep Frozen OceanThe EndDeep DarkEnd Barrens‌[JE  only]End Highlands‌[JE  only]End Midlands‌[JE  only]Small End Islands‌[JE  only]Cold Ocean‌[BE  only]Deep Cold Ocean‌[BE  only] | JungleBamboo JungleSparse JungleBadlandsEroded BadlandsWooded BadlandsDesertSavannaSavanna PlateauWindswept SavannaWarm OceanMangrove Swamp[n 1]Basalt DeltasCrimson ForestNether WastesSoul Sand ValleyWarped ForestStony Peaks‌[BE  only]Lukewarm Ocean‌[BE  only]Deep Lukewarm Ocean‌[BE  only] |

Notes

↑ a b Frogs spawn naturally in this biome.


## Data values
### ID
Java Edition:

| Name    | Identifier | Entity tags                                                                                     | Translation key          |
|---------|------------|-------------------------------------------------------------------------------------------------|--------------------------|
| Tadpole | tadpole    | aquaticaxolotl_hunt_targetscan_breathe_under_waternot_scary_for_pufferfishsensitive_to_impaling | entity.minecraft.tadpole |

Bedrock Edition:

| Name    | Identifier | Numeric ID | Translation key     |
|---------|------------|------------|---------------------|
| Tadpole | tadpole    | 133        | entity.tadpole.name |

### Entity data
Tadpoles have entity data associated with them that contain various properties.

Java Edition:

Main article: Entity format

 Entity data
Tags common to all entities
Tags common to all mobs
 Age: Represents the age of the tadpole in ticks. When greater than or equal to 24000 game ticks (20 minutes), the tadpole grows up to a frog.
 FromBucket: 1 or 0 (true/false) - Whether the tadpole had ever been released from a bucket.

