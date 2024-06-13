### Note blocks
Fence gates can be placed under note blocks to produce "bass" sounds.

### Helmet


While a fence gate cannot be equipped in the head slot in Survival mode, equipping it using commands causes it to appear as eyeglasses.

## Data values
### ID
Java Edition:

| Name                | Identifier            | Form         | Block tags                                                          | Item tags            | Translation key                       |
|---------------------|-----------------------|--------------|---------------------------------------------------------------------|----------------------|---------------------------------------|
| Oak Fence Gate      | `oak_fence_gate`      | Block & Item | `fence_gates`<br/>`unstable_bottom_center`                          | None                 | `block.minecraft.oak_fence_gate`      |
| Spruce Fence Gate   | `spruce_fence_gate`   | Block & Item | `fence_gates`<br/>`unstable_bottom_center`                          | None                 | `block.minecraft.spruce_fence_gate`   |
| Birch Fence Gate    | `birch_fence_gate`    | Block & Item | `fence_gates`<br/>`unstable_bottom_center`                          | None                 | `block.minecraft.birch_fence_gate`    |
| Jungle Fence Gate   | `jungle_fence_gate`   | Block & Item | `fence_gates`<br/>`unstable_bottom_center`                          | None                 | `block.minecraft.jungle_fence_gate`   |
| Acacia Fence Gate   | `acacia_fence_gate`   | Block & Item | `fence_gates`<br/>`unstable_bottom_center`                          | None                 | `block.minecraft.acacia_fence_gate`   |
| Dark Oak Fence Gate | `dark_oak_fence_gate` | Block & Item | `fence_gates`<br/>`unstable_bottom_center`                          | None                 | `block.minecraft.dark_oak_fence_gate` |
| Mangrove Fence Gate | `mangrove_fence_gate` | Block & Item | `fence_gates`<br/>`unstable_bottom_center`                          | None                 | `block.minecraft.mangrove_fence_gate` |
| Cherry Fence Gate   | `cherry_fence_gate`   | Block & Item | `fence_gates`<br/>`unstable_bottom_center`                          | None                 | `block.minecraft.cherry_fence_gate`   |
| Bamboo Fence Gate   | `bamboo_fence_gate`   | Block & Item | `fence_gates`<br/>`unstable_bottom_center`                          | None                 | `block.minecraft.bamboo_fence_gate`   |
| Crimson Fence Gate  | `crimson_fence_gate`  | Block & Item | `fence_gates`<br/>`non_flammable_wood`<br/>`unstable_bottom_center` | `non_flammable_wood` | `block.minecraft.crimson_fence_gate`  |
| Warped Fence Gate   | `warped_fence_gate`   | Block & Item | `fence_gates`<br/>`non_flammable_wood`<br/>`unstable_bottom_center` | `non_flammable_wood` | `block.minecraft.warped_fence_gate`   |

Bedrock Edition:

| Name                | Identifier            | Numeric ID | Form                       | Item ID[i 1]   | Translation key                 |
|---------------------|-----------------------|------------|----------------------------|----------------|---------------------------------|
| Oak Fence Gate      | `fence_gate`          | `107`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.fence_gate.name`          |
| Spruce Fence Gate   | `spruce_fence_gate`   | `183`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.spruce_fence_gate.name`   |
| Birch Fence Gate    | `birch_fence_gate`    | `184`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.birch_fence_gate.name`    |
| Jungle Fence Gate   | `jungle_fence_gate`   | `185`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.jungle_fence_gate.name`   |
| Acacia Fence Gate   | `acacia_fence_gate`   | `187`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.acacia_fence_gate.name`   |
| Dark Oak Fence Gate | `dark_oak_fence_gate` | `186`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.dark_oak_fence_gate.name` |
| Mangrove Fence Gate | `mangrove_fence_gate` | `-492`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.mangrove_fence_gate.name` |
| Cherry Fence Gate   | `cherry_fence_gate`   | `-533`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.cherry_fence_gate.name`   |
| Bamboo Fence Gate   | `bamboo_fence_gate`   | `-516`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.bamboo_fence_gate.name`   |
| Crimson Fence Gate  | `crimson_fence_gate`  | `513`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.crimson_fence_gate.name`  |
| Warped Fence Gate   | `warped_fence_gate`   | `514`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.warped_fence_gate.name`   |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑ a b c d e f g h i j kAvailable with /give command.
3. ↑ a b c d e f g h i j kThe block's direct item form has the same id as the block.

### Block states
Main article: Block states
Java Edition:

| Name    | Default value | Allowed values                            | Description                                                                                                                                                                            |
|---------|---------------|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing  | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | For an open gate, the direction the gates swing open.<br/>For a closed gate, the direction the player was facing when the gate was placed, or the last direction the gates have swung. |
| in_wall | `false`       | `false`<br/>`true`                        | If true, the gate is lowered by three pixels, to accommodate attaching more cleanly withwalls.                                                                                         |
| open    | `false`       | `false`<br/>`true`                        | If true, the gate is opened.                                                                                                                                                           |
| powered | `false`       | `false`<br/>`true`                        | If true, the gate is receiving redstone power.                                                                                                                                         |

Bedrock Edition:

| Name        | Metadata Bits   | Default value | Allowed values              | Values forMetadata Bits     | Description                                                                                                                                                                                                                                                                                                    |
|-------------|-----------------|---------------|-----------------------------|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| direction   | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`1`<br/>`2`<br/>`3` | The direction the gate is facing0: Facing south<br/>1: Facing west<br/>2: Facing north<br/>3: Facing east<br/>For an open gate, it's the direction the gates swing open.<br/>For a closed gate, it's the direction the player was facing when the gate was placed, or the last direction the gates have swung. |
| in_wall_bit | `0x8`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | If the gate is lowered by three pixels, to accommodate attaching more cleanly withwalls.                                                                                                                                                                                                                       |
| open_bit    | `0x4`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | If the gate is opened.                                                                                                                                                                                                                                                                                         |


