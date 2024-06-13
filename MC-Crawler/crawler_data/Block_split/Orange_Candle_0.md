# Candle
A candle is block that emits light when lit with a flint and steel. It comes in the sixteen dye colors. Up to four of the same color of candle can be placed in one block space, which affects the amount of light produced.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Container loot
	- 1.4 Crafting
- 2 Usage
	- 2.1 Light
	- 2.2 Cakes
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Trivia
- 8 Gallery
	- 8.1 Renders
		- 8.1.1 Candles
		- 8.1.2 Lit candles
		- 8.1.3 Cake with candle
		- 8.1.4 Cake with lit candle
		- 8.1.5 Item textures
	- 8.2 Screenshots
- 9 References
- 10 External links

## Obtaining
### Breaking
All candles can be mined using any tool, or without a tool.

| Block    | CandleDyed Candle   |
|----------|---------------------|
| Hardness | 0.1                 |
|          | Breakingtime (secs) |
| Default  | 0.15                |

### Natural generation
Non-dyed candles and white candles can be found in ancient cities, and brown, green, purple, and red candles can be found in trail ruins. Red candles can also be found in the trial chambers.

### Container loot
| Item          | Structure    | Container         | Quantity | Chance          |
|---------------|--------------|-------------------|----------|-----------------|
|               |              |                   |          | Java Edition    |
| Brown Candle  | Trail Ruins  | Suspicious gravel | 1        | 4.4%            |
| Candle        | Ancient City | Chest             | 1–4      | 23.2%           |
| Green Candle  | Trail Ruins  | Suspicious gravel | 1        | 4.4%            |
| Purple Candle | Trail Ruins  | Suspicious gravel | 1        | 4.4%            |
| Red Candle    | Trail Ruins  | Suspicious gravel | 1        | 4.4%            |
|               |              |                   |          | Bedrock Edition |
| Brown Candle  | Trail Ruins  | Suspicious gravel | 1        | 4.3%            |
| Candle        | Ancient City | Chest             | 1–4      | 23.2%           |
| Green Candle  | Trail Ruins  | Suspicious gravel | 1        | 4.3%            |
| Purple Candle | Trail Ruins  | Suspicious gravel | 1        | 4.3%            |
| Red Candle    | Trail Ruins  | Suspicious gravel | 1        | 4.3%            |

### Crafting
| Name        | Ingredients        | Crafting recipe |
|-------------|--------------------|-----------------|
| Candle      | String+Honeycomb   |                 |
| Dyed Candle | Candle+MatchingDye |                 |

## Usage
### Light

All candles can be used as a light source, emitting light like a sea pickle. A single candle emits a light level of 3. Up to four identically colored candles may be placed in one block, with each candle increasing the emitted light level by 3, for a maximum light level of 12. They also emit fire particles.

Candles are not lit when they are placed, and must be lit using flint and steel, fire charge, or any flaming projectile. If any candle is already lit, more candle(s) that may be added (if possible) are also lit. In Bedrock Edition, a mob/player that is burning, a Fire Aspect book or any sword enchanted with Fire Aspect can also be used to light candles. Any candle may be waterlogged, but waterlogged candles cannot be lit. Lit candles can be extinguished using water (even a water bottle‌[Java Edition  only]) or by the player interacting with the candle.


### Cakes

A single candle of any color may be used on an uneaten cake, turning it into a candle cake, which acts as a normal, singular candle on top of a cake. If the candle cake is eaten at all or destroyed, the candle is dropped. Interacting with the lit candle (but not the cake) extinguishes it. Interacting with a lit candle cake causes the player to eat it if possible, but if the held item is a flint and steel or fire charge, the appropriate block becomes lit, if possible (otherwise nothing happens).


## Data values
### ID
Java Edition:

