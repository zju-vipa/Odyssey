# Marker
Markers are entities intended for use in data packs and map-making. They can only be created with the /summon command. 

## Contents
- 1 Behavior
- 2 Data values
	- 2.1 ID
	- 2.2 Entity data
- 3 History
- 4 Issues
- 5 References
- 6 See also

## Behavior
Markers are intended to have minimal behavior. Markers do not move, do not take damage, do not make sounds, and cannot be given status effects. They cannot support passengers (even when summoned with a Passengers tag, the passengers are not created).

Markers do not cause any updates. Markers only exist on the server side,[1] so they do not render. Using the debug key combination F3 + B, which normally draws the hitboxes of all visible entities, does not show a hitbox for a marker. Using F3 + I while aiming at a marker does not copy the entity data to the clipboard. They do not count toward the E-value (total amount of entities) listed on the debug screen. Markers do not obstruct the placement of blocks, nor do they push players or other entities away from their own position. Markers can be saved in structures via structure blocks.

## Data values
### ID
Java Edition:

| Entity | Identifier | Translation key           |
|--------|------------|---------------------------|
| Marker | `marker`   | `entity.minecraft.marker` |

### Entity data
See also: Entity format

Markers have entity data associated with them that contain various properties of the entity.

- Entity data
	- 
	- Tags common to all entities
	- data: Any NBT data.


