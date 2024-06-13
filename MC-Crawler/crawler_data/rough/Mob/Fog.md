# Fog
Fog is a rendering feature intended for obscuring the player's view distance, usually for atmospheric effect or for seamlessly occluding sharp boundaries such as unloaded chunks. While traditionally referring to render distance, there are many other types of fog that can be encountered in-game under specific circumstances.

## Contents
- 1 Java Edition
	- 1.1 Fog types
		- 1.1.1 Distance fog
		- 1.1.2 Water fog
		- 1.1.3 Lava fog
		- 1.1.4 Powder snow fog
	- 1.2 Fog modifiers
		- 1.2.1 Height
		- 1.2.2 Blindness and darkness
		- 1.2.3 Wither
		- 1.2.4 Night vision
		- 1.2.5 Nether and ender dragon
	- 1.3 Removed
		- 1.3.1 Void fog
- 2 Bedrock Edition
	- 2.1 Vanilla fog settings
- 3 History
- 4 Issues
- 5 Gallery
	- 5.1 Screenshots
- 6 References

## Java Edition
### Fog types
There are four fog types, each occurring in four different circumstances.

#### Distance fog

  

This section is named by the community. 
An official name has not been given. Please update the name if confirmed by reliable sources.


This refers to fog that is rendered in normal circumstances, and becomes the most notable with low render distance.

The sight distance in the distance fog is equal to the render distance, and the shape is a cylinder. Its color depends mainly on the biome the camera is in, and is affected by:

- the current day-time, and theeffectthe dimension uses
	- For the overworld effect, the brightness of the color changes with day time.
	- For the nether effect, the brightness of the color isnotaffected by day time.
	- For the end effect, the brightness of the color does not change with day time, but is 15% of the biome fog color.
- the current sky color, and the render distance
	- The smaller the rendering distance, the closer the color of the fog is adjusted to the sky color.
	- When the rendering distance is 32, the color of the fog is not affected by the sky color.
- the direction the player is facing during a sunrise or sunset if the render distance is not less than 4
- the currentweather

#### Water fog
When the camera is in water, a dedicated fog in the shape of a cylinder is applied to simulate this. Underwater fog progressively recedes with time spent underwater. The color depends on the biome the camera is in. The color of the water fog changes gradually for 5 seconds when the camera traveled in water into another biome. Notably, swamps and mangrove swamps have a thicker fog than most other biomes, which is controlled by the biome tag has_closer_water_fog.

#### Lava fog
When the camera is in lava, an even thicker fog in the shape of a sphere is applied. Its color is RGB(0.6,0.1,0.0). With this fog, normally the player can see only 1 block away. The Fire Resistance effect can mitigate the fog so that the sight distance becomes 3 blocks. In spectator mode, the fog is even less opaque to reveal objects located within up to half the render distance.

#### Powder snow fog
Being beneath powder snow imparts another fog in the shape of a sphere. Its color is RGB(0.623, 0.734, 0.785). With this fog, normally the player can see only 2 blocks away. In spectator mode, the fog becomes more thinner so that things within half of the render distance are visible.

### Fog modifiers
#### Height
If the world is not a superflat world, and the camera is not in lava and not in powder snow, the brightness becomes power(clamp((y-minY)*0.03125,0.0,1.0)) of the original, which means that the color changes to pure black gradually from minY+32 to minY.

#### Blindness and darkness
Blindness and darkness set the color to pure black. The sight distance with blindness is 5 blocks, while the sight distance with darkness is 15 blocks. And the shape of the fog becomes a sphere.

A difference between the two is that darkness has fade-in and fade-out, while blinding has only fade-out.

Blindness has a higher priority than darkness. The two effects do not work if the camera is in lava or powder snow.

#### Wither
If there is a wither boss event, the color becomes darker and slightly redder.

#### Night vision
If the camera is not in water, and the entity has no darkness effect, night vision makes the color brighter.

#### Nether and ender dragon
If the entity has no blindness or darkness, in a dimension with the nether effect, or a dimension where there's an ender dragon boss event, the sight distance in the distance fog (not water, lava, powder snow fog) is half of the rendering distance, and the maximum sight distance is 96 blocks. The shape becomes a sphere.

### Removed
#### Void fog

  

This section describes content that exists only in outdated versions of Java Edition. 
This feature used to be in the game but has since been removed.



In prior versions of Java Edition (specifically Beta 1.8 Pre-release through 14w34b inclusive, up to its removal in 14w34c), a thick black fog was introduced. As the player descended below Y=26, this fog would start to appear. As the player traveled deeper, the fog at the edge of the render distance would become closer until the player reached the first layers of bedrock, where visibility was reduced to just a few blocks, beyond which was complete darkness. The gray void particles started appearing below Y=7, as well as in the void.

