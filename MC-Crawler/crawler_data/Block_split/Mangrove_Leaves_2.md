#### Snowy leaves

  

This feature is exclusive to  Bedrock Edition. 


Trees in a snowy biome during snowfall.
In any biome with a base temperature of below 0.15, all leaves exposed to the sky gradually fade to white once snowfall begins, giving them a frosted appearance for the storm's duration. Cherry, azalea, and flowering azalea leaves are not affected, and the change is entirely invisible to the client if the fancy graphics option is disabled (though it still takes place, and leaves are the correct color phase for the time if the option is reenabled). After snowfall ends, leaves gradually fade back to their normal coloration.

## Data values
### ID
Java Edition:

| Name                    | Identifier              | Form         | Block tags                                              | Item tags     | Translation key                         |
|-------------------------|-------------------------|--------------|---------------------------------------------------------|---------------|-----------------------------------------|
| Oak Leaves              | oak_leaves              | Block & Item | lava_pool_stone_cannot_replaceleavesmineable/hoe        | leaves        | block.minecraft.oak_leaves              |
| Spruce Leaves           | spruce_leaves           | Block & Item | lava_pool_stone_cannot_replaceleavesmineable/hoe        | leaves        | block.minecraft.spruce_leaves           |
| Birch Leaves            | birch_leaves            | Block & Item | lava_pool_stone_cannot_replaceleavesmineable/hoe        | leaves        | block.minecraft.birch_leaves            |
| Jungle Leaves           | jungle_leaves           | Block & Item | lava_pool_stone_cannot_replaceleavesmineable/hoe        | leaves        | block.minecraft.jungle_leaves           |
| Acacia Leaves           | acacia_leaves           | Block & Item | lava_pool_stone_cannot_replaceleavesmineable/hoe        | leaves        | block.minecraft.acacia_leaves           |
| Dark Oak Leaves         | dark_oak_leaves         | Block & Item | lava_pool_stone_cannot_replaceleavesmineable/hoe        | leaves        | block.minecraft.dark_oak_leaves         |
| Mangrove Leaves         | mangrove_leaves         | Block & Item | lava_pool_stone_cannot_replaceleavesmineable/hoe        | leaves        | block.minecraft.mangrove_leaves         |
| Cherry Leaves           | cherry_leaves           | Block & Item | lava_pool_stone_cannot_replaceleavesmineable/hoe        | leaves        | block.minecraft.cherry_leaves           |
| Azalea Leaves           | azalea_leaves           | Block & Item | lava_pool_stone_cannot_replaceleavesmineable/hoe        | leaves        | block.minecraft.azalea_leaves           |
| Flowering Azalea Leaves | flowering_azalea_leaves | Block & Item | flowerslava_pool_stone_cannot_replaceleavesmineable/hoe | flowersleaves | block.minecraft.flowering_azalea_leaves |

Bedrock Edition:

| Name                   | Identifier             | Alias ID    | Numeric ID | Form                       | Item ID[i 1]   | Translation key                                   |
|------------------------|------------------------|-------------|------------|----------------------------|----------------|---------------------------------------------------|
| Oak Leaves             | oak_leaves             | leaves / 0  | 18         | Block & Giveable Item[i 2] | Identical[i 3] | tile.leaves.oak.name                              |
| Spruce Leaves          | spruce_leaves          | leaves / 1  | -800       | Block & Giveable Item[i 2] | Identical[i 3] | tile.leaves.spruce.name                           |
| Birch Leaves           | birch_leaves           | leaves / 2  | -801       | Block & Giveable Item[i 2] | Identical[i 3] | tile.leaves.birch.name                            |
| Jungle Leaves          | jungle_leaves          | leaves / 3  | -802       | Block & Giveable Item[i 2] | Identical[i 3] | tile.leaves.jungle.name                           |
| Acacia Leaves          | acacia_leaves          | leaves2 / 0 | 161        | Block & Giveable Item[i 2] | Identical[i 3] | tile.leaves2.acacia.nametile.leaves.acacia.name   |
| Dark Oak Leaves        | dark_oak_leaves        | leaves2 / 1 | -803       | Block & Giveable Item[i 2] | Identical[i 3] | tile.leaves2.big_oak.nametile.leaves.big_oak.name |
| Mangrove Leaves        | mangrove_leaves        | None        | -472       | Block & Giveable Item[i 2] | Identical[i 3] | tile.mangrove_leaves.name                         |
| Cherry Leaves          | cherry_leaves          | None        | -548       | Block & Giveable Item[i 2] | Identical[i 3] | tile.cherry_leaves.name                           |
| Azalea Leaves          | azalea_leaves          | None        | 579        | Block & Giveable Item[i 2] | Identical[i 3] | tile.azalea_leaves.name                           |
| Flowered Azalea Leaves | azalea_leaves_flowered | None        | 580        | Block & Giveable Item[i 2] | Identical[i 3] | tile.azalea_leaves_flowered.name                  |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ a b c d e f g h i j Available with /give command.

↑ a b c d e f g h i j The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values | Description                                                                             |
|-------------|---------------|----------------|-----------------------------------------------------------------------------------------|
| distance    | 7             | 1234567        | How far away this block is from the nearest log or wood, intaxicab distance.            |
| persistent  | false         | falsetrue      | If the block persists regardless of having no wood nearby.truefor player-placed leaves. |
| waterlogged | false         | falsetrue      | Whether or not there's water in the same place as this leaves.                          |

Bedrock Edition:

| Name           | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                                |
|----------------|---------------|---------------|----------------|-------------------------|------------------------------------------------------------|
| persistent_bit | Not Supported | false         | falsetrue      | Unsupported             | If the block persists regardless of having no wood nearby. |
| update_bit     | Not Supported | false         | falsetrue      | Unsupported             | If the block checks for nearby wood and decays.            |




