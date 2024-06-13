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

