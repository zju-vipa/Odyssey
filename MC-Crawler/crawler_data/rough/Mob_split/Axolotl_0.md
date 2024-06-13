# Axolotl
An axolotl is a passive bucketable aquatic mob found in lush caves that hunts most other aquatic mobs, and can assist players with aquatic combat and grant them Regeneration.

## Contents
- 1 Spawning
	- 1.1 Colors
- 2 Behavior
	- 2.1 Breeding
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Entity data
- 5 Achievements
- 6 Advancements
- 7 History
- 8 Issues
- 9 Trivia
- 10 Gallery
	- 10.1 Renders
	- 10.2 Textures
	- 10.3 Screenshots
	- 10.4 Development images
	- 10.5 Concept artwork
	- 10.6 In other media
- 11 References

## Spawning
Axolotls spawn underwater in the lush caves biome and when there is a clay block less than five blocks below the spawning space.

### Colors
Axolotls can be one of five colors: pink (leucistic), brown (wild), gold, cyan and blue. 

When breeding axolotls, there is a 1⁄1200 (0.083%) chance of the offspring having the blue mutation, leaving 1199⁄1200 (99.917%) chance of matching one of the parents (including blue parents).

| Pose              | Color     |       |      |      |       |
|-------------------|-----------|-------|------|------|-------|
|                   | Leucistic | Wild  | Gold | Cyan | Blue  |
| Ground crawling   |           |       |      |      |       |
| Ground stationary |           |       |      |      |       |
| Swimming          |           |       |      |      |       |
| Water stationary  |           |       |      |      |       |
| Animation         |           |       |      |      | Color |
|                   | Leucistic | Brown | Gold | Cyan | Blue  |
| Ground crawling   |           |       |      |      |       |

## Behavior
Axolotls are passive toward players, can be attached to leads, and follow players holding a bucket of tropical fish on either the main hand or the off-hand. When a player kills a mob that is in combat with one or more axolotls, axolotls remove Mining Fatigue from the player, and give the player Regeneration I for 100 game ticks (5 seconds) per axolotl in the fight, up to a duration of 2400 game ticks (2 minutes) in Java Edition, and uncapped in Bedrock Edition.

Axolotls attack all aquatic mobs except turtles, dolphins, frogs and other axolotls. They also attack drowned. An axolotl deals 2 points of damage per attack.

After killing a non-hostile mob, there is a two minute cooldown before another non-hostile mob can be hunted. Axolotls prioritize attacking hostile mobs over non-hostile mobs.

If an axolotl takes damage underwater, it may play dead, dropping to the ground for 200 game ticks (10 seconds) while gaining Regeneration I. Hostile aquatic mobs ignore healing axolotls. There is a 1⁄3 chance for an axolotl to play dead to recover 4. In addition, if either a random integer from 0–2 (inclusive) is less than the amount of incoming damage, or the axolotl's health before the damage is dealt is less than 50% of its maximum health, it plays dead. 

Axolotls can leave the water and wander about on land. When an axolotl leaves the water, it wanders as far as 8 or 9 blocks beyond the water's edge before returning to the water, as long as there is water at least 2 blocks deep within 16 blocks of the axolotl. If 2-block-deep water is outside this range, the axolotl can wander off randomly on land in search of more deep water, and die after 6000 game ticks (5 minutes) exposure out of water. Axolotls are not attracted to shallow (1 block deep) water. They require water at least 2 blocks deep within 16 blocks to pathfind to the water.[1]

Axolotls can also die out of water as passengers in a boat. Unlike fish and squid, axolotls do not die on land in rain or in a thunderstorm.

Unlike most mobs, axolotls cannot be moved by flowing water. However, they are still affected by bubble columns.

As aquatic mobs, in Java Edition they take extra damage from the Impaling enchantment. Unlike other aquatic mobs, they cause nearby pufferfish to inflate.

Axolotls picked up with a water bucket and re-spawned do not despawn.

Axolotls can be renamed by placing a bucket of axolotl into an anvil, the same as if renaming any other item.

### Breeding
Main article: Breeding
Adult axolotls can be led and bred with buckets of tropical fish. After breeding, a baby axolotl spawns and 1–7 experience is generated. The parents cannot be bred again for 5 minutes in Java Edition or 1 minute in Bedrock Edition. The baby axolotl has a 1⁄1200 chance to be the rare blue variant; otherwise, it inherits the color of one parent at random. Babies follow adults, and grow to adulthood in 20 minutes. The growth of baby axolotls can be accelerated using buckets of tropical fish; each use reduces the remaining growing time by 10%.

## Data values
### ID
Java Edition:

| Name    | Identifier | Entity tags                                                         | Translation key            |
|---------|------------|---------------------------------------------------------------------|----------------------------|
| Axolotl | `axolotl`  | `aquatic`<br/>`can_breathe_under_water`<br/>`sensitive_to_impaling` | `entity.minecraft.axolotl` |

Bedrock Edition:

| Name    | Identifier | Numeric ID | Translation key       |
|---------|------------|------------|-----------------------|
| Axolotl | `axolotl`  | `130`      | `entity.axolotl.name` |

### Entity data
Axolotls have entity data associated with them that contain various properties.

Java Edition:

Main article: Entity format
- Entity data
	- 
	- Additional fields for mobs that can breed
	- 
	- Tags common to all entities
	- 
	- Tags common to all mobs
	- FromBucket: 1 or 0 (true/false) – iftrue, indicates the axolotl has been released from a bucket.
	- Variant: ID of the axolotl's variant.


Axolotl Variant
Main article: Axolotl/DV[edit]

Bedrock Edition:

| Color | Data value |
|-------|------------|
|       | `0`        |
|       | `1`        |
|       | `2`        |
|       | `3`        |
|       | `4`        |

SeeBedrock Edition level format/Entity format.

