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


