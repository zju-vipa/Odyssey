### Attacking
Main article: Damage
All bees nearby are angered when an individual bee is attacked (unless the bee attacked is killed in one hit‌[Java Edition  only]), honey or honeycombs are collected (unless a campfire is placed under the nest), or a bee nest/beehive is destroyed. Even destroying newly-placed uninhabitated artificial beehives anger nearby bees. Hitting or walking on a beehive does not anger bees; it must be destroyed to anger them. When destroyed, a beehive releases any bees that it contained, and these bees are angry. If the beehive is destroyed with a Silk Touch tool, bees outside the hive become angry ‌[Bedrock Edition  only],[7] while those kept within it remain neutral even after the hive is placed again.

The Invisibility effect does not cause stingers in stung players to disappear.
Bees attack and swarm the player as a group when angered, and the eyes of angered bees turn red. Collecting a honeycomb or a honey bottle from a nest or hive causes the bees that are currently in that nest or hive to leave and swarm the player unless a campfire is placed below the hive. Bees attack only once, similar to llamas, and non-aggressive pandas. Bees do not deal any damage in Peaceful difficulty and are completely passive.

If the player deflects a bee's attack with a shield, the bee continues attacking until it succeeds in hitting the player.

When a bee's attack on a player succeeds, the player is poisoned. A bee loses its stinger after a successful attack, cannot attack further, and dies approximately one minute later. This can be delayed with potion effects (Regeneration/Resistance/Absorption) that have a 255 potency.

It is possible to (quickly) breed at least one angered bee with another, even if it or they had stung and lost the stinger. However, they remain angered and still die later due to being stingerless.

Bees also swarm and attack other mobs when damaged, for example, if a skeleton accidentally shoots a bee.

Bees become neutral if they fail to land a hit on their target within 25 seconds.

- The stinging animation; the bee can remain upside down for longer periods of time if a distance is kept.
- Prior to stinging
- After stinging

In Java Edition, a bee's stinger is visible on the player as a small black dot after the bee successfully attacked.

- 

### Breeding
Main article: Breeding
Bees follow players holding any 1- or 2-block tall flowers, flowering azalea, cherry leaves, flowering azalea leaves, mangrove propagule, spore blossom, pink petals, or chorus flower. If the player is standing still and being followed by bees, the bees go toward the player, face the player, and rest on the ground. They do this until the player moves.

If bees are given any of the blocks listed above, they enter love mode and pair up to create baby bees, granting the player 1-7 experience. The parent bees have a cooldown of 5 minutes (6000 ticks) before they can breed again. Babies take 20 minutes (1 in-game day) to grow up. The growth of baby bees can be accelerated using flowers; each use reduces the remaining time by 10%. However, bees' growth timer and breeding cooldowns are frozen while working in a hive; thus, when rapidly growing a population, it may be desirable to temporarily remove the hives.

Any of the 1- or 2-block flowers can be used for breeding, including the wither rose,[8] even though it usually harms bees that touch it.

## Data values
### ID
Java Edition:

| Name | Identifier | Entity tags                                                                                         | Translation key        |
|------|------------|-----------------------------------------------------------------------------------------------------|------------------------|
| Bee  | `bee`      | `arthropod`<br/>`beehive_inhabitors`<br/>`fall_damage_immune`<br/>`sensitive_to_bane_of_arthropods` | `entity.minecraft.bee` |

Bedrock Edition:

| Name | Identifier | Numeric ID | Translation key   |
|------|------------|------------|-------------------|
| Bee  | `bee`      | `122`      | `entity.bee.name` |

### Entity data
Bees have entity data associated with them that contains various properties.

Java Edition:

Main article: Entity format
- Entity data
	- 
	- Additional fields for mobs that can become angry
	- 
	- Additional fields for mobs that can breed
	- 
	- Tags common to all entities
	- 
	- Tags common to all mobs
	- CannotEnterHiveTicks: Time left in ticks until the bee can enter a beehive. Used when the bee is angered and released from the hive by a player, but the hive is smoked by acampfire.
	- CropsGrownSincePollination: How many crops the bee has grown since its last pollination. Used to limit number of crops it can grow.
	- FlowerPos: Coordinates of the flower the bee is circling.
		- X: X coordinate.
		- Y: Y coordinate.
		- Z: Z coordinate.
	- HasNectar: 1 or 0 (true/false) - true if the bee is carrying pollen.
	- HasStung: 1 or 0 (true/false) - true if the bee has stung a mob or player.
	- HivePos: Coordinates of the bee'shive.
		- X: X coordinate.
		- Y: Y coordinate.
		- Z: Z coordinate.
	- TicksSincePollination: Number of ticks passed since the bee's last pollination.

Bedrock Edition:

SeeBedrock Edition level format/Entity format.

