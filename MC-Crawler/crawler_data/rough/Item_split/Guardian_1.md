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

