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

