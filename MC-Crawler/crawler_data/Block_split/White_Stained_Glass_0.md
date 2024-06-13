# Stained Glass
Stained glass is a dyed variant of the glass block.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Beacon beam color
	- 2.2 Crafting ingredient
- 3 Sounds
- 4 Data values
	- 4.1 ID
- 5 History
	- 5.1 Data history
- 6 Issues
- 7 Trivia
- 8 Gallery
	- 8.1 Screenshots
- 9 See also
- 10 References
- 11 External links

## Obtaining
### Breaking
Stained glass drops itself only if it is broken with a tool enchanted with Silk Touch. Otherwise, it drops nothing.

Stained glass does not have an assigned tool; it is mined at the same speed regardless of what tool is used.[1]

| Block    | Stained Glass       |
|----------|---------------------|
| Hardness | 0.3                 |
|          | Breakingtime (secs) |
| Default  | 0.45                |

### Natural generation
Magenta stained glass blocks naturally generate as windows in end cities.

Magenta stained glass naturally generating in an end city.
Brown stained glass blocks generate in trail ruins.

### Crafting
| Ingredients       | Crafting recipe  |
|-------------------|------------------|
| Glass+MatchingDye | 8888888888888888 |




Ingredients
Crafting recipe
Description


Glass +Bone Meal orLapis Lazuli orCocoa Beans orInk Sac

8888

‌[Bedrock Edition and Minecraft Education  only]



## Usage
Stained glass blocks adjacent to other glass blocks are invisible when viewed through glass that is identical in color.

Mobs cannot normally spawn on stained glass blocks. An exception to this is zombie reinforcements, which can spawn on stained glass blocks (but not stained glass panes).

Stained glass blocks cannot be seen through by mobs, as they treat them as completely opaque. Mobs may look at players through stained glass, but this is purely visual.

Redstone dust and components can be placed on stained glass, but cannot power stained glass. Stained glass can't cut vertical redstone. Vertical redstone can be placed on stained glass. In Java Edition, it transmits redstone signals up, not down. Otherwise, stained glass in redstone circuits is functionally the same as an upside-down slab.

### Beacon beam color
The color of the beam may be changed by placing blocks of stained glass (or stained glass panes) anywhere above the beacon block. The beam changes colors according to the colors of glass placed above it: the first block sets the beam color, while each additional block sets the color by averaging the red, green, and blue components of the current beam color and the block's color. The color values are the same as those for the corresponding dye. This also works using hardened stained glass and hardened stained glass panes.‌[Bedrock Edition and Minecraft Education  only] Stained glass panes have the same effect on the beam as stained glass blocks.

The resulting beam color can be found as C=12n+1(c0+∑i=1n2i−1ci)where ci is the sequence of glass colors (c0 corresponds to the lowest block and cn to the highest one).

As the blending algorithm is considerably simpler than that of leather-dyeing, a much larger part of the sRGB space is available.[more information needed] A player may experiment with stacking glass, although programs that calculate combinations are also available.[2]

With only 15 types of stained glass you can make all colors, for example; red + white stained glass above a beacon will be pink, the more white you add, the lighter the color will be.

An interactive widget is being loaded. If this does not work for you, please reload the page or check if JavaScript is enabled.
### Crafting ingredient
| Name                   | Ingredients                                         | Crafting recipe                  | Description                                                                                    |
|------------------------|-----------------------------------------------------|----------------------------------|------------------------------------------------------------------------------------------------|
| Hardened Stained Glass | Aluminum Oxide+MatchingStained Glass+Boron Trioxide | 3333333333333333                 | A representation ofalumino-borosilicate glass.‌[Bedrock Edition and Minecraft Education  only] |
| Stained Glass Pane     | MatchingStained Glass                               | 16161616161616161616161616161616 |                                                                                                |

## Data values
### ID
Java Edition:

