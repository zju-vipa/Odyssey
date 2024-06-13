### Fuel
Bamboo can be used as fuel for smelting. Each bamboo item smelts 0.25 items. Crafting two bamboo into a stick and using that as fuel is equivalent, smelting 0.5 items.

Bamboo can be crafted into other items to increase its fuel efficiency.

- By crafting 9 bamboo into 2bamboo planks, 3 items can be smelted instead of 2.25, a 33.3% increase in efficiency.
	- InBedrock Edition, the fuel efficiency can be further doubled by crafting the bamboo planks into twice the amount ofslabs.[4]

### Flower pots
Bamboo can be placed in a flower pot, where it retains the design it has in its item form.

### Crafting ingredient
| Name            | Ingredients   | Crafting recipe | Description                           |
|-----------------|---------------|-----------------|---------------------------------------|
| Block of Bamboo | Bamboo        |                 | Cannot be crafted back into 9 bamboo. |
| Scaffolding     | Bamboo+String | 6               |                                       |
| Stick           | Bamboo        |                 |                                       |

## Appearance
The different stages of bamboo growth.
The appearance of bamboo changes as it grows. When first placed, it takes the form of a small shoot, which has no hitbox. When it grows one block taller it grows to 2 pixels in length and width and the top block has leaves coming off it. At 3 blocks, the top 2 blocks have leaves and at 4 blocks the bamboo expands to 3×3 pixels. At 5 blocks tall, the top 3 blocks have leaves on them. As the bamboo grows, the leaves move up and stay at the top 3 blocks. Destroying a block of bamboo does not change the appearance of the blocks below it. Bamboo is oriented at a random position in the block that it is in.

## Data values
### ID
Java Edition:

| Name         | Identifier     | Form         | Block tags          | Translation key                |
|--------------|----------------|--------------|---------------------|--------------------------------|
| Bamboo       | bamboo         | Block & Item | bamboo_plantable_on | block.minecraft.bamboo         |
| Bamboo Shoot | bamboo_sapling | Block        | bamboo_plantable_on | block.minecraft.bamboo_sapling |

Bedrock Edition:

| Name           | Identifier     | Numeric ID | Form                         | Item ID[i 1]   | Translation key  |
|----------------|----------------|------------|------------------------------|----------------|------------------|
| Bamboo         | bamboo         | 418        | Block & Giveable Item[i 2]   | Identical[i 3] | tile.bamboo.name |
| Bamboo Sapling | bamboo_sapling | 419        | Block & Ungiveable Item[i 4] | Identical[i 3] | —                |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ a b The block's direct item form has the same id as the block.

↑ Unavailable with /give command


### Block states
See also: Block states

Java Edition:
Bamboo

| Name   | Default value | Allowed values | Description                                                                                           |
|--------|---------------|----------------|-------------------------------------------------------------------------------------------------------|
| age    | 0             | 01             | The age of the bamboo, if this is 1 the bamboo appears thicker.                                       |
| leaves | none          | largenonesmall | The size of the leaves on this bamboo block.                                                          |
| stage  | 0             | 01             | The stage is incremented at random intervals.At stage 1, bamboo may try to grow more bamboo above it. |

Bedrock Edition:
Bamboo:

| Name                   | Metadata Bits | Default value | Allowed values                    | Values forMetadata Bits | Description                                                                                          |
|------------------------|---------------|---------------|-----------------------------------|-------------------------|------------------------------------------------------------------------------------------------------|
| age_bit                | 0x8           | false         | falsetrue                         | 01                      | The stage is incremented at random intervals.When true, bamboo may try to grow more bamboo above it. |
| bamboo_leaf_size       | 0x20x4        | no_leaves     | no_leavessmall_leaveslarge_leaves | 012                     | The size of the leaves on this bamboo block.                                                         |
| bamboo_stalk_thickness | 0x1           | thin          | thinthick                         | 01                      | The thickness of the bamboo, if this is thick the bamboo appears thicker.                            |

Bamboo Sapling:

| Name         | Metadata Bits | Default value | Allowed values                     | Values forMetadata Bits | Description                           |
|--------------|---------------|---------------|------------------------------------|-------------------------|---------------------------------------|
| age_bit      | 0x1           | false         | falsetrue                          | 01                      | Specifies the sapling's growth stage. |
| sapling_type | Not Supported | oak           | acaciabirchdark_oakjungleoakspruce | Unsupported             | Unused.                               |




