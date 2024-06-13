## Data values
### ID
Java Edition:

| Name        | Identifier  | Form         | Block tags                                  | Item tags | Translation key             |
|-------------|-------------|--------------|---------------------------------------------|-----------|-----------------------------|
| Pink Petals | pink_petals | Block & Item | mineable/hoeflowersinside_step_sound_blocks | flowers   | block.minecraft.pink_petals |

Bedrock Edition:

| Name        | Identifier  | Numeric ID | Form                       | Item ID[i 1]   | Translation key       |
|-------------|-------------|------------|----------------------------|----------------|-----------------------|
| Pink Petals | pink_petals | -549       | Block & Giveable Item[i 2] | Identical[i 3] | tile.pink_petals.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:

| Name          | Default value | Allowed values     | Description                                                                                                              |
|---------------|---------------|--------------------|--------------------------------------------------------------------------------------------------------------------------|
| facing        | north         | eastnorthsouthwest | The direction the pink petals are facing.The opposite from the direction the player faces while placing the pink petals. |
| flower_amount | 1             | 1234               | The amount of pink petals in the block.                                                                                  |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                                                                                                              |
|------------------------------|---------------|---------------|--------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------|
| growth                       | Not Supported | 0             | 01234567           | Unsupported             | The amount of pink petals in the block. A value greater than 3 can only be obtained via commands.                        |
| minecraft:cardinal_direction | Not Supported | south         | eastnorthsouthwest | Unsupported             | The direction the pink petals are facing.The opposite from the direction the player faces while placing the pink petals. |




