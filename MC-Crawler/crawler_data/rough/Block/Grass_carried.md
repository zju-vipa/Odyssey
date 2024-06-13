# grass_carried
grass_carried[1] was a block which was used for storing the item model for grass blocks.

## Contents
- 1 Obtaining
- 2 Usage
	- 2.1 Appearance
	- 2.2 Functional differences from grass blocks
- 3 Data values
	- 3.1 ID
- 4 History
- 5 Issues
- 6 References

## Obtaining
grass_carried is only known to be obtainable through the use of inventory editors and other external tools. If placed in a world, the block can be mined instantly with any item, but it does not drop anything regardless of the method used.

## Usage
### Appearance
grass_carried obviously highly resembles the actual grass block. However, there are two key differences between it and normal grass blocks:

- The top texture is a noticeably different color, and in fact matches the side texture much more than normal grass blocks.
	- This is due to this block using a pre-tinted texture, whereas the normal grass block uses a grayscale texture with a constant tint.
- While grass blocks use thedirttexture on the bottom,grass_carrieduses the side texture on the bottom:

### Functional differences from grass blocks
Despite very closely resembling the grass block visually, grass_carried has notable functional differences from normal grass blocks:

- It can be broken instantly.[2]
- It does not drop anything at all when broken.[2]
- It does not have an icon in the inventory.[3]
- It cannot be turned intofarmland.[4]
- Blocks which require a dirt-like block below them to exist, such asflowersandsugar cane, cannot be placed on it.[4]
- Placing an opaque block on top on it does not gradually convert it to dirt.

## Data values
### ID
| Name        | Numeric ID | Form                       | Item ID[i 1]   |
|-------------|------------|----------------------------|----------------|
| Grass Block | `253`      | Block & Giveable Item[i 2] | Identical[i 3] |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

