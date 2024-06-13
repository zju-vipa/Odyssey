# Place Block
The place block is a joke block added in 23w13a_or_b, unlocked by a vote, that takes other blocks from a container on its back side and places them in front of it when given a redstone signal.

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
A place block can be mined with a pickaxe, in which case it drops only itself as it has no storage capacity on its own. If mined without a pickaxe, it drops nothing.

| Block     | Place Block           |
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
| Ingredients                                         | Crafting recipe |
|-----------------------------------------------------|-----------------|
| Cobblestone+<br/>Hopper+<br/>Redstone Dust+<br/>Bow |                 |

## Usage
As part of Java Edition 23w13a_or_b the place block can only be "used" when the vote for minecraft:place_block is approved. If this is not the case, the block cannot be:

- placed (nothing happens)
- dropped (the block gets removed from the inventory but no item appears)
- activated (the block doesn't react to redstone signals)
- crafted (the output of the crafting table stays empty)

#### Activation
A place block can be activated by:

- an adjacent activepower component(Exceptions:a redstone torch does not turn ON a place block it is attached to)
- an adjacent powered opaqueblock(strongly-powered or weakly-powered)
- a poweredredstone repeaterorredstone comparatorfacing the place block
- poweredredstone dustconfigured to point at the place block, or on top of it, or a directionless "dot" next to it; a place block isnotactivated by adjacent powered redstone dust that is configured to point in another direction.

A place block is not activated by adjacent powered redstone dust that is configured to point in another direction.

#### Basic utility
A place block can be used to place blocks either from a container (e.g. chest) behind it, or that were dropped as items behind it. A place block can be placed so that its in- and outputs face in any direction, including up or down. When placed, the output faces toward the player. The texture of this side is identical to the output of an observer.

1. After being activated, the place block checks the block behind it. If there is a container, place block pulls one item from the first available slot of that container: there is no check if the item is in fact a placeable block. Valid containers include: chests andtrapped chests(both small and large),barrels,shulker boxes,dispensers,droppersandhoppers, as well asminecarts with chestsandminecarts with hoppers. Only the fuel slot can be accessed fromfurnaces,blast furnacesandsmokers. In case ofbrewing stands, place block can pull from the blaze powder slot and potion slot, but none of these can actually contain placeable blocks. It can also pullmusic discsout of ajukeboxand books from achiseled bookshelf, but those items can't be placed either.
2. If there is no container, or if all available slots are empty, the place block next checks if there are any item entities in the 1×1×1 space behind it. If there are, it pulls an item with the largestAge.
3. Immediately after pulling an item, the place block attempts to place the item in front of itself (the place block does not have any storage). If the attempt fails, item is ejected instead, just like from a dropper.

Attempt to place can fail for multiple reasons:

- Item isn't a placeable block.
- Space on the output side is occupied by another block.
	- However if space is occupied by a replaceable block, likeshort grassorwater, another block can be placed.
		- In case of water, if a block that is attempted to be placed can bewaterlogged, it is then waterlogged.
- Space on the output side is blocked by an entity.
	- However non-solid blocks, like flowers, can be placed.
- Other conditions don't allow to place the block in that space, e.g. attempting to place a flower on stone.

Even if a block can in theory be placed, attempt still might fail due to the place block being an unpolished feature: for example, placing a hanging sign never works, no matter how many blocks are provided to support it.

Place block can't spawn mobs from spawn eggs, place minecarts on rails, or perform other similar tasks that usually involve the player right-clicking.

## Data values
### ID
| Name        | Identifier    | Form         | Translation key               |
|-------------|---------------|--------------|-------------------------------|
| Place Block | `place_block` | Block & Item | `block.minecraft.place_block` |

### Block states
See also: Block states

Place Block/BS


