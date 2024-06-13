### Block data
A structure block also has a block entity associated with it.

Java Edition:

See also: Block entity format

- Block entity data
	- 
	- Tags common to all block entities
	- author: Author of the structure; only set to "?" for most vanilla structures.
	- ignoreEntities: 1 or 0 (true/false): Whether entities should be ignored in the structure.
	- integrity: How complete the structure is that gets placed.
	- metadata: Value of the data structure block field.
	- mirror: How the structure is mirrored, one of "NONE", "LEFT_RIGHT" (mirrored over X axis when not rotated), or "FRONT_BACK" (mirrored over Z axis when not rotated).
	- mode: The current mode of this structure block, one of "SAVE", "LOAD", "CORNER", or "DATA".
	- name: Name of the structure.
	- posX: X-position of the structure.
	- posY: Y-position of the structure.
	- posZ: Z-position of the structure.
	- powered: 1 or 0 (true/false): Whether this structure block is being powered by redstone.
	- rotation: Rotation of the structure, one of "NONE", "CLOCKWISE_90", "CLOCKWISE_180", or "COUNTERCLOCKWISE_90".
	- seed: The seed to use for the structure integrity, 0 means random.
	- showboundingbox: 1 or 0 (true/false): Whether to show the structure's bounding box to players in Creative mode.
	- sizeX: X-size of the structure, its length.
	- sizeY: Y-size of the structure, its height.
	- sizeZ: Z-size of the structure, its depth.

Bedrock Edition:

SeeBedrock Edition level format/Block entity format.
## Notes
1. ↑Structures created in versions before 1.13 are saved in .minecraft/saves/(WorldName)/structures.
2. ↑Only available on Windows 10


