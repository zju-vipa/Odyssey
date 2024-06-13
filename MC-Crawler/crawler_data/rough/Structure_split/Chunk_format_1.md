## Block format
In the Anvil format, block positions are ordered YZX for compression purposes.

The coordinate system is as follows:

- Xincreases East, decreases West
- Yincreases upward, decreases downward
- Zincreases South, decreases North

This means indices are ordered like in a book, with its top to the North, read from beneath and with words written backward: each letter is a different X-index, each line a Z-index, and each page a Y-index. In case of a flat 2D array, the Y-index is omitted, and the array reads like a single page.


Each section is a 16×16×16-block area, with up to 16 sections in a chunk : from 0 at the bottom, to 15 on top. Empty sections are not saved. Each section has a "Y" byte for its Y-index (0 to 15), a "Palette" list linking IDs to block states, and a "BlockStates" long array storing the IDs per block location, compressed by fitting multiple IDs inside each entry (see NBT_structure above for details on the compression). There might be an additional section at the top and or bottom of the world used to store light, so that light travels properly over and under the world limits.

The pseudo-code below shows how to access individual block information from a single section.

byte Nibble4(byte[] arr, int index){
	return index%2 == 0 ? arr[index/2]&0x0F : (arr[index/2]>>4)&0x0F;
}
int BlockPos = y*16*16 + z*16 + x; 
compound Block = Palette[change_array_element_size(BlockStates,Log2(length(Palette)))[BlockPos]];
string BlockName = Block.Name; 
compound BlockState = Block.Properties; 
byte Blocklight = Nibble4(BlockLight, BlockPos); 
byte Skylight = Nibble4(SkyLight, BlockPos);

## Block entity format
| Block Entities         |                         |
|------------------------|-------------------------|
| Block Entity ID        | Associated Block        |
| banner                 | Banner                  |
| barrel                 | Barrel                  |
| beacon                 | Beacon                  |
| bed                    | Bed                     |
| beehive                | Bee nest/beehive        |
| bell                   | Bell                    |
| blast_furnace          | Blast Furnace           |
| brewing_stand          | Brewing Stand           |
| calbrated_sculk_sensor | Calibrated Sculk Sensor |
| campfire               | Campfire                |
| chest                  | Chest                   |
| chiseled_bookshelf     | Chiseled Bookshelf      |
| comparator             | Redstone Comparator     |
| command_block          | Command Block           |
| conduit                | Conduit                 |
| crafter                | Crafter                 |
| daylight_detector      | Daylight Detector       |
| decorated_pot          | Decorated Pot           |
| dispenser              | Dispenser               |
| dropper                | Dropper                 |
| enchanting_table       | Enchanting Table        |
| ender_chest            | Ender Chest             |
| end_gateway            | End Gateway             |
| end_portal             | End Portal              |
| furnace                | Furnace                 |
| hanging_sign           | Hanging Sign            |
| hopper                 | Hopper                  |
| jigsaw                 | Jigsaw Block            |
| jukebox                | Jukebox                 |
| lectern                | Lectern                 |
| mob_spawner            | Monster Spawner         |
| piston                 | Moving Piston           |
| shulker_box            | Shulker Box             |
| sign                   | Sign                    |
| skull                  | Mob head                |
| sculk_catalyst         | Sculk Catalyst          |
| sculk_sensor           | Sculk Sensor            |
| sculk_shrieker         | Sculk Shrieker          |
| smoker                 | Smoker                  |
| soul_campfire          | Soul Campfire           |
| structure_block        | Structure Block         |
| suspicious_gravel      | Suspicious Gravel       |
| suspicious_sand        | Suspicious Sand         |
| trapped_chest          | Trapped Chest           |
| trial_spawner          | Trial Spawner           |
| vault                  | Vault                   |

A block entity (not related to entity) is used by Minecraft to store information about a block that can't be stored in the block's block states. Block entities were called "tile entities" until the 1.18 snapshots and that term is still used in some command usage.


banners



 Block entity data
Tags common to all block entities
 CustomName: Optional. The name of this banner in JSON text component, which is used for showing the banner on a map.
 Patterns: List of all patterns applied to the banner.
