### Cooking
Main article: Campfire § Cooking
### Hoppers
Soul campfires do not have an external inventory. Raw food cannot be loaded into the soul campfire with a hopper.

A hopper placed directly underneath a soul campfire pulls through any items dropped into the soul campfire. Any drops from a mob that dies in the soul campfire get pulled into the hopper.

### Bees
Placing a soul campfire under a beehive or bee nest allows players to harvest honey bottles or honeycomb without provoking the bees.
There must be unobstructed air between the soul campfire and the beehive or bee nest. Carpets are an exception.‌[Java Edition  only]

### Piglins
Lit soul campfires repel piglins that are not currently attacking. This occurs when the piglin is within an 8 block radius of the soul campfire.

### Light source
Soul campfires emit a light level of 10. Due to their lower light level, soul campfires do not melt snow or ice.

### Note blocks
Soul campfires can be placed under note blocks to produce "bass" sounds.

### Converting soul sand to soul soil
Soul campfires can be used to convert soul sand into soul soil. If a soul campfire is crafted using soul sand, placed, and then broken without Silk Touch, that soul campfire drops soul soil.[4]

### Piston interactivity
In Bedrock Edition, pushing a soul campfire with a piston or sticky piston breaks it. Soul campfires cannot be pulled by sticky pistons.

In Java Edition, pistons do not interact with soul campfires. Soul campfires neither move nor break when pushed or pulled by pistons.

## Data values
### ID
Java Edition:

| Name          | Identifier    | Form         | Block tags                 | Translation key               |
|---------------|---------------|--------------|----------------------------|-------------------------------|
| Soul Campfire | soul_campfire | Block & Item | campfirespiglin_repellents | block.minecraft.soul_campfire |

| Name         | Identifier |
|--------------|------------|
| Block entity | campfire   |

Bedrock Edition:

| Name  | Identifier    | Numeric ID | Form                         | Item ID[i 1]       | Translation key         |
|-------|---------------|------------|------------------------------|--------------------|-------------------------|
| Block | soul_campfire | 545        | Block & Ungiveable Item[i 2] | item.soul_campfire | tile.soul_campfire.name |
| Item  | soul_campfire | 622        | Item                         | —                  | tile.soul_campfire.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Unavailable with /give command


| Name         | Savegame ID |
|--------------|-------------|
| Block entity | Campfire    |

### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values     | Description                                                                                                       |
|-------------|---------------|--------------------|-------------------------------------------------------------------------------------------------------------------|
| facing      | north         | eastnorthsouthwest | The direction the campfire is facing.The opposite from the direction the player faces while placing the campfire. |
| lit         | true          | falsetrue          | Whether the campfire is lit.                                                                                      |
| signal_fire | false         | falsetrue          | Whether the campfire has ahay balebelow it.                                                                       |
| waterlogged | false         | falsetrue          | Whether or not there's water in the same place as this campfire.                                                  |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                                                                                                       |
|------------------------------|---------------|---------------|--------------------|-------------------------|-------------------------------------------------------------------------------------------------------------------|
| extinguished                 | 0x4           | false         | falsetrue          | 01                      | Whether the campfire is put out.                                                                                  |
| minecraft:cardinal_direction | Not Supported | south         | eastnorthsouthwest | Unsupported             | The direction the campfire is facing.The opposite from the direction the player faces while placing the campfire. |



### Block data
A soul campfire has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format


 Block entity data
Tags common to all block entities
 CookingTimes: How long each item has been cooking, first index is slot 0, etc.
 CookingTotalTimes: How long each item has to cook, first index is slot 0, etc.
 Items: List of up to 4 items currently cooking.
Tags common to all items

Bedrock Edition:

See Bedrock Edition level format/Block entity format.

