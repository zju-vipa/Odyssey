# Beacon
A beacon is a block that projects a beam skyward, and can provide beneficial status effects to players in a radius around it when placed on top of a solid pyramid base constructed from iron, gold, diamond, emerald or netherite blocks.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
- 2 Usage
	- 2.1 Activation
		- 2.1.1 Pyramids
	- 2.2 Beam
		- 2.2.1 Colors
	- 2.3 Powers
		- 2.3.1 Range
	- 2.4 Light source
	- 2.5 Piston interactivity
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block data
- 5 Achievements
- 6 Advancements
- 7 Video
- 8 History
- 9 Issues
- 10 Trivia
- 11 Gallery
	- 11.1 Renders
	- 11.2 Screenshots
	- 11.3 Development images
	- 11.4 In other media
- 12 References
- 13 See also

## Obtaining
### Breaking
A beacon can be mined successfully by hand or with any tool. When destroyed by an explosion, the block always drops as an item.

| Block    | Beacon              |
|----------|---------------------|
| Hardness | 3                   |
|          | Breakingtime (secs) |
| Default  | 4.5                 |

### Crafting
| Name   | Ingredients                | Crafting recipe |
|--------|----------------------------|-----------------|
| Beacon | Glass+Nether Star+Obsidian |                 |

## Usage
When "activated", beacon blocks provide two unique functions: 

- A landmark beam reaching into the sky, which can be visible from far away.
- Powers, which give players status effects within a certain range.

Additionally, in Bedrock Edition beacons can also be waterlogged and conduct redstone power at the same time.

### Activation
The beacon base can be made of the different mineral blocks combined.
In order to activate a beacon, the beacon must meet the following requirements:

- Beacons require an unobstructed view of the sky.Transparentblocks (glass, water, etc.) and bedrock (the nether ceiling)  are allowed.
- The beacon is on top of a pyramid constructed fromiron blocks,gold blocks,emerald blocks,diamond blocks, and/ornetherite blocks.

#### Pyramids
The four possible pyramid arrangements when using the beacon block. From left to right the pyramid structures decrease in complexity and strength.
Pyramids are the structures required to activate beacons. There are four possible pyramid heights. More pyramid levels make more powers available in a wider affected vicinity. The type of mineral block used to build the pyramid is entirely cosmetic and has no functional effect. Several different block types can be mixed without affecting functionality. If the pyramid is damaged so that the beacon deactivates, the previously-set powers resume their effects upon reactivation when the pyramid is repaired. This applies to piston-altered pyramids as well. 

| Level | Mineral blocks             | Materials                  | Layers                     |
|-------|----------------------------|----------------------------|----------------------------|
| 1     | 9                          | 81 (1 stack + 17 items)    | 3×3, beacon                |
| 2     | 34                         | 306 (4 stacks + 50 items)  | 5×5, 3×3, beacon           |
| 3     | 83 (1 stack + 19 blocks)   | 747 (11 stacks + 43 items) | 7×7, 5×5, 3×3, beacon      |
| 4     | 164 (2 stacks + 36 blocks) | 1476 (23 stacks + 4 items) | 9×9, 7×7, 5×5, 3×3, beacon |

This six-beacon pyramid provides all six effects from a single structure using the fewest mineral blocks possible.
Multiple beacons can make use of the same specific mineral blocks below them. Combined pyramids do not need to be symmetrical. The image to the right shows a 6-beacon (2 by 3) pyramid. It requires a total of 244 mineral blocks, with a base layer of 10 by 11.

| Level | Mineral blocks             | Materials                   | Layers                        |
|-------|----------------------------|-----------------------------|-------------------------------|
| 1     | 20                         | 180 (2 stacks + 52 items)   | 4×5, beacons                  |
| 2     | 62                         | 558 (8 stacks + 46 items)   | 6×7, 4×5, beacons             |
| 3     | 134 (2 stacks + 6 blocks)  | 1206 (18 stacks + 54 items) | 8×9, 6×7, 4×5, beacons        |
| 4     | 244 (3 stacks + 52 blocks) | 2196 (34 stacks + 20 items) | 10×11, 8×9, 6×7, 4×5, beacons |

