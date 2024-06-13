# Funky Portal
The funky portal is a joke block introduced in Java Edition 20w14∞ that allows entry into randomly generated dimensions. It is a colored variant of the nether portal block with the color being determined by the destination dimension.

## Contents
- 1 Obtaining
	- 1.1 Breaking
- 2 Usage
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Block data
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Renders
	- 7.2 Textures

## Obtaining
The funky portal block cannot be obtained as an item even by using the /give command. The funky portal block can be placed using commands such as /fill or /setblock and is generated when throwing a written book into a nether portal. After throwing the book into the portal, the book is destroyed.  It does not go through the portal after having changed it. The generated portal has a random destination, unless the text leads to an Easter Egg dimension. Rarely, when throwing the book into the portal, the nether portal turns into multiple funky portal colors. Each book generates its own dimension, and books with the same page content generate the same dimension. Using /setblock ~ ~ ~ neither_portal sets the block and give it randomized block data as to its destination dimension. The color of a funky portal is determined by its destination dimension. The color of any portal can be found by converting its dimension ID into hexadecimal. The last six digits of that number is the RGB color.

### Breaking
Funky portal blocks cannot be broken by tools except in creative mode, but can be destroyed by breaking the portal frame, by explosions, or by placing a liquid inside the portal.

## Usage
Running /data get block on funky portal blocks returns the data that includes the name of the dimension.

## Data values
### ID
| Name         | Identifier     | Form  | Translation key                |
|--------------|----------------|-------|--------------------------------|
| Funky Portal | neither_portal | Block | block.minecraft.neither_portal |

### Block states
See also: Block states

| Name | Default value | Allowed values | Description                              |
|------|---------------|----------------|------------------------------------------|
| axis | x             | x              | The portal's long edge runs east–west.   |
|      |               | z              | The portal's long edge runs north–south. |

### Block data
A funky portal has a block entity associated with it that holds additional data about the block.

See also: Block entity format


 Block entity data
Tags common to all block entities
 Dimension: The ID of the dimension the portal links to.


