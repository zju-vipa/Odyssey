# Piston/Technical components
Pistons and sticky pistons have 2 technical blocks that cannot be obtained. These include the piston head and moving piston blocks.

## Contents
- 1 Piston head
	- 1.1 Block states
- 2 Moving piston
	- 2.1 Block states
	- 2.2 Block data
- 3 Data values
	- 3.1 ID
- 4 History
	- 4.1 Appearances
	- 4.2 Names
- 5 References
- 6 Trivia

## Piston head

Piston Head















Renewable


Yes



Stackable


No



Tool


Any tool



Blast resistance


0.5



Hardness


1.5



Luminous


No



Transparent


Yes



Flammable


No



Catches fire from lava


No




{
    "title": "Piston Head",
    "rows": [
        {
            "field": "Yes",
            "label": "(link to Renewable resource article, displayed as Renewable)"
        },
        {
            "field": "No",
            "label": "Stackable"
        },
        {
            "field": "Any tool",
            "label": "Tool"
        },
        {
            "field": "0.5",
            "label": "(link to Explosion#Blast resistance article, displayed as Blast resistance)"
        },
        {
            "field": "1.5",
            "label": "(link to Breaking#Blocks by hardness article, displayed as Hardness)"
        },
        {
            "field": "No",
            "label": "(link to Light article, displayed as Luminous)"
        },
        {
            "field": "Yes",
            "label": "(link to Opacity article, displayed as Transparent)"
        },
        {
            "field": "No",
            "label": "(link to Flammable article, displayed as Flammable)"
        },
        {
            "field": "No",
            "label": "Catches fire from (link to lava article, displayed as lava)"
        }
    ],
    "invimages": [
        "pistonArmCollision"
    ],
    "images": [
        "Piston Head.png",
        "Piston Head BE.png",
        "Sticky Piston Head.png",
        "Sticky Piston Head BE.png"
    ]
}
The piston head is a technical block used as the second block of an extended piston. A block state defines whether it is a normal or a sticky piston head. It can be placed using the /setblock command or with the debug stick, though if not part of a proper piston, it disappears after receiving any block tick, such as when a block is placed next to it unless the player uses the debug stick. It drops nothing.

In Java Edition, the normal and sticky piston heads are distinguished by a block state. In Bedrock Edition, they use separate block IDs, and it can be obtained as an item via inventory editors.

### Block states
See also: Block states

Java Edition:

| Name   | Default value | Allowed values           | Description                                                 |
|--------|---------------|--------------------------|-------------------------------------------------------------|
| facing | north         | downeastnorthsouthupwest | The direction the piston head is pointing.                  |
| short  | false         | falsetrue                | If true, the piston arm is shorter than usual, by 4 pixels. |
| type   | normal        | normalsticky             | The type of piston head.                                    |

Bedrock Edition:
Piston Head:

| Name             | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                                                                                                         |
|------------------|---------------|---------------|----------------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| facing_direction | 0x10x20x4     | 0             | 012345         | 012345                  | The direction the piston head is pointing.0: facing up 1: facing down 2: facing south 3: facing north 4: facing east 5: facing west |

Sticky Piston Head:

| Name             | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                                                                                                         |
|------------------|---------------|---------------|----------------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| facing_direction | Not Supported | 0             | 012345         | Unsupported             | The direction the piston head is pointing.0: facing up 1: facing down 2: facing south 3: facing north 4: facing east 5: facing west |




## Moving piston

Moving Piston




Renewable


Yes



Stackable


No



Tool


None



Blast resistance


0



Hardness


-1



Luminous


No



Transparent


Yes



Flammable


No



Catches fire from lava


No




{
    "title": "Moving Piston",
    "rows": [
        {
            "field": "Yes",
            "label": "(link to Renewable resource article, displayed as Renewable)"
        },
        {
            "field": "No",
            "label": "Stackable"
        },
        {
            "field": "None",
            "label": "Tool"
        },
        {
            "field": "0",
            "label": "(link to Explosion#Blast resistance article, displayed as Blast resistance)"
        },
        {
            "field": "-1",
            "label": "(link to Breaking#Blocks by hardness article, displayed as Hardness)"
        },
        {
            "field": "No",
            "label": "(link to Light article, displayed as Luminous)"
        },
        {
            "field": "Yes",
            "label": "(link to Opacity article, displayed as Transparent)"
        },
        {
            "field": "No",
            "label": "(link to Flammable article, displayed as Flammable)"
        },
        {
            "field": "No",
            "label": "Catches fire from (link to lava article, displayed as lava)"
        }
    ],
    "invimages": [
        "movingBlock"
    ],
    "images": [
        "Moving Piston.png"
    ]
}
The moving piston, also known as block 36 due to its pre-flattening block ID, is an unobtainable technical block that contains part of a piston head, and/or part of one or two blocks that the piston is carrying into or out of the grid cell (including blocks carried indirectly via slime blocks). Since moving blocks vary in how much of each grid cell they occupy, they can't be stored as normal blocks and are instead stored as block entities. It is overwritten with air, the piston head or the carried block at the end of the piston stroke; but if it is placed through editing and no piston is connected, it remains indefinitely.

It is invisible and non-solid in Java Edition, and cannot be broken without the use of commands or TNT. Although it is non-solid, fluids cannot pass through it. It also prevents players from building at its location. Mobs can see through it, but cannot walk through it.
The game treats the block as a stone block when it comes to the player's footstep sounds. It is similar to Invisible Bedrock in properties with the exception that the player can walk through the moving piston but not invisible bedrock.

### Block states
See also: Block states

Java Edition:

| Name   | Default value | Allowed values           | Description                                            |
|--------|---------------|--------------------------|--------------------------------------------------------|
| facing | north         | downeastnorthsouthupwest | The direction the block is being pushed by the piston. |
| type   | normal        | normalsticky             | What piston base this has.                             |



### Block data
The moving piston has a block entity associated with it that holds additional data about the block.

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

## Data values
### ID
Java Edition:

| Name          | Identifier    | Form  | Block tags                 | Translation key               |
|---------------|---------------|-------|----------------------------|-------------------------------|
| Piston Head   | piston_head   | Block | None                       | block.minecraft.piston_head   |
| Moving Piston | moving_piston | Block | dragon_immunewither_immune | block.minecraft.moving_piston |

| Name                 | Identifier |
|----------------------|------------|
| Moving piston entity | piston     |

Bedrock Edition:

| Name               | Identifier                  | Alias ID                 | Numeric ID | Form                         | Item ID[i 1]                                               | Translation key                       |
|--------------------|-----------------------------|--------------------------|------------|------------------------------|------------------------------------------------------------|---------------------------------------|
| Piston Head        | piston_arm_collision        | pistonArmCollision       | 34         | Block & Ungiveable Item[i 2] | piston_arm_collisionAlias ID:pistonarmcollision            | tile.piston_arm_collision.name        |
| Sticky Piston Head | sticky_piston_arm_collision | stickyPistonArmCollision | 472        | Block & Ungiveable Item[i 2] | stick_piston_arm_collisionAlias ID:stickpistonarmcollision | tile.sticky_piston_arm_collision.name |
| Moving Block       | moving_block                | movingBlock              | 250        | Block & Ungiveable Item[i 2] | moving_blockAlias ID:movingblock                           | tile.moving_block.name                |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ a b c Unavailable with /give command


| Name                | Savegame ID |
|---------------------|-------------|
| Moving block entity | MovingBlock |

