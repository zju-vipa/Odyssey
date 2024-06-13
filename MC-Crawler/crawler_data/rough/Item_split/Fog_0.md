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

