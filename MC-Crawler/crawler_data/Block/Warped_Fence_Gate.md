# Fence Gate
A fence gate is a block that shares the functions of both the door and the fence.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Placing
	- 2.2 Barrier
	- 2.3 Redstone component
	- 2.4 Fuel
	- 2.5 Note blocks
	- 2.6 Helmet
- 3 Sounds
	- 3.1 Generic
		- 3.1.1 Normal wood
		- 3.1.2 Cherry wood
		- 3.1.3 Bamboo wood
		- 3.1.4 Nether wood
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 Video
- 6 History
- 7 Gallery
	- 7.1 Renders
		- 7.1.1 Closed
		- 7.1.2 Open
- 8 Issues
- 9 References

## Obtaining
### Breaking
A fence gate can be broken with anything, but an axe is fastest.

| Block     | Fence Gate            |
|-----------|-----------------------|
| Hardness  | 2                     |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 3                     |
| Wooden    | 1.5                   |
| Stone     | 0.75                  |
| Iron      | 0.5                   |
| Diamond   | 0.4                   |
| Netherite | 0.35                  |
| Golden    | 0.25                  |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Natural generation
Oak
Oak fence gates generate as part of:

- Plainsvillages

Spruce
Spruce fence gates generate as part of:

- Taiga, snowy tundra and snowy taiga‌[BE  only]villages

Jungle
Jungle fence gates generate as part of:

- Desertvillages

Acacia
Acacia fence gates generate as part of:

- Savannavillages

Dark oak
Dark oak fence gates generate as part of:

- Woodland mansions

### Crafting
| Ingredients          | Crafting recipe |
|----------------------|-----------------|
| MatchingPlanks+Stick |                 |

## Usage
### Placing
A fence gate can provide access to a fenced-in area.
A fence gate can be used as a switchable barrier that can be opened and closed by hand or by redstone power.

When placed, a fence gate automatically faces toward the player who placed it, regardless of any other fences around it.

A fence gate can be placed whether there is a solid block beneath it or not.

Fences, nether brick fences and walls connect to fence gates, but glass panes and iron bars do not. A fence gate floats in mid-air when placed with no connection to anything else.

### Barrier
A fence gate can be opened or closed by using it. When a fence gate opens or closes, it immediately changes its orientation without affecting anything in the space it "passes through"—moving fence gates don't push entities the way that pistons do. When opened by hand, a fence gate always opens away from the player.

Although a fence gate appears to be only one block tall, a closed fence gate is a barrier one and a half blocks high. Most mobs cannot jump over a fence gate, and entities on top of the fence gate stand half a block above it.

An open fence gate is completely non-solid, similar to a sign or a torch.[1] Multiple open fence gates next to each other can be passed through as if the entire space is open.

Hostile mobs recognize closed fence gates as a block and cannot detect players through it unless they were already detected.

The sound of opening and closing of a fence gate can be heard up to 16 blocks away, like most mob sounds.

### Redstone component
See also: Redstone circuit

A fence gate can be controlled with redstone power.

A fence gate is a redstone mechanism and can be activated by:

- an adjacent activepower component, including above or below: for example, aredstone torch, ablock of redstone, adaylight sensor, etc.
- an adjacentpowered block(for example, a block with an active redstone torch under it), including above or below
- a poweredredstone comparatororredstone repeaterfacing the fence gate
- poweredredstone dustconfigured to point at the fence gate or a directionless "dot" next to it; a fence gate isnotactivated by adjacent powered redstone dust that is configured to point in another direction.

When activated, a fence gate opens immediately. When deactivated, a fence gate closes immediately.

An activated fence gate can still be closed by a player, and won't re-open until it receives a new activation signal. (That is, if a fence gate has been closed "by hand", it still needs to be deactivated and then reactivated to open by redstone).

Fence gates can be moved by pistons. When an activated fence gate is moved by a piston to a position where it shouldn't be activated, it doesn't change its state until it receives a redstone update.

### Fuel
Overworld wooden fence gates can be used as a fuel in furnaces, smelting 1.5 items per fence gate.

### Note blocks
Fence gates can be placed under note blocks to produce "bass" sounds.

### Helmet


While a fence gate cannot be equipped in the head slot in Survival mode, equipping it using commands causes it to appear as eyeglasses.

## Data values
### ID
Java Edition:

