# Barrel
A barrel is a solid block used to store items. Unlike a chest, it cannot connect to other barrels. It also serves as a fisherman's job site block.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Chest loot
	- 1.4 Crafting
- 2 Usage
	- 2.1 Container
	- 2.2 Changing profession
	- 2.3 Fuel
	- 2.4 Note Blocks
	- 2.5 Piglins
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Block data
- 5 History
- 6 Issues
- 7 Trivia
- 8 Gallery
	- 8.1 Renders
	- 8.2 Screenshots
- 9 References
- 10 External links

## Obtaining
### Breaking
Barrels can be mined with or without any tool, but axes are the quickest.

| Block     | Barrel                |
|-----------|-----------------------|
| Hardness  | 2.5                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 3.75                  |
| Wooden    | 1.9                   |
| Stone     | 0.95                  |
| Iron      | 0.65                  |
| Diamond   | 0.5                   |
| Netherite | 0.45                  |
| Golden    | 0.35                  |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Natural generation
Empty barrels can generate naturally in fisher cottages in villages. Up to 3 barrels can generate in a village fisher cottage. Barrels with loot can be found in the trial chambers.

### Chest loot
| Item   | Structure | Container         | Quantity | Chance       |
|--------|-----------|-------------------|----------|--------------|
|        |           |                   |          | Java Edition |
| Barrel | Village   | Fisherman's chest | 1–3      | 24.2%        |

### Crafting

| Ingredients              | Crafting recipe |
|--------------------------|-----------------|
| AnyPlanks+AnyWooden Slab |                 |

## Usage
Barrels can be moved by pistons,‌[Bedrock Edition  only] water and lava flow around barrels without affecting them. Lava can create fire in air blocks next to barrels as if the barrel was flammable, but the barrel does not actually catch fire and can't be burned.

### Container
The GUI of the barrel.
Barrels have a container inventory with 27 slots, which is the same as a single chest. Unlike chests, a barrel can be placed below a solid block and still be able to be opened.
They can be filled by droppers and both filled and emptied by hoppers. When broken, barrels drop the contents of the container and the barrel item itself. 

To open the barrel interface, use the Use Item control. To move items between the barrel inventory and the player inventory or hotbar while the barrel interface is open, drag or shift-click the items. Holding Shift and double-clicking while holding an item moves all items of the type clicked on in or out of the barrel to the extent that space is available for them.‌[Java Edition  only] To exit the barrel interface, use the Esc control.

By default, the interface of a barrel is labeled "Barrel". A barrel's GUI label can be changed by naming the barrel in an anvil before placing it or by using the /data command‌[Java Edition  only] (for example, to label a barrel at (0,64,0) as "Bonus Barrel!", use /data merge block 0 64 0 {CustomName:'"Bonus Barrel!"'}).

In Java Edition, a barrel can be "locked" by setting its Lock tag using the /data command. If a barrel's Lock tag is not blank, the barrel cannot be opened unless the player is holding an item with the same name as the Lock tag's text. For example, to lock a barrel at (0,64,0) so that the barrel cannot be opened unless the player is holding an item named "Barrel Key", use /data merge block 0 64 0 {Lock:"Barrel Key"}.

### Changing profession
If a village has a barrel that has not been claimed by a villager, any villager who does not have a chosen job site block has a chance to change their profession into a fisherman.

### Fuel
Barrels can be used as a fuel in furnaces, smelting 1.5 items per block.

### Note Blocks
Barrels can be placed under note blocks to produce "bass" sounds.

### Piglins
Piglins become hostile toward players who open or break barrels.

## Data values
### ID
Java Edition:

| Name   | Identifier | Form         | Block tags         | Translation key        |
|--------|------------|--------------|--------------------|------------------------|
| Barrel | barrel     | Block & Item | guarded_by_piglins | block.minecraft.barrel |

| Name         | Identifier |
|--------------|------------|
| Block entity | barrel     |

Bedrock Edition:

| Name   | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key  |
|--------|------------|------------|----------------------------|----------------|------------------|
| Barrel | barrel     | 458        | Block & Giveable Item[i 2] | Identical[i 3] | tile.barrel.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


| Name         | Savegame ID |
|--------------|-------------|
| Block entity | Barrel      |

### Block states
See also: Block states

Java Edition:

| Name   | Default value | Allowed values           | Description                                                                                       |
|--------|---------------|--------------------------|---------------------------------------------------------------------------------------------------|
| facing | north         | downeastnorthsouthupwest | The direction the barrel is facing.                                                               |
| open   | false         | falsetrue                | Whether the barrel is currently being looked at by a player; changes the texture on the top face. |

Bedrock Edition:

| Name             | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                                                                                                                                      |
|------------------|---------------|---------------|----------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing_direction | 0x10x20x4     | 0             | 012345         | 012345                  | The direction the barrel is facing.0:Down facing barrel 1:Up facing barrel 2:East facing barrel 3:West facing barrel 4:South facing barrel 5:North facing barrel |
| open_bit         | 0x8           | 0             | 01             | 01                      | Whether the barrel is currently being looked at by a player; changes the texture on the top face.                                                                |



### Block data
A barrel has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format


 Block entity data
Tags common to all block entities

 CustomName: Optional. The name of this container in JSON text component, which appears in its GUI where the default name ordinarily appears.
 Items: List of items in the container.
: An item, including the slot tag. Barrel slots are numbered 0-26, 0 starts in the top left corner.
Tags common to all items

 Lock: Optional. When not blank, prevents the container from being opened unless the opener is holding an item whose name matches this string.

 LootTable: Optional. Name of the loot table to use. If this is used in a chest-like container, the loot table generates its content when it is opened. Generating the items in the container removes both loot table tags ( LootTable and  LootTableSeed).
 LootTableSeed: Optional. Seed for generating the loot table. The default value works similarly to the seeds for worlds, where value of 0 or an omitted value causes the game to use a random seed.

Bedrock Edition:

See Bedrock Edition level format/Block entity format.
