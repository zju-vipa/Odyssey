# Wither Skeleton
Wither skeletons are tall black variants of skeletons equipped with stone swords that inflict the poison-like Wither effect. They are found exclusively in nether fortresses and are the only source of wither skeleton skulls, as well as the only renewable source of coal.

## Contents
- 1 Spawning
	- 1.1 Halloween
	- 1.2 Withers
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
- 10 Trivia
- 11 Gallery
	- 11.1 Renders
	- 11.2 Screenshots
	- 11.3 In other media
- 12 References

## Spawning
Wither skeletons spawn in nether fortresses at a light level between 0 and 7, in groups of up to 4. They are the only mobs that can spawn inside wither roses due to their immunity to the damaging effect.

### Halloween

  

This feature is exclusive to  Java Edition. 


On Halloween, wither skeletons have a 22.5% chance of spawning wearing a carved pumpkin and a 2.5% chance of spawning wearing a jack o'lantern. This is not dropped.

### Withers

  

This feature is exclusive to  Bedrock Edition. 


The wither spawns 3-4 wither skeletons when below half health on normal and hard difficulties.

## Drops
| Item |                           | Roll Chance    | Quantity (Roll Chance) |           |            |              |
|------|---------------------------|----------------|------------------------|-----------|------------|--------------|
|      |                           |                | Default                | Looting I | Looting II | Looting III  |
|      | Coal                      | 33.33%–66.67%  | 1 (33.33%)             | 1–2 (50%) | 1–3 (60%)  | 1–4 (66.67%) |
|      | Bone                      | 100%           | 0–2                    | 0–3       | 0–4        | 0–5          |
|      | Wither Skeleton Skull(JE) | 2.5%–5.5%[d 1] | 1 (2.5%)               | 1 (3.5%)  | 1 (4.5%)   | 1 (5.5%)     |
|      | Wither Skeleton Skull(BE) | 2.5%–8.5%[d 1] | 1 (2.5%)               | 1 (4.5%)  | 1 (6.5%)   | 1 (8.5%)     |
|      | Wither Skeleton Skull     | 100%[d 2]      | 1                      | 1         | 1          | 1            |

1. ↑ a bDropped only when kill credit is given to the player
2. ↑Only when killed by a charged creeper. In Java Edition, only one skull or head drops per charged creeper explosion, even if multiple mobs are killed by it.

- 8.5% chance of dropping their unenchanted stoneswordwhich has a randomdurability. This chance increases by 1% per level of Looting, for a maximum of 11.5% chance with Looting III.
- 5 experience orbs when killed by aplayeror tamedwolf, and an additional1–3 is dropped per piece of naturally-spawned equipment thatdoes notdrop upon death.
	- Because all wither skeletons spawn with a stone sword, each of them effectively drop6–8 if the sword is not dropped.
	- If the wither skeletondoesdrop its stone sword, it drops the default5 instead.
- Acarved pumpkinorjack o'lanternworn by a wither skeleton spawned on Halloween is never dropped.

## Behavior
Wither skeletons wander aimlessly when idle, but sprint to attack players, snow golems, iron golems, baby turtles, piglins, and piglin brutes within 16 blocks. They flee from wolves but retaliate if attacked. 

When an entity is attacked by a wither skeleton in any difficulty, it is inflicted with the Wither effect for ten seconds, which turns the health bar black ( × 10) and decreases it by 1 every two seconds. Unlike Poison, this effect can drop HP to zero and cause death.

In Normal and Hard difficulties, some wither skeletons pick up dropped equipment. The chance depends on regional difficulty, with up to 55% of them capable of picking up swords higher than stone tier plus any armor. Wither skeletons never take bows; in Java Edition, if they hold a bow (which can be done with /summon wither_skeleton ~ ~ ~ {HandItems:[{id:bow,Count:1b}]}) they shoot flaming arrows even if their bows are not enchanted. They cannot use crossbows.

Wither skeletons are immune to fire and the Wither effect. They still seek shade or water during daylight if they are in the Overworld even though they do not burn in sunlight.

In Bedrock Edition, the player can burn them by throwing a trident enchanted with Channeling during a thunderstorm.

Being an undead mob, they are: 

- damaged by the status effectInstant Healthand healed by the status effectInstant Damage.
- unaffected by the status effectsRegenerationandPoison.
- ignored by thewither.
- affected by theSmiteenchantment.
- unable to swim inwater, but do not drown.
- a threat toarmadillos, causing them to hide in their shell.‌[upcoming: JE 1.20.5 & BE 1.20.80]

## Data values
### ID
Java Edition:

| Name            | Identifier        | Entity tags                                                                                                                                | Translation key                    |
|-----------------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| Wither Skeleton | `wither_skeleton` | `can_breathe_under_water`<br/>`ignores_poison_and_regen`<br/>`inverted_healing_and_harm`<br/>`skeletons`<br/>`undead`<br/>`wither_friends` | `entity.minecraft.wither_skeleton` |

Bedrock Edition:

| Name            | Identifier        | Numeric ID | Translation key               |
|-----------------|-------------------|------------|-------------------------------|
| Wither Skeleton | `wither_skeleton` | `48`       | `entity.wither_skeleton.name` |

### Entity data
Wither skeleton have entity data associated with them that contains various properties. The wither skeleton is taller than the skeleton.

Java Edition:

Main article: Entity format
- Entity data
	- 
	- Tags common to all entities
	- 
	- Tags common to all mobs

Bedrock Edition:

SeeBedrock Edition level format/Entity format.

