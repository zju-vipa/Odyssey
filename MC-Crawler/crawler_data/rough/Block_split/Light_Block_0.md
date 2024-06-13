# Light Block
Light blocks (in Bedrock Edition) or lights (in Java Edition) are invisible blocks, primarily intended for map makers, that can produce any light level from 0 to 15. The light block is also the only light-emitting block capable of producing light level 8.‌[until JE 1.21 & BE 1.21.0]

## Contents
- 1 Obtaining
- 2 Usage
	- 2.1 Light source
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Gallery
	- 6.1 Renders
	- 6.2 Screenshots
- 7 Issues
- 8 References

## Obtaining
Light blocks cannot be mined, similar to air, and can be targeted only if the player is holding a Light item in the main hand. Light blocks with a light level of 0 are functionally identical to air.

They do not attach to any block, meaning that breaking an adjacent block does not remove the light block. However, they can be broken by replacing them with another block.[1] The exception is water (including, in Bedrock Edition, flowing water), which can occupy the same space as a light block. See Waterlogging for more information.

In Java Edition, light blocks are available in the Creative inventory. Across both Java Edition and Bedrock Edition, they can also be obtained by using commands such as /give. In Bedrock Edition, specifying the data value from 0 to 15 determines the block's light level; if the data value is not specified, the light block emits a light level of 0. The command is: /give <target> light_block [amount: int] [data: int (0 - 15)] [components: json]. In Java Edition, using /give <target> minecraft:light{BlockStateTag:{level:"<int>"}} can give a light block with a specific light level and corresponding texture. If the level is below 0, the non-bulb texture is used, and above 15 the level 15 texture. If the block state is not specified or not between 0 and 15, the light block emits a light level of 15.

## Usage
The difference between air (top left) and light (bottom right) when "show invisible blocks" is enabled.
A light block with a light level of 9.
Each light block has an associated light level, which can be anything from 0 to 15. In the player's inventory, light blocks display their light level in the top-left corner with a unique sprite for each light level.

Light blocks are not visible, and have no hitbox unless the player is holding another light block in their main hand. When the player holds a light block, any placed light blocks become interactive, displaying a small icon in the center indicating the blocks location and current light level. The block icon is a particle, and does not become visible if particles are set to their lowest setting, although the hitbox remains visible and interactive until the light block leaves the players main hand.

When holding a light block in the main hand, clicking 'use' on a light block that is already placed on the ground causes the light level of the light block to increase by one. If the light level is already 15, it resets to 0. If a light block's level has been modified, it can be copied back into the players hotbar by using the 'pick block' button while holding another light block. 

Liquids such as water and lava cannot pass through light blocks unless they are waterlogged (either with the debug stick or by placing water on either side of the block.) but falling blocks like sand, gravel, and anvils pass through the Light block as if it is air. If a falling block lands on a light block, or another block is placed over it, the light block is destroyed.

Light blocks are detected by observers, and in Bedrock Edition they can be pushed and pulled by pistons.

### Light source
Light blocks produce their associated light level.

## Data values
### ID
Java Edition:

| Name  | Identifier | Form         | Block tags                               | Translation key         |
|-------|------------|--------------|------------------------------------------|-------------------------|
| Light | `light`    | Block & Item | `dragon_transparent`<br/>`wither_immune` | `block.minecraft.light` |

Bedrock Edition:

| Name        | Identifier    | Numeric ID | Form                       | Item ID[i 1]   | Translation key         |
|-------------|---------------|------------|----------------------------|----------------|-------------------------|
| Light Block | `light_block` | `470`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.light_block.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values                                                                                                                    | Description                                                         |
|-------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| waterlogged | `false`       | `true`<br/>`false`                                                                                                                | Whether or not there's water in the same place as this light block. |
| level       | `15`          | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | The amount of light this block outputs.                             |

Bedrock Edition:

| Name              | Metadata Bits                       | Default value | Allowed values                                                                                                                    | Values forMetadata Bits                                                                                                           | Description                             |
|-------------------|-------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| block_light_level | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | The amount of light this block outputs. |




