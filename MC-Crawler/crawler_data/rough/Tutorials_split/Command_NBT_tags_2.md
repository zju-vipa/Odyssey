### Villager
These tags are used when summoning villagers.  (Offers NBT can't be done in 1.14+)

| Tagname    | Description                               | Value type       | Syntax                                                                                    |
|------------|-------------------------------------------|------------------|-------------------------------------------------------------------------------------------|
| Profession | Determines the profession of the villager | Numerical, 0 - 5 | {Profession:#}                                                                            |
| Offers     | Determines what the villager sells        | A string         | {Offers:{Recipes:[{buy:{id:"stone",Count:1},maxUses:9999999,sell:{id:"stone",Count:1}}]}} |

### Item Frame
These tags are used when summoning itemframes.

| Tag name     | Description                                           | Value type                                                        | Syntax                                       |
|--------------|-------------------------------------------------------|-------------------------------------------------------------------|----------------------------------------------|
| Facing       | Determines the direction of the item frame            | Numerical, 0 - 5 (0 up; 1 down; 2 south; 3 north; 4 east; 5 west) | {Facing:#}                                   |
| ItemRotation | Determines the rotation of the item in the item frame | Numerical, 0 - 7 (Clockwise)                                      | {ItemRotation:#}                             |
| Item         | Determines the item in the item frame                 | A string                                                          | {Item:{id:"minecraft:<item>",Count:<count>}} |
| Invisible    | Determines if the item frame is invisible             | 0b or 1b                                                          | {Invisible:#}                                |
| Fixed        | Determines if the item frame is fixed                 | 0b or 1b                                                          | {Fixed:#}                                    |

### Potion
These tags are used to customize potions

| Tagname             | Description                                          | Value type                | Syntax                                                |
|---------------------|------------------------------------------------------|---------------------------|-------------------------------------------------------|
| Potion              | Determines which type of potion be receive in / give | minecraft:(potion effect) | {Potion:"minecraft:#"}                                |
| CustomPotionEffects | Customize the effect of potions                      | Numerical                 | {CustomPotionEffects:[{Id:#,Amplifier:#,Duration:#}]} |
| CustomPotionColor   | Determines the Color of Potion Bottle (1.11+)        | Decimal color code        | {CustomPotionColor:#}                                 |

### Armor Stand
These tags are used when summoning armor stands.

| NBT Tag     | Description                                                                 | Value type                                 | Syntax                                                                                                                 |
|-------------|-----------------------------------------------------------------------------|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| NoGravity   | Toggles gravity                                                             | 0b or 1b (0b for false, 1b for true)       | {NoGravity:#}                                                                                                          |
| ShowArms    | Determines whether you can see the armor stand's arms or not.               | Byte, 0b or 1b (0b for false, 1b for true) | {ShowArms:#}                                                                                                           |
| NoBasePlate | Determines whether the armor stand has a base plate or not.                 | Byte, 0b or 1b                             | {NoBasePlate:#}                                                                                                        |
| Small       | Determines whether the armor stand is small or not.                         | Byte, 0b or 1b                             | {Small:#}                                                                                                              |
| Rotation    | Changes the rotation of the armor stand                                     | Byte, 0b or 1b                             | {Rotation:[#f,#f]}                                                                                                     |
| Marker      | Small Hit box                                                               | Byte, 0b or 1b                             | {Marker:#}                                                                                                             |
| Pose        | Changes the pose of the armor stand's body parts. Any subtag can be ommited | Byte, 0b or 1b                             | {Pose:{Head:[#f,#f,#f],Body:[#f,#f,#f],LeftArm:[#f,#f,#f],RightArm:[#f,#f,#f],LeftLeg:[#f,#f,#f],RightLeg:[#f,#f,#f]}} |
| Invisible   | Determines whether the armor stand is invisible or not.                     | Byte, 0b or 1b                             | {Invisible:#}                                                                                                          |

Note: The Equipment tag also works for armor stands.

### Turtle
These tags are used when summoning turtles.

| Tagname    | Description                                                                             | Value type                       | Syntax         |
|------------|-----------------------------------------------------------------------------------------|----------------------------------|----------------|
| HomePosX   | Determines the X coordinate of a turtle's home beach.                                   | Numerical                        | {HomePosX:#}   |
| HomePosY   | Determines the Y coordinate of a turtle's home beach.                                   | Numerical                        | {HomePosY:#}   |
| HomePosZ   | Determines the Z coordinate of a turtle's home beach.                                   | Numerical                        | {HomePosZ:#}   |
| TravelPosX | Determines the distance a turtle can lay eggs from its home coordinates, on the X axis. | Numerical                        | {TravelPosX:#} |
| TravelPosY | Determines the distance a turtle can lay eggs from its home coordinates, on the Y axis. | Numerical                        | {TravelPosY:#} |
| TravelPosZ | Determines the distance a turtle can lay eggs from its home coordinates, on the Z axis. | Numerical                        | {TravelPosZ:#} |
| HasEgg     | Determines if the turtle has an egg to lay                                              | 0 – 0b – false<br/>1 – 1b – true | {HasEgg:#}     |

## Blocks
Tags used in /setblock and /fill:

| Tagname | Description                                                                                       | Value Type                       | Syntax                      |
|---------|---------------------------------------------------------------------------------------------------|----------------------------------|-----------------------------|
| Command | Used with command blocks. Places command block with command.                                      | A string                         | {Command:"desired command"} |
| auto    | Used with command blocks. Places command block with "Always Active" rather than "Needs Redstone". | 0 - 0b - false<br/>1 - 1b - true | {auto:#}                    |

Note: This is also used for Command Block Minecarts

### Generic
These tags can be used on most tile entitied blocks

| Tagname    | Description                                                                                                                  | Value Type            | Syntax                         |
|------------|------------------------------------------------------------------------------------------------------------------------------|-----------------------|--------------------------------|
| CustomName | Displayed in the top left corner of the inventory, instead of the regular name. Works only where such a regular name exists. | A JSON text component | {CustomName:"\"Custom Name\""} |
| Lock       | Says a name needed on a held item to open the inventory.                                                                     | A string              | {Lock:"Key's Name"}            |

### Beacon
| Tagname   | Description                                                                                                                                            | Value Type                     | Syntax        |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|---------------|
| Primary   | This determines the firststatus effectthat the beacon creates. It defaults to level 1 of the effect.                                                   | An ID of a status effect.      | {Primary:#}   |
| Secondary | This determines the second status effect. If its the same as Primary, then it increases the status effect to level 2. Otherwise it is level 1.         | Also an ID of a status effect. | {Secondary:#} |
| Levels    | This number determines how many layers of valid blocks are below the beacon. This value updates automatically, and overrides /data inputs immediately. | Integer                        | {Levels:#}    |

### Spawner
These tags are used when using /setblock or /summon (spawner minecarts) to create spawners. Add only those data tags you want to avoid a potential error.

| Tagname             | Description                                                                                                                                                                                                                                                | Value Type        | Syntax                                                                      |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|-----------------------------------------------------------------------------|
| EntityId            | Specifies what entity the spawner spawns.                                                                                                                                                                                                                  | A ID of a Mob     | {SpawnData:{entity: {id: "minecraft:EntityName"}}                           |
| SpawnData           | Used for spawners that spawn entities with data tags.                                                                                                                                                                                                      | An entity NBT tag | {SpawnData:{NBT tag}}                                                       |
| SpawnCount          | How many entities the spawner can spawn at one time.                                                                                                                                                                                                       | Integer           | {SpawnCount:#}                                                              |
| SpawnRange          | The range of which the entities can spawn.                                                                                                                                                                                                                 | Integer           | {SpawnRange:#}                                                              |
| RequiredPlayerRange | The range of which a player must be in for the spawner to start spawning entities.                                                                                                                                                                         | Integer           | {RequiredPlayerRange:#}                                                     |
| Delay               | The number of ticks before entities spawn when a player is first detected.                                                                                                                                                                                 | Integer           | {Delay:#}                                                                   |
| MinSpawnDelay       | After the first spawn, this is the minimum amount of ticks before more entities can spawn.                                                                                                                                                                 | Integer           | {MinSpawnDelay:#}                                                           |
| MaxSpawnDelay       | Similar to MinSpawnDelay. After the first spawn, this is the maximum amount of ticks before more entities can spawn.                                                                                                                                       | Integer           | {MaxSpawnDelay:#}                                                           |
| MaxNearbyEntities   | Checks the number of entities within the spawn range ('SpawnRange' tag). If the number of entities it detects is over the set MaxNearbyEntities number, it does not spawn more entities unless the amount of entities within the spawn range is decreased. | Integer           | {MaxNearbyEntities:#}                                                       |
| SpawnPotentials     | Used when creating spawners that spawn multiple types of entities. A weighted list of entities to be spawned, including NBT tags.                                                                                                                          | A List            | SpawnPotentials:[{data: {entity: {id: "minecraft:EntityName"} }, weight:#}] |
| Weight              | Used if spawning multiple entities using SpawnPotentials. If the same as another SpawnPotentials entity, both have an even chance of spawning.                                                                                                             | A number          | {Weight:#}                                                                  |

Sub-tags used in the SpawnPotentials data tag.

| Tagname    | Description                                                                                                                                                               | Value Type        | Syntax                                     |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--------------------------------------------|
| Type       | Determines the other entity that spawns with the entity specified in the EntityId data tag. MUST be used with SpawnPotentials.                                            | A string          | {SpawnPotentials:[{Type:"EntityName"}]}    |
| Weight     | Determines the chance of spawning the entity specified in the 'Type' sub-tag. If set to the same as another other entity's weight, they have the same chance of spawning. | A number          | {SpawnPotentials:[{Weight:#}]}             |
| Properties | Determines the entity data tag(s) that the entity (specified in the 'Type' sub-tag) is spawned with.                                                                      | An entity NBT tag | {SpawnPotentials:[{Properties:{NBT tag}}]} |