| Name                | Identifier          | Form         | Block tags                                          | Item tags          | Translation key                     |
|---------------------|---------------------|--------------|-----------------------------------------------------|--------------------|-------------------------------------|
| Oak Fence Gate      | oak_fence_gate      | Block & Item | fence_gatesunstable_bottom_center                   | None               | block.minecraft.oak_fence_gate      |
| Spruce Fence Gate   | spruce_fence_gate   | Block & Item | fence_gatesunstable_bottom_center                   | None               | block.minecraft.spruce_fence_gate   |
| Birch Fence Gate    | birch_fence_gate    | Block & Item | fence_gatesunstable_bottom_center                   | None               | block.minecraft.birch_fence_gate    |
| Jungle Fence Gate   | jungle_fence_gate   | Block & Item | fence_gatesunstable_bottom_center                   | None               | block.minecraft.jungle_fence_gate   |
| Acacia Fence Gate   | acacia_fence_gate   | Block & Item | fence_gatesunstable_bottom_center                   | None               | block.minecraft.acacia_fence_gate   |
| Dark Oak Fence Gate | dark_oak_fence_gate | Block & Item | fence_gatesunstable_bottom_center                   | None               | block.minecraft.dark_oak_fence_gate |
| Mangrove Fence Gate | mangrove_fence_gate | Block & Item | fence_gatesunstable_bottom_center                   | None               | block.minecraft.mangrove_fence_gate |
| Cherry Fence Gate   | cherry_fence_gate   | Block & Item | fence_gatesunstable_bottom_center                   | None               | block.minecraft.cherry_fence_gate   |
| Bamboo Fence Gate   | bamboo_fence_gate   | Block & Item | fence_gatesunstable_bottom_center                   | None               | block.minecraft.bamboo_fence_gate   |
| Crimson Fence Gate  | crimson_fence_gate  | Block & Item | fence_gatesnon_flammable_woodunstable_bottom_center | non_flammable_wood | block.minecraft.crimson_fence_gate  |
| Warped Fence Gate   | warped_fence_gate   | Block & Item | fence_gatesnon_flammable_woodunstable_bottom_center | non_flammable_wood | block.minecraft.warped_fence_gate   |

Bedrock Edition:

| Name                | Identifier          | Numeric ID | Form                       | Item ID[i 1]   | Translation key               |
|---------------------|---------------------|------------|----------------------------|----------------|-------------------------------|
| Oak Fence Gate      | fence_gate          | 107        | Block & Giveable Item[i 2] | Identical[i 3] | tile.fence_gate.name          |
| Spruce Fence Gate   | spruce_fence_gate   | 183        | Block & Giveable Item[i 2] | Identical[i 3] | tile.spruce_fence_gate.name   |
| Birch Fence Gate    | birch_fence_gate    | 184        | Block & Giveable Item[i 2] | Identical[i 3] | tile.birch_fence_gate.name    |
| Jungle Fence Gate   | jungle_fence_gate   | 185        | Block & Giveable Item[i 2] | Identical[i 3] | tile.jungle_fence_gate.name   |
| Acacia Fence Gate   | acacia_fence_gate   | 187        | Block & Giveable Item[i 2] | Identical[i 3] | tile.acacia_fence_gate.name   |
| Dark Oak Fence Gate | dark_oak_fence_gate | 186        | Block & Giveable Item[i 2] | Identical[i 3] | tile.dark_oak_fence_gate.name |
| Mangrove Fence Gate | mangrove_fence_gate | -492       | Block & Giveable Item[i 2] | Identical[i 3] | tile.mangrove_fence_gate.name |
| Cherry Fence Gate   | cherry_fence_gate   | -533       | Block & Giveable Item[i 2] | Identical[i 3] | tile.cherry_fence_gate.name   |
| Bamboo Fence Gate   | bamboo_fence_gate   | -516       | Block & Giveable Item[i 2] | Identical[i 3] | tile.bamboo_fence_gate.name   |
| Crimson Fence Gate  | crimson_fence_gate  | 513        | Block & Giveable Item[i 2] | Identical[i 3] | tile.crimson_fence_gate.name  |
| Warped Fence Gate   | warped_fence_gate   | 514        | Block & Giveable Item[i 2] | Identical[i 3] | tile.warped_fence_gate.name   |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ a b c d e f g h i j k Available with /give command.

↑ a b c d e f g h i j k The block's direct item form has the same id as the block.


### Block states
Main article: Block states
Java Edition:

| Name    | Default value | Allowed values     | Description                                                                                                                                                                       |
|---------|---------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing  | north         | eastnorthsouthwest | For an open gate, the direction the gates swing open.For a closed gate, the direction the player was facing when the gate was placed, or the last direction the gates have swung. |
| in_wall | false         | falsetrue          | If true, the gate is lowered by three pixels, to accommodate attaching more cleanly withwalls.                                                                                    |
| open    | false         | falsetrue          | If true, the gate is opened.                                                                                                                                                      |
| powered | false         | falsetrue          | If true, the gate is receiving redstone power.                                                                                                                                    |

Bedrock Edition:

| Name        | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                                                                                                                                                                                                                                                              |
|-------------|---------------|---------------|----------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| direction   | 0x10x2        | 0             | 0123           | 0123                    | The direction the gate is facing0: Facing south 1: Facing west 2: Facing north 3: Facing eastFor an open gate, it's the direction the gates swing open.For a closed gate, it's the direction the player was facing when the gate was placed, or the last direction the gates have swung. |
| in_wall_bit | 0x8           | false         | falsetrue      | 01                      | If the gate is lowered by three pixels, to accommodate attaching more cleanly withwalls.                                                                                                                                                                                                 |
| open_bit    | 0x4           | false         | falsetrue      | 01                      | If the gate is opened.                                                                                                                                                                                                                                                                   |

