## Tile tick format
Tile Ticks represent block updates that need to happen because they could not happen before the chunk was saved. Examples reasons for tile ticks include redstone circuits needing to continue updating, water and lava that should continue flowing, recently placed sand or gravel that should fall, etc. Tile ticks are not used for purposes such as leaf decay, where the decay information is stored in the leaf block data values and handled by Minecraft when the chunk loads. For map makers, tile ticks can be used to update blocks after a period of time has passed with the chunk loaded into memory.

- A Tile Tick
	- 
	- i: The ID of the block; used to activate the correct block update procedure.
	- p: If multiple tile ticks are scheduled for the same tick, tile ticks with lower p are processed first. If they also have the same p, the order is unknown.
	- t: The number of ticks until processing should occur. May be negative when processing is overdue.
	- x: X position
	- y: Y position
	- z: Z position

## ToBeTicked format
This  List is always present, and contains 16  Sublists, each representing one of the "sections" of the chunk. Those inside lists may contain  Shorts, each representing a packed coordinate relative to the section : The 4 most significant bits are always 0, then each group of 4 bits (or nibble) represents a section-relative coordinate, from 0 to 15. The order of sections in the list appear to be ordered from bottom to top, and the packing order of the coordinates is 0ZYX, where 0 refers to the chunk section. When converting proto-chunks to full chunks, only coordinates that are stored in PostProcessing appear to receive a tick update, tick updates stored in block_ticks, and fluid_ticks are ignored. [verify]


