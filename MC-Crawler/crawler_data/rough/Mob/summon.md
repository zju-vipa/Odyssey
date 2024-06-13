# Commands/summon
Summons an entity.

## Contents
- 1 Syntax
- 2 Arguments
- 3 Result
- 4 Output
- 5 Examples
- 6 History

## Syntax
- Java Edition

summon <entity> [<pos>] [<nbt>]
- Bedrock Edition

summon <entityType: EntityType> [spawnPos: x y z] [yRot: value] [xRot: value] [spawnEvent: string] [nameTag: string]
summon <entityType: EntityType> <nameTag: string> [spawnPos: x y z]
summon <entityType: EntityType> [spawnPos: x y z] facing <lookAtEntity: target> [spawnEvent: string] [nameTag: string]
summon <entityType: EntityType> [spawnPos: x y z] facing <lookAtPosition: x y z> [spawnEvent: string] [nameTag: string]
## Arguments
JE: <entity>: resourceBE: entityType: EntityType: enum

Specifies the entity to be summoned.
InJava Edition, must be an existing registeredresource locationinminecraft:entity_typeregistry. InBedrock Edition, must be an ID of anentitytype. And it should‌[JE  only]/must‌[BE  only]not be the player.
JE: <pos>: vec3BE: spawnPos: x y z: CommandPositionFloat

Specifies the position to summon the entity. If not specified, defaults to the position of the command's execution.
Must be three-dimensional coordinates withdouble-precision floating-point number‌[Java Edition  only]orsingle-precision floating-point number‌[Bedrock Edition  only]elements. Acceptstilde and caret notations.
JE: <nbt>: nbt_compound_tag

Specifies thedata tagfor the entity.
Must be acompoundNBTin SNBT format.
BE: yRot: value: RelativeFloat and xRot: value: RelativeFloat

Specifies the rotation of the summoned entity.
Must be a rotation consisting of two float number elements, including yaw and pitch, measured in degrees.
- For the horizontal rotation (yaw), -180.0 for due north, -90.0 for due east, 0.0 for due south, 90.0 for due west, to 179.9 for just west of due north, before wrapping back around to -180.0.
- For the vertical rotation (pitch), -90.0 for straight up to 90.0 for straight down.

Tilde notation can be used to specify a rotation relative to the execution rotation.
BE: lookAtEntity: target: CommandSelector<Actor>

Specifies the entity to make the summoned entity facing to.
Must be a player name or atarget selector.
BE: lookAtPosition: x y z: CommandPositionFloat

Specifies the coordinates to make the summoned entity facing to.
Must be three-dimensional coordinates withsingle-precision floating-point numberelements. Acceptstilde and caret notations.
BE: spawnEvent: string: basic_string

Specifies the in-game event for the entity. Should be aspawn event(event name for entities in behavior pack).
Must be a string. And it must be a single word that has no space or a double-quoted string (When quoted,\can be used to escape characters).
BE: nameTag: string: basic_string

Specifies the name of the entity.
Must be a string. And it must be a single word that has no space or a double-quoted string (When quoted,\can be used to escape characters).
## Result








| Command | Trigger                                                                                                                         | Java Edition | Bedrock Edition |
|---------|---------------------------------------------------------------------------------------------------------------------------------|--------------|-----------------|
| Any     | The command is incomplete, or any argument is not specified correctly.                                                          | Unparseable  | Unparseable     |
|         | Specified position is unloaded.                                                                                                 | Failed       | Failed          |
|         | Trying to summon hostiles in peaceful difficulty.                                                                               | Successful   |                 |
|         | Attempting to summon a player entity.                                                                                           | Failed       | N/A             |
|         | Attempting to summon an entity with a duplicate UUID.                                                                           |              |                 |
|         | Designated position's <X> or <Z> exceeds the range of [-30000000, 30000000), or <Y> exceeds the range of [-20000000, 20000000). |              | Successful      |
|         | Otherwise                                                                                                                       |              | Successful      |

## Output





| Command | Edition         | Situation  | Success Count | /execute store success ... | /execute store result ... |
|---------|-----------------|------------|---------------|----------------------------|---------------------------|
| Any     | Java Edition    | On fail    | 0             | 0                          | 0                         |
|         |                 | On success | 1             | 1                          | 1                         |
|         | Bedrock Edition | On fail    | 0             | N/A                        | N/A                       |
|         |                 | On success | 1             | N/A                        | N/A                       |

## Examples
- To summon lightning 10 blocks west of the current position of the executing player:
	- summon lightning_bolt ~-10 ~ ~

- Java Edition:
	- To summon acharged creeperat the current position named "Powered Creeper":
		- summon creeper ~ ~ ~ {powered:1b,CustomName:'{"text":"Powered Creeper"}'}
		- NOTE: CustomName is araw JSON text.
	- To summon an unbreakablediamond pickaxe:
		- summon item ~ ~ ~ {Item:{id:"minecraft:diamond_pickaxe",Count:1b,tag:{Unbreakable:True}}}
	- To summon aspider jockey:
		- summon spider ~ ~ ~ {Passengers:[{id:"minecraft:skeleton",HandItems:[{id:"minecraft:bow",Count:1b}]}]}
	- To summon avillagerthat trades 1 dirt block in exchange for 1 diamond:
		- summon villager ~ ~ ~ {Offers:{Recipes:[{buy:{id:dirt,Count:1},sell:{id:diamond,Count:1},rewardExp:false}]}}
- Bedrock Edition:
	- To summon apatrolcaptain pillager at the current position:
		- summon pillager ~ ~ ~ minecraft:promote_to_patrol_captain
	- To summon adolphinwith the name "Dolphin" in a golden color:
		- summon dolphin §6Dolphin ~ ~ ~
	- To summon aboatrotated 180 degrees:
		- summon boat ~ ~ ~ 180 180

