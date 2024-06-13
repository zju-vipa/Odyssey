# Display
Display entities are entities useful for map or data pack creators to display various things. There are Block Displays, Item Displays and Text Displays, which are used to display blocks, items and texts respectively. They can be created only with the /summon or /execute summon command.

## Contents
- 1 Behavior
- 2 Usage
	- 2.1 Item Displays
	- 2.2 Block Displays
	- 2.3 Text Displays
	- 2.4 Interpolation
- 3 Data values
	- 3.1 ID
	- 3.2 Entity data
- 4 History

## Behavior
Much like markers, display entities do not move, do not take damage, do not make sounds, and have no collision. They do not obstruct the placement of blocks, nor do they push players or other entities away from their own position. Unlike markers, display entities are sent to the client for rendering and do count toward in the E value (total amount of entities) listed on the debug screen.

Display entities have no hitbox. Using the debug key combination F3 + B, which normally draws the hitboxes of all visible entities, does not show a hitbox for display entities. Using F3 + I while aiming at a display entity does not copy the entity data to the clipboard.

## Usage
Display entities can be summoned only by commands. Block Displays, Item Displays, and Text Displays have the default NBT data of {block_state:{Name:"minecraft:air"}}, {item:{id:"minecraft:air",Count:0b}}, and {text:'{"text":""}'} respectively and so, if spawned without any NBT data specified, they are not visible. By modifying the entities' data one can easily edit their display content and other visual effects, and rotate, scale, or translate the model.

### Item Displays
Item Display entities can display any item in the game using the item tag.

Using the Item Display entity with custom_model_data can easily display any custom model.

For the Item Display entity, in addition to directly modifying the NBT, the displayed item can also be modified using the /loot and /item commands with the slot container.0.

Per default, the location of an item display without transformations represents the center of the item.

### Block Displays

  

This section is a work in progress. 
Please help expand and improve it. The talk page may contain suggestions.


Block Display entities can display any block in the game using the block_state tag.

The location of a block display without transformations represents the north-west-bottom (negative XYZ) corner of the block.

### Text Displays

  

This section is a work in progress. 
Please help expand and improve it. The talk page may contain suggestions.


Text Display entities can display any text using the text tag.

The displayed text is only visible from one side, which is without transformations the direction the text display is rotated towards.

The location of a text display without transformations represents the bottom center of the text.

### Interpolation
Some visual effects of these entities can be interpolated over game time to display gradient animation.

All fields marked as "Interpolated" in #Entity data below can be interpolated. These properties do not interpolate independently of each other.

Any change to any of these properties causes client to record both the previous and changed values of these properties. Since server synchronizes entities with the client at most once per game tick, multiple changes within one game tick still count as a single change.

The entity rendering is interpolated over time between the previous values and the current values. The game time to start interpolation (entity fully in previous state) is start_interpolation (gametime, in game ticks). Trying to set a value less than 0 sets it to the current game time. The game time when interpolation ends (entity fully in current state) is start_interpolation + interpolation_duration (gametime, in game ticks).

## Data values
### ID
| Entity        | Identifier      | Translation key                  |
|---------------|-----------------|----------------------------------|
| Block Display | `block_display` | `entity.minecraft.block_display` |
| Item Display  | `item_display`  | `entity.minecraft.item_display`  |
| Text Display  | `text_display`  | `entity.minecraft.text_display`  |

### Entity data
See also: Entity format

Display entities have entity data associated with them that contain various properties of the entity.

Item Display:

- root tag
	- 
	- Tags common to all entities
	- 
	- Tags common to all display entities
	- item: The item to display.
		- 
		- Tags common to all items
	- item_display: The model to display. Describes item model transform applied to item (as defined indisplayfield inmodelJSON. Can benone,thirdperson_lefthand,thirdperson_righthand,firstperson_lefthand,firstperson_righthand,head,gui,ground, andfixed. Defaults tonone.

Block Display:

- root tag
	- 
	- Tags common to all entities
	- 
	- Tags common to all display entities
	- block_state: The block state to display.
		- 
		- Block state

Text Display:

- root tag
	- 
	- Tags common to all entities
	- 
	- Tags common to all display entities
	- alignment: Text alignment direction. Can becenter,left, andright. Defaults tocenter.
	- background: The background color, arranged by ARGB. Since pixel with an alpha channel less than 0.1 are discarded when rendering in vanillashader, the background becomes fully transparent when A is less than 26 (0x1A). Defaults to 1073741824 (0x40000000). Interpolated.
	- default_background: If true, rendering uses default text background color (same as in chat), which overridesbackground. Defaults tofalse.
	- line_width: Maximum line width used to split lines (note: new line can be also added with\ncharacters). Defaults to 200.
	- see_through: Whether the text be visible through blocks. Defaults tofalse.
	- shadow: Whether the text is displayed with shadow. Defaults tofalse.
	- text: The text to be displayed in the format ofraw JSON text, which are resolved with the context of the display entity.
	- text_opacity: Alpha value of rendered text. Alpha value is from 0 to 255. Since there are no unsigned bytes in NBT, values greater than 127 need to be replaced withalpha-256. So, the value is from -128 to 127. Similar to the background, the text rendering is discarded when it is less than 26. Defaults to -1, which represents 255 and is completely opaque. Interpolated.


