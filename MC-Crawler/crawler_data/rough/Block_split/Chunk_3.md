## Finding chunk edges

X and Z coordinates that are divisible by 16 represent the boundaries between chunks.  EG:  (96, -32) is a corner where four chunks meet. One of those chunks is between X coordinates 80 to 96 and Z coordinates -48 to -32. Another one is between X coordinates 96 to 112 and Z coordinates -32 to -16, and so on. When either X or Z crosses a multiple of 16, the player is moving across chunks. 

Essentially, the player is in the top-left corner (north-western) of a chunk when both X and Z coordinates are divisible by 16.

Additionally, the player can know the chunk they are on by this formula:
The X of a chunk is floor(X coordinate / 16)
The Z of a chunk is floor(Z coordinate / 16)
Where floor is the largest previous integer. E.g. Floor( 27.9561 ) is 27 
In other words, if X was 27, Z was −15 the chunk is chunk (Floor(27/16), Floor(−15/16)), meaning that the player is on chunk (1, −1).
Also, the coordinates of a block within a chunk can be found by taking the coordinate mod 16.

In Java Edition, the key F3 + G can be used to display chunk boundaries. Alternately, pressing the "F3" button opens the Debug screen that shows the player's X, Y, and Z coordinates, in addition to the "chunk" variable. These coordinates change as the player moves around. The player can know the chunk they are in by the variable "chunk".

In Bedrock Edition, when toggling fancy graphics, the world renders again, loading only the chunk the player is in for a split second, briefly showing the chunk boundaries. When the player changes the render distance rapidly, chunk barriers appear as a blue line.
Also, if in mid-air and bridging with full blocks, the next block placed fades into view when a chunk border is intersected, showing the chunk border. This is sometimes unreliable, and it happens only on chunk borders. This does not happen underground or when the block placed is close to more than one block.

## Slime chunks
Main article: Slime § Slime chunks
Each chunk has a 1⁄10 chance of generating as a slime chunk, a chunk that slimes are able to spawn in below Y=40 and regardless of light level. These chunks are otherwise identical to normal chunks.

In Java Edition, whether a chunk at a particular set of coordinates becomes a slime chunk is determined by the world's seed. In Bedrock Edition, however, they are generated at the same coordinates in every world.