| Name                     | Identifier               | Form         | Block tags  | Translation key                          |
|--------------------------|--------------------------|--------------|-------------|------------------------------------------|
| White Stained Glass      | white_stained_glass      | Block & Item | impermeable | block.minecraft.white_stained_glass      |
| Orange Stained Glass     | orange_stained_glass     | Block & Item | impermeable | block.minecraft.orange_stained_glass     |
| Magenta Stained Glass    | magenta_stained_glass    | Block & Item | impermeable | block.minecraft.magenta_stained_glass    |
| Light Blue Stained Glass | light_blue_stained_glass | Block & Item | impermeable | block.minecraft.light_blue_stained_glass |
| Yellow Stained Glass     | yellow_stained_glass     | Block & Item | impermeable | block.minecraft.yellow_stained_glass     |
| Lime Stained Glass       | lime_stained_glass       | Block & Item | impermeable | block.minecraft.lime_stained_glass       |
| Pink Stained Glass       | pink_stained_glass       | Block & Item | impermeable | block.minecraft.pink_stained_glass       |
| Gray Stained Glass       | gray_stained_glass       | Block & Item | impermeable | block.minecraft.gray_stained_glass       |
| Light Gray Stained Glass | light_gray_stained_glass | Block & Item | impermeable | block.minecraft.light_gray_stained_glass |
| Cyan Stained Glass       | cyan_stained_glass       | Block & Item | impermeable | block.minecraft.cyan_stained_glass       |
| Purple Stained Glass     | purple_stained_glass     | Block & Item | impermeable | block.minecraft.purple_stained_glass     |
| Blue Stained Glass       | blue_stained_glass       | Block & Item | impermeable | block.minecraft.blue_stained_glass       |
| Brown Stained Glass      | brown_stained_glass      | Block & Item | impermeable | block.minecraft.brown_stained_glass      |
| Green Stained Glass      | green_stained_glass      | Block & Item | impermeable | block.minecraft.green_stained_glass      |
| Red Stained Glass        | red_stained_glass        | Block & Item | impermeable | block.minecraft.red_stained_glass        |
| Black Stained Glass      | black_stained_glass      | Block & Item | impermeable | block.minecraft.black_stained_glass      |

Bedrock Edition:

| Name                     | Identifier               | Alias ID           | Numeric ID | Form                       | Item ID[i 1]   | Translation key                    |
|--------------------------|--------------------------|--------------------|------------|----------------------------|----------------|------------------------------------|
| White Stained Glass      | white_stained_glass      | stained_glass / 0  | 241        | Block & Giveable Item[i 2] | Identical[i 3] | tile.stained_glass.white.name      |
| Orange Stained Glass     | orange_stained_glass     | stained_glass / 1  | -673       | Block & Giveable Item[i 2] | Identical[i 3] | tile.stained_glass.orange.name     |
| Magenta Stained Glass    | magenta_stained_glass    | stained_glass / 2  | -674       | Block & Giveable Item[i 2] | Identical[i 3] | tile.stained_glass.magenta.name    |
| Light Blue Stained Glass | light_blue_stained_glass | stained_glass / 3  | -675       | Block & Giveable Item[i 2] | Identical[i 3] | tile.stained_glass.light_blue.name |
| Yellow Stained Glass     | yellow_stained_glass     | stained_glass / 4  | -676       | Block & Giveable Item[i 2] | Identical[i 3] | tile.stained_glass.yellow.name     |
| Lime Stained Glass       | lime_stained_glass       | stained_glass / 5  | -677       | Block & Giveable Item[i 2] | Identical[i 3] | tile.stained_glass.lime.name       |
| Pink Stained Glass       | pink_stained_glass       | stained_glass / 6  | -678       | Block & Giveable Item[i 2] | Identical[i 3] | tile.stained_glass.pink.name       |
| Gray Stained Glass       | gray_stained_glass       | stained_glass / 7  | -679       | Block & Giveable Item[i 2] | Identical[i 3] | tile.stained_glass.gray.name       |
| Light Gray Stained Glass | light_gray_stained_glass | stained_glass / 8  | -680       | Block & Giveable Item[i 2] | Identical[i 3] | tile.stained_glass.silver.name     |
| Cyan Stained Glass       | cyan_stained_glass       | stained_glass / 9  | -681       | Block & Giveable Item[i 2] | Identical[i 3] | tile.stained_glass.cyan.name       |
| Purple Stained Glass     | purple_stained_glass     | stained_glass / 10 | -682       | Block & Giveable Item[i 2] | Identical[i 3] | tile.stained_glass.purple.name     |
| Blue Stained Glass       | blue_stained_glass       | stained_glass / 11 | -683       | Block & Giveable Item[i 2] | Identical[i 3] | tile.stained_glass.blue.name       |
| Brown Stained Glass      | brown_stained_glass      | stained_glass / 12 | -684       | Block & Giveable Item[i 2] | Identical[i 3] | tile.stained_glass.brown.name      |
| Green Stained Glass      | green_stained_glass      | stained_glass / 13 | -685       | Block & Giveable Item[i 2] | Identical[i 3] | tile.stained_glass.green.name      |
| Red Stained Glass        | red_stained_glass        | stained_glass / 14 | -686       | Block & Giveable Item[i 2] | Identical[i 3] | tile.stained_glass.red.name        |
| Black Stained Glass      | black_stained_glass      | stained_glass / 15 | -687       | Block & Giveable Item[i 2] | Identical[i 3] | tile.stained_glass.black.name      |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ a b c d e f g h i j k l m n o p Available with /give command.

↑ a b c d e f g h i j k l m n o p The block's direct item form has the same id as the block.


