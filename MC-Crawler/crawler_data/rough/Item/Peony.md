# Peony
A peony is a tall flower that can be crafted into pink dye.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Post-generation
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Bees
	- 2.3 Breeding
	- 2.4 Bee nests
	- 2.5 Composting
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
	- 5.1 Data history
- 6 Issues
- 7 Trivia
- 8 References
- 9 External links

## Obtaining
### Breaking
A peony can be broken instantly with any item or by hand, dropping itself.

A peony also breaks if water or lava runs over its location, if a piston extends or pushes a block into its location, or if a block under the plant is moved or destroyed.

| Block    | Peony               |
|----------|---------------------|
| Hardness | 0                   |
|          | Breakingtime (secs) |
| Default  | 0.05                |

### Natural generation
Peonies generate naturally on dirt and grass blocks in  forest,  flower forest,  birch forest,  old growth birch forest, and  dark forest biomes as part of vegetation features.


### Post-generation
Main article: Flower § Post-generation
When bone meal is applied to a peony, the flower drops a copy of itself.

## Usage
Main article: Flower § Usage
Like other flowers, peonies can be used as decoration and planted on grass blocks, dirt, coarse dirt, rooted dirt, farmland, podzol, mycelium, moss blocks, mud, or muddy mangrove roots. Like other tall flowers, peonies cannot be placed inside flower pots. 

### Crafting ingredient
| Name     | Ingredients | Crafting recipe |
|----------|-------------|-----------------|
| Pink Dye | Peony       | 2               |

### Bees
Bees engage in a pollinating behavior with peonies, increasing the honey level in beehives and bee nests by 1.

### Breeding
Peonies can be used to breed, grow, and lead bees.

### Bee nests
Oak, birch, and cherry trees grown from saplings that are within 2 blocks of a peony have a 5% chance to grow with a bee nest and 1-3 bees in it.

### Composting
Placing a peony into a composter has a 65% chance of raising the compost level by 1. A stack of peonies yields an average of 5.94 bone meal.

## Data values
### ID
Java Edition:

| Name  | Identifier | Form         | Block tags                   | Item tags                    | Translation key         |
|-------|------------|--------------|------------------------------|------------------------------|-------------------------|
| Peony | `peony`    | Block & Item | `flowers`<br/>`tall_flowers` | `flowers`<br/>`tall_flowers` | `block.minecraft.peony` |

Bedrock Edition:

| Name  | Identifier                       | Alias ID           | Numeric ID | Form                       | Item ID[i 1]   | Translation key                  |
|-------|----------------------------------|--------------------|------------|----------------------------|----------------|----------------------------------|
| Peony | `double_plant‌[until BE 1.21.0]` | None               | `175`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.double_plant.paeonia.name` |
| Peony | `peony‌[upcoming: BE 1.21.0]`    | `double_plant / 5` | `-867`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.double_plant.paeonia.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑ a bAvailable with /give command.
3. ↑ a bThe block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name | Default value | Allowed values      | Description                                    |
|------|---------------|---------------------|------------------------------------------------|
| half | `lower`       | `lower`<br/>`upper` | The half of the plant contained in this block. |

Bedrock Edition:

| Name              | Metadata Bits             | Default value | Allowed values     | Values forMetadata Bits | Description                                               |
|-------------------|---------------------------|---------------|--------------------|-------------------------|-----------------------------------------------------------|
| double_plant_type | `0x1`<br/>`0x2`<br/>`0x4` | `sunflower`   | `sunflower`        | `0`                     | Sunflower                                                 |
|                   |                           |               | `syringa`          | `1`                     | Lilac                                                     |
|                   |                           |               | `grass`            | `2`                     | Double Tallgrass                                          |
|                   |                           |               | `fern`             | `3`                     | Large Fern                                                |
|                   |                           |               | `rose`             | `4`                     | Rose Bush                                                 |
|                   |                           |               | `paeonia`          | `5`                     | Peony                                                     |
| upper_block_bit   | `0x8`                     | `false`       | `false`<br/>`true` | `0`<br/>`1`             | If it is the upper half of the plant. For items, it is 0. |

