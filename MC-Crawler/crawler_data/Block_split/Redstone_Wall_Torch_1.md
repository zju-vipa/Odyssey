## Data values
### ID
Java Edition:

| Name                | Identifier          | Form         | Block tags         | Translation key                     |
|---------------------|---------------------|--------------|--------------------|-------------------------------------|
| Redstone Torch      | redstone_torch      | Block & Item | wall_post_override | block.minecraft.redstone_torch      |
| Redstone Wall Torch | redstone_wall_torch | Block        | None               | block.minecraft.redstone_wall_torch |

Bedrock Edition:

| Name                 | Identifier           | Numeric ID | Form                         | Item ID[i 1]   | Translation key                |
|----------------------|----------------------|------------|------------------------------|----------------|--------------------------------|
| Redstone Torch       | redstone_torch       | 76         | Block & Giveable Item[i 2]   | Identical[i 3] | tile.redstone_torch.name       |
| Unlit Redstone Torch | unlit_redstone_torch | 75         | Block & Ungiveable Item[i 4] | Identical[i 3] | tile.unlit_redstone_torch.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ a b The block's direct item form has the same id as the block.

↑ Unavailable with /give command


### Block states
See also: Block states

Java Edition:
Floor:

| Name | Default value | Allowed values | Description          |
|------|---------------|----------------|----------------------|
| lit  | true          | falsetrue      | If the torch is lit. |

Wall:

| Name   | Default value | Allowed values     | Description                                   |
|--------|---------------|--------------------|-----------------------------------------------|
| facing | north         | eastnorthsouthwest | The direction the top of the torch is facing. |
| lit    | true          | falsetrue          | If the torch is lit.                          |

Bedrock Edition:

| Name                   | Metadata Bits | Default value | Allowed values        | Values forMetadata Bits | Description                                                                                                                                  |
|------------------------|---------------|---------------|-----------------------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| torch_facing_direction | 0x10x20x4     | west          | westeastnorthsouthtop | 12345                   | The face of the block that the torch is attached to. If the torch is a wall torch, the top of the torch faces opposite to this direction.[1] |
|                        |               |               | unknown               | 0                       | Unused                                                                                                                                       |