: An individual pattern.
 Color: Color of the section.
 Pattern: The banner pattern code the color is applied to.


Pattern color
Main article: Banner/DV[edit]


Pattern
Main article: Banner/Patterns[edit]




barrel



 Block entity data
Tags common to all block entities

 CustomName: Optional. The name of this container in JSON text component, which appears in its GUI where the default name ordinarily appears.
 Items: List of items in the container.
: An item, including the slot tag. Barrel slots are numbered 0-26, 0 starts in the top left corner.
Tags common to all items

 Lock: Optional. When not blank, prevents the container from being opened unless the opener is holding an item whose name matches this string.

 LootTable: Optional. Name of the loot table to use. If this is used in a chest-like container, the loot table generates its content when it is opened. Generating the items in the container removes both loot table tags ( LootTable and  LootTableSeed).
 LootTableSeed: Optional. Seed for generating the loot table. The default value works similarly to the seeds for worlds, where value of 0 or an omitted value causes the game to use a random seed.




beacon



 Block entity data
Tags common to all block entities
 CustomName: Optional. The name of this beacon in JSON text component, which appears when attempting to open it, while it is locked.

 Lock: Optional. When not blank, prevents the container from being opened unless the opener is holding an item whose name matches this string.
 primary_effect: Optional. The primary effect selected, see Potion effects for resource locations. Cannot be set to an effect that beacons do not normally use. Although Regeneration cannot normally be chosen as the primary effect, setting this value to minecraft:regeneration works and even allows Regeneration II to be chosen as the secondary via the normal beacon GUI.
 secondary_effect: Optional. The secondary effect selected, see Potion effects for resource locations. Cannot be set to an effect that beacons do not normally use. When set without a primary effect, does nothing. When set to the same as the primary, the effect is given at level 2 (the normally available behavior for 5 effects). When set to a different value than the primary (normally only Regeneration), gives the effect at level 1.




bed



 Block entity data
Tags common to all block entities




beehive



 Block entity data
Tags common to all block entities
 Bees: Entities currently in the hive.
 An entity in the hive.
 EntityData: The NBT data of the entity in the hive.
See entity format.
 MinOccupationTicks: The minimum amount of time in ticks for this entity to stay in the hive.
 TicksInHive: The amount of ticks the entity has stayed in the hive.
 FlowerPos: Stores the location of a flower, so other bees can go to it.
 X: X coordinate of the flower.
 Y: Y coordinate of the flower.
 Z: Z coordinate of the flower.




bell



 Block entity data
Tags common to all block entities




blast_furnace



 Block entity data
Tags common to all block entities
 BurnTime: Number of ticks left before the current fuel runs out.
 CookTime: Number of ticks the item has been smelting for. The item finishes smelting when this value reaches 200 (10 seconds). Is reset to 0 if BurnTime reaches 0.
 CookTimeTotal: Number of ticks It takes for the item to be smelted.

 CustomName: Optional. The name of this container in JSON text component, which appears in its GUI where the default name ordinarily appears.
 Items: List of items in this container.
: An item in the blast furnace, including the slot tag:Slot 0: The item(s) being smelted.Slot 1: The item(s) to use as the next fuel source.Slot 2: The item(s) in the result slot.
Tags common to all items

 Lock: Optional. When not blank, prevents the container from being opened unless the opener is holding an item whose name matches this string.
 RecipesUsed: Recipes that have been used since the last time a recipe result item was manually removed from the GUI. Used to calculate experience given to the player when taking out the resulting item.
 recipe ID: How many times this specific recipe has been used. The recipe ID is the identifier of the smelting recipe, as a resource location, as used in the /recipe command.




brewing_stand



 Block entity data
Tags common to all block entities
 BrewTime: The number of ticks the potions have to brew.

 CustomName: Optional. The name of this container in JSON text component, which appears in its GUI where the default name ordinarily appears.
 Fuel: Remaining fuel for the brewing stand. 20 when full, and counts down by 1 each time a potion is brewed.
 Items: List of items in this container.
