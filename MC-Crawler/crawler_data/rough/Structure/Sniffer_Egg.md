# Sniffer Egg
A sniffer egg is a block that can be brushed out of suspicious sand in warm ocean ruins, or obtained by breeding two sniffers. It slowly hatches into a snifflet (baby sniffer) when placed as a block in the world, which takes half as much time when it is placed on a moss block.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Mob loot
	- 1.3 Archaeology
- 2 Usage
	- 2.1 Placing
	- 2.2 Hatching
	- 2.3 Piston interactivity
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 Advancements
- 6 History
- 7 Issues
- 8 Gallery
	- 8.1 Screenshots
	- 8.2 In other media
- 9 References

## Obtaining
### Breaking
Sniffer eggs can be mined with any tool, even with bare hands, and always drop themselves. Unlike turtle eggs, Silk Touch is not needed.[1]

| Block    | Sniffer Egg         |
|----------|---------------------|
| Hardness | 0.5                 |
|          | Breakingtime (secs) |
| Default  | 0.75                |

### Mob loot
Sniffer eggs can also be obtained by breeding two sniffers with torchflower seeds. Unlike turtle eggs or frogspawn which are placed into the world in block form, sniffer eggs are dropped as items, similar to chicken eggs.

### Archaeology
| Item        | Structure   | Container                  | Quantity | Chance                         |
|-------------|-------------|----------------------------|----------|--------------------------------|
|             |             |                            |          | Java EditionandBedrock Edition |
| Sniffer Egg | Ocean ruins | Warm ruins suspicious sand | 1        | 6.7%                           |

## Usage
### Placing
Sniffer eggs can be placed in block form and slowly hatch into snifflets. 

Sniffer eggs do not require a supporting block below.[2] Unlike dragon eggs, they are not affected by gravity.

### Hatching
Sniffer eggs crack over time and hatch after cracking twice. They hatch in 20 minutes, and they hatch twice as fast, in 10 minutes, on moss blocks.

Sniffer eggs do not need to receive random ticks to hatch. Therefore, the hatching speed of sniffer eggs is not affected by the randomTickSpeed game rule.[3]

### Piston interactivity
Sniffer eggs can be pushed and pulled by pistons.[4]

## Data values
### ID
Java Edition:

| Name        | Identifier    | Form         | Translation key               |
|-------------|---------------|--------------|-------------------------------|
| Sniffer Egg | `sniffer_egg` | Block & Item | `block.minecraft.sniffer_egg` |

Bedrock Edition:

| Name        | Identifier    | Numeric ID | Form                       | Item ID[i 1]   | Translation key         |
|-------------|---------------|------------|----------------------------|----------------|-------------------------|
| Sniffer Egg | `sniffer_egg` | `-596`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.sniffer_egg.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name  | Default value | Allowed values      | Description                                                                          |
|-------|---------------|---------------------|--------------------------------------------------------------------------------------|
| hatch | `0`           | `0`<br/>`1`<br/>`2` | Determines how close an egg is to hatching; starts at 0 and is randomly incremented. |

Bedrock Edition:

| Name          | Metadata Bits | Default value | Allowed values                              | Values forMetadata Bits | Description                                                                                  |
|---------------|---------------|---------------|---------------------------------------------|-------------------------|----------------------------------------------------------------------------------------------|
| cracked_state | Not Supported | `no_cracks`   | `no_cracks`<br/>`cracked`<br/>`max_cracked` | `Unsupported`           | Determines how close an egg is to hatching; starts at no cracks and is randomly incremented. |

