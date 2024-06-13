# Powerful Potato
A powerful potato is a block which can be found in the Potato dimension in 24w14potato.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
- 2 Usage
	- 2.1 Growing
	- 2.2 Piston interactivity
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Screenshots

## Obtaining
### Breaking
| Block    | Powerful Potato     |
|----------|---------------------|
| Hardness | 0.4                 |
|          | Breakingtime (secs) |
| Default  | 0.6                 |

### Natural generation
Powerful potatoes generate rarely in the wasteland biome, in Potato dimension. They drop when broken with any tool or by hand.

## Usage
### Growing
A powerful potato grows in a similar way to the chorus tree, but downwards. Naturally found powerful potatoes have the age parameter set to 3, and a number of weak roots growing down from the block into the terrain of Potato dimension. They don't grow further.

When mined and replaced, the age parameter is reset to 0. Powerful potato starts growing strong roots instead of weak roots - both downward and to the sides. Any block that is replaced by the strong roots is dropped on top of the powerful potato. It doesn't seem like this process ever ends by itself: strong roots aren't replaced by weak roots, and age of the powerful potato doesn't increase. Infinite growth can be stopped only by destroying the powerful potato block.

### Piston interactivity
Powerful potatoes are destroyed when pushed by pistons. They do not stick to sticky pistons, slime blocks or honey blocks.

## Data values
### ID
| Name            | Identifier        | Translation key                   |
|-----------------|-------------------|-----------------------------------|
| Powerful Potato | `powerful_potato` | `block.minecraft.powerful_potato` |

### Block states
See also: Block states

| Name | Default value | Allowed values              | Description                                                           |
|------|---------------|-----------------------------|-----------------------------------------------------------------------|
| age  | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | The powerful potato can only grow strong roots when its age is not 3. |