: An item in the brewing stand, including the slot tag:Slot 0: Left potion slot.Slot 1: Middle potion slot.Slot 2: Right potion slot.Slot 3: Where the potion ingredient goes. Slot 4: Fuel (Blaze Powder).
Tags common to all items

 Lock: Optional. When not blank, prevents the container from being opened unless the opener is holding an item whose name matches this string.




calibrated_sculk_sensor



: Block entity data.
Tags common to all block entities
 last_vibration_frequency: The frequency of the last vibration.
 listener: The vibration event listener for this sculk shrieker, sculk sensor, or calibrated sculk sensor.
 event: Only exists if there is an incoming vibration.
 distance: The distance between this vibration's source and the block.
 game_event: The resource location of the vibration event that caused the current incoming vibration.
 pos: The coordinates of the source of this vibration.
: X coordinate.
: Y coordinate.
: Z coordinate.
 projectile_owner: If the vibration was caused by a projectile, this is the UUID of the entity that launched the projectile. Does not exist if vibration was not caused by a projectile.
 source: The UUID of the entity that caused the vibration. Does not exist if vibration was not caused by an entity.
 event_delay: How many ticks remain until triggered by the vibration. Set to 0 if there is no incoming vibration
 selector: The data of the vibration selector.[more information needed]
 tick: The game time when the vibration occurs, or -1 if there is no vibration to choose from.[more information needed]
 event: Candidate game event, with the same structure as the  event tag above.[more information needed]




campfire



 Block entity data
Tags common to all block entities
 CookingTimes: How long each item has been cooking, first index is slot 0, etc.
 CookingTotalTimes: How long each item has to cook, first index is slot 0, etc.
 Items: List of up to 4 items currently cooking.
Tags common to all items




chiseled_bookshelf



 Block entity data
Tags common to all block entities
 Items: List of books in the bookshelf.
: An item, including the slot tag. The valid slot numbers are 0-5.
Tags common to all items
 last_interacted_slot: Last interacted slot (0–5), or -1 if no slot has been interacted with yet.




chest



 Block entity data
Tags common to all block entities
Tags common to all objects that can be renamed
 Items: List of items in this container.
: An item, including the slot tag. Chest slots are numbered 0-26, 0 starts in the top left corner.
Tags common to all items
Tags common to all containers that can be locked
Tags common to all objects that use loot tables to produce items
 gold: Exists only in the april fools snapshot 23w13a_or_b. Optional. When set to anything but 0, turns the chest into a golden chest.




comparator



 Block entity data
Tags common to all block entities
 OutputSignal: Represents the strength of the analog signal output of this redstone comparator.




command_block



 Block entity data
Tags common to all block entities
 auto: 1 or 0 (true/false) - Allows to activate the command without the requirement of a redstone signal.
 Command: The command to issue to the server.
 conditionMet: 1 or 0 (true/false) - Indicates whether a conditional command block had its condition met when last activated. True if not a conditional command block.
 CustomName: Optional. The name JSON text component of this command block, replacing the usual '@' when using commands such as /say and /tell.
 LastExecution: stores the tick a chain command block was last executed in.
 LastOutput: The last line of output generated by the command block. Still stored even if the game rule commandBlockOutput is false. Appears in the GUI of the block when right-clicked, and includes a timestamp of when the output was produced.
 powered: 1 or 0 (true/false) - States whether or not the command block is powered by redstone or not.
 SuccessCount: Represents the strength of the analog signal output by redstone comparators attached to this command block.
 TrackOutput: 1 or 0 (true/false) - Determines whether the LastOutput is stored. Can be toggled in the GUI by clicking a button near the "Previous Output" textbox. Caption on the button indicates current state: "O" if true, "X" if false.
 UpdateLastExecution: 1 or 0 (true/false) - Defaults to true. If set to false, loops can be created where the same command block can run multiple times in one tick.




conduit



 Block entity data
Tags common to all block entities
 Target: The UUID of the hostile mob the conduit is currently attacking, stored as four ints. May not be present.




crafter



 Block entity data
