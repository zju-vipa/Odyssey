# Detector Rail
A detector rail is a type of rail that produces a redstone signal while a minecart is on it.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Chest loot
	- 1.3 Crafting
- 2 Usage
	- 2.1 Rail
	- 2.2 Redstone component
	- 2.3 Mob interaction
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 Video
- 6 History
	- 6.1 Data history
- 7 Issues
- 8 Gallery
	- 8.1 Screenshots
- 9 See also

## Obtaining
### Breaking
A detector rail can be broken fairly easily by hand, dropping itself as an item. It can be broken faster by using a pickaxe. 

| Block     | Detector Rail         |
|-----------|-----------------------|
| Hardness  | 0.7                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 1.05                  |
| Wooden    | 0.55                  |
| Stone     | 0.3                   |
| Iron      | 0.2                   |
| Diamond   | 0.15                  |
| Netherite | 0.15                  |
| Golden    | 0.1                   |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


A detector rail also drops as an item if:

- the block beneath it is removed
- waterorlavaflows over it‌[Java Edition  only]
- apistonmoves it into a space with no floor below it.

### Chest loot
| Item          | Structure | Container | Quantity | Chance                         |
|---------------|-----------|-----------|----------|--------------------------------|
|               |           |           |          | Java EditionandBedrock Edition |
| Detector Rail | Mineshaft | Chest     | 1–4      | 27.1%                          |

### Crafting
| Ingredients                                   | Crafting recipe |
|-----------------------------------------------|-----------------|
| Iron Ingot+Stone Pressure Plate+Redstone Dust | 6               |

## Usage
A detector rail can be used as a rail that can detect when minecarts are on it or how full container minecarts on it are.

To place a detector rail, use the Place Block control on the face of a block adjacent to the destination space.

A detector rail can be attached to:

- thetopof any full solidopaqueblock (stone, dirt, blocks of gold, etc.), including full-block mechanism components (command blocks,dispensers,droppers,note blocks, andredstone lamps)
- thetopof ahopper, upside-downslab, or upside-downstairs.

A detector rail cannot be attached to the side or bottom of any block, but attempting to make such an attachment may cause the detector rail to attach to the top of a block under the destination space. For example, if a fence is on the ground, attempting to attach a detector rail to the side of the fence causes the detector rail to be attached to the top of the ground next to the fence instead.

If updated while on an opened trapdoor, a detector rail (or other rails) breaks drops as an item. Placing a minecart on a detector rail on top of a closed and unpowered trapdoor opens the trapdoor and updates it, causing the detector rail to break. If the trapdoor is powered while the minecart is placed, the trapdoor does not open and the rail does not break. The minecart on the detector rail powers the trapdoor and keeps it closed even if the external power source is removed, allowing the detector rail to stay on.

When placed, a detector rail configures itself to line up with any adjacent rails (including activator rails, powered rails, and other detector rails), as well as adjacent rails one block up. If there are two adjacent rails on non-opposite sides, or three or more adjacent rails, a detector rail lines up in the east-west direction. If there are no adjacent rails, a detector rail lines up in the north-south direction (but if a rail is later placed to the east or west, the detector rail re-orients itself in the east-west direction even if it is already connected to another rail to the north or south). If a rail it would line up with is one block up, a detector rail slants upward toward it (with multiple options to slant upward to, a detector rail "prefers", in order: west, east, south, and north). Other configurations can be created by placing and removing various rails.

Mobs avoid walking across a detector rail (or other rails), but can be pushed onto them.

It cannot be placed suspended in midair, even with commands.[1]