### Beam
A vertical beam appears from a beacon if the beacon is activated, extending from the beacon block up to beyond the top of the world.

- InJava Edition, the beam is visible up to 256 blocks away.
- InBedrock Edition, the beam is visible up to 64 blocks away, regardless of how high the render distance is set.[1]

#### Colors
The color of the beam may be changed by placing blocks of stained glass or stained glass panes anywhere above the beacon block. The beam changes colors according to the colors of glass placed above it: the first block sets the beam color, while each additional block sets the color by averaging the red, green, and blue components of the current beam color and the block's color. The color values are the same as those for the corresponding dye. This also works using hardened stained glass and hardened stained glass panes.‌[Bedrock Edition and Minecraft Education  only] Stained glass panes have the same effect on the beam as stained glass blocks.

The resulting beam color can be found as C→=12n+1(c0→+∑i=1n2i−1ci→) where ci→ is the sequence of glass colors (c0→ corresponds to the lowest block and cn→ to the highest one).

Beacon beams cannot go through most blocks, but can go through bedrock (to allow beacons to be used in the Nether) and end portal frames.

Using just 15 colors of stained glass, It is possible to make all colors, for example; red + white stained glass above a beacon makes pink; in addition to this, the more white that is added, the lighter the color.

An interactive widget is being loaded. If this does not work for you, please reload the page or check if JavaScript is enabled.
### Powers
See also: Effect

The GUI shown when pressing use on the block.
Once the beacon is emitting a beam, it can then be fed one iron ingot, gold ingot, emerald, diamond, or netherite ingot to select the status effects given to players within range of the beacon. This is done through the beacon's GUI, displayed by pressing use while looking at the beacon block. It doesn't matter which of the items is fed into the beacon.

In the GUI, the player places the item to be fed in the empty slot and clicks an effect from the "Primary Power" section on the left. If the beacon is sitting on a 4-level pyramid, the "Secondary Power" section on the right also becomes active. The player can then choose either to turn on the Regeneration power in addition to the Primary Power or to raise the primary power to Level II. The user clicks the "Done" button (green checkmark), the item is consumed, and the power(s) become activated, with the outline of the effect on the HUD having a blue outline.‌[JE  only] To change the beacon's powers, this process must be followed again, consuming another ingot or gem.

If the pyramid is broken, effects deactivate or weaken depending on the level of the pyramid that is no longer complete. Upon restoration of the pyramid, the originally selected power returns without the need to spend another item.

The five primary powers are: 

- SpeedI: Increased movement speed.
- HasteI: Increased mining and attack speed.
- ResistanceI: Decreased nearly all incoming damage (2-level pyramid required).
- Jump BoostI: Increased jumping distance and height (2-level pyramid required).
- StrengthI: Increased melee damage (3-level pyramid required).

The secondary powers available with a 4-level pyramid are:

- RegenerationI: Regenerates health.
- Increasing the primary power to level II.

It is also possible to combine two different primary Level I powers:‌[Java Edition  only]

- select a primary power in the left panel
- select the Level II option in the right panel
- select the second desired power back in the left panel

Only one of the two powers appear to be selected, although both effects are active.[2]

Every four seconds, the selected powers are applied with a duration of 9 seconds, plus 2 seconds per pyramid level, to all players in range. Thus, when powers are changed or a player travels outside the area-of-effect, the powers persist for 5–9 seconds, or 13-17 seconds with a full pyramid.

#### Range
The beacon affects an area in the shape of a square column, which reaches downward and out to each side at a range determined by the size of the pyramid base (see table below), and upward a distance of that range + the height of this dimension blocks.

The effect duration from the beacon is also determined by the size of the pyramid base (9 + Pyramid size * 2).

The range of the beacon effect is limited by the simulation distance. As such, on simulation distance of 4 with a level 4 pyramid, the effect does not reach the chunks on the corners of the beacon range.