Tags common to all block entities
 crafting_ticks_remaining: Set to 6 when the crafter crafts something.[more information needed]
 triggered: Set to 1 when it is powered. It is otherwise 0.
 disabled_slots: Indexes of slots that are disabled.
 Items: List of items in this container.
: An item in the crafter, including the slot tag. Crafter slots are numbered 0-8. 0 starts in the top left corner.
Tags common to all items

 Lock: Optional. When not blank, prevents the container from being opened unless the opener is holding an item whose name matches this string.

 LootTable: Optional. Name of the loot table to use. If this is used in a chest-like container, the loot table generates its content when it is opened. Generating the items in the container removes both loot table tags ( LootTable and  LootTableSeed).
 LootTableSeed: Optional. Seed for generating the loot table. The default value works similarly to the seeds for worlds, where value of 0 or an omitted value causes the game to use a random seed.




daylight_detector



 Block entity data
Tags common to all block entities




decorated_pot



 Block entity data
Tags common to all block entities
 sherds: List of sherds on this decorated pot.
: Item ID of this face. Each value defaults to bricks's ID, and can be either a brick or any sherd.
 item: The item stored within the pot. A decorated pot does not use  Slot to describe its contents, even though it functionally has 1 item slot.
Tags common to all items
Tags common to all objects that use loot tables to produce items




dispenser



 Block entity data
Tags common to all block entities
Tags common to all objects that can be renamed
 Items: List of items in this container.
: An item, including the slot tag. Dispenser slots are numbered 0-8 with 0 in the top left corner.
Tags common to all items
Tags common to all containers that can be locked
Tags common to all objects that use loot tables to produce items




dropper



 Block entity data
Tags common to all block entities
Tags common to all objects that can be renamed
 Items: List of items in this container.
: An item, including the slot tag. Dropper slots are numbered 0-8 with 0 in the top left corner.
Tags common to all items
Tags common to all containers that can be locked
Tags common to all objects that use loot tables to produce items
 Lunar: Exists only in the april fools snapshot 23w13a_or_b. Optional. When set to any full number from -128 to 127, turns it to a lunar base dropper, and placing light or heavy pressure plate on top of it creates the lunar base structure.




enchanting_table



 Block entity data
Tags common to all block entities

 CustomName: Optional. The name of this container in JSON text component, which appears in its GUI where the default name ordinarily appears.




ender_chest



 Block entity data
Tags common to all block entities




end_gateway



 Block entity data
Tags common to all block entities
 Age: Age of the portal, in ticks. This is used to determine when the beam is rendered.
 ExactTeleport: 1 or 0 (true/false) - Teleports entities directly to the ExitPortal coordinates instead of near them.
 ExitPortal: Location entities are teleported to when entering the portal.
 X: X coordinate of target location.
 Y: Y coordinate of target location.
 Z: Z coordinate of target location.




end_portal



 Block entity data
Tags common to all block entities




furnace



 Block entity data
Tags common to all block entities
 BurnTime: Number of ticks left before the current fuel runs out.
 CookTime: Number of ticks the item has been smelting for. The item finishes smelting when this value reaches 200 (10 seconds). Is reset to 0 if BurnTime reaches 0.
 CookTimeTotal: Number of ticks It takes for the item to be smelted.
Tags common to all objects that can be renamed
 Items: List of items in this container.
: An item in the furnace, including the slot tag:Slot 0: The item(s) being smelted.Slot 1: The item(s) to use as the next fuel source.Slot 2: The item(s) in the result slot.
Tags common to all items
Tags common to all containers that can be locked
 RecipesUsed: Which recipes have been used since the last time a recipe result item was manually removed from the GUI. Used to calculate experience given to the player when taking out the resulting item.
 recipe ID: How many times this specific recipe has been used. The recipe ID is the identifier of the smelting recipe, as a resource location, as used in the /recipe command.




hanging_sign



 Block entity data
