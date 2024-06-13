# Sticky Piston
A sticky piston is a variant of the piston that can additionally pull most blocks when it retracts.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Pulling
		- 2.1.1 Spitting
			- 2.1.1.1 Exceptions
- 3 Technical components
- 4 Sounds
	- 4.1 Generic
	- 4.2 Unique
- 5 Data values
	- 5.1 ID
	- 5.2 Block states
	- 5.3 Block data
- 6 History
	- 6.1 Data history
- 7 Issues
- 8 Trivia
- 9 Gallery
	- 9.1 Screenshots
- 10 See also
- 11 Notes
- 12 References

## Obtaining
### Breaking
A sticky piston can be broken using any tool with equal efficiency, and always drops itself.
In Java Edition, it is faster to break them with a pickaxe. The pickaxe is also the preferred tool for breaking the head when extended.[1]

| Block     | Sticky Piston         |
|-----------|-----------------------|
| Hardness  | 1.5                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 2.25                  |
| Wooden    | 1.15                  |
| Stone     | 0.6                   |
| Iron      | 0.4                   |
| Diamond   | 0.3                   |
| Netherite | 0.25                  |
| Golden    | 0.2                   |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Natural generation
Three sticky pistons generate as part of each jungle temple. Five sticky pistons also generate in each ancient city.

### Crafting
| Ingredients      | Crafting recipe |
|------------------|-----------------|
| Slimeball+Piston |                 |

## Usage
See also: Piston

A sticky piston behaves the same as a normal piston, exept when pulling. A sticky piston pulls when it is unpowered.

### Pulling
A sticky piston also pulls the block attached to its head and any blocks attached to the head via slime- or honey blocks, but not any of the other blocks it may have pushed.

Sticky pistons stick to a block only when retracting, so if the block at the head of the sticky piston is pushed, it will move. It also will not hold a falling block.

#### Spitting

  

This section is named by the community. 
An official name has not been given. Please update the name if confirmed by reliable sources.


In Java Edition, sticky pistons finish extending early and start retracting if given a pulse shorter than 3 or 2 game ticks (depending on if there is start delay). This causes a sticky piston to "spit" its block, leaving it behind. Also, this causes the block to end up in its final position earlier. Sticky pistons will still pull a block back if there was an air gap before it extended. 

| Block                                                                                                                                                                | Effect (Java Edition)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Effect (Bedrock Edition)                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
|                                                                                                                                                                      | Barrier Beacon Bedrock Calibrated Sculk Sensor Command Block Crying Obsidian Enchanting Table End Gateway End Portal End Portal Frame Ender Chest Grindstone Jigsaw Block Jukebox Light Block Lodestone Monster Spawner Moving Piston Nether Portal Obsidian Piston (extended) Piston Head Reinforced Deepslate Respawn Anchor Sculk Catalyst Sculk Sensor Sculk Shrieker Structure Block Structure Void‌[BE  only]                                                                                                                                                                                                                                                                                                                                                                                    | Cannot be pushed or pulled.                                                                 |
| Allow Deny Border Structure Air                                                                                                                                      | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Cannot be pushed or pulled.                                                                 |
|                                                                                                                                                                      | Compound Creator Element Element Constructor Hardened Glass Hardened Glass Pane Heat Block Lab Table Material Reducer Underwater TNT                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Can be pushed or pulled.                                                                    |
|                                                                                                                                                                      | Underwater Torch Colored Torches                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Breaks when pushed, turning to drops when applicable. Cannot be pulled.                     |
| Barrel Beehive Bee Nest Blast Furnace Brewing Stand Chest Chiseled Bookshelf Conduit Daylight Detector Dispenser Dropper Furnace Hopper Lectern Smoker Trapped Chest | Cannot be pushed or pulled, because these blocks holdblock entities.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Can be pushed or pulled.                                                                    |
|                                                                                                                                                                      | Large chest                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Can be pushed or pulled, but separates into two chests.                                     |
|                                                                                                                                                                      | Banner Hanging Sign Sign                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Breaks when pushed or unsupported, turning into drops.                                      |
|                                                                                                                                                                      | Campfire Soul Campfire                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Breaks when pushed, turning to drops when applicable. Cannot be pulled.                     |
|                                                                                                                                                                      | Glazed Terracotta                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Can be pushed, but not pulled.                                                              |
|                                                                                                                                                                      | Carpets (not moss)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Can be pushed and pulled. Breaks when pulled downward, turning into drops.                  |
| Bell Candle Lantern Soul Lantern                                                                                                                                     | Breaks when pushed, turning to drops when applicable. Cannot be pulled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Can be pushed or pulled.                                                                    |
|                                                                                                                                                                      | Amethyst Cluster Bamboo Bed Budding Amethyst Button Cactus Cake Carved Pumpkin Cave Vines Chorus Flower Chorus Plant Cobweb Cocoa Dead Bush Decorated Pot Door Dragon Egg[note 1] Fire Flower Pot Flower Frogspawn   Grass Head Item Frame[note 2] [note 3] Jack o'Lantern Ladder Lava Leaves Lever Lily Pad Melon Melon Stem Moss Block Moss Carpet Mushroom Nether Wart Painting[note 4] Pink Petals Pointed Dripstone Pressure Plate Pumpkin Pumpkin Stem Redstone Comparator Redstone Dust Redstone Repeater Redstone Torch Saplings Scaffolding Sculk Vein Sea Pickle Shulker Box Snow Soul Fire Structure Void‌[JE  only] Sugar Cane Suspicious Sand Torch Torchflower Torchflower Crop Tripwire Tripwire Hook Turtle Egg Twisting Vines Vines Water Weeping Vines Weighted Pressure Plate Wheat | Breaks when pushed, turning to drops when applicable. Cannot be pulled.                     |
| Anvil                                                                                                                                                                | Cannot be pulled. Pushable only whenin a falling state.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Can be pushed or pulled, but falls if unsupported. Cannot be pulled whenin a falling state. |
|                                                                                                                                                                      | Concrete Powder Gravel Red Sand Sand                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Can be pushed or pulled, but falls if unsupported. Cannot be pulled whenin a falling state. |

