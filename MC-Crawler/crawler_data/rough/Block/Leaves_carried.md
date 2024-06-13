# leaves_carried
leaves_carried[1] was a block that was used as the item model for leaves.

## Contents
- 1 Obtaining
	- 1.1 Breaking
- 2 Usage
	- 2.1 Appearance
	- 2.2 Functional differences from leaves
- 3 Data values
	- 3.1 ID
- 4 History
- 5 Issues
- 6 References

## Obtaining
leaves_carried is known to be obtainable only through the use of inventory editors and other external tools.

### Breaking
The speed at which leaves_carried breaks is not currently known.[needs testing] They drop themselves when broken with shears.[needs testing]

| Block    | BlockSprite leaves-carried.png: Sprite image for leaves-carried in Minecraft linking to leaves_carriedleaves_carried |
|----------|----------------------------------------------------------------------------------------------------------------------|
| Hardness | 0                                                                                                                    |
|          | Breakingtime (secs)                                                                                                  |
| Default  | 0.05                                                                                                                 |

## Usage
### Appearance
In its base state, leaves_carried highly resembles actual leaves. There are, however, differences: the main difference is that it appears darker than normal leaves, which is due to them using a tint, despite the texture they use already being colored, rather than the grayscale that tinted blocks usually use. Specifically, this tint is the color  #48b518.

However, higher metadata versions of leaves_carried behave unexpectedly. Perhaps most interesting is metadata 1, which corresponds to spruce leaves, which uses a crafting table's side textures rather than anything relevant to leaves. This could be explainable through examination of terrain.png, however, this is yet to be done.[more information needed]

Metadata 1 (corresponding to spruce leaves) is tinted with  #619961, and metadata 2 (corresponding to birch leaves) is tinted with  #80a755. The behavior of metadata 3, which corresponds to what would eventually become jungle leaves in the same version that removes leaves_carried, is currently unknown.[more information needed]

- leaves_carried with metadata 0, Fast graphics
- leaves_carried with metadata 1, Fast graphics
- leaves_carried with metadata 2, Fast graphics
- leaves_carried with metadata 0, Fancy graphics
- leaves_carried with metadata 1, Fancy graphics
- leaves_carried with metadata 2, Fancy graphics

### Functional differences from leaves
Despite very closely resembling leaves visually, leaves_carried do not decay.

Other differences, such as whether they drop saplings when broken without shears, or indeed drop anything at all, are unknown.[more information needed]

## Data values

  

This section is missing information about Metadata variants in table format. 
Please expand the section to include this information. Further details may exist on the talk page.


### ID
| Name   | Numeric ID | Form                       | Item ID[i 1]   |
|--------|------------|----------------------------|----------------|
| Leaves | `254`      | Block & Giveable Item[i 2] | Identical[i 3] |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

