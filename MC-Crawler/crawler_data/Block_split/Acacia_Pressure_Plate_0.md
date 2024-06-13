# Wooden Pressure Plate
A wooden pressure plate is a wooden variant of the pressure plate. It can detect all entities, producing the maximum signal strength of 15. Wooden pressure plates come in all variants of wood.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Redstone component
		- 2.1.1 Placement
		- 2.1.2 Activation
		- 2.1.3 Behavior
	- 2.2 Fuel
	- 2.3 Note blocks
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
- 5 History
- 6 Gallery
	- 6.1 Renders
- 7 Issues
- 8 References

## Obtaining
### Breaking
A wooden pressure plate can be mined using any tool, or without a tool, and drops itself as an item. However, axes are the fastest way to break one.

| Block     | Wooden Pressure Plate |
|-----------|-----------------------|
| Hardness  | 0.5                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 0.75                  |
| Wooden    | 0.4                   |
| Stone     | 0.2                   |
| Iron      | 0.15                  |
| Diamond   | 0.1                   |
| Netherite | 0.1                   |
| Golden    | 0.1                   |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


A pressure plate is removed and drops itself as an item if:

- the block beneath it is moved, removed, or destroyed
- apistontries to push it or moves a block into its space

### Natural generation
Oak pressure plates can generate in some plains village houses.

Acacia pressure plates can generate in some savanna village houses.

Spruce pressure plates can generate in some snowy tundra village houses.

### Crafting
| Ingredients    | Crafting recipe |
|----------------|-----------------|
| MatchingPlanks |                 |

## Usage
### Redstone component
See also: Redstone circuit

A pressure plate can be used to detect entities on top of it (players, mobs, items, etc.).

#### Placement
Pressure plate placement and behavior.
Pressure plates on fences.
To place a pressure plate, use it while aiming at the face of a block adjacent to the destination space.

A pressure plate can be attached to:

- thetopof any full solidopaqueblock (stone, dirt, blocks of gold, etc.), including full-block mechanism components (command blocks,dispensers,droppers,note blocks, andredstone lamps)
- thetopof ahopper,fence,nether brick fence, an upside-downslab, or upside-downstairs.

A pressure plate cannot be attached to the side or bottom of any block, but attempting to make such an attachment may cause the plate to attach to the top of a block under the destination space. For example, if a fence is on the ground, attempting to attach a plate to the side of the fence causes the plate to be attached to the top of the ground next to the fence instead.

More information regarding placement on transparent blocks can be found at Opacity/Placement.

#### Activation
A pressure plate activates when an entity is on top of it (specifically, when the entity's collision mask intersects the bottom quarter-block of the pressure plate's space, which may include entities flying close to the ground), with a minimum activation time of 1 second (20 game ticks).

A wooden pressure plate is activated by all entities (including players, mobs, items, arrows, experience orbs, fishing bobs, etc.) besides snowballs.

Once activated, a pressure plate checks if entities are still present at regular intervals. Wooden pressure plates check every 10 redstone ticks (1 second), starting 10 redstone ticks after activation, so they deactivate up to 10 redstone ticks after no entities are on top of them.

A minecart traveling on rails activates a pressure plate next to a diagonal track but not one next to a straight track.

#### Behavior
While active, a pressure plate:

- powers adjacentredstone dust, and adjacentredstone comparatorsorredstone repeatersfacing away from the plate
- strongly powers any full solid opaqueblockbeneath it
- activates adjacentmechanism components, including above or below, such aspistons,redstone lamps, etc.

The power level is always 15.

Water and lava flow around a pressure plate without affecting it.

A pressure plate is not solid (it is not a barrier to entity movement). A block under a pressure plate can provide a solid barrier underneath it (for mobs to walk across, items to fall on, etc.), but when a pressure plate is placed on a block with a small collision mask, such as a fence or nether brick fence, it is possible for entities to move through the pressure plate while still activating it (walking through it horizontally, or falling through it vertically). Thus, a pressure plate on a fence can be used to detect entities without stopping them (more compactly than a tripwire circuit).

Pressure plates are 0.0625 blocks high (1⁄16 of a block) when inactive and 0.03125 blocks high (1⁄32 of a block) when active, but because they are not solid they do not affect the position of entities "on top" of them, so a player on top of a pressure plate is actually standing on the block beneath it.

Pressure plates can also open doors, activate TNT, and power command blocks.