Tags common to all block entities
 is_waxed: 1 or 0 (true/false) - true if the text is locked with honeycomb.
 front_text: A compound that discribes front text.
 has_glowing_text: 1 or 0 (true/false) - true if the sign has been dyed with a glow ink sac.
 color: The color that has been used to dye the sign. The default value is black One of white, orange, magenta, light_blue, yellow, lime, pink, gray, light_gray, cyan, purple, blue, brown, green, red, and black.
 filtered_messages: Only in Realms. The lines of text shown to players with the profanity filter turned on instead of the regular lines. This tag is automatically set to "" for lines containing blocked words and to the line's normal contents for the other lines when a player with the profanity filter turned off edits the sign, so players with the filter on cannot see the blocked words. If a player with the filter on tries to use blocked words in one or more lines, the line(s) in  messages containing blocked words are set to "", which makes them render completely blank, and this tag is also given the same contents. If multiple lines have been edited before the sign editing GUI is closed, only the lines containing blocked words are blanked.
 messages: A list of text for each line.
: Text for each line. Must be Raw JSON text format.
 back_text: A compound that discribes back text.　The same structure as  front_text.

The character limit for the Text tags depends on the width of the characters. Although the Text tags are string objects, they should contain JSON text, which are evaluated as compound objects. 




hopper



 Block entity data
Tags common to all block entities
Tags common to all objects that can be renamed
 Items: List of items in this container.
: An item, including the slot tag.
Tags common to all items
Tags common to all containers that can be locked
Tags common to all objects that use loot tables to produce items
 TransferCooldown: Time until the next transfer in game ticks, naturally between 1 and 8 or 0 if there is no transfer.




jigsaw



 Block entity data
Tags common to all block entities
 final_state: The block that this jigsaw block becomes.
 joint: The joint option value, either "rollable" or "aligned".
 name: The jigsaw block's name. This jigsaw block gets aligned with another structure's jigsaw block that has this value in the target tag.
 pool: The jigsaw block's target pool to select a structure from.
 target: The jigsaw block's target name. This jigsaw block gets aligned with another structure's jigsaw block that has this value in the name tag.
 selection_priority: Priority of this jigsaw block being selected for generation. Jigsaw blocks with higher selection priority get selected first.
 placement_priority: Priority of the piece generated by this jigsaw block to place its children. Pieces with higher placement priority generate their children first.




jukebox



 Block entity data
Tags common to all block entities
 IsPlaying: Whether the record is currently playing.
 RecordItem: The item, without the Slot tag.
Tags common to all items
 RecordStartTick: Value of TickCount when the record started playing.
 TickCount: Count of the number of record-playing ticks this jukebox has processed. Increments only while a record is loaded, whether playing or not.




lectern



 Block entity data
Tags common to all block entities
 Book: The book item, without the slot tag, currently on the lectern, may not exist.
Tags common to all items
 Page: The page the book is currently on, starting from 0, does not exist if there's no book. Value is clamped between 0 and the last page - 1.




mob_spawner



 Block entity data
Tags common to all block entities
Tags common to monster spawner and minecart with monster spawner




piston



 Block entity data
Tags common to all block entities
 blockState: The moving block represented by this block entity.
Block state
 extending: 1 or 0 (true/false) – true if the piston is extending instead of withdrawing.
 facing: Direction that the piston pushes (0=down, 1=up, 2=north, 3=south, 4=west, 5=east).
 progress: How far the block has been moved. Starts at 0.0, and increments by 0.5 each tick. If the value is 1.0 or higher at the start of a tick (before incrementing), then the block transforms into the stored blockState. Negative values can be used to increase the time until transformation.
 source: 1 or 0 (true/false) – true if the block represents the piston head itself, false if it represents a block being pushed.




sculk_catalyst



 Block entity data
Tags common to all block entities
 cursors: List of sculk charge clusters associated with the sculk catalyst.
