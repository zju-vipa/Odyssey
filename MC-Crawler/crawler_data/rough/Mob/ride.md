# Commands/ride
Allows entities to mount or dismount other entities.

## Contents
- 1 Usage
- 2 Syntax
- 3 Arguments
- 4 Result
- 5 Output
- 6 Example
- 7 History

## Usage
Main article: Riding
In Java Edition, all types of entities (except marker and player) can ride and be ridden by other entities of any types. Marker and player cannot be ridden.

In Bedrock Edition, an entity cannot ride entities which are not normally rideable for it in vanilla game, which is mainly data driven, controlled by the minecraft:rideable component in the entity files in behavior packs (see Riding#Valid riding combinations in vanilla for details; see also the official doc). In Bedrock Edition, this command can also be used to summon passengers and mounts.

## Syntax
- Java Edition

ride <target> mount <vehicle>Makes <target> ride on <vehicle>.
ride <target> dismountDismounts target from any vehicle it is riding.
- Bedrock Edition

ride <riders: target> start_riding <ride: target> [teleportRules: TeleportRules] [howToFill: FillType]Tries to make <riders: target> ride on <ride: target>.
ride <riders: target> stop_ridingMakes <riders: target> dismount.
ride <rides: target> evict_ridersMakes entities that are riding on <rides: target> dismount.
ride <rides: target> summon_rider <entityType: EntityType> [spawnEvent: string] [nameTag: string]Summons an entity at the position of each of <rides: target> that are rideable and not full, and then tries to make them ride on <rides: target>.
ride <riders: target> summon_ride <entityType: EntityType> [rideRules: RideRules] [spawnEvent: string] [nameTag: string]Summons an entity at the position of each of <riders: target>, and then tries to make <riders: target> ride on them.
## Arguments
JE: <target>: entity

Specifies the passenger.
Must be a player name, atarget selectoror aUUID.  And the target selector must be insingle type.
JE: <vehicle>: entity

Specifies the mount.
Must be a player name, atarget selectoror aUUID.  And the target selector must be insingle type.
BE: riders: target: CommandSelector<Actor>

Specifies the passengers.
If instart_ridingmode, should be only one entity ifteleportRules: TeleportRulesisteleport_ride.
Must be a player name or atarget selector.
BE: ride: target: CommandSelector<Actor>

Specifies an mount.
Should be only one entity.
Must be a player name or atarget selector.
BE: rides: target: CommandSelector<Actor>

Specifies the mounts.
Must be a player name or atarget selector.
BE: teleportRules: TeleportRules: enum

Must be one ofteleport_rideandteleport_rider.
Specified which entities are teleported. If unspecified, defaults toteleport_rider.
BE: howToFill: FillType: enum

Must be one ofif_group_fitsanduntil_full.
- Ifif_group_fits, checks whether allriders: targetcan ride onride: targetat the same time, and makes them ride only if true.
- Ifuntil_fullor unspecified, makes them ride up one by one until it's full.

BE: entityType: EntityType: enum

Specifies the entities to be summoned.
Must be an ID of an entity type.
BE: spawnEvent: string: basic_string

Specifies the entity event for the to-be-summoned entities. Should be aspawn event(event name for entities in behavior pack).
Must be a string. And it must be a single word that has no space or a double-quoted string (When quoted,\can be used to escape characters).
BE: nameTag: string: basic_string

Specifies the name of the to-be-summoned entities.
Must be a string. And it must be a single word that has no space or a double-quoted string (When quoted,\can be used to escape characters).
BE: rideRules: RideRules: enum

Must be one ofno_ride_change,reassign_rides, andskip_riders.
- Ifskip_riders, summons entities only for<riders: target>that are not riding on another entity.
- Ifno_ride_change, summons entities only for<riders: target>that are not riding on and not ridden by other entity(s).
- Ifreassign_ridesor unspecified, makes<riders: target>dismount if they're riding, then summons entities for all of them.

## Result























| Command                 | Trigger                                                                                                                    | Java Edition | Bedrock Edition |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------|--------------|-----------------|
| Any                     | The command is incomplete, or any argument is not specified correctly.                                                     | Unparseable  | Unparseable     |
|                         | `<target>`or`<vehicle>`fails to resolve to an entity (named players must be online).                                       | Failed       | N/A             |
| `/ride ... mount ...`   | `<target>`is already riding on an entity.                                                                                  |              |                 |
|                         | `<vehicle>`is a player.                                                                                                    |              |                 |
|                         | A mounting loop is detected (`<vehicle>`is riding`<target>`, or its passengers, or passengers of its passengers, etc.).    |              |                 |
|                         | `<target>`and`<vehicle>`are in different dimensions.                                                                       |              |                 |
|                         | `<vehicle>`is amarker.                                                                                                     |              |                 |
| `/ride ... dismount`    | `<target>`is not riding on an entity.                                                                                      |              |                 |
| Any                     | `riders: target`,`rides: target`, or`ride: target`fails to resolve to one or more entities (named players must be online). | N/A          | Failed          |
| `/... start_riding ...` | More than one entity is targeted by`ride: target`.                                                                         |              |                 |
|                         | The entity targeted by`ride: target`is already full.                                                                       |              |                 |
|                         | `teleportRules: TeleportRules`is`teleport_ride`and more than one entity is targeted by`riders: target`.                    |              |                 |
|                         | `howToFill: FillType`is not specified or`until_full`and the`ride: target`is not rideable for all of`riders: target`.       |              |                 |
|                         | `howToFill: FillType`is`if_group_fits`and too many entities are targeted by`riders: target`to ride up at the same time.    |              |                 |
|                         | `howToFill: FillType`is`if_group_fits`and the`ride: target`is not rideable for at least one of`riders: target`.            |              |                 |
| `/... stop_riding`      | None of`riders: target`is riding on other entity.                                                                          |              |                 |
| `/... evict_riders`     | None of`rides: target`is ridden by other entities.                                                                         |              |                 |
| `/... summon_rider ...` | All`rides: target`are already full or not rideable for the riders.                                                         |              |                 |
|                         | Trying to summon hostiles in peaceful difficulty.                                                                          |              |                 |
| `/... summon_ride ...`  | All summoned entities are not rideable for`riders: target`.                                                                |              |                 |
|                         | Trying to summon hostiles in peaceful difficulty.                                                                          |              |                 |
| Any                     | Otherwise                                                                                                                  |              | Successful      |

## Output









| Command                 | Edition         | Situation  | Success Count                                                                       | /execute store success ... | /execute store result ... |
|-------------------------|-----------------|------------|-------------------------------------------------------------------------------------|----------------------------|---------------------------|
| Any                     | Java Edition    | On fail    | 0                                                                                   | 0                          | 0                         |
|                         |                 | On success | 1                                                                                   | 1                          | 1                         |
| Any                     | Bedrock Edition | On fail    | 0                                                                                   | N/A                        | N/A                       |
| `/... start_riding ...` |                 | On success | the number of entities that get riding on the targeted ride                         | N/A                        | N/A                       |
| `/... stop_riding ...`  |                 | On success | the number of entities that get dismounted                                          | N/A                        | N/A                       |
| `/... evict_riders ...` |                 | On success | the number of entities that successfully evict their riders                         | N/A                        | N/A                       |
| `/... summon_rider ...` |                 | On success | the number of summoned entities that successfully ride on their linked rides        | N/A                        | N/A                       |
| `/... summon_ride ...`  |                 | On success | the number of summoned entities that are successfully ridden by their linked riders | N/A                        | N/A                       |

## Example
In Java Edition, to ride and try to tame a skeleton horse or zombie horse:

- /ride @s mount @e[type=minecraft:skeleton_horse,limit=1]or/ride @s mount @e[type=minecraft:zombie_horse,limit=1]

In Java Edition, make the nearest player ride on an nearest arrow:

- /ride @p mount @e[type=arrow,sort=nearest,limit=1]

In Bedrock Edition, summon an arrow at the position of each player who have "A" tag:

- /ride @a[tag=A] summon_ride arrow

In Bedrock Edition, summon a charged creeper at the position of each player who have "A" tag:

- /ride @a[tag=A] summon_ride creeper reassign_rides minecraft:become_charged

