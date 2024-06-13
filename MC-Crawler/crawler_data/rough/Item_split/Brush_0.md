# Brush
A brush is a tool used in archaeology to excavate suspicious sand and suspicious gravel for different items. It can also brush armadillos for armadillo scutes.

## Contents
- 1 Obtaining
	- 1.1 Crafting
	- 1.2 Repairing
		- 1.2.1 Combining
		- 1.2.2 Unit repair
- 2 Usage
	- 2.1 Brushing
		- 2.1.1 Suspicious blocks
		- 2.1.2 Armadillos
	- 2.2 Enchantments
- 3 Sounds
- 4 Data values
	- 4.1 ID
- 5 Advancements
- 6 History
- 7 Issues
- 8 External links

## Obtaining
### Crafting
| Ingredients                          | Crafting recipe |
|--------------------------------------|-----------------|
| Feather+<br/>Copper Ingot+<br/>Stick |                 |

### Repairing
#### Combining
| Ingredients  | Crafting recipe | Description                                                                              |
|--------------|-----------------|------------------------------------------------------------------------------------------|
| DamagedBrush |                 | Thedurabilityof the two brushes is added together, plus an extra 3 points of durability. |

| Ingredients     | Grinding recipe | Description                                                                                |
|-----------------|-----------------|--------------------------------------------------------------------------------------------|
| 2× DamagedBrush |                 | The durability of the two brushes is added together, plus an extra 3 points of durability. |

#### Unit repair
Main article: Anvil mechanics § Unit repair
Repair & NameDamaged Brush
A brush can be combined with another brush in an anvil, preserving the enchantments of both.

## Usage
### Brushing
Using the brush on any block displays a brushing animation, slowing down the player and creating breaking particles, but not actually damaging the block or brush.

#### Suspicious blocks
Main articles: Suspicious Sand and Suspicious Gravel
When continuously brushing suspicious sand or suspicious gravel, an item dependent on the structure's loot table slowly emerges from it until it drops out, and the block turns into regular sand or regular gravel, depleting 1 durability point on the brush. It takes 96 game ticks (4.8 seconds) to brush a single suspicious block.

If the player stops brushing a suspicious block, the block remains in its half-excavated state for a few seconds, before gradually returning to its unexcavated state one stage at a time.

#### Armadillos

  

This section describes content that may be included in Java Edition. 
This content has appeared in Java Edition 1.20.5 development versions, but the full update containing it has not been released yet.



  

This section describes an experimental feature in Bedrock Edition. 
This feature is not enabled in-game by default and requires enabling the "Armadillo and Wolf Armor" setting in the "Experiments" section in Bedrock Edition.


When using the brush on an armadillo, it drops a single armadillo scute. Brushing an armadillo removes 16 points of durability from the brush. A brush with full durability and no enchantments can brush an armadillo four times in Java Edition or five times in Bedrock Edition before breaking.

### Enchantments
A brush can receive the following enchantments:

| Name               | Description                                           | Max Level | Method | Weight |
|--------------------|-------------------------------------------------------|-----------|--------|--------|
| Unbreaking         | Grants a chance to negate durability consumption.     | III       | Anvil  | 5      |
| Mending            | Repairs the brush when obtainingexperience.           | I         | Anvil  | 2      |
| Curse of Vanishing | The brush vanishes on death, not dropping as an item. | I         | Anvil  | 1      |

## Data values
### ID
Java Edition:

| Name  | Identifier | Form | Translation key        |
|-------|------------|------|------------------------|
| Brush | `brush`    | Item | `item.minecraft.brush` |

Bedrock Edition:

| Name  | Identifier | Numeric ID | Form | Translation key   |
|-------|------------|------------|------|-------------------|
| Brush | `brush`    | `684`      | Item | `item.brush.name` |


