# Illusioner
The illusioner is an unused illager armed with a bow. It attacks using illusions and can also fire arrows.

## Contents
- 1 Spawning
- 2 Drops
- 3 Behavior
	- 3.1 Casting blindness
	- 3.2 Summoning duplicates
- 4 Sounds
- 5 Data values
	- 5.1 ID
	- 5.2 Entity data
- 6 Advancements
- 7 History
- 8 Issues
- 9 Trivia
- 10 Gallery
- 11 References

## Spawning
An illusioner has no spawn egg in the Creative mode inventory. An illusioner can be spawned only using data packs or the /summon illusioner in-game command. Illusioners do not spawn in woodland mansions or pillager outposts, nor at raids or patrols. Similarly to the other unused giant and zombie horse mobs, illusioners do not spawn in any biome, monster spawner or world-generated structure.

## Drops
When an illusioner is killed by a player or a tamed wolf, any naturally spawned equipment, including its unenchanted bow, has an 8.5% chance of dropping (or 9.5% with Looting I, 10.5% with Looting II and 11.5% with Looting III) and drops with a random item durability. In addition, 5 experience orbs are dropped on player or tamed wolf kills.

An invisible illusioner captain and its four copies strafing. The real banner is invisible.
The illusioner also drops one  illager ominous banner if it is a raid captain.

## Behavior
Although they do not naturally spawn in raids, illusioners spawned by the player attack players, adult villagers, iron golems and wandering traders within a 16×4×16 cubic area. 

An illusioner joins a nearby raid if it occurs or joins a patrol if sufficiently near a patrol captain. 

The illusioner attacks with its spells and its bow, firing an arrow every second. Unless the illusioner is summoned using commands, it cannot attack with a non-bow item in its hand, cannot use tipped arrows in its offhand slot (but can use spectral arrows) and cannot use enchanted bows. Also, it is the only illager that can see its target through walls. 

The Illusioner moves quickly on a semi-circular fashion and always tries to maintain a consistent distance between itself and the player, strafing from left to right and vice-versa, retreating if the player gets too close or advancing if the player retreats. 

Finally, the illusioner has two spells: a spell that blinds its opponent and a spell that summons visual pseudo-duplicates and makes the illusioner invisible.

If it has no bow, the illusioner  becomes "passive", a unarmed illusioner can be spawned with this command /summon illusioner ~ ~ ~ {}.

### Casting blindness
The illusioner casts its blindness spell only if the regional difficulty is greater than 2. As a result, the world difficulty setting, the inhabited time of a chunk, the total daytime in the world and the phase of the moon from the day-night cycle affects its ability.

An illusioner's four false duplicates. The real illusioner is invisible.
An illusioner casts a Blindness effect that lasts for 20 seconds upon first engaging a new player opponent. It signals this attack by raising its arms during a short-timed animation, making a low pitched sound and producing a black mist of particles (). Other entities (typically a wolf, a snow golem or an iron golem) do not trigger this magic. The illusioner does not cast this spell more than once on the same player opponent, unless it has first shifted its attention to another opponent and then back to that original opponent. 

This spell resets the illusioner's spell cooldown to 1 second and resets the cooldown for the blinding spell to 9 seconds.

### Summoning duplicates
As long as an illusioner is engaged in combat, it casts an Invisibility status effect on itself that lasts 60 seconds and refreshes the effect whenever the Invisibility's time runs out. The illusioner signals this spell by raising its arms, making a strange high pitched sound and producing a blue mist of particles called "mirror" ().

When an illusioner becomes invisible through this or another method, it creates four false duplicates of itself. These hover and waver at short distances from the actually invisible illusioner, though they do not space themselves out until the first time the illusioner is attacked. They face in exactly the same direction as the illusioner and move somewhat in step with the original, appearing to no-clip through blocks like a vex does. Despite using the shooting animation whenever the original uses its bow, only the real illusioner can shoot and be damaged.

The clones move to new positions if they were not triggered and are still bunched together. The Illusioner can also do this once in a while to "refresh" the clones' positions.

When the real illusioner is damaged, its duplicates all snap back to where the real illusioner is, then quickly snap back out to new positions, making a teleporting sound, signaling the hit.

If an invisible illusioner receives the Glowing effect, all of the duplicates glow, while the true illusioner remains invisible. Moreover, only the invisible illusioner burns when catching fire.

The duplicates dissipate once the illusioner's Invisibility effect ends.

This spell resets the illusioner's spell cooldown to 1 second and resets the cooldown for the invisibility spell to 17 seconds.

## Data values
### ID
| Name       | Identifier | Entity tags                   | Translation key             |
|------------|------------|-------------------------------|-----------------------------|
| Illusioner | illusioner | illagerillager_friendsraiders | entity.minecraft.illusioner |

### Entity data
See also: Entity format

Illusioners have entity data associated with them that contain various properties.


 Entity data
Tags common to all entities
Tags common to all mobs
Tags common to all mobs spawnable in raids
 SpellTicks: Number of ticks until a spell can be cast. Set to a positive value when a spell is cast, and decreases by 1 per tick.

