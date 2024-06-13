# Pressure Plate
A pressure plate is a non-solid block that produces a redstone signal when stood on by an entity, with various variants.

## Contents
- 1 Variants
- 2 Obtaining
	- 2.1 Breaking
- 3 Usage
	- 3.1 Activation
- 4 History
	- 4.1 Pre-1.7.2 requirements
- 5 Issues
- 6 References

## Variants
- Wooden Pressure Plate
	- Oak Pressure Plate
	- Birch Pressure Plate
	- Spruce Pressure Plate
	- Jungle Pressure Plate
	- Acacia Pressure Plate
	- Dark Oak Pressure Plate
	- Mangrove Pressure Plate
	- Cherry Pressure Plate
	- Bamboo Pressure Plate
	- Crimson Pressure Plate
	- Warped Pressure Plate
- Stone Pressure Plate
- Polished Blackstone Pressure Plate
- Heavy Weighted Pressure Plate
- Light Weighted Pressure Plate

## Obtaining
### Breaking
A pressure plate is removed and drops itself as an item if:

- the block beneath it is moved, removed, or destroyed
- apistontries to push it or moves a block into its space

## Usage
See also: Redstone circuit

This section is about the behavior and usage of pressure plate in general. For more information see the respective variant page (listed in the previous section)

A pressure plate can be used to detect entities on top of it (players, mobs, items, etc.).
Pressure plate placement and behavior.
Pressure plates on fences.
To place a pressure plate, use it while aiming at the face of a block adjacent to the destination space.

A pressure plate can be attached to:

- thetopof any full solidopaqueblock (stone, dirt, blocks of gold, etc.), including full-block mechanism components (command blocks,dispensers,droppers,note blocks, andredstone lamps)
- thetopof ahopper,fence,nether brick fence, an upside-downslab, or upside-downstairs.

A pressure plate cannot be attached to the side or bottom of any block, but attempting to make such an attachment may cause the plate to attach to the top of a block under the destination space. For example, if a fence is on the ground, attempting to attach a plate to the side of the fence causes the plate to be attached to the top of the ground next to the fence instead.

More information regarding placement on transparent blocks can be found at Opacity/Placement.

### Activation
A pressure plate activates when an entity is on top of it (specifically, when the entity's collision mask intersects the bottom quarter-block of the pressure plate's space, which may include entities flying close to the ground), with a minimum activation time of 1 second. How it is activated varies depending on which kind of pressure plate is.

A minecart traveling on rails activates a pressure plate next to a diagonal track but not one next to a straight track (stone pressure plates are activated only if the minecart contains a mob or player).

** Behavior **
While active, a pressure plate:

- powers adjacentredstone dust, and adjacentredstone comparatorsorredstone repeatersfacing away from the plate
- strongly powers any full solid opaqueblockbeneath it
- activates adjacentmechanism components, including above or below, such aspistons,redstone lamps, etc.

Water and lava flows around a pressure plate without affecting it.

Pressure plates can also open doors, activate TNT, and power command blocks.


