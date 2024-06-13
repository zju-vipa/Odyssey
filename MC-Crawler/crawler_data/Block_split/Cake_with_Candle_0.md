# Cake
Cake is a food and a block that can be eaten by the player.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Chest loot
	- 1.3 Crafting
	- 1.4 Trading
- 2 Usage
	- 2.1 Pandas
	- 2.2 Composting
	- 2.3 Piston interactivity
	- 2.4 Cakes with candles
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 Achievements
- 6 Advancements
- 7 History
	- 7.1 Cake "item"
		- 7.1.1 Appearances
		- 7.1.2 Names
- 8 Issues
- 9 Trivia
	- 9.1 Interaction
	- 9.2 Miscellaneous
- 10 Gallery
	- 10.1 Renders
		- 10.1.1 Cake
		- 10.1.2 Cake with candle
		- 10.1.3 Lit cake with candle
	- 10.2 Screenshots
- 11 References

## Obtaining
### Breaking
Once the cake is placed, it cannot be recollected even with the use of Silk Touch. Candle cakes always drop their respective candle when broken.

| Block    | Cake                |
|----------|---------------------|
| Hardness | 0.5                 |
|          | Breakingtime (secs) |
| Default  | 0.75                |

### Chest loot
| Item | Structure       | Container          | Quantity | Chance          |
|------|-----------------|--------------------|----------|-----------------|
|      |                 |                    |          | Java Edition    |
| Cake | Trial Chambers  | Intersection chest | 1–4      | 39.7%           |
|      |                 |                    |          | Bedrock Edition |
| Cake | Buried Treasure | Chest              | 1        | 4.1%            |
|      | Trial Chambers  | Intersection chest | 1–4      | 39.7%           |

### Crafting
| Ingredients                 | Crafting recipe | Description                                                      |
|-----------------------------|-----------------|------------------------------------------------------------------|
| Milk Bucket+Sugar+Egg+Wheat |                 | Emptybucketsremain in the crafting grid after crafting the cake. |

### Trading
Expert-level farmer villagers can sell cake for a single emerald each. The chance is 2⁄7 in Java Edition.

## Usage
See also: Tutorials/Hunger management

Sunny and Alex eating a cake together.
Unlike most food, the cake cannot be eaten as an item in the hotbar. Before being eaten, it must first be placed on top of a solid block. Placing the cake on a slab also works, as the slab acts like a solid block. The cake instead floats half a block on top of the slab.

Each cake has seven "slices"; each use consumes one slice progressing inward from the west. A single slice restores 2 () hunger and 0.4 hunger saturation. Eating all seven slices of a cake restores 14 ( × 7) hunger and 2.8 hunger saturation.

Since eating a cake comes with no animation, the cake can be eaten at a rate of one slice per tick. Multiple players can eat from the same cake at the same time. In Java Edition, eating cake makes no sound, unlike other foods.

As a redstone component, when connected to a comparator, a whole cake emits a signal strength of 14. The signal strength decreases two units with each slice.

Cake destroys falling blocks if placed under them, similar to a torch.

### Pandas
Some pandas move toward a dropped cake to pick up and eat it. Some may not, depending on the cake's location. 

### Composting
Placing a cake into a composter raises the compost level by 1.

### Piston interactivity
A cake is broken when pushed by a piston, and it drops nothing.

### Cakes with candles
A cake with candle created by placing a candle on an uneaten cake.
Using a candle on an uneaten cake creates a candle cake of that color (including uncolored). Eating any of the cake causes the candle to drop. 

Using flint and steel, fire charge, or any flaming projectile on an unlit candle cake lights its candle. Lit candle cakes emit a light level of 3. Interacting with the lit candle (but not the cake) extinguishes it.

## Data values
### ID
Java Edition:

