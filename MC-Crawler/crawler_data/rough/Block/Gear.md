# Gear
The gear was a block that could be placed on walls and grounds, but had no clearly defined or implemented functionality. It is believed that gears were intended to be used in mechanisms, similarly to redstone wire. 

## Contents
- 1 Obtaining
	- 1.1 Post-Generation
- 2 Usage
	- 2.1 Texture generation
- 3 Data values
	- 3.1 ID
- 4 History
- 5 Issues
- 6 Gallery
	- 6.1 Screenshots
- 7 References

## Obtaining
Gears are only known to be obtainable through the use of inventory editors and other external tools.

### Post-Generation
Gears can generate when water spawners and lava spawners collide in Indev versions in Java Edition. They were pretty tough to remove and the only way to get rid of is by using explosions.

## Usage
Gears would only render on the sides of full, solid blocks, including water and lava spawners.
When edited into the game, a placed gear would show nothing in its block space and was invisible unless horizontally adjacent to one or more blocks. The placed gear would then show an animated gear sprite on the near side of each of those blocks. It was not possible to destroy a placed gear by mining a block that its gear sprite was shown on, because the placed gear itself was actually adjacent to that block. If the block a gear sprite was shown on was destroyed, the adjacent placed gear would no longer show that sprite. Removing all blocks adjacent to a placed gear would remove all of its visible gear sprites, leaving the placed gear invisible. Placed gears could not be destroyed directly by the player; attempts to do so would phase through to the block behind it, much like water. Placed gears could only be removed by letting water[needs testing] flow into them, or by explosions.

### Texture generation
Code which generates the frames of the gear texture can be found here.

The animation for gears was generated using two predefined image files - misc/gear.png for the rotating gear and misc/gearmiddle.png for the stationary center.

- misc/gear.png
- misc/gearmiddle.png

The animation, updated every game tick,[1] is rendered as a 16×16 texture like most other blocks. The resulting gear has 18.75 RPM.[1]

There are two different animations used for gears - one for clockwise rotation, and another for anticlockwise rotation, to allow for logical meshing. These are generated effectively identically, with the only difference being the direction of rotation; both start on the same frame, but cycle through them in the opposite direction.[1]

- Clockwise rotation
- Anticlockwise rotation

## Data values
### ID
| Name                | Numeric ID | Form         |
|---------------------|------------|--------------|
| [No displayed name] | `55`       | Block & Item |

