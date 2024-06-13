# Block of Redstone
A block of redstone is a mineral block equivalent to nine redstone dust. It acts as a permanently powered redstone power source that can be pushed by pistons.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Redstone component
- 3 Sounds
- 4 Data values
	- 4.1 ID
- 5 History
- 6 Issues
- 7 Trivia
- 8 Gallery
	- 8.1 Screenshots
- 9 References
- 10 External links

## Obtaining
### Breaking
A block of redstone can be mined using any pickaxe (unlike redstone ore, which requires an iron pickaxe or better).[1] If mined without a pickaxe, a block of redstone drops nothing.

| Block     | Block of Redstone     |
|-----------|-----------------------|
| Hardness  | 5                     |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 25                    |
| Wooden    | 3.75                  |
| Stone     | 1.9                   |
| Iron      | 1.25                  |
| Diamond   | 0.95                  |
| Netherite | 0.85                  |
| Golden    | 0.65                  |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
In each ancient city, 2 blocks of redstone can be found integrated into circuitry within a secret room at the city center.

### Crafting
| Ingredients   | Crafting recipe |
|---------------|-----------------|
| Redstone Dust |                 |

## Usage
A block of redstone can be used as a redstone power source and can be crafted back into redstone dust. It can also be used as storage if the player's inventory is full of redstone dust from mining.

### Crafting ingredient
Blocks of redstone can be crafted back into redstone dust, and thus provide compact storage for redstone, like other blocks of materials (block of iron, block of gold, etc.).

| Name          | Ingredients       | Crafting recipe |
|---------------|-------------------|-----------------|
| Redstone Dust | Block of Redstone | 9               |

### Redstone component
A block of redstone powers dust and repeaters, deactivates attached torches, and activate mechanisms (left) – but does not power adjacent opaque blocks (right).
See also: Redstone circuit

To place a block of redstone, use the Place Block control.

Blocks of redstone are always active and cannot be turned off. A block of redstone:

- powers any adjacentredstone dust, including above or below, topower level15
- powers any adjacentredstone comparatorsorredstone repeatersfacing away from the block of redstone to power level 15
- activates any adjacentmechanism components(doors,redstone lamps, etc.), including above or below, with the exception ofpistons, which cannot be activated by any power source directly in front of them

Adjacent opaque blocks are not powered.

If a redstone torch is attached to a block of redstone, it deactivates after 1 redstone tick and does not reactivate (which is normal behavior for a redstone torch attached to a powered block).

A block of redstone can be moved by a piston. Water and lava flow around a block of redstone without affecting it.

## Data values
### ID
Java Edition:

| Name              | Identifier       | Form         | Translation key                  |
|-------------------|------------------|--------------|----------------------------------|
| Block of Redstone | `redstone_block` | Block & Item | `block.minecraft.redstone_block` |

Bedrock Edition:

| Name              | Identifier       | Numeric ID | Form                       | Item ID[i 1]   | Translation key            |
|-------------------|------------------|------------|----------------------------|----------------|----------------------------|
| Block of Redstone | `redstone_block` | `152`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.redstone_block.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

