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

