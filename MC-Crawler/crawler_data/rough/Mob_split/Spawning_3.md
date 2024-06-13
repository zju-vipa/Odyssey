#### Spawn conditions
Whether a spawn condition fails differs from the above determination if the game tries to spawn them in that biome. For example, dolphins can have pack spawns that occur inside of frozen ocean and deep frozen ocean biomes, but no other biomes. These rules apply to variants of the same mob, such as baby zombies and jockeys.

Each individual spawn attempt succeeds only if all of the following conditions are met:

- There must be no players or the world spawn point within a 24 radius block distance (spherical) of the spawning block
- The number of loaded mobs of that type must be less than the mob cap for that type. (I.e. the corresponding mobcap must not be full)
- The mob's collision box upon spawning must not collide with another collision box. A mob cannot spawn inside of anything that would collide with it upon spawning.
- The mob's collision box must not intersect with a solid block.
- For all mob types excluding passives and fish, spawns fail unless within a 128 radius block sphere around the player. For fish, spawns fail unless within a 64 block radius of the player.[2]
- /gamerule doMobSpawningistrue
- For non-aquatic mobs, the spawning block and the block above that cannot berails,powered rails,detector rails,activator rails,redstone power components, wither roses (except for wither skeletons) or sweet berry bushes (except for foxes).

** Hostile mobs **
- The difficulty must not be Peaceful, excluding piglins and hoglins
	- This also affects ocelots[3]
- For all hostiles other than guardians, drowned, and phantoms:
	- the block directly below it must have a solid, opaque, top surface (this includes upside downslabs, upside downstairs, and others) or besoul sandor aslime block.
	- the block directly below it must not bebedrock,barrier, or any type of trapdoor or glass.
	- The mob's collision box must not collide with any liquid.
	- The block above the spawning block must betransparent.
	- The mob must be immune to the damaging effects of the spawning block and the block directly below it. For instance, if the block directly below the spawning block is amagma block, the mob must be immune to fire damage. If the spawning block contains awither rose, the mob must be immune to wither damage. (Currently, this is only true for wither skeletons).

The basic rules for spawning are as follows:

- In the Overworld, block light level must be 0 and sky light must be 7 or below (which it always is inside a cave).
- In the Nether, block light level must be 11 or less. Sky light is always 0 in the Nether.
- In the End, block light level must be 0. Sky light is always 0 in the End.

When doing the light check in the Overworld and End, the spawn chances are randomized and a spawn only occurs if the light level is less than or equal to a random number between 0 and 7. In the Nether, as long as the light level is below 11, the spawn is allowed.

Some mobs have some additional rules in addition to the ones above.

| Mob                       | Rules                                                                                                                                                                                      |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Blaze                     | Spawns only in nether fortresses<br/>                                                                                                                                                      |
| Drowned                   | Spawning block and block below must be water<br/>In rivers, has 1⁄15 chance to spawn<br/>In oceans, has 1⁄40 chance to spawn and must be 5 block below sea level<br/>                      |
| Ghast                     | 95% chance of spawn failure.<br/>                                                                                                                                                          |
| Guardian                  | The spawning block and the block below must be water, including waterlogged blocks and bubble columns.<br/>95% chance of failure if the spawning block has sky exposure (details).<br/>    |
| Hoglin                    | Cannot spawn on nether wart block<br/>                                                                                                                                                     |
| Husk                      | The location of the spawn must have sky access<br/>                                                                                                                                        |
| Magma Cube                | Cannot spawn on liquid<br/>                                                                                                                                                                |
| Ocelot                    | Spawn has a 1⁄3 chance of failure<br/>Can spawn on leaves<br/>                                                                                                                             |
| Piglin                    | Cannot spawn on nether wart block<br/>                                                                                                                                                     |
| Skeleton(nether fortress) | There is an 80% chance of spawning a wither skeleton instead[verify]<br/>                                                                                                                  |
| Slime(swamp biome)        | the spawning block must be in a swamp biome<br/>the spawning block be on level 51 through 69 inclusive<br/>chance of failure based on the phase of the moon<br/>50% chance of failure<br/> |
| Slime(slime chunks)       | the spawning block is below level 40.<br/>90% chance of failure.<br/>                                                                                                                      |
| Stray                     | The location of the spawn must have sky access<br/>                                                                                                                                        |
| Wither Skeleton           | Spawns only in Nether fortresses<br/>                                                                                                                                                      |
| Zombified Piglin          | Cannot spawn on nether wart block<br/>                                                                                                                                                     |

