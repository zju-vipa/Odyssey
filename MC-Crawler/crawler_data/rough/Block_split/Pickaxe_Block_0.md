# Pickaxe Block
The pickaxe block is a joke block added in 23w13a_or_b, unlocked by a vote, that can instantly destroy any other block (including blocks indestructible in Survival) when given a redstone signal.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
- 2 Usage
	- 2.1 Activation
	- 2.2 Basic utility
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 Issues
- 6 See also

## Obtaining
### Breaking
A pickaxe block can be mined with a pickaxe, in which case it drops itself. If mined without a pickaxe, it drops nothing.

| Block     | Pickaxe Block         |
|-----------|-----------------------|
| Hardness  | 3                     |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 15                    |
| Wooden    | 2.25                  |
| Stone     | 1.15                  |
| Iron      | 0.75                  |
| Diamond   | 0.6                   |
| Netherite | 0.5                   |
| Golden    | 0.4                   |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Crafting
| Ingredients                                       | Crafting recipe |
|---------------------------------------------------|-----------------|
| Cobblestone +<br/>Any Pickaxe +<br/>Redstone Dust |                 |

## Usage
As part of the April Fools' update of 2023, the pickaxe block can only gets "used" when the vote for minecraft:pickaxe_block was approved earlier. If this is not the case, the block cannot get:

- placed (nothing happens).
- dropped (the block gets removed from the inventory but noitemappears).
- activated (the block loses its functionality and doesn't react to redstone signals).
- crafted (the output of the crafting table stays empty).

#### Activation
A pickaxe block can be activated by:

- an adjacent activepower component(Exceptions:a redstone torch does not turn ON a pickaxe block it is attached to)
- an adjacent powered opaqueblock(strongly-powered or weakly-powered)
- a poweredredstone repeaterorredstone comparatorfacing the pickaxe block
- poweredredstone dustconfigured to point at the pickaxe block, or on top of it, or a directionless "dot" next to it; a pickaxe block isnotactivated by adjacent powered redstone dust that is configured to point in another direction.

A pickaxe block is not activated by adjacent powered redstone dust that is configured to point in another direction.

#### Basic utility
A pickaxe block can be placed so that its mining side faces in any direction, including up or down. When placed, the mining side faces toward the player. The texture of this side is identical to the output of an observer. 

When activated, a pickaxe block instantly breaks any block in front of it. This includes everything that is destroyable in Creative mode with a left click: a pickaxe block can break bedrock, barriers, command blocks, end portal blocks and other blocks indestructible in Survival, but can't break water or lava. Pickaxe block can even break light blocks, despite the fact that those blocks can be targeted by players only if they are holding such block in their hand.

When broken, most blocks react as if they were destroyed by an unenchanted diamond or netherite pickaxe, no matter which pickaxe was used in the crafting recipe: 

- Grass blockdrops dirt,stonedrops cobblestone
- Coal oredrops one coal and experience,lapis lazuli oredrops 4-9 lapis lazuli and experience
- Monster spawnerdrops only experience
- Infested blocksdrop nothing and spawn a silverfish
- Gilded blackstonedrops itself 90% of the time, and golden nuggets 10% of the time

Exceptions include:

- All blocks indestructible in Survival drop nothing
- Snow blockdrops 4 snowballs (when player mines it with a pickaxe, block drops nothing - a shovel is required to get snowballs)
	- However, asnow layerstill drops nothing when destroyed by a pickaxe block
- Amethyst clusterdrops 2 amethyst shards (when player mines it with a pickaxe, block drops 4 shards)
- Cobwebdrops a string (when player mines it with a pickaxe, block drops nothing - a sword or shears are required to get string)
- Icedoesn't melt into water, it just disappears
- Bee nestandbeehivealso disappear and no bees are spawned

The pickaxe block can also destroy (and drop) the dragon egg without it teleporting away.

## Data values
### ID
| Name          | Identifier      | Form         | Translation key                 |
|---------------|-----------------|--------------|---------------------------------|
| Pickaxe Block | `pickaxe_block` | Block & Item | `block.minecraft.pickaxe_block` |

### Block states
See also: Block states

Pickaxe Block/BS