The distance from the player to the beacon block does not affect the intensity of the status effect.

| Pyramid size | Effect range(blocks) | Effect duration(seconds) |
|--------------|----------------------|--------------------------|
| 1 level      | 20                   | 11                       |
| 2 levels     | 30                   | 13                       |
| 3 levels     | 40                   | 15                       |
| 4 levels     | 50                   | 17                       |

### Light source
Beacon blocks can function as light sources, emitting a light level 15. Like other light sources, they melt snow and ice.

### Piston interactivity
Beacons cannot be pushed or pulled by pistons or sticky pistons.

## Data values
### ID
Java Edition:

| Name   | Identifier | Form         | Translation key        |
|--------|------------|--------------|------------------------|
| Beacon | beacon     | Block & Item | block.minecraft.beacon |

| Name         | Identifier |
|--------------|------------|
| Block entity | beacon     |

Bedrock Edition:

| Name   | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key  |
|--------|------------|------------|----------------------------|----------------|------------------|
| Beacon | beacon     | 138        | Block & Giveable Item[i 2] | Identical[i 3] | tile.beacon.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


| Name         | Savegame ID |
|--------------|-------------|
| Block entity | Beacon      |

### Block data
A beacon has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format


 Block entity data
Tags common to all block entities
 CustomName: Optional. The name of this beacon in JSON text component, which appears when attempting to open it, while it is locked.

 Lock: Optional. When not blank, prevents the container from being opened unless the opener is holding an item whose name matches this string.
 primary_effect: Optional. The primary effect selected, see Potion effects for resource locations. Cannot be set to an effect that beacons do not normally use. Although Regeneration cannot normally be chosen as the primary effect, setting this value to minecraft:regeneration works and even allows Regeneration II to be chosen as the secondary via the normal beacon GUI.
 secondary_effect: Optional. The secondary effect selected, see Potion effects for resource locations. Cannot be set to an effect that beacons do not normally use. When set without a primary effect, does nothing. When set to the same as the primary, the effect is given at level 2 (the normally available behavior for 5 effects). When set to a different value than the primary (normally only Regeneration), gives the effect at level 1.

Bedrock Edition:

See Bedrock Edition level format/Block entity format.
## See also
- Conduit
- Wither

| Natural       |                                                                                                                                                                                                                                                           |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Soil          | Clay Crimson Nylium Dirt Coarse Rooted Grass Block Gravel Mud Mycelium Podzol Sand Red Soul Sand Soul Soil Warped Nylium                                                                                                                                  |
| Stone         | Andesite Basalt Bedrock Blackstone Calcite Cobblestone Mossy Deepslate Diorite Pointed Dripstone Block End Stone Glowstone Granite Infested Block Magma Block Netherrack Obsidian Sandstone Red Stone Terracotta Stained Tuff                             |
| Ore/Mineral   | Amethyst Bud Cluster Ancient Debris Budding Amethyst Coal Ore Deepslate Copper Ore Deepslate Diamond Ore Deepslate Emerald Ore Deepslate Gold Ore Deepslate Nether Iron Ore Deepslate Lapis Lazuli Ore Deepslate Nether Quartz Ore Redstone Ore Deepslate |
| Fluid/Related | Bubble Column Ice Blue Packed Lava Snow Powder Block Water                                                                                                                                                                                                |
| Non-physical  | Air Cave‌[JE  only] Void‌[JE  only] Fire Soul                                                                                                                                                                                                             |

