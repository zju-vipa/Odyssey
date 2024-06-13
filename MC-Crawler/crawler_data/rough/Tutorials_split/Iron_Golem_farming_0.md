# Tutorials/Iron Golem farming
Iron golem farming uses village mechanics to produce iron and poppies. Usually, an iron golem farm is a player-constructed village in which golems are spawned and then either killed immediately or moved to a holding cell outside the village boundary for later killing. Iron golem farming is preferable to other methods of iron farming from zombies and skeletons due to a much higher chance of iron dropping and therefore much higher quantities of iron. In Java Edition, it is also superior to most other farms in that it does not require player presence, meaning it can produce iron indefinitely as long as the chunks it's in are loaded. 

## Contents
- 1 Java Edition
- 2 Bedrock Edition
	- 2.1 Spawning requirements
		- 2.1.1 Simulation Distance
		- 2.1.2 Frequency of Spawns
		- 2.1.3 Spawnable Space
		- 2.1.4 Iron Harvesting Rate
	- 2.2 Village center
	- 2.3 Maximizing rates
	- 2.4 Survival mode build: Iron golem village
- 3 Videos
	- 3.1 Java Edition
	- 3.2 Bedrock Edition
- 4 See also

## Java Edition
In Java Edition, a villager can attempt to spawn an iron golem while not having a golem alive within the box of radius 16 blocks around the villager and more than 30 seconds has passed.

An iron golem needs an available volume in which to spawn. There must be at least 3 transparent blocks above the spawning surface, and that surface must be solid and flat (but not a bottom slab).

Zombies and pillagers nearby increase the spawn rate of iron golems. If a zombie/pillager is seen by villagers, they panic and increase the rate of spawn attempts. Zombies are easier to use as scaring mobs than pillagers, as you'd need a disarmed pillager (one without crossbow) for the farm to work, although pillagers have a much larger range to scare villagers than zombies, also they don't burn in sunlight unlike zombies and won't hurt you if their crossbow breaks.

Nether portals can also be used to increase rates, since the iron golem cap instantly resets when it's teleported to the Nether. Aside portals, one can also construct a chute where the golems fall into after spawning, which clears the mob cap. This is more reliable than nether portals.

## Bedrock Edition
### Spawning requirements
Villages attempt to spawn iron golems around the village center when the following requirements are met: 

1. The village contains at least 20 beds.
2. The village contains at least 10 villagers.
3. At least 75% of the villagers have worked at their workstations the previous day.
4. All of the villagers must be linked to a bed.
5. The village must be within a player'ssimulation distancevolume.
6. There must be space to spawn an iron golem within a 16×6×16 volume around thevillage center.
7. There is less than one naturally generated or spawned (i.e. not player-created) iron golem for every 10 villagers in the village. The ratio of iron golems to villagers is rounded down to the nearest whole number, so to spawn a second iron golem while the first is still alive requires 20 villagers, to spawn a third golem requires 30 villagers, and so on.

#### Simulation Distance
To clarify, iron golems can spawn as long as the player is within simulation range of the village's boundaries; being near the village center is not necessary. Simulation distance remains consistent both horizontally and vertically. The formula for calculating simulation range is as follows:

SimulationRange=8×SimulationDistance

#### Frequency of Spawns
There is a 1/700 chance of an iron golem spawn attempt during each game tick when these conditions are met. This averages to one spawn attempt every 35 seconds. However, the spawn attempt only succeeds in spawning a golem if the game finds a spawnable spot.

#### Spawnable Space
To search for a spawnable spot during a spawn attempt, the game checks 10 random X, Y, Z coordinates in the 16×6×16 volume around the village center. The spawn attempt succeeds if a chosen coordinate meets the following conditions: 

- There is a solid block underneath.
- The 2×4×2 volume extending -1 X (west), +3 Y (upward), and -1 Z (north) from the chosen coordinate does not contain any solid or full blocks.

If these conditions are met but there is a partial or transparent block at the chosen coordinate, then the iron golem may appear to spawn on top of the partial or transparent block. This gives the appearance that iron golems can spawn on top of normally non-spawnable blocks like bottom slabs, carpets, and glass.

