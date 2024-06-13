# Piston
A piston is a block capable of pushing most entities and blocks when given a redstone signal. 

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Redstone component
		- 2.2.1 Start delay
	- 2.3 Limitations
		- 2.3.1 Exceptions
	- 2.4 Powering pistons
	- 2.5 Slime blocks and honey blocks
- 3 Technical components
- 4 Sounds
	- 4.1 Generic
	- 4.2 Unique
- 5 Data values
	- 5.1 ID
	- 5.2 Block states
	- 5.3 Block data
- 6 Achievements
- 7 Video
- 8 History
	- 8.1 Data history
- 9 Issues
- 10 Trivia
- 11 Gallery
	- 11.1 Screenshots
	- 11.2 Concept artwork
	- 11.3 In other media
- 12 See also
- 13 Notes
- 14 References
- 15 External links

## Obtaining
### Breaking
A piston can be broken using any tool with equal efficiency, and always drops itself.
In Java Edition, it is faster to break them with a pickaxe. The pickaxe is also the preferred tool for breaking the head when extended.[1]

| Block     | Piston                |
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


### Crafting
| Ingredients                                    | Crafting recipe |
|------------------------------------------------|-----------------|
| AnyPlanks+Cobblestone+Iron Ingot+Redstone Dust |                 |

## Usage
See also: Tutorials/Piston uses and Mechanics/Redstone/Piston circuits

### Crafting ingredient
| Ingredients      | Crafting recipe |
|------------------|-----------------|
| Slimeball+Piston |                 |

### Redstone component
Pistons are always placed facing toward the player. When powered, the piston's wooden surface (the "head") tries to start extending after start delay. When it extends, it pushes at most 12 blocks. The piston makes a sound that can be heard within a 31×31×31 cube centered on the activating piston. Any entities in the path of the extending head are pushed with the blocks. If there is no place for the entities to go, the block pushes inside them, suffocating mobs if the block is not transparent when pushed into the eye height of the mob.

When a piston loses power, its head retracts. Like extending, this retraction starts after start delay. It finishes retracting 2 game ticks (1 redstone tick; 0.1 seconds) after it starts. 

A piston that pushes a slime block bounces any entity that it displaces in the direction the piston is facing. In addition, when a slime block is moved by a piston, any movable blocks adjacent (not diagonally) to the slime block also moves. See the #Slime blocks and honey blocks section below for more details.

In Bedrock Edition, blocks that stick to walls (such as levers) can be placed on pistons without being destroyed when activated.

#### Start delay
A piston won't extend or retract immediately when it is activated: this is called start delay.

In Bedrock Edition, the start delay is fixed at 2 game ticks (1 redstone tick; 0.1 seconds), meaning that the piston starts to extend or retract 2gt after it's activated.

In Java Edition, the start delay can be 0 game ticks (0 redstone ticks; 0 seconds) (start at the same tick) or 1 game tick (0.5 redstone ticks; 0.05 seconds) (start at the next tick) depending on the game process when the piston is activated:

- If the piston is updated and activated in thescheduled tickstage,random tickstage or block event stage, the piston stage is executed in this game tick's block event stage. At this time, the start delay is 0gt, which means the piston starts at the same tick.
- If the piston is activated during the execution of entity or tile entity, or activated by player actions, the piston stage is executed in the next game tick's block event stage. At this time, the start delay is 1gt, which means the piston starts at the next tick.

### Limitations
Pistons can push most blocks except those listed in the table below. 

Pistons cannot push blocks into the void or beyond the top of the map. They also cannot push more than 12 blocks. If the requirements for a block to be pushed are not met, the piston simply does not extend.

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