| Biota         |                                                                                                                                                                                                                                                                                                                                                                                                       |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Wood/Hypha    | Logs Stripped Wood Stripped Stems Stripped Hyphae Stripped                                                                                                                                                                                                                                                                                                                                            |
| Flower        | Allium Azure Bluet Blue Orchid Cornflower Dandelion Lilac Lily of the Valley Oxeye Daisy Peony Pitcher Plant Crop Poppy Rose Bush Sunflower Torchflower Crop Tulips Wither Rose                                                                                                                                                                                                                       |
| Plant         | Azalea Flowering Bamboo Shoot Block Stripped Beetroots Big Dripleaf Small Cactus Carrots Cave Vines Chorus Plant Flower Cocoa Dead Bush Fern Large Hanging Roots Leaves Lily Pad Mangrove Propagule Mangrove Roots Muddy Melon Stem Moss Block Carpet Pink Petals Potatoes Pumpkin Carved Stem Saplings Seagrass Tall Short Grass Tall Spore Blossom Sugar Cane Sweet Berry Bush Vines Wheat Hay Bale |
| Fungus        | Fungi Glow Lichen Mushrooms Blocks Stem Nether Sprouts Nether Wart Nether Wart Block Warped Crimson Roots Warped Roots Shroomlight Twisting Vines Weeping Vines                                                                                                                                                                                                                                       |
| Algae         | Kelp Dried Block                                                                                                                                                                                                                                                                                                                                                                                      |
| Fauna         | Coral Dead Coral Blocks Dead Coral Fans Dead Sea Pickle                                                                                                                                                                                                                                                                                                                                               |
| Fauna/Related | Bee Nest Bone Block Cobweb Dragon Egg Frogspawn Sniffer Egg Turtle Egg                                                                                                                                                                                                                                                                                                                                |
| Sculk         | Sculk Sculk Catalyst Sculk Sensor Calibrated Sculk Shrieker Sculk Vein                                                                                                                                                                                                                                                                                                                                |

| Building      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Lighting      | Candle Dyed End Rod Froglight Jack o'Lantern Lantern Soul Sea Lantern Torch Soul                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Ornamental    | Bamboo Mosaic Bookshelf Carpets Chain Crying Obsidian Fences Wooden Nether Brick Iron Bars Gilded Blackstone Glass Pane Tinted Stained Glass Pane Glazed Terracotta Honeycomb Block Slabs Cut Copper Wooden Stairs Cut Copper Wooden Walls Wool                                                                                                                                                                                                                                                                                                                                                                |
| Mineral Block | Block of Amethyst Block of Coal Block of Copper Cut Raw Block of Diamond Block of Emerald Block of Gold Raw Block of Iron Raw Block of Lapis Lazuli Block of Netherite Block of Quartz Bricks Chiseled Pillar Smooth Block of RedstoneUpcoming   Chiseled Copper Copper Grate                                                                                                                                                                                                                                                                                                                                  |
| Upcoming      | Chiseled Copper Copper Grate                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Structural    | Bricks Cobbled Deepslate Concrete Powder Cut Sandstone Chiseled Smooth Cut Red Sandstone Chiseled Smooth Deepslate Bricks Cracked Deepslate Tiles Cracked Dirt Path End Stone Bricks Nether Bricks Chiseled Cracked Red Packed Mud Mud Bricks Planks Polished Andesite Polished Basalt Smooth Basalt Polished Blackstone Chiseled Polished Blackstone Bricks Cracked Polished Diorite Polished Granite Polished Deepslate Chiseled Prismarine Bricks Dark Purpur Block Pillar Reinforced Deepslate Smooth Stone Stone Bricks Chiseled Cracked MossyUpcoming   Chiseled Tuff Polished Tuff Tuff Bricks Chiseled |
| Upcoming      | Chiseled Tuff Polished Tuff Tuff Bricks Chiseled                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| BE&eduonly    | Colored Torches Elements Hardened Glass Pane Hardened Stained Glass Pane                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

| Upcoming | Chiseled Copper Copper Grate |
|----------|------------------------------|

| Upcoming | Chiseled Tuff Polished Tuff Tuff Bricks Chiseled |
|----------|--------------------------------------------------|