### Rail
Main article: Rail
Detector rails (and other rails) act as "roads" for minecarts. A minecart that enters a detector rail's space from either end of the detector rail continues to move, losing only a little velocity (which can then be increased again with powered rails). A minecart that enters a detector rail's space from the side turns east or south (depending on the detector rail's orientation), or in the downward direction for a slanted detector rail.

### Redstone component
Example for signal strength of a full minecart (right) and a half-full one (left)
See also: Redstone circuit

A detector rail activates when any minecart is on it (even if only a portion of the minecart is on it), and deactivates when no minecarts are on it. The duration of the signal is always a multiple of 10 redstone ticks (although lag or unloading/reloading a chunk might affect this). While active, a detector rail:

- powers adjacentredstone dustand adjacentredstone repeatersfacing away from the detector rail, topower level15
- powers adjacentredstone comparatorsfacing away from the detector rail to a level corresponding to the fullness of the minecart if it is aminecart with chestor aMinecart with Hopper.
- strongly powers any full solid opaqueblockbeneath the detector rail to power level 15
- activates any adjacentmechanism components, including above or below, such aspistons,redstone lamps,powered rails,hoppers, etc.

Comparators give a signal for a minecart with chest or a minecart with hopper
If the minecart on the detector rail is a minecart with chest or minecart with hopper, an adjacent redstone comparator facing away from the detector rail outputs a power level proportional to the container's fullness, possibly power level 0. For any other type of minecart (including a regular minecart with a mob riding it) the comparator's output is zero.

A comparator can read the contents of a minecart with hopper or with chest on a detector rail through a solid opaque block, as it can with other container blocks.


### Mob interaction
Like other types of rails, spiders, cave spiders, and wardens are the only land mobs that can walk onto detector rails.

## Data values
### ID
Java Edition:

| Name          | Identifier    | Form         | Block tags                       | Item tags | Translation key               |
|---------------|---------------|--------------|----------------------------------|-----------|-------------------------------|
| Detector Rail | detector_rail | Block & Item | prevent_mob_spawning_insiderails | rails     | block.minecraft.detector_rail |

Bedrock Edition:

| Name          | Identifier    | Numeric ID | Form                       | Item ID[i 1]   | Translation key         |
|---------------|---------------|------------|----------------------------|----------------|-------------------------|
| Detector Rail | detector_rail | 28         | Block & Giveable Item[i 2] | Identical[i 3] | tile.detector_rail.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values                                             | Description                                                                                                                                     |
|-------------|---------------|------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| powered     | false         | falsetrue                                                  | True if rail is activated.                                                                                                                      |
| shape       | north_south   | east_westnorth_south                                       | Specifies the rail's orientation.                                                                                                               |
|             |               | ascending_eastascending_northascending_southascending_west | A rail that ascendstowardthe direction noted.For example, anascending_westrail is a straight rail that goes upward from the easttowardthe west. |
| waterlogged | false         | falsetrue                                                  | Whether or not there's water in the same place as this rail.                                                                                    |

Bedrock Edition:

| Name           | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                         |
|----------------|---------------|---------------|----------------|-------------------------|-------------------------------------|
| rail_data_bit  | 0x8           | false         | falsetrue      | 01                      | True if rail is activated.          |
| rail_direction | 0x10x20x4     | 0             | 0              | 0                       | flat track going north-south        |
|                |               |               | 1              | 1                       | flat track going east-west          |
|                |               |               | 2              | 2                       | sloped track ascending to the east  |
|                |               |               | 3              | 3                       | sloped track ascending to the west  |
|                |               |               | 4              | 4                       | sloped track ascending to the north |
|                |               |               | 5              | 5                       | sloped track ascending to the south |
|                |               |               | 6789           | Unsupported             | Unused                              |

## See also
- Rail
- Activator Rail
- Powered Rail

| Redstone circuits & tutorials |                                                                                                                                                      |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Redstone circuits             | Clock circuits Components Logic circuits Memory circuits Miscellaneous circuits Pulse circuits Transmission circuits                                 |
| Featured tutorials            | Advanced redstone circuits Block update detector (BUD) Comparator update detector (CUD) Mechanisms Piston circuits Quasi-connectivity Redstone music |

| Redstone components |                                                                                                                                                                                                                                                                                                                      |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Power               | Block of Redstone Buttons Wooden Stone Polished Blackstone Chiseled Bookshelf Daylight Detector Detector Rail Lectern Lever Lightning Rod Observer Pressure Plates Wooden Stone Polished Blackstone Heavy Weighted Light Weighted Redstone Torch Sculk Sensor Calibrated Target Trapped Chest Tripwire Hook Tripwire |
| Transmission        | Redstone Wire Redstone Comparator Redstone Repeater                                                                                                                                                                                                                                                                  |
| Mechanisms          | Bell Dropper Dispenser Doors Iron Wooden Fence Gates Hopper Jukebox Note Block Piston Sticky Rail Activator Powered Detector Redstone Lamp TNT Trapdoors Iron Wooden Command Block Structure Block                                                                                                                   |
| Other               | Block of Amethyst Minecart with Chest with Command Block with Furnace with Hopper with Monster Spawner with TNT Opaque and transparent blocks Movable and immovable blocks Slime Block and Honey Block                                                                                                               |
| Miscellaneous       | Redstone Ore Deepslate                                                                                                                                                                                                                                                                                               |
| Upcoming            | Copper Bulb Copper Door Copper Trapdoor Crafter                                                                                                                                                                                                                                                                      |
| Joke                | Etho Slab Pickaxe Block Place Block USB Charger Block Floatater                                                                                                                                                                                                                                                      |

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


↑ MC-182709 — resolved as "Invalid".