: A sculk charge cluster. Each cluster is stored within a single sculk block.
 charge: How many sculk charges are being carried in the cluster.
 pos: List of three integers representing the coordinates of the cluster.
 decay_delay: 1 or 0 (true/false) - Not to be confused with update_delay. This controls the decay of the cluster. If this is true, then the cluster was spread from a sculk block or sculk vein, and this cluster can only spread to sculk, sculk veins, and blocks with the  sculk_replaceable tag set to true. If this is false, then all the sculk charges disappear when the cluster discharges to a block that is not in the sculk family.
 update_delay: Delay in game ticks until the cluster begins to discharge (or travel) after being created. Usually starts at 1 game tick when a cluster discharges to a new block.
 facings: If the block to replace is an air or water block, the block is replaced with sculk veins, and the faces where the sculk veins are placed are also stored in their block state. The sculk veins never grow directly on the faces of a sculk block. The same thing is done to any air or water blocks that are adjacent to blocks that are adjacent to this sculk block, if sculk veins can't grow in the blocks adjacent to this sculk block without growing directly on the faces of sculk blocks.




sculk_sensor



: Block entity data.
Tags common to all block entities
 last_vibration_frequency: The frequency of the last vibration.
 listener: The vibration event listener for this sculk shrieker, sculk sensor, or calibrated sculk sensor.
 event: Only exists if there is an incoming vibration.
 distance: The distance between this vibration's source and the block.
 game_event: The resource location of the vibration event that caused the current incoming vibration.
 pos: The coordinates of the source of this vibration.
: X coordinate.
: Y coordinate.
: Z coordinate.
 projectile_owner: If the vibration was caused by a projectile, this is the UUID of the entity that launched the projectile. Does not exist if vibration was not caused by a projectile.
 source: The UUID of the entity that caused the vibration. Does not exist if vibration was not caused by an entity.
 event_delay: How many ticks remain until triggered by the vibration. Set to 0 if there is no incoming vibration
 selector: The data of the vibration selector.[more information needed]
 tick: The game time when the vibration occurs, or -1 if there is no vibration to choose from.[more information needed]
 event: Candidate game event, with the same structure as the  event tag above.[more information needed]




skulk_shrieker



: The block entity's root tag.
 VibrationListener: The vibration event listener of the sculk shrieker, sculk sensor, and calibrated sculk sensor.
 event: Unknown.
 pending: Unknown.
 distance: Unknown.
 source: Unknown.
 vibration: Unknown.
 x: Unknown.
 y: Unknown.
 z: Unknown.
 selector: Unknown.
 ticks: Unknown.




shulker_box



 Block entity data
Tags common to all block entities
Tags common to all objects that can be renamed
 Items: List of items in this container.
: An item, including the slot tag. Shulker box slots are numbered 0–26, 0 starts in the top left corner.
Tags common to all items
Tags common to all containers that can be locked
Tags common to all objects that use loot tables to produce items




sign



 Block entity data
Tags common to all block entities
 is_waxed: 1 or 0 (true/false) - true if the text is locked with honeycomb.
 front_text: A compound that discribes front text.
 has_glowing_text: 1 or 0 (true/false) - true if the sign has been dyed with a glow ink sac.
 color: The color that has been used to dye the sign. The default value is black One of white, orange, magenta, light_blue, yellow, lime, pink, gray, light_gray, cyan, purple, blue, brown, green, red, and black.
 filtered_messages: Only in Realms. The lines of text shown to players with the profanity filter turned on instead of the regular lines. This tag is automatically set to "" for lines containing blocked words and to the line's normal contents for the other lines when a player with the profanity filter turned off edits the sign, so players with the filter on cannot see the blocked words. If a player with the filter on tries to use blocked words in one or more lines, the line(s) in  messages containing blocked words are set to "", which makes them render completely blank, and this tag is also given the same contents. If multiple lines have been edited before the sign editing GUI is closed, only the lines containing blocked words are blanked.
 messages: A list of text for each line.
: Text for each line. Must be Raw JSON text format. The character limit for the Text tags depends on the width of the characters.
 back_text: A compound that discribes back text.
The same structure as  front_text.


Before 1.20:


 Block entity data
Tags common to all block entities
 GlowingText: 1 or 0 (true/false) - true if the sign has been dyed with a glow ink sac.
 Color: The color that has been used to dye the sign. The default value is "black". One of "white", "orange", "magenta", "light_blue", "yellow", "lime", "pink", "gray", "light_gray", "cyan", "purple", "blue", "brown", "green", "red", or "black".
 Text1: First row of text.
 Text2: Second row of text.
 Text3: Third row of text.
 Text4: Fourth row of text.