| Utility                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Interactable            | Anvil Chipped Damaged Barrel Beacon Brewing Stand Cartography Table Chest Ender Crafting Table Enchanting Table Furnace Blast Smoker Grindstone Lectern Loom Shulker Box Dyed Sign Hanging Smithing Table Stonecutter                                                                                                                                                                                                                                                                                        |
| Utilizable              | Banners Ominous Beehive Beds Bell Cake with Candle Campfire Soul Cauldron Lava Powder Snow Water Chiseled Bookshelf Composter Conduit Decorated Pot End Gateway End Portal End Portal Frame Farmland Fletching Table Flower Pot Frosted Ice Heads Skeleton Wither Skeleton Zombie Creeper Piglin Dragon Jukebox Ladder Lodestone Monster Spawner Nether Portal Respawn Anchor Scaffolding Sponge Wet Suspicious Gravel Suspicious Sand TNTUpcoming   Heavy Core Trial Spawner Ominous Vault Ominous          |
| Upcoming                | Heavy Core Trial Spawner Ominous Vault Ominous                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Redstone/Mechanical     | Buttons Wooden Stone Polished Blackstone Daylight Detector Dispenser Dropper Doors Iron Wooden Honey Block Hopper Lever Lightning Rod Note Block Observer Piston Sticky Head Moving Pressure Plates Wooden Stone Polished Blackstone Heavy Weighted Light Weighted Rail Activator Detector Powered Redstone Lamp Redstone Wire Comparator Repeater Torch Slime Block Target Trapped Chest Trapdoors Iron Wooden Fence Gates Tripwire Hook TripwireUpcoming   Copper Bulb Copper Door Copper Trapdoor Crafter |
| Upcoming                | Copper Bulb Copper Door Copper Trapdoor Crafter                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Minecraft Educationonly | Chalkboard                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| BE&eduonly              | Allow Border Compound Creator Deny Element Constructor Heat Block Item Frame Glow Lab Table Material Reducer Underwater TNT Underwater Torch                                                                                                                                                                                                                                                                                                                                                                 |

| Upcoming | Heavy Core Trial Spawner Ominous Vault Ominous |
|----------|------------------------------------------------|

| Upcoming | Copper Bulb Copper Door Copper Trapdoor Crafter |
|----------|-------------------------------------------------|

| Creative or commands only |                                                                                                                            |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------|
| All editions              | Barrier Command Block Chain Repeating Jigsaw Block  Light Petrified Oak Slab Player Head Structure Block Void Unstable TNT |
| BE&eduonly                | Structure Air                                                                                                              |
| China Editiononly         | mod_ore                                                                                                                    |

| Unimplemented |                                                                                                                                             |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| All editions  | Branches Copper Button Colored Wood Planks Coral Slab Dirt Slab Empty Barrel Fish Barrel Furniture Paeonia  Sculk Jaw Spike Block Wax Block |

| Unused              |                                                                                                                                                                                                                                                 |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bedrock Editiononly | Camera   Chalkboard                                                                                                                                                                                                                             |
| BE&eduonly          | Broken Anvil Chiseled Purpur tile.client_request_placeholder_block.name Glowing Obsidian info_update info_update2 Invisible Bedrock   Nether Reactor Core tile.purpur_block.smooth.name reserved6 Smooth Stone Bricks Stonecutter (old) Unknown |

| Joke features    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| April Fools 2013 | Block of Coal Etho Slab Tinted Glass Torch (Burnt-out)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| April Fools 2016 | USB Charger Block                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| April Fools 2020 | An Ant Box of Infinite Books Cursor Funky Portal Leftover Swaggiest stairs ever                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| April Fools 2022 | How did we get here?                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| April Fools 2023 | Cheese Copper Sink Copper Spleaves Golden Chest Other Portal Packed Air Pickaxe Block Place Block                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| April Fools 2024 | Baked Potato Bricks Expired Charred Big Brain Block of Amber Block of Potato Peels Corrupted Compressed Poisonous Potato Block Double Triple Quadruple Floatater Floatato Frying Table Gravtater Pedestal Peelgrass Block Corrupted Poison Farmland Poison Path Poisonous Mashed Potato Poisonous Potato Block Poisonous Potato Cutter Poisonous Potato Head Block Poisonous Potato Headpiece Poisonous Potato Ore Deepslate Potato Battery Potato Bud Potato flower Potato Fruit Potato Leaves Potato Pedicule Potato Portal Potato Refinery Potato Sprouts Potato Stem Planks Slab Stairs Door Trapdoor Button Pressure Plate Sign Hanging Sign Fence Fence Gate Potone Copper Ore Diamond Ore Gold Ore Iron Ore Lapis Lazuli Ore Redstone Ore Resin Ore Powerful Potato Strong Roots Taterstone Terre de Pomme Vicious Potato Weak Roots |

