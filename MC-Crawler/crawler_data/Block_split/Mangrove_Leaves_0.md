# Leaves
Leaves are transparent natural blocks that generate as part of trees. They decay when not attached to a tree trunk, but persist when placed by a player.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Post-generation
- 2 Usage
	- 2.1 Redstone component
	- 2.2 Piston interactivity
	- 2.3 Composting
	- 2.4 Bees
	- 2.5 Bee nests
	- 2.6 Color
		- 2.6.1 Biome colors
		- 2.6.2 Snowy leaves
- 3 Sounds
	- 3.1 Other leaves
	- 3.2 Azalea leaves
	- 3.3 Cherry leaves
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
	- 5.1 Data history
- 6 Issues
- 7 Trivia
- 8 Gallery
	- 8.1 Renders
	- 8.2 Screenshots
- 9 References
- 10 External links

## Obtaining
### Breaking
See also: Fortune § Tabulated probabilities

Hoes are the default tools for breaking leaves, but leaves can be obtained only with shears or Silk Touch enchanted tools.

| Block     | Leaves                |
|-----------|-----------------------|
| Hardness  | 0.2                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 0.3                   |
| Wooden    | 0.15                  |
| Stone     | 0.1                   |
| Iron      | 0.05                  |
| Diamond   | 0.05                  |
| Netherite | 0.05                  |
| Golden    | 0.05                  |
| Shears    | 0.05                  |
| Sword     | 0.2                   |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


| Drop                   | Source                       | No Fortune   | Fortune I      | Fortune II     | Fortune III    |
|------------------------|------------------------------|--------------|----------------|----------------|----------------|
| Jungle Saplings        | Jungle Leaves                | 2.5% (1⁄40)  | 2.78% (1⁄36)   | 3.125% (1⁄32)  | 4.17% (1⁄24)   |
| Azaleaor otherSaplings | Azalea Leaves or otherLeaves | 5% (1⁄20)    | 6.25% (1⁄16)   | 8.33% (1⁄12)   | 10% (1⁄10)     |
| 1-2Sticks              | All Leaves                   | 2% (1⁄50)    | 2.22% (1⁄45)   | 2.5% (1⁄40)    | 3.33% (1⁄30)   |
| Apples                 | Oak andDark Oak Leaves       | 0.5% (1⁄200) | 0.556% (1⁄180) | 0.625% (1⁄160) | 0.833% (1⁄120) |

### Natural generation
Leaves occur naturally on trees and azaleas throughout the Overworld. Specially, oak leaves‌[Java Edition  only] or jungle leaves‌[Bedrock Edition  only] generate in jungle bushes. Oak leaves also generate in the tree at meeting points in plains villages. Dark oak leaves also generate in woodland mansions.


### Post-generation
See also: Tutorials/Tree farming

Leaves generate as part of trees grown from saplings, azaleas, or mangrove propagules.

## Usage
Leaves from trees spontaneously decay (disappear) when they receive a block tick if they are not connected to a block with the logs tag (log or wood block), either directly or via other leaf blocks, with a maximum distance of 6 blocks‌[Java Edition  only] or 4 blocks‌[Bedrock Edition  only]. Leaves placed by players never decay.

Leaves that decay, or are destroyed without using Silk Touch or shears, yield saplings 5% (1⁄20) of the time, sticks 2% of the time, and otherwise drop nothing. Jungle leaves drop saplings 2.5% (1⁄40) of the time. Oak and dark oak leaves also have a separate but additional 0.5% (1⁄200) chance of dropping an apple, making it extremely rare but possible for a single leaf to drop a sapling, a stick and an apple at the same time. Rates are increased by the Fortune enchantment. Leaves that are burned do not yield saplings or apples.

Leaves take on a different shade of green depending on the biome in which they are placed.

Leaves are always transparent to light, but cannot be seen through when the graphics mode is set to "Fast"; the transparent regions are instead black‌[JE  only]/dark green‌[BE  only]. They diffuse sky light, causing the shadows they cast under trees.

Leaves can be waterlogged, despite being a full block. Water does not spread out‌[Java Edition  only] and waterlogged leaves follow the same rules as any other waterlogged block. When concrete powder is placed on any side of the waterlogged leaves it turns into concrete, without the danger of the water running out of the block.

Applying bone meal to mangrove leaves with a space beneath produces a hanging mangrove propagule with age=0.

### Redstone component

  

This feature is exclusive to  Java Edition. 


The state of a leaves block—including a player-placed block—changes after 1 game tick (half a redstone tick) when the distance to the nearest log or wood block changes, up to 6 blocks of leaves away. Observers facing away from the leaves detect this change and transmit a redstone signal in the same game tick, making leaves useful for redstone signal transmission. This has been called "Leafstone" by the Minecraft Community.