skull



 Block entity data
Tags common to all block entities
 note_block_sound: Optional. The sound event this skull plays when played with a note block.
 ExtraType: Name of the player this is a skull of. This tag is converted to SkullOwner below upon loading the NBT. When loaded sets the name to the value and the UUID to null.
 SkullOwner: The definition of the skull's owner. When this is a player_head or player_wall_head, shows this player's skin; if missing, shows the head of the default Steve skin.

 Id: UUID of owner, stored as four ints. Optional. Used to update the other tags when the chunk loads or the holder logs in, in case the owner's name has changed.
 Name: Username of owner. If missing or empty, the head appears as a Steve head. Otherwise, used to store or retrieve the downloaded skin in the cache. Need not be a valid player name, but must not be all spaces.
 Properties
 textures
: An individual texture.
 Value: A Base64-encoded JSON object.
 isPublic: Optional.
 signatureRequired
 profileId: Optional: The hexadecimal text form of the player's UUID, without hyphens.
 profileName: Optional: Player name.
 textures
 CAPE: Optional.
 url: URL of a player cape (64x32 PNG).
 SKIN
 url: URL of a player skin on textures.minecraft.net.
 metadata
 model: The model of the player skin. Can be "classic" or "slim".
 timestamp: Optional: Unix time in milliseconds.
 Signature: Optional.




smoker



 Block entity data
Tags common to all block entities
 BurnTime: Number of ticks left before the current fuel runs out.
 CookTime: Number of ticks the item has been smelting for. The item finishes smelting when this value reaches 200 (10 seconds). Is reset to 0 if BurnTime reaches 0.
 CookTimeTotal: Number of ticks It takes for the item to be smelted.

 CustomName: Optional. The name of this container in JSON text component, which appears in its GUI where the default name ordinarily appears.
 Items: List of items in this container.
: An item in the smoker, including the slot tag:Slot 0: The item(s) being smelted.Slot 1: The item(s) to use as the next fuel source.Slot 2: The item(s) in the result slot.
Tags common to all items

 Lock: Optional. When not blank, prevents the container from being opened unless the opener is holding an item whose name matches this string.
 RecipesUsed: Which recipes have been used since the last time a recipe result item was manually removed from the GUI. Used to calculate experience given to the player when taking out the resulting item.
 recipe ID: How many times this specific recipe has been used. The recipe ID is the identifier of the smelting recipe, as a resource location, as used in the /recipe command.




soul_campfire



 Block entity data
Tags common to all block entities
 CookingTimes: How long each item has been cooking, first index is slot 0, etc.
 CookingTotalTimes: How long each item has to cook, first index is slot 0, etc.
 Items: List of up to 4 items currently cooking.
Tags common to all items




structure_block



 Block entity data
Tags common to all block entities
 author: Author of the structure; only set to "?" for most vanilla structures.
 ignoreEntities: 1 or 0 (true/false): Whether entities should be ignored in the structure.
 integrity: How complete the structure is that gets placed.
 metadata: Value of the data structure block field.
 mirror: How the structure is mirrored, one of "NONE", "LEFT_RIGHT" (mirrored over X axis when not rotated), or "FRONT_BACK" (mirrored over Z axis when not rotated).
 mode: The current mode of this structure block, one of "SAVE", "LOAD", "CORNER", or "DATA".
 name: Name of the structure.
 posX: X-position of the structure.
 posY: Y-position of the structure.
 posZ: Z-position of the structure.
 powered: 1 or 0 (true/false): Whether this structure block is being powered by redstone.
 rotation: Rotation of the structure, one of "NONE", "CLOCKWISE_90", "CLOCKWISE_180", or "COUNTERCLOCKWISE_90".
 seed: The seed to use for the structure integrity, 0 means random.
 showboundingbox: 1 or 0 (true/false): Whether to show the structure's bounding box to players in Creative mode.
 sizeX: X-size of the structure, its length.
 sizeY: Y-size of the structure, its height.
 sizeZ: Z-size of the structure, its depth.




