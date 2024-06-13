# Copper Door
A copper door is a type of door made of copper that can be opened and closed by the player without redstone.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Barrier
	- 2.2 Redstone component
	- 2.3 Oxidation
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
		- 3.2.1 Waxing
		- 3.2.2 Opening
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 Achievements
- 6 Advancements
- 7 History
- 8 Issues
- 9 Gallery
	- 9.1 Screenshots
- 10 References

## Obtaining
### Breaking
Copper doors can be mined only with a stone pickaxe or better. If a copper door is mined without the use of a pickaxe, it drops nothing.

| Block     | Copper Door           |
|-----------|-----------------------|
| Hardness  | 3                     |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 15                    |
| Wooden    | 7.5                   |
| Stone     | 1.15                  |
| Iron      | 0.75                  |
| Diamond   | 0.6                   |
| Netherite | 0.5                   |
| Golden    | 1.25                  |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Copper doors generate naturally between the rooms of trial chambers.

### Crafting
| Name                                       | Ingredients                                                         | Crafting recipe |
|--------------------------------------------|---------------------------------------------------------------------|-----------------|
| UnwaxedCopper Dooror<br/>Waxed Copper Door | Matching UnwaxedBlock of Copperor<br/>MatchingWaxed Block of Copper | 33333333        |
| Waxed Copper Door                          | Matching UnwaxedCopper Door+<br/>Honeycomb                          |                 |

## Usage
Main article: Door § Usage
Copper doors can be opened and closed using a redstone signal, or by players, villagers[1], piglins, wandering traders‌[BE  only], vindicators‌[JE  only]. Copper doors are also affected by the wind burst of thrown wind charges, causing them to open if closed, or vice versa.

In Hard difficulty, copper doors can be broken by vindicators and all variants of zombies except drowned.[2]

### Barrier
A copper door can be opened or closed by pressing the Use Item/Place Block control. When a door opens or closes, it immediately changes its orientation without affecting anything in the space it "swings through".

Some zombies can break copper doors in Hard difficulty. Zombies have a 5% chance to spawn with the ability to break doors. Vindicators spawned from a raid in Normal and Hard difficulty can also break copper doors, but they do so only to reach targeted players, villagers, or wandering traders. In Java Edition, some vindicators may sometimes open a copper door instead of breaking it. Both zombies and vindicators attempt to break a copper door only when the door is in its "closed" state; this is the case even when the door is placed in such a way as to allow passage in its "closed" state and block passage in its "open" state (for example, by facing sideways when placing the door).

- A vindicator breaking a closed copper door placed sideways, even though it allows passage

### Redstone component
See also: Redstone circuit

Copper doors can be controlled with redstone power.

A copper door is a redstone mechanism component and can be activated by  weakly powering any cardinally adjacent block.

When activated, the copper door immediately opens. When deactivated, it immediately closes. Players and mobs can still open and close a door that is controlled by a redstone signal.

All methods of activating a door can be applied to either the top or bottom parts of a door.

### Oxidation
Main article: Oxidation
Non-waxed copper doors have four stages of oxidation (including the initial normal state).[3] Lightning bolts and axes can remove the oxidation on copper doors. They can be waxed with honeycomb to prevent oxidation from progressing.

As the block begins to oxidize (exposed), it gets discolored and green spots begin to appear. As the oxidation continues (weathered), the block is a green color with brown spots. In the last stage (oxidized), the block is teal with several green spots.

## Data values
### ID
Java Edition:

| Name                        | Identifier                    | Form         | Block tags                                                                                  | Translation key                               |
|-----------------------------|-------------------------------|--------------|---------------------------------------------------------------------------------------------|-----------------------------------------------|
| Copper Door                 | `copper_door`                 | Block & Item | `wooden_doors`<br/>`mineable/pickaxe`<br/>`needs_stone_tool`<br/>`doors`<br/>`mineable/axe` | `block.minecraft.copper_door`                 |
| Exposed Copper Door         | `exposed_copper_door`         | Block & Item | `wooden_doors`<br/>`mineable/pickaxe`<br/>`needs_stone_tool`<br/>`doors`<br/>`mineable/axe` | `block.minecraft.exposed_copper_door`         |
| Weathered Copper Door       | `weathered_copper_door`       | Block & Item | `wooden_doors`<br/>`mineable/pickaxe`<br/>`needs_stone_tool`<br/>`doors`<br/>`mineable/axe` | `block.minecraft.weathered_copper_door`       |
| Oxidized Copper Door        | `oxidized_copper_door`        | Block & Item | `wooden_doors`<br/>`mineable/pickaxe`<br/>`needs_stone_tool`<br/>`doors`<br/>`mineable/axe` | `block.minecraft.oxidized_copper_door`        |
| Waxed Copper Door           | `waxed_copper_door`           | Block & Item | `wooden_doors`<br/>`mineable/pickaxe`<br/>`needs_stone_tool`<br/>`doors`<br/>`mineable/axe` | `block.minecraft.waxed_copper_door`           |
| Waxed Exposed Copper Door   | `waxed_exposed_copper_door`   | Block & Item | `wooden_doors`<br/>`mineable/pickaxe`<br/>`needs_stone_tool`<br/>`doors`<br/>`mineable/axe` | `block.minecraft.waxed_exposed_copper_door`   |
| Waxed Weathered Copper Door | `waxed_weathered_copper_door` | Block & Item | `wooden_doors`<br/>`mineable/pickaxe`<br/>`needs_stone_tool`<br/>`doors`<br/>`mineable/axe` | `block.minecraft.waxed_weathered_copper_door` |
| Waxed Oxidized Copper Door  | `waxed_oxidized_copper_door`  | Block & Item | `wooden_doors`<br/>`mineable/pickaxe`<br/>`needs_stone_tool`<br/>`doors`<br/>`mineable/axe` | `block.minecraft.waxed_oxidized_copper_door`  |

Bedrock Edition:

| Name                        | Identifier                    | Numeric ID | Form                       | Item ID[i 1]   | Translation key                         |
|-----------------------------|-------------------------------|------------|----------------------------|----------------|-----------------------------------------|
| Copper Door                 | `copper_door`                 | `-784`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.copper_door.name`                 |
| Exposed Copper Door         | `exposed_copper_door`         | `-785`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.exposed_copper_door.name`         |
| Weathered Copper Door       | `weathered_copper_door`       | `-786`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.weathered_copper_door.name`       |
| Oxidized Copper Door        | `oxidized_copper_door`        | `-787`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.oxidized_copper_door.name`        |
| Waxed Copper Door           | `waxed_copper_door`           | `-788`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.waxed_copper_door.name`           |
| Waxed Exposed Copper Door   | `waxed_exposed_copper_door`   | `-789`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.waxed_exposed_copper_door.name`   |
| Waxed Weathered Copper Door | `waxed_weathered_copper_door` | `-790`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.waxed_weathered_copper_door.name` |
| Waxed Oxidized Copper Door  | `waxed_oxidized_copper_door`  | `-791`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.waxed_oxidized_copper_door.name`  |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑ a b c d e f g hAvailable with /give command.
3. ↑ a b c d e f g hThe block's direct item form has the same id as the block.

### Block states
Main article: Door § Block states
