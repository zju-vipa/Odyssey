### Pandas
Bamboo items are eaten by pandas and can be used to speed up the growth of baby pandas. Bamboo can also be used to breed pandas when at least 1 bamboo block (not a bamboo shoot) is within 5 blocks of the pandas, making the panda the only animal in the game to have extra breeding requirements. At this point, the player can feed them bamboo and they mate to have a baby.

### Fuel
Bamboo can be used as fuel for smelting. Each bamboo item smelts 0.25 items. Crafting two bamboo into a stick and using that as fuel is equivalent, smelting 0.5 items.

Bamboo can be crafted into other items to increase its fuel efficiency.

- By crafting 9 bamboo into 2bamboo planks, 3 items can be smelted instead of 2.25, a 33.3% increase in efficiency.
	- InBedrock Edition, the fuel efficiency can be further doubled by crafting the bamboo planks into twice the amount ofslabs.[4]

### Flower pots
Bamboo can be placed in a flower pot, where it retains the design it has in its item form.

### Crafting ingredient
| Name            | Ingredients        | Crafting recipe | Description                           |
|-----------------|--------------------|-----------------|---------------------------------------|
| Block of Bamboo | Bamboo             |                 | Cannot be crafted back into 9 bamboo. |
| Scaffolding     | Bamboo+<br/>String | 6               |                                       |
| Stick           | Bamboo             |                 |                                       |

## Appearance
The different stages of bamboo growth.
The appearance of bamboo changes as it grows. When first placed, it takes the form of a small shoot, which has no hitbox. When it grows one block taller it grows to 2 pixels in length and width and the top block has leaves coming off it. At 3 blocks, the top 2 blocks have leaves and at 4 blocks the bamboo expands to 3×3 pixels. At 5 blocks tall, the top 3 blocks have leaves on them. As the bamboo grows, the leaves move up and stay at the top 3 blocks. Destroying a block of bamboo does not change the appearance of the blocks below it. Bamboo is oriented at a random position in the block that it is in.

## Data values
### ID
Java Edition:

| Name         | Identifier       | Form         | Block tags            | Translation key                  |
|--------------|------------------|--------------|-----------------------|----------------------------------|
| Bamboo       | `bamboo`         | Block & Item | `bamboo_plantable_on` | `block.minecraft.bamboo`         |
| Bamboo Shoot | `bamboo_sapling` | Block        | `bamboo_plantable_on` | `block.minecraft.bamboo_sapling` |

Bedrock Edition:

| Name           | Identifier       | Numeric ID | Form                         | Item ID[i 1]   | Translation key    |
|----------------|------------------|------------|------------------------------|----------------|--------------------|
| Bamboo         | `bamboo`         | `418`      | Block & Giveable Item[i 2]   | Identical[i 3] | `tile.bamboo.name` |
| Bamboo Sapling | `bamboo_sapling` | `419`      | Block & Ungiveable Item[i 4] | Identical[i 3] | —                  |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑ a bThe block's direct item form has the same id as the block.
4. ↑Unavailable with /give command

### Block states
See also: Block states

Java Edition:
Bamboo

| Name   | Default value | Allowed values                 | Description                                                                                                |
|--------|---------------|--------------------------------|------------------------------------------------------------------------------------------------------------|
| age    | `0`           | `0`<br/>`1`                    | The age of the bamboo, if this is 1 the bamboo appears thicker.                                            |
| leaves | `none`        | `large`<br/>`none`<br/>`small` | The size of the leaves on this bamboo block.                                                               |
| stage  | `0`           | `0`<br/>`1`                    | The stage is incremented at random intervals.<br/>At stage 1, bamboo may try to grow more bamboo above it. |

Bedrock Edition:
Bamboo:

| Name                   | Metadata Bits   | Default value | Allowed values                                    | Values forMetadata Bits | Description                                                                                               |
|------------------------|-----------------|---------------|---------------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------------------------|
| age_bit                | `0x8`           | `false`       | `false`<br/>`true`                                | `0`<br/>`1`             | The stage is incremented at random intervals.<br/>When true, bamboo may try to grow more bamboo above it. |
| bamboo_leaf_size       | `0x2`<br/>`0x4` | `no_leaves`   | `no_leaves`<br/>`small_leaves`<br/>`large_leaves` | `0`<br/>`1`<br/>`2`     | The size of the leaves on this bamboo block.                                                              |
| bamboo_stalk_thickness | `0x1`           | `thin`        | `thin`<br/>`thick`                                | `0`<br/>`1`             | The thickness of the bamboo, if this is thick the bamboo appears thicker.                                 |

Bamboo Sapling:

| Name         | Metadata Bits | Default value | Allowed values                                                          | Values forMetadata Bits | Description                           |
|--------------|---------------|---------------|-------------------------------------------------------------------------|-------------------------|---------------------------------------|
| age_bit      | `0x1`         | `false`       | `false`<br/>`true`                                                      | `0`<br/>`1`             | Specifies the sapling's growth stage. |
| sapling_type | Not Supported | `oak`         | `acacia`<br/>`birch`<br/>`dark_oak`<br/>`jungle`<br/>`oak`<br/>`spruce` | `Unsupported`           | Unused.                               |