Pistons do not move blocks that are "attached to a block", as they detach and drop as an item.

##### Exceptions
- Rails: as long as they remain on top of a solid face of a block in their new position, and that block isn't moving at the same time.
	- An exception is when the rail and block supporting it are on two parallelextendedpistons at which the rail remains attached. InJava Edition, in order for the rail to successfully move without breaking, the piston moving the block must be powered 1 block event after the piston moving the rail. Trying to move both on the same piston usingslime blocksdoes not work, nor does moving them on perpendicular pistons (although the latter temporarilyappearsto work because of the bugMC-75716).
	- Rails re-orient themselves after being pushed, similar to when placed manually.



## Technical components
Main article: Piston/Technical components
Sticky pistons have 2 technical blocks that cannot be obtained. These include the piston head and moving piston blocks.

## Data values
### ID
Java Edition:

| Name          | Identifier    | Form         | Block tags | Translation key               |
|---------------|---------------|--------------|------------|-------------------------------|
| Sticky Piston | sticky_piston | Block & Item | None       | block.minecraft.sticky_piston |

| Name         | Identifier |
|--------------|------------|
| Block entity | piston     |

Bedrock Edition:

| Name          | Identifier    | Alias ID | Numeric ID | Form                       | Item ID[i 1]   | Translation key         |
|---------------|---------------|----------|------------|----------------------------|----------------|-------------------------|
| Sticky Piston | sticky_piston | None     | 29         | Block & Giveable Item[i 2] | Identical[i 3] | tile.sticky_piston.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


| Name                | Savegame ID |
|---------------------|-------------|
| Piston block entity | PistonArm   |

### Block states
See also: Block states

The sticky_piston block uses following block states:

Java Edition:

| Name     | Default value | Allowed values           | Description                                                                                                          |
|----------|---------------|--------------------------|----------------------------------------------------------------------------------------------------------------------|
| extended | false         | falsetrue                | If true, the piston is extended.                                                                                     |
| facing   | north         | downeastnorthsouthupwest | The direction the piston head is pointing.The opposite from the direction the player faces while placing the piston. |

Bedrock Edition:

| Name             | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                                                                                                    |
|------------------|---------------|---------------|----------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| facing_direction | 0x10x20x4     | 0             | 012345         | 012345                  | The direction the piston is pointing.0: facing down 1: facing up 2: facing south 3: facing north 4: facing east 5: facing west |

### Block data
A sticky piston has a block entity associated with it that holds additional data about the block.
Java Edition:

See also: Block entity format


 Block entity data
Tags common to all block entities
 blockState: The moving block represented by this block entity.
Block state
 extending: 1 or 0 (true/false) – true if the piston is extending instead of withdrawing.
 facing: Direction that the piston pushes (0=down, 1=up, 2=north, 3=south, 4=west, 5=east).
 progress: How far the block has been moved. Starts at 0.0, and increments by 0.5 each tick. If the value is 1.0 or higher at the start of a tick (before incrementing), then the block transforms into the stored blockState. Negative values can be used to increase the time until transformation.
 source: 1 or 0 (true/false) – true if the block represents the piston head itself, false if it represents a block being pushed.

Bedrock Edition:

See Bedrock Edition level format/Block entity format.
## See also
- Piston
- Slime block
- Redstone
- Tutorials/Piston uses
- Tutorials/Headless pistons
- Mechanics/Redstone/Piston circuits

## Notes

↑  Dragon eggs can be pushed, when in a falling state.

↑ In Java Edition, item frames are entities, 
not blocks. In Bedrock Edition, they are blocks.

↑ In Java Edition, if the "Fixed" NBT tag is set to "1", the item frame does not break when attempting to push it using a piston, but it still does not push. If the "Invulnerable" NBT tag is set to "1", the item frame breaks when pushed.

↑ Paintings are technically entities, not blocks.