| Name              | Identifier        | Form         | Translation key                   |
|-------------------|-------------------|--------------|-----------------------------------|
| Candle            | candle            | Block & Item | block.minecraft.candle            |
| White Candle      | white_candle      | Block & Item | block.minecraft.white_candle      |
| Orange Candle     | orange_candle     | Block & Item | block.minecraft.orange_candle     |
| Magenta Candle    | magenta_candle    | Block & Item | block.minecraft.magenta_candle    |
| Light Blue Candle | light_blue_candle | Block & Item | block.minecraft.light_blue_candle |
| Yellow Candle     | yellow_candle     | Block & Item | block.minecraft.yellow_candle     |
| Lime Candle       | lime_candle       | Block & Item | block.minecraft.lime_candle       |
| Pink Candle       | pink_candle       | Block & Item | block.minecraft.pink_candle       |
| Gray Candle       | gray_candle       | Block & Item | block.minecraft.gray_candle       |
| Light Gray Candle | light_gray_candle | Block & Item | block.minecraft.light_gray_candle |
| Cyan Candle       | cyan_candle       | Block & Item | block.minecraft.cyan_candle       |
| Purple Candle     | purple_candle     | Block & Item | block.minecraft.purple_candle     |
| Blue Candle       | blue_candle       | Block & Item | block.minecraft.blue_candle       |
| Brown Candle      | brown_candle      | Block & Item | block.minecraft.brown_candle      |
| Green Candle      | green_candle      | Block & Item | block.minecraft.green_candle      |
| Red Candle        | red_candle        | Block & Item | block.minecraft.red_candle        |
| Black Candle      | black_candle      | Block & Item | block.minecraft.black_candle      |

Bedrock Edition:

| Name              | Identifier        | Numeric ID | Form                       | Item ID[i 1]   | Translation key             |
|-------------------|-------------------|------------|----------------------------|----------------|-----------------------------|
| Candle            | candle            | 667        | Block & Giveable Item[i 2] | Identical[i 3] | tile.candle.name            |
| White Candle      | white_candle      | 668        | Block & Giveable Item[i 2] | Identical[i 3] | tile.white_candle.name      |
| Orange Candle     | orange_candle     | 669        | Block & Giveable Item[i 2] | Identical[i 3] | tile.orange_candle.name     |
| Magenta Candle    | magenta_candle    | 670        | Block & Giveable Item[i 2] | Identical[i 3] | tile.magenta_candle.name    |
| Light Blue Candle | light_blue_candle | 671        | Block & Giveable Item[i 2] | Identical[i 3] | tile.light_blue_candle.name |
| Yellow Candle     | yellow_candle     | 672        | Block & Giveable Item[i 2] | Identical[i 3] | tile.yellow_candle.name     |
| Lime Candle       | lime_candle       | 673        | Block & Giveable Item[i 2] | Identical[i 3] | tile.lime_candle.name       |
| Pink Candle       | pink_candle       | 674        | Block & Giveable Item[i 2] | Identical[i 3] | tile.pink_candle.name       |
| Gray Candle       | gray_candle       | 675        | Block & Giveable Item[i 2] | Identical[i 3] | tile.gray_candle.name       |
| Light Gray Candle | light_gray_candle | 676        | Block & Giveable Item[i 2] | Identical[i 3] | tile.light_gray_candle.name |
| Cyan Candle       | cyan_candle       | 677        | Block & Giveable Item[i 2] | Identical[i 3] | tile.cyan_candle.name       |
| Purple Candle     | purple_candle     | 678        | Block & Giveable Item[i 2] | Identical[i 3] | tile.purple_candle.name     |
| Blue Candle       | blue_candle       | 679        | Block & Giveable Item[i 2] | Identical[i 3] | tile.blue_candle.name       |
| Brown Candle      | brown_candle      | 680        | Block & Giveable Item[i 2] | Identical[i 3] | tile.brown_candle.name      |
| Green Candle      | green_candle      | 681        | Block & Giveable Item[i 2] | Identical[i 3] | tile.green_candle.name      |
| Red Candle        | red_candle        | 682        | Block & Giveable Item[i 2] | Identical[i 3] | tile.red_candle.name        |
| Black Candle      | black_candle      | 683        | Block & Giveable Item[i 2] | Identical[i 3] | tile.black_candle.name      |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ a b c d e f g h i j k l m n o p q Available with /give command.

↑ a b c d e f g h i j k l m n o p q The block's direct item form has the same id as the block.