** Passive mobs **
- The mob's collision box must not collide with any liquid.
	- if it is not astrider, the light level of the spawning block must be 9 or brighter.
		- If it is amooshroom, then...
			- the block directly below the spawning block must bemycelium.
		- If it is aturtle, then...
			- the block directly below the spawning block must besand.
			- the spawning block must be y-level 66 or lower.
		- If it is aparrot, then...
			- the block directly below the spawning block must either begrass block,leaves,log, orair.
		- If it is arabbit, then...
			- the block directly below the spawning block must either begrass block,snow block,snow[4], orsand.
		- If it is awolf, then...
			- the block directly below the spawning block must either begrass block,snow block, orsnow[4].
		- If it is afox, then...
			- the block directly below the spawning block must either begrass block,snow block,snow[4],podzol, orcoarse dirt.
		- If it is apolar bearspawning in afrozen oceanor deep frozen ocean biome, then...
			- the block directly below the spawning block must beice.
		- If it is agoat, then...
			- the block directly below the spawning block must either bestone,snow block,snow[4],packed ice, orgravel.
		- For all others then...
			- the block directly below the spawning block must be agrass block.
	- If it is astrider, then...
		- Spawn attempts with lava above check upward as long as there is still lava for if they can successfully spawn in a lava block with air on top.

** Aquatic mobs **
- The spawning block must be water
	- Forcod,salmon,pufferfish,tropical fish,squidordolphin:
		- the block directly below the spawning block must be water
		- the block directly above the spawning block must be water and cannot be waterlogged
		- the spawning block must be between level 50 and 63, inclusive. This does not apply totropical fishspawning in lush caves
	- If it is aglow squid, then...
		- the light level must be 0
		- the spawning block must be level 30 or lower
	- If it is anaxolotl, then...
		- the block directly above the spawning block must not be a solid block
		- the block directly below the spawning block must beclay

** Ambient mobs **
- The mob's collision box must not collide with any liquid.
	- If it is abat, then...
		- the spawning block must be at level 62 or below.
		- the block directly below it must have a solid, opaque, top surface.
		- the block directly below it must not bebedrock,barrier, or any type of trapdoor or glass.
		- If the real-time day is between October 20 and November 3, then the light level must be 7 or darker. Otherwise, the light level must be 4 or darker.

If all of these conditions are met then the mob is spawned.

** Spawn costs **
Locations that do not have spawning potential reliant spawns are marked by wart blocks or netherrack
The warped forest and soul sand valley biomes introduced a new mechanic to limit the amount of mobs that naturally spawn in them. The spawn cost (also called spawn potential or spawn density) takes on a value for each block in the biome. Certain mobs increase that value by some number ("charge") divided by their distance to the block. If a new spawn attempt would bring the "potential" of the spawning block above a certain threshold, the spawn attempt is canceled. This results in mobs not spawning too close to one another in these biomes, and new spawns in the area are completely blocked long before the full mobcap of 70 hostile mobs is ever reached.

More specifically, a mob may be spawned at a location if sum( existing mob's charge ÷ distance to mob ) × new mob's charge < new mob's maximum potential. While the code allows for different mobs to have different charges and maximum potential, all checked mobs have the same charge and maximum potential within both the warped forest and the soul sand valley.

Which mobs contribute to the charge, how much they add, and what the maximum potential is are all biome-specific. Mobs carry charge according to their current biome, and affect spawning in an adjacent biome even if they would not contribute a charge if in that biome. For example, striders in a soul sand valley affect enderman spawns in an adjacent warped forest, even though striders in the warped forest itself do not.

Due to the limited total number of mobs in soul sand valleys and warped forests, a larger-than-usual amount of mobs spawn in any space outside of these biomes, including in nether fortresses.

** Notes **
- Buildings surrounded by air spawn more mobs inside than underground rooms because packs that spawn outside of the building can spawn mobs inside it. The mob caps tend to be reached in seconds.
- If the player's view distance or the server view distance in multiplayer is at 9 or below, mob spawning is severely reduced (or they despawn too quickly), and may result in the player encountering no mobs at all. Set the view distance to 10 or higher to ensure mobs spawn correctly.

