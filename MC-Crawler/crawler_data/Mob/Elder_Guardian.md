# Elder Guardian
An elder guardian is a stronger and larger variant of the guardian, and the largest aquatic mob. It attacks the same way as a normal guardian, but also applies Mining Fatigue to players in a large radius around itself. They are only found in ocean monuments; three of them generate in each one.

## Contents
- 1 Spawning
- 2 Drops
	- 2.1 Primary loot
	- 2.2 Secondary loot
- 3 Behavior
	- 3.1 Laser
	- 3.2 Inflicting Mining Fatigue
	- 3.3 Spikes defense
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
	- 12.1 Screenshots
	- 12.2 In other media
- 13 References
- 14 External links

## Spawning
Three elder guardians spawn naturally during the generation of each ocean monument:

- One in the top room of the monument.
- Two in each wing of the monument.

They are spawned with the ocean monument, and thus, they do not respawn.

## Drops
#### Primary loot
| Item |                  | Roll Chance | Quantity (Roll Chance) |           |            |             |
|------|------------------|-------------|------------------------|-----------|------------|-------------|
|      |                  |             | Default                | Looting I | Looting II | Looting III |
|      | Prismarine Shard | 100%        | 0–2                    | 0–3       | 0–4        | 0–5         |
|      | Wet Sponge       | 100%[d 1]   | 1                      | 1         | 1          | 1           |
|      | Tide Armor Trim  | 20%         | 1                      | 1         | 1          | 1           |
|      | Random Fish[d 2] | 2.5%–5.5%   | 1 (2.5%)               | 1 (3.5%)  | 1 (4.5%)   | 1 (5.5%)    |


↑ Dropped only when kill credit is given to the player

↑ Dropped fish is determined by the Fishing loot table.Dropped as a random cooked fish if on fire when killed. (Java Edition only)


#### Secondary loot
In addition to the drops above, one of the following is selected

| Item |                     | Roll Chance | Quantity (Roll Chance) |           |            |             |
|------|---------------------|-------------|------------------------|-----------|------------|-------------|
|      |                     |             | Default                | Looting I | Looting II | Looting III |
|      | Raw Cod[d 1]        | 3/6         | 0–1                    | 0–2       | 0–3        | 0–4         |
|      | Prismarine Crystals | 2/6         | 0–1                    | 0–2       | 0–3        | 0–4         |
|      | Nothing             | 1/6         | 1                      | 1         | 1          | 1           |


↑ Dropped as cooked cod if on fire when killed. (Java Edition only)


- 10 –  when killed by a player or tamed wolf.

## Behavior

  

This section would benefit from the addition of more images. 
Please remove this notice once you've added  suitable images to the article.  The specific instructions are: Animated images of the elder guardian cursing effect, distinct ones for java and bedrock due to animation differences


Elder guardians do not swim around as much as normal guardians. Elder guardians do not swim away when approached by a player it is targeting, unlike regular guardians. Like normal guardians, elder guardians attempt to attack the player, squid, and glow squid.

The elder guardian's eye follows and stares at any nearby players, and always looks directly at its target. The eye still follows a player under the effects of Invisibility or in Spectator mode, but doesn't attack.

Elder guardian are considered aquatic mobs, and thus are affected by the Impaling enchantment. ‌[Java Edition  only] ‌[until JE Combat Tests]

The elder guardian has three methods of attacking, including firing its laser, inflicting Mining Fatigue, and a defensive thorn-like attack. 

The elder guardian pathfinds toward an ocean monument if it is not within one. 

An elder guardian attacks axolotls that are not playing dead. Otherwise, an elder guardian does not attack mobs (such as iron golems) that attack it, although the attacking mob takes damage from the elder guardian's natural spikes defense.

### Laser
Laser
The laser takes several seconds to charge, doing no damage and allowing the player to move away in the meantime. As it charges it turns from purple to bright yellow (thus acting as a warning indicator). Once charged, the beam flashes green, abruptly ends, and deals 12 × 6 damage on Hard difficulty. The elder guardian swims around for a few seconds before firing again. The beam cannot be dodged and has a maximum range of approximately 14 blocks. Once the player is out of range, if the beam is obstructed by solid blocks, or if the player has a shield, the guardian's beam disengages from the player and deals no damage.

### Inflicting Mining Fatigue
In Java Edition, immediately after spawning and once each minute thereafter, the elder guardian searches for any player within a spherical radius of 50 blocks to afflict with Mining Fatigue III. In Bedrock Edition the elder guardian inflicts any unafflicted player within range immediately.

When afflicted, the player sees a ghostly image of the elder guardian and hears a ghostly noise. The effect decreases a player's attack speed by 30% and decreases mining speed even more for 5 minutes. The attack targets players through blocks, even underground, and a potion of Invisibility offers no defense. This is not considered an attack in regards to the Thorns enchantment.

The image of the elder guardian is a particle effect that can be recreated by issuing the command /particle minecraft:elder_guardian.‌[Java Edition  only]

### Spikes defense
An elder guardian deals 2 (3 on Hard mode) of damage every time it is hit while its spikes are extended, similar to the Thorns enchantment on armor. If cornered by a player or axolotl, the elder guardian usually extends its spikes and fires at point-blank range.

## Data values
### ID
Java Edition:

| Name           | Identifier     | Entity tags                                                                                        | Translation key                 |
|----------------|----------------|----------------------------------------------------------------------------------------------------|---------------------------------|
| Elder Guardian | elder_guardian | aquaticaxolotl_always_hostilescan_breathe_under_waternot_scary_for_pufferfishsensitive_to_impaling | entity.minecraft.elder_guardian |

Bedrock Edition:

| Name           | Identifier     | Numeric ID | Translation key            |
|----------------|----------------|------------|----------------------------|
| Elder Guardian | elder_guardian | 50         | entity.elder_guardian.name |

### Entity data
Elder guardians have entity data associated with them that contains various properties.

Java Edition:

Main article: Entity format

 Entity data
Tags common to all entities
Tags common to all mobs

Bedrock Edition:

See Bedrock Edition level format/Entity format.