The existence of this fog depended on a lack of sky lighting. If vent holes were opened up to allow skylight to enter an otherwise secluded underground space, void fog would no longer be present, so long as the player kept near this skylight source.

Void fog was removed late into 1.8's development for performance reasons and general community distaste.[1]

- A player's view limit would decrease with depth.


## Bedrock Edition
In Bedrock Edition, fogs has six types used in six different circumstances:

- air: When the camera is in air
- water: When the camera is in water
- lava: When the camera is in lava, and the player has nofire resistance
- lava resistance: When the camera is in lava, and the player hasfire resistance
- weather: When in air and it's raining
- powder snow: When the camera is in powder snow

In a fog setting file in a resource pack, one or more of above types can be specified. Active fog settings are determined from three aspects:

- Custom fog stack (from/fogcommand)
- Fog settings for the current biome
- Default fog setting

Whenever the game needs to get the current fog, it checks the fog settings from these three aspects from the top (the newest fog setting in the fog stack from the command) to the bottom (default fog setting) in order, until it finds a fog definition for the current fog type. If it finds no matching setting, the game uses the hardcoded default setting of the Bedrock Engine.

In other words, this is equivalent to that all fog settings from the three aspects are applied one by one from the bottom (default fog setting) to the top (the newest fog setting in the fog stack from the command) in order. The fogs in a fog setting applied later overrides that of earlier fog settings. Each fog type works independently. Hardcoded default setting of the game engine is applied before settings from these three aspects.

See also this official document.

### Vanilla fog settings
Here are all the fog setting IDs that are currently in the vanilla game. 

- minecraft:fog_bamboo_jungle
- minecraft:fog_bamboo_jungle_hills
- minecraft:fog_basalt_deltas
- minecraft:fog_beach
- minecraft:fog_birch_forest
- minecraft:fog_birch_forest_hills
- minecraft:fog_cold_beach
- minecraft:fog_freezing_ocean
- minecraft:fog_cold_taiga
- minecraft:fog_cold_taiga_hills
- minecraft:fog_cold_taiga_mutated
- minecraft:fog_crimson_forest
- minecraft:fog_deep_cold_ocean
- minecraft:fog_deep_frozen_ocean
- minecraft:fog_deep_lukewarm_ocean
- minecraft:fog_deep_cold_ocean
- minecraft:fog_deep_warm_ocean
- minecraft:fog_default
- minecraft:fog_desert
- minecraft:fog_desert_hills
- minecraft:fog_extreme_hills
- minecraft:fog_extreme_hills_edge
- minecraft:fog_extreme_hills_mutated
- minecraft:fog_extreme_hills_plus_trees
- minecraft:fog_extreme_hills_plus_trees_mutated
- minecraft:fog_flower_forest
- minecraft:fog_forest
- minecraft:fog_forest_hills
- minecraft:fog_frozen_ocean
- minecraft:fog_frozen_river
- minecraft:fog_hell
- minecraft:fog_ice_mountains
- minecraft:fog_ice_plains
- minecraft:fog_ice_plains_spikes
- minecraft:fog_jungle
- minecraft:fog_jungle_edge
- minecraft:fog_jungle_hills
- minecraft:fog_jungle_mutated
- minecraft:fog_lukewarm_ocean
- minecraft:fog_mangrove_swamp
- minecraft:fog_mega_spruce_taiga
- minecraft:fog_mega_spruse_taiga_mutated
- minecraft:fog_mega_taiga
- minecraft:fog_mega_taiga_hills
- minecraft:fog_mega_taiga_mutated
- minecraft:fog_mesa
- minecraft:fog_mesa_bryce
- minecraft:fog_mesa_mutated
- minecraft:fog_mesa_plateau
- minecraft:fog_mesa_plateau_stone
- minecraft:fog_mushroom_island
- minecraft:fog_mushroom_island_shore
- minecraft:fog_ocean
- minecraft:fog_plains
- minecraft:fog_powder_snow
- minecraft:fog_river
- minecraft:fog_roofed_forest
- minecraft:fog_savanna
- minecraft:fog_savanna_mutated
- minecraft:fog_savanna_plateau
- minecraft:fog_soulsand_valley
- minecraft:fog_stone_beach
- minecraft:fog_sunflower_plains
- minecraft:fog_swampland
- minecraft:fog_swampland_mutated
- minecraft:fog_taiga
- minecraft:fog_taiga_hills
- minecraft:fog_taiga_mutated
- minecraft:fog_the_end
- minecraft:fog_warm_ocean
- minecraft:fog_warped_forest

