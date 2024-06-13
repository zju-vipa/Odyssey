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


