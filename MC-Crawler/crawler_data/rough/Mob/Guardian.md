# Guardian
Guardians are pufferfish-like hostile mobs that spawn in and around ocean monuments. They attack with a slow-charging laser beam, and inflict retaliatory damage when damaged by a melee attack.

## Contents
- 1 Spawning
- 2 Drops
	- 2.1 Primary loot
	- 2.2 Secondary loot
- 3 Behavior
	- 3.1 Combat
- 4 Sounds
- 5 Data values
	- 5.1 ID
	- 5.2 Entity data
- 6 Achievements
- 7 Advancements
- 8 Video
- 9 History
- 10 Issues
- 11 Trivia
- 12 Gallery
	- 12.1 Textures
	- 12.2 Screenshots
	- 12.3 In other media
- 13 References
- 14 External links

## Spawning
Guardians spawn naturally in ocean monuments. They require water, flowing or stationary, to spawn. 

In Java Edition guardians spawn less often in ocean open to the sky than they do in covered areas (such as inside or underneath the monument). Specifically, spawning fails 95% of the time if the spawning water block is below sea level (Y=63 by default), all blocks between the spawning water block and sea level are liquid or fully transparent, and the block at sea level has a view of the sky. They can spawn only if the spawning block and the block below the spawning block are both water. 

In Bedrock Edition, guardians are structure spawns, spawning in water source blocks in 25 pre-determined spawning columns. Guardians usually do not (or possibly never) spawn near a player. Also, guardians seem not to spawn below solid blocks such as the prismarine blocks of the monument unless there are no water source blocks available above the solid blocks. This means that guardians don't spawn inside an ocean monument until most or all of the spawning column blocks above it are unavailable (i.e., no longer water source blocks). Guardians can spawn between Y=39–61 (inclusive, from the monument floor to one block above its highest point). To find the X and Z coordinates of the columns, start counting from the northwest corner of the monument. That is, standing on the furthest corner prismarine block with the smallest X and Z coordinates, let's say (X, 41, Z). The coordinates of each spawning spot are in a grid at X+2, X+13, X+29, X+45, and X+55, combined with Z+2, Z+13, Z+29, Z+45, and Z+55. For example, the bottom of the most northwest column is at (X+2, 39, Z+2) and the top block belonging to the southeast corner column is at (X+55, 61, Z+55). The guardians spawn at the northwest corner of a spawning column block, which can be helpful for some guardian farming mechanics such as causing them to spawn inside of a portal where they are immediately sent to the nether.

Guardians will spawn even if the monument has been destroyed by the player.

## Drops
See also: Guardian farming

#### Primary loot
| Item |                  | Roll Chance | Quantity (Roll Chance) |           |            |             |
|------|------------------|-------------|------------------------|-----------|------------|-------------|
|      |                  |             | Default                | Looting I | Looting II | Looting III |
|      | Prismarine Shard | 100%        | 0–2                    | 0–3       | 0–4        | 0–5         |
|      | Random Fish[d 1] | 2.5%–5.5%   | 1 (2.5%)               | 1 (3.5%)  | 1 (4.5%)   | 1 (5.5%)    |

1. ↑Dropped fish is determined by the Fishing loot table.Dropped as a random cooked fish if on fire when killed. (Java Edition only)

#### Secondary loot
In addition to the drops above, one of the following is selected

| Item |                     | Roll Chance | Quantity (Roll Chance) |           |            |             |
|------|---------------------|-------------|------------------------|-----------|------------|-------------|
|      |                     |             | Default                | Looting I | Looting II | Looting III |
|      | Raw Cod[d 1]        | 3/6         | 0–1                    | 0–2       | 0–3        | 0–4         |
|      | Prismarine Crystals | 2/6         | 0–1                    | 0–2       | 0–3        | 0–4         |
|      | Nothing             | 1/6         | 1                      | 1         | 1          | 1           |

1. ↑Dropped as cooked cod if on fire when killed. (Java Edition only)

Guardians also drop 10 when killed by a player or tamed wolf.

## Behavior
Guardians swim around in water, attacking any players, squid, glow squid, or axolotl that come into range of its laser. They swim in abrupt charges, moving their tail rapidly when doing so. When swimming, their spikes retract. When not swimming, they sink slowly and their spikes extend and quiver.

During idle swimming, a guardian will choose a water or waterlogged block within a 9x9x9 area centred on itself as the destination to pathfind towards. If unreachable, they swim directly towards the target despite any blocks in the way. They attempt to cross air blocks and do not try to prevent fall damage.

Stationary guardians are pushed much faster horizontally by flowing water than other mobs, but when swimming they are completely unimpeded - they remain affected by bubble columns however.

There is a slight bias for blocks with a higher light level to be the chosen destination when swimming. If undisturbed, guardians can be seen loosely congregating around the sea lantern blocks of their ocean structure.

When out of water, guardians always have their spikes extended, squeak loudly and move with erratic, random hopping - making no attempt to directly move towards water. Unable to use their laser attack, any previous pathfinding or mob target is instantly abandoned. Guardians do not suffocate and can survive indefinitely without water unlike other aquatic mobs.

The guardian's eye follows and stares at any nearby players, and always looks directly at its target. In Java Edition, the eye does not follow unarmored players under the effects of a potion of Invisibility and the guardians cannot attack them. A player can wear one piece of armor while under the effects of Invisibility and not be attacked.

Guardians, as aquatic mobs, are affected by the Impaling enchantment.‌[JE  only]

### Combat
See also: Tutorials/Combat § Guardians

Guardians have two methods of attack: a laser and a defensive attack analogous to the Thorns enchantment. Unlike most other hostile mobs, a guardian does not follow a player who moves out of sight. Instead, it simply continues swimming until the player becomes visible again to start charging its laser.

Guardians attack players, axolotls, and squid. Otherwise, a guardian does not retaliate against mobs (such as iron golems) that attack it, other than damaging the attacking mob with its natural thorns defense.

** Laser **
The laser takes 2 seconds to charge, doing no damage in the meantime. It starts out purple and fades to yellow. Once charged, the laser flashes green and deals 6 regular damage and additional 1 magical damage on normal difficulty. The latter bypasses armor. Guardians swim around for 3 seconds before firing again. If the target approaches while the guardian is loading its laser, it stops firing and swims away until it is at a comfortable range, at which point it continues attacking. The laser cannot be dodged or blocked by a shield and has a maximum range of 15 blocks.

Once the target is out of range, or if the laser is obstructed by solid blocks (including transparent blocks like glass), the guardian's laser disengages.

** Spikes defense **
Guardians deal damage each time it is hit with a melee attack while its spikes are extended, similar to the Thorns armor enchantment. If cornered, the guardian usually extends its spikes and fires at the player, even at point-blank range.

## Data values
### ID
Java Edition:

| Name     | Identifier | Entity tags                                                                                                                      | Translation key             |
|----------|------------|----------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| Guardian | `guardian` | `aquatic`<br/>`axolotl_always_hostiles`<br/>`can_breathe_under_water`<br/>`not_scary_for_pufferfish`<br/>`sensitive_to_impaling` | `entity.minecraft.guardian` |

Bedrock Edition:

| Name     | Identifier | Numeric ID | Translation key        |
|----------|------------|------------|------------------------|
| Guardian | `guardian` | `49`       | `entity.guardian.name` |

### Entity data
Guardians have entity data associated with them that contains various properties.

Java Edition:

Main article: Entity format
- Entity data
	- 
	- Tags common to all entities
	- 
	- Tags common to all mobs

Bedrock Edition:

SeeBedrock Edition level format/Entity format.
