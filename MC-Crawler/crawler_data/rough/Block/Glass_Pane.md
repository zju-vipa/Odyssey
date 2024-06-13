# Glass Pane
A glass pane is a transparent block that can be used as a more efficient alternative to glass blocks. It can be dyed into stained glass panes.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Placement
	- 2.2 Crafting ingredient
	- 2.3 Locking maps
	- 2.4 Trading
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Screenshots
- 8 References
- 9 External links

## Obtaining
### Breaking
Glass panes can be obtained using a tool enchanted with Silk Touch. If one is broken without a Silk Touch enchantment, it drops nothing.

Glass panes do not have an assigned tool; they are mined at the same speed regardless of what tool is used.[1]

| Block    | Glass Pane          |
|----------|---------------------|
| Hardness | 0.3                 |
|          | Breakingtime (secs) |
| Default  | 0.45                |

### Natural generation
Glass panes generate naturally as windows in villages, woodland mansions, and ancient cities.

### Crafting
| Ingredients | Crafting recipe |
|-------------|-----------------|
| Glass       | 16              |

## Usage
Glass panes are more efficient to use than glass blocks, as six glass blocks can be crafted into sixteen glass panes, yielding 22⁄3 panes per block. Windows built using glass panes can be up to 267% (22⁄3 times) larger in area than windows built with regular glass blocks.

A single space between two glass panes results in a 2×1 hole, which spiders can pass through.
### Placement
If placed without anything on the sides, they appear as a thin vertical • shape, 2×2 pixels in size; but when other blocks occupy adjacent spaces, it becomes flat or turns into a  or  or  shape depending on the items surrounding it. The collision box is identical to the shape of the pane. Therefore, two glass panes placed with one empty space in between forms a gap that is two blocks wide.

Glass panes are never oriented horizontally. Horizontal glass surfaces must be made from glass blocks.

Glass panes can be waterlogged, which means water can be in the same place as a glass pane, unlike regular glass.

### Crafting ingredient
| Name                                                                                  | Ingredients                                                  | Crafting recipe  | Description                                                                                    |
|---------------------------------------------------------------------------------------|--------------------------------------------------------------|------------------|------------------------------------------------------------------------------------------------|
| Blue Stained Glass Paneor<br/>Brown Stained Glass Paneor<br/>Black Stained Glass Pane | Glass Pane+<br/>Lapis Lazulior<br/>Cocoa Beansor<br/>Ink Sac | 888              | ‌[Bedrock Edition and Minecraft Education  only]                                               |
| Hardened Glass Pane                                                                   | Aluminum Oxide+<br/>Glass Pane+<br/>Boron Trioxide           | 3                | A representation ofalumino-borosilicate glass.‌[Bedrock Edition and Minecraft Education  only] |
| Stained Glass Pane                                                                    | Glass Pane+<br/>MatchingDye                                  | 8888888888888888 |                                                                                                |

### Locking maps
Glass panes can be used in cartography tables to lock maps, which makes them unable to be filled again when exploring.

### Trading
Apprentice-level cartographer villagers buy 11 glass panes for an emerald as part of their trades.

## Data values
### ID
Java Edition:

| Name       | Identifier   | Form         | Translation key              |
|------------|--------------|--------------|------------------------------|
| Glass Pane | `glass_pane` | Block & Item | `block.minecraft.glass_pane` |

Bedrock Edition:

| Name       | Identifier   | Alias ID | Numeric ID | Form                       | Item ID[i 1]   | Translation key        |
|------------|--------------|----------|------------|----------------------------|----------------|------------------------|
| Glass Pane | `glass_pane` | None     | `102`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.glass_pane.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values     | Description                                                          |
|-------------|---------------|--------------------|----------------------------------------------------------------------|
| east        | `false`       | `false`<br/>`true` | When true, the glass pane extends from the center post to the east.  |
| north       | `false`       | `false`<br/>`true` | When true, the glass pane extends from the center post to the north. |
| south       | `false`       | `false`<br/>`true` | When true, the glass pane extends from the center post to the south. |
| waterlogged | `false`       | `false`<br/>`true` | Whether or not there's water in the same place as this glass pane.   |
| west        | `false`       | `false`<br/>`true` | When true, the glass pane extends from the center post to the west.  |