| Name                        | Identifier             | Form         | Block tags   | Translation key                        |
|-----------------------------|------------------------|--------------|--------------|----------------------------------------|
| Cake                        | cake                   | Block & Item | None         | block.minecraft.cake                   |
| Cake with Candle            | candle_cake            | Block        | candle_cakes | block.minecraft.candle_cake            |
| Cake with White Candle      | white_candle_cake      | Block        | candle_cakes | block.minecraft.white_candle_cake      |
| Cake with Orange Candle     | orange_candle_cake     | Block        | candle_cakes | block.minecraft.orange_candle_cake     |
| Cake with Magenta Candle    | magenta_candle_cake    | Block        | candle_cakes | block.minecraft.magenta_candle_cake    |
| Cake with Light Blue Candle | light_blue_candle_cake | Block        | candle_cakes | block.minecraft.light_blue_candle_cake |
| Cake with Yellow Candle     | yellow_candle_cake     | Block        | candle_cakes | block.minecraft.yellow_candle_cake     |
| Cake with Lime Candle       | lime_candle_cake       | Block        | candle_cakes | block.minecraft.lime_candle_cake       |
| Cake with Pink Candle       | pink_candle_cake       | Block        | candle_cakes | block.minecraft.pink_candle_cake       |
| Cake with Gray Candle       | gray_candle_cake       | Block        | candle_cakes | block.minecraft.gray_candle_cake       |
| Cake with Light Gray Candle | light_gray_candle_cake | Block        | candle_cakes | block.minecraft.light_gray_candle_cake |
| Cake with Cyan Candle       | cyan_candle_cake       | Block        | candle_cakes | block.minecraft.cyan_candle_cake       |
| Cake with Purple Candle     | purple_candle_cake     | Block        | candle_cakes | block.minecraft.purple_candle_cake     |
| Cake with Blue Candle       | blue_candle_cake       | Block        | candle_cakes | block.minecraft.blue_candle_cake       |
| Cake with Brown Candle      | brown_candle_cake      | Block        | candle_cakes | block.minecraft.brown_candle_cake      |
| Cake with Green Candle      | green_candle_cake      | Block        | candle_cakes | block.minecraft.green_candle_cake      |
| Cake with Red Candle        | red_candle_cake        | Block        | candle_cakes | block.minecraft.red_candle_cake        |
| Cake with Black Candle      | black_candle_cake      | Block        | candle_cakes | block.minecraft.black_candle_cake      |

Bedrock Edition:

| Cake                        | Identifier             | Numeric ID | Form                         | Item ID[i 1]   | Translation key                  |
|-----------------------------|------------------------|------------|------------------------------|----------------|----------------------------------|
| Block                       | cake                   | 92         | Block & Ungiveable Item[i 2] | item.cake      | tile.cake.name                   |
| Item                        | cake                   | 417        | Item                         | —              | item.cake.name                   |
| Cake with Candle            | candle_cake            | 684        | Block & Ungiveable Item[i 2] | Identical[i 3] | tile.candle_cake.name            |
| Cake with White Candle      | white_candle_cake      | 685        | Block & Ungiveable Item[i 2] | Identical[i 3] | tile.white_candle_cake.name      |
| Cake with Orange Candle     | orange_candle_cake     | 686        | Block & Ungiveable Item[i 2] | Identical[i 3] | tile.orange_candle_cake.name     |
| Cake with Magenta Candle    | magenta_candle_cake    | 687        | Block & Ungiveable Item[i 2] | Identical[i 3] | tile.magenta_candle_cake.name    |
| Cake with Light Blue Candle | light_blue_candle_cake | 688        | Block & Ungiveable Item[i 2] | Identical[i 3] | tile.light_blue_candle_cake.name |
| Cake with Yellow Candle     | yellow_candle_cake     | 689        | Block & Ungiveable Item[i 2] | Identical[i 3] | tile.yellow_candle_cake.name     |
| Cake with Lime Candle       | lime_candle_cake       | 690        | Block & Ungiveable Item[i 2] | Identical[i 3] | tile.lime_candle_cake.name       |
| Cake with Pink Candle       | pink_candle_cake       | 691        | Block & Ungiveable Item[i 2] | Identical[i 3] | tile.pink_candle_cake.name       |
| Cake with Gray Candle       | gray_candle_cake       | 692        | Block & Ungiveable Item[i 2] | Identical[i 3] | tile.gray_candle_cake.name       |
| Cake with Light Gray Candle | light_gray_candle_cake | 693        | Block & Ungiveable Item[i 2] | Identical[i 3] | tile.light_gray_candle_cake.name |
| Cake with Cyan Candle       | cyan_candle_cake       | 694        | Block & Ungiveable Item[i 2] | Identical[i 3] | tile.cyan_candle_cake.name       |
| Cake with Purple Candle     | purple_candle_cake     | 695        | Block & Ungiveable Item[i 2] | Identical[i 3] | tile.purple_candle_cake.name     |
| Cake with Blue Candle       | blue_candle_cake       | 696        | Block & Ungiveable Item[i 2] | Identical[i 3] | tile.blue_candle_cake.name       |
| Cake with Brown Candle      | brown_candle_cake      | 697        | Block & Ungiveable Item[i 2] | Identical[i 3] | tile.brown_candle_cake.name      |
| Cake with Green Candle      | green_candle_cake      | 698        | Block & Ungiveable Item[i 2] | Identical[i 3] | tile.green_candle_cake.name      |
| Cake with Red Candle        | red_candle_cake        | 699        | Block & Ungiveable Item[i 2] | Identical[i 3] | tile.red_candle_cake.name        |
| Cake with Black Candle      | black_candle_cake      | 700        | Block & Ungiveable Item[i 2] | Identical[i 3] | tile.black_candle_cake.name      |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ a b c d e f g h i j k l m n o p q r Unavailable with /give command

↑ a b c d e f g h i j k l m n o p q The block's direct item form has the same id as the block.


