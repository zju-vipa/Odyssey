# Barrier
A barrier is an invisible block used to create solid boundaries.

## Contents
- 1 Obtaining
	- 1.1 Natural generation
- 2 Usage
	- 2.1 Waterlogging
	- 2.2 Piston interactivity
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Trivia
- 8 Gallery
	- 8.1 Screenshots
	- 8.2 Development images
- 9 References

## Obtaining
Barriers can be obtained only using commands such as /give, /item in Java Edition, and /replaceitem in Bedrock Edition and cannot be broken in Survival mode.

In Java Edition, barriers are available in the Creative inventory if cheats are enabled and the "Operator Items Tab" setting is turned on.

### Natural generation
In normal worlds, barriers don't generate naturally. In Java Edition, they only generate in debug mode worlds, where barriers generate as the floor.

## Usage
The difference between air (top left) and barriers (bottom left) when "show invisible blocks" is enabled.
Barrier blocks are mainly used to build an impenetrable barrier that cannot be broken in standard Survival mode. For example, they can be used to protect a reserved area from entry by players, mobs, and other entities. Unlike other kinds of unbreakable blocks that could be used for this purpose (such as bedrock), barrier blocks are unobtrusive because they are invisible. Barrier blocks cannot be destroyed by TNT, creeper explosions, or any other explosions. Furthermore, they have a greater amount of blast resistance than any other unbreakable block.

Unlike other operator blocks such as command blocks, barriers can be placed by players in Survival mode.

In the player's inventory, the block is displayed as a red box with a slash through it, but when placed it is completely invisible.

Barriers are transparent to light and do not block a beacon. Fences, iron bars, glass panes, and similar blocks do not visually connect with barriers. Barriers interact with blocks and mobs as a solid block. All dependent blocks can be placed on a barrier, such as torches or redstone, and it can suffocate mobs. Mobs cannot spawn on barriers.

In Creative mode, if a player is holding a barrier block in their hand, all placed barrier blocks display the barrier icon as a particle. This effect is client-side, and if a player holds a barrier block in Survival mode, the particle does not appear. Barrier blocks are not shown if the particle setting is set to "minimal". 

- 
- 

### Waterlogging
Barrier blocks can be waterlogged by being placed into a water source block or by manually using a water bucket on them. In Java Edition, water cannot be placed in them or taken out by non-direct interactions such as dispensers; this is allowed in Bedrock Edition. In Java Edition, only players in Creative mode can waterlog or remove water from barriers, while in Bedrock Edition there are no game mode restrictions. In Java Edition, water doesn't flow out of waterlogged barriers. See waterlogging for more details on what blocks can be waterlogged.

### Piston interactivity
Barriers cannot be pushed by pistons. They also cannot be pushed nor pulled by sticky pistons.

## Data values
### ID
Java Edition:

| Name    | Identifier | Form         | Block tags                 | Translation key         |
|---------|------------|--------------|----------------------------|-------------------------|
| Barrier | barrier    | Block & Item | dragon_immunewither_immune | block.minecraft.barrier |

Bedrock Edition:

| Name    | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key   |
|---------|------------|------------|----------------------------|----------------|-------------------|
| Barrier | barrier    | 416        | Block & Giveable Item[i 2] | Identical[i 3] | tile.barrier.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values | Description                                                     |
|-------------|---------------|----------------|-----------------------------------------------------------------|
| waterlogged | false         | truefalse      | Whether or not there's water in the same place as this barrier. |