suspicious gravel



 Block entity data
Tags common to all block entities
 LootTable: Optional. Loot table to be used to generate the hidden item when brushed.[note 1]
 LootTableSeed: Optional. Seed for generating the loot table. 0 or omitted use a random seed.[note 1]
 item: The item in the block. May not exist.
See item format.

↑ a b Both loot table tags are removed once the items have been generated.





suspicious_sand



 Block entity data
Tags common to all block entities
 LootTable: Optional. Loot table to be used to generate the hidden item when brushed.[note 1]
 LootTableSeed: Optional. Seed for generating the loot table. 0 or omitted use a random seed.[note 1]
 item: The item in the block. May not exist.
See item format.

↑ a b Both loot table tags are removed once the items have been generated.





trapped_chest



 Block entity data
Tags common to all block entities
Tags common to all objects that can be renamed
 Items: List of items in this container.
: An item, including the slot tag. Chest slots are numbered 0-26, 0 starts in the top left corner.
Tags common to all items
Tags common to all containers that can be locked
Tags common to all objects that use loot tables to produce items
 gold: Exists only in the april fools snapshot 23w13a_or_b. Optional. When set to anything but 0, turns the chest into a golden chest.




trial_spawner



 Block entity data
Tags common to all block entities
 required_player_range: Between 1 and 128. Defaults to 14. — Maximum distance in blocks for players to join the battle.
 target_cooldown_length: Defaults to 36000. — Time in ticks of the cooldown period. Includes the time spend dispensing the reward.
 normal_config: Optional, see configuration for defaults. — The configuration to use when not ominous.
Trial Spawner Configuration
 ominous_config: Optional, defaults to  normal_config. When individual entries are omitted, they also default to their setting in  normal_config. — The configuration to use when ominous.
Trial Spawner Configuration
The following fields are used to keep track of the current state of the trial spawner.
 registered_players: A set of player UUIDs. — All the players that have joined the battle. The length of this array determines the amount of mobs and amount of reward.
: A UUID.
 current_mobs: A set of mob UUIDs. — The mobs that were spawned by this spawner and are still alive.
: A UUID.
 cooldown_ends_at: Gametime in ticks when the cooldown ends. 0 if not currently in cooldown.
 next_mob_spawns_at: Gametime in ticks when the next spawn attempt happens. 0 if not currently active.
 total_mobs_spawned: The total amount of mobs that have already been spawned in this cycle. 0 if not currently active.
 spawn_data: The next mob to attempt to spawn. Selected from  spawn_potentials after the last attempt. Determines the mob displayed in the spawner.
Spawn Data
 ejecting_loot_table: A resource location to the loot table that is given as reward. Unset if not currently giving rewards. Selected from  loot_tables_to_eject after all mobs are defeated.




vault‌[upcoming]



 Block entity data
Tags common to all block entities
 config: Configuration data that does not automatically change. All fields are optional.
 loot_table: A resource location to the loot table that is ejected when unlocking the vault. Defaults to "minecraft:chests/trial_chambers/reward".
 override_loot_table_to_display: A resource location to the loot table that is used to display items in the vault. If not present, the game uses the loot_table field.
 activation_range: The range in blocks when the vault should activate. Defaults to 4.
 deactivation_range: The range in blocks when the vault should deactivate. Defaults to 4.5.
 key_item: The key item that is used to check for valid keys. Defaults to "minecraft:trial_key".
Tags common to all items
 server_data: Data that is only stored on the server.
 rewarded_players: A set of player UUIDs that have already received their rewards from this vault.
 state_updating_resumes_at: The game time when the vault processes block state changes, such as changing from unlocking to ejecting after a delay.
 items_to_eject: List of item stacks that have been rolled by the loot table and are waiting to be ejected.
: An item stack
Tags common to all items
 total_ejections_needed: The total amount of item stacks that need to be ejected.
 shared_data: Data that is synced between the server and client.
 display_item: The item that is currently being displayed.
 connected_players: A set of player UUIDs that are within range of the vault.
 connected_particles_range: The range in blocks when the vault emits particles.




