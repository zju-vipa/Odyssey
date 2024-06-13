# Firework Rocket
A firework rocket is an item and entity used for creating decorative explosions, boosting when flying with elytra, and loading into a crossbow as ammunition.

## Contents
- 1 Obtaining
	- 1.1 Crafting
- 2 Usage
	- 2.1 Launching fireworks
		- 2.1.1 Dispenser
		- 2.1.2 Crossbow
	- 2.2 Boosting elytra
	- 2.3 Village raids
- 3 Behavior
	- 3.1 Duration and direction
- 4 Sounds
- 5 Data values
	- 5.1 ID
	- 5.2 Item data
	- 5.3 Entity data
- 6 Advancements
- 7 History
- 8 Issues
- 9 Trivia
- 10 Gallery
	- 10.1 Screenshots
- 11 References

## Obtaining
Firework rockets can be obtained by crafting.

In Java Edition, firework rockets with no explosive effects and 3 different flight durations are available in the Creative inventory. In Bedrock Edition, 16 firework rockets with the different base colors and the "small ball" effect, and a single firework with no explosion are available in the Creative inventory; these all have a flight duration of 1.

### Crafting
| Ingredients                                | Crafting recipe | Description                                                                                                                                                                                                                                                                                                                                 |
|--------------------------------------------|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Paper+<br/>Gunpowder                       | 3               | When crafted this way (without a firework star), the rocket does not have explosion effects. The value of gunpowder affects theflight duration.                                                                                                                                                                                             |
| AnyFirework Star+<br/>Paper+<br/>Gunpowder | 3               | Adding more gunpowder increases the duration of the rocket. Up to three gunpowder can be used. Up to five firework stars can also be used with three gunpowder. Up to seven firework stars can be used by using firework stars instead of additional gunpowder. All firework stars explode almost simultaneously when the rocket detonates. |

## Usage
### Launching fireworks
A firework rocket can be launched up vertically by using its item on a block. Firework rockets can also be launched from dispensers and crossbows.

#### Dispenser
Using firework rockets with a dispenser is different than launching it on a block. The direction the dispenser is facing launches the firework in that direction; for example, if the dispenser is facing downward, the firework goes downward instead of going up.

#### Crossbow
A firework rocket can be used as ammunition for crossbows, although it deals damage only if it has an explosion effect. A higher flight duration gives the firework rocket a longer range, and more damage is added per firework star. If shot from a Multishot crossbow, then 3 rockets fire with the same effects. The Piercing enchantment has no effect on firework rockets shot from a crossbow.

In Java Edition, if a firework rocket shot from a crossbow hits an entity, the rocket instantly explodes, no matter the flight duration. Attempting to do this in Bedrock Edition, however, results in the firework passing through the entity,[1] so the player must plan where to aim.

### Boosting elytra
Normally, elytra can glide for a short distance, but with the use of fireworks, the player can fly a long distance, gain speed, and take off from the ground. Using a firework rocket while flying with elytra propels the player in the direction they are facing. If the rocket is equipped with a firework star of any kind, the player takes damage when it explodes.

The duration of the speed boost depends on the flight duration of the rocket - a higher flight duration means a longer boost.

| Firework flight duration | Elytra flight boost duration | Boost amount per gunpowder |
|--------------------------|------------------------------|----------------------------|
| 1                        | ~1.17 seconds                | 100%                       |
| 2                        | ~1.48 seconds                | 120%                       |
| 3                        | ~2.22 seconds                | 128%                       |

### Village raids
After successfully defending a village from a raid, the villagers may celebrate by setting off firework rockets.

## Behavior
See also: Firework Star § Effects

Once launched, fireworks fly out vertically, with random horizontal offset up to 5 blocks. Fireworks can fly in any of the 6 directions a dispenser can point. After some time, the firework explodes into a colorful explosion based on the effects of the firework stars added upon crafting, or no explosion if no firework star was used. If multiple firework stars were added to the rocket upon crafting, they all explode simultaneously.

The explosion of a firework rocket deals damage to mobs and players that are within 5 blocks and not obstructed by solid blocks. The maximum damage of a rocket with one firework star is 7, with the damage decreasing with distance. Each additional firework star on the rocket adds 2 points of damage, for a maximum damage of 19 × 9.5 with 7 stars. Using commands to add additional firework stars results in more damage. The damage dealt is unaffected by any other ingredients used. The explosion does not destroy end crystals, item frames, or paintings, but does destroy armor stands.

There is a delay between the detonation and the player hearing the sound, emulating real fireworks, but this sound travels much more slowly than in the real world.[2][3] In Java Edition, the explosion of a firework can be seen 64 blocks away, regardless of its height. In Bedrock Edition, the explosion can be seen from the player's render distance.

If the explosion exceeds the (unmodded) particle limit of 16,384, the oldest particles are removed before displaying new ones, resulting in severely diminished firework quality / duration. At most a firework should have 3 trail stars, more than that could waste diamonds, firework stars, and other fireworks. Particle counts per star are:

| Ball type | Plain | Trail |
|-----------|-------|-------|
| Small     | 98    | ~1300 |
| Large     | 387   | 4000+ |
| Star      | 122   | ~1600 |
| Creeper   | 266   | ~3500 |
| Burst     | 72    | ~930  |

Twinkle effect adds 2 particles to the count.

Like most other entities, they can be moved by water and explosions, and teleported via portals. They also cannot move through solid surfaced blocks: upon hitting one, they either move to a side or explode based on the duration. If a firework explodes under a block, its explosion is flattened.

