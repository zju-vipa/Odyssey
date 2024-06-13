### Beams
The end crystal naturally shoots a beam at the ender dragon and heals it when the dragon is within range. This beam can be manually created using the command /data merge entity @e[type=end_crystal,limit=1] {BeamTarget:{X:0, Y:0, Z:0}}. The beam can be pointed in any direction, allowing it to mark locations or objects.

### Properties
A base-less end crystal.
End crystals are of two kinds: the ones with a base beneath them are created either by game mechanism or by the /summon command; while the base-less ones are created by players by manually placing the crystal items on top of obsidian or bedrock.

The base appears to be made of bedrock, with a crystal hovering over it. While in the End, a crystal continually generates fire at its current position, one block above the base (directly on top of the block the base is embedded in), replacing any other block at that location. This fire is capable of spreading.

The end crystal entity is not solid and can be walked through freely. End crystals can be pushed by pistons, but they explode if moved while on fire. Because fire is checked only when an entity moves, end crystals do not normally take damage from their own fire unless moved.

## Data values
### ID
Java Edition:

| Item        | Identifier    | Form | Translation key              |
|-------------|---------------|------|------------------------------|
| End Crystal | `end_crystal` | Item | `item.minecraft.end_crystal` |

| Entity      | Identifier    | Translation key                |
|-------------|---------------|--------------------------------|
| End Crystal | `end_crystal` | `entity.minecraft.end_crystal` |

Bedrock Edition:

| Item        | Identifier    | Numeric ID | Form | Translation key         |
|-------------|---------------|------------|------|-------------------------|
| End Crystal | `end_crystal` | `637`      | Item | `item.end_crystal.name` |

| Entity      | Identifier      | Numeric ID | Translation key             |
|-------------|-----------------|------------|-----------------------------|
| End Crystal | `ender_crystal` | `71`       | `entity.ender_crystal.name` |

### Entity data
End crystals have entity data that define various properties of the entity.

Java Edition:

Main article: Entity format
- Entity data
	- 
	- Tags common to all entities
	- BeamTarget: The block location its beam points to.
		- X: X-coordinate.
		- Y: Y-coordinate.
		- Z: Z-coordinate.
	- ShowBottom: 1 or 0 (true/false) – if true, the end crystal shows the bedrock slate underneath. Defaults to false when placing by hand, and true when naturally generated or using/summon.

Bedrock Edition:

SeeBedrock Edition level format/Entity format.