| Removed                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| All editions               | Grassless Dirt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Java Editiononly           | Cloth Dead Coral Block Gear Lava Spawner Locked chest Rose Potted Shrub Water Spawner                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Bedrock Editiononly        | Blue Rose grass_carried leaves_carriedUpcoming   Fern Fern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Upcoming                   | Fern Fern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| MinecraftEduonly           | Big Sign Border block Build allow block Build disallow block Foundation block Home Block Information block Information Sign Number Block Spawn Block Teleport Block                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Legacy Console Editiononly | Ring Block                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                            | Extreme metadata variants   All editions   Directionless Hopper Seamless Stone Slab Six-sided Hay Bale   Six-sided Piston   Java Edition only   Faceless Furnace Faceless Jack o'Lantern Green Shrub Potted Inaccessible "Boring" Blocks Invisible stairs Misaligned torch Redstone Nether portal post Overripe Melon Stem Attached Overripe Pumpkin Stem Attached Overgrown Cocoa Overeaten Cake Overgrown Wheat Potted non-flower block Snowy Dirt Coarse  Strange buttons   Bedrock Edition only   Bell Stand Diorite Bell Granite Bell Polished Six-sided Bone Block Six-sided Purpur Pillar Six-sided Quartz Pillar Smokeless Campfire |
|                            | Extreme metadata variants                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| All editions               | Directionless Hopper Seamless Stone Slab Six-sided Hay Bale   Six-sided Piston                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Java Editiononly           | Faceless Furnace Faceless Jack o'Lantern Green Shrub Potted Inaccessible "Boring" Blocks Invisible stairs Misaligned torch Redstone Nether portal post Overripe Melon Stem Attached Overripe Pumpkin Stem Attached Overgrown Cocoa Overeaten Cake Overgrown Wheat Potted non-flower block Snowy Dirt Coarse  Strange buttons                                                                                                                                                                                                                                                                                                                |
| Bedrock Editiononly        | Bell Stand Diorite Bell Granite Bell Polished Six-sided Bone Block Six-sided Purpur Pillar Six-sided Quartz Pillar Smokeless Campfire                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

| Upcoming | Fern Fern |
|----------|-----------|

| Extreme metadata variants |                                                                                                                                                                                                                                                                                                                              |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| All editions              | Directionless Hopper Seamless Stone Slab Six-sided Hay Bale   Six-sided Piston                                                                                                                                                                                                                                               |
| Java Editiononly          | Faceless Furnace Faceless Jack o'Lantern Green Shrub Potted Inaccessible "Boring" Blocks Invisible stairs Misaligned torch Redstone Nether portal post Overripe Melon Stem Attached Overripe Pumpkin Stem Attached Overgrown Cocoa Overeaten Cake Overgrown Wheat Potted non-flower block Snowy Dirt Coarse  Strange buttons |
| Bedrock Editiononly       | Bell Stand Diorite Bell Granite Bell Polished Six-sided Bone Block Six-sided Purpur Pillar Six-sided Quartz Pillar Smokeless Campfire                                                                                                                                                                                        |

| Java Edition only | Amplified Single biome Debug mode Large Biomes |
|-------------------|------------------------------------------------|

| Java Edition only   | Custom Map theme Map shape Map type Level previewer Old Customized Winter mode |
|---------------------|--------------------------------------------------------------------------------|
| Bedrock Editiononly | Old Nether Reactor                                                             |

