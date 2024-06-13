# Sculk Sensor
The sculk sensor is a block in the sculk family. It detects vibrations caused by actions and events in a radius around it and emits a redstone signal, and, if it was triggered by a player, also activates nearby sculk shriekers. Players can sneak to avoid making vibrations and wool can be used to occlude and block them.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Chest loot
	- 1.4 Post-generation
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Light
	- 2.3 Vibration detection
	- 2.4 Redstone emission
		- 2.4.1 Vibration frequencies
		- 2.4.2 Vibration resonance
		- 2.4.3 Things which are not detected
	- 2.5 Piston interactivity
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Block data
- 5 Achievements
- 6 Advancements
- 7 History
- 8 Issues
- 9 Trivia
- 10 Gallery
	- 10.1 Screenshots
	- 10.2 Development images
- 11 References
- 12 External links

## Obtaining
### Breaking
Sculk sensors can be mined with any tool enchanted with Silk Touch, but hoes are the quickest. If mined with a non-Silk Touch tool, they drop 5 experience instead.

| Block     | Sculk Sensor          |
|-----------|-----------------------|
| Hardness  | 1.5                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 2.25                  |
| Wooden    | 1.15                  |
| Stone     | 0.6                   |
| Iron      | 0.4                   |
| Diamond   | 0.3                   |
| Netherite | 0.25                  |
| Golden    | 0.2                   |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Natural generation
Sculk sensors generate within the deep dark biome and ancient cities.


### Chest loot
| Item         | Structure    | Container | Quantity | Chance                         |
|--------------|--------------|-----------|----------|--------------------------------|
|              |              |           |          | Java EditionandBedrock Edition |
| Sculk Sensor | Ancient City | Chest     | 1–3      | 23.2%                          |

### Post-generation
A sculk catalyst has a 9% chance of generating a sculk sensor on top of a sculk block.

## Usage
### Crafting ingredient
Sculk sensors can be used to craft calibrated sculk sensors.

| Name                    | Ingredients                 | Crafting recipe |
|-------------------------|-----------------------------|-----------------|
| Calibrated Sculk Sensor | Amethyst Shard+Sculk Sensor |                 |

### Light
A sculk sensor has a light level of 1. When active, it changes to a lighter block state without a change to the light level.

### Vibration detection
The sculk sensor vibration particle.
Sculk sensors detect vibrations in an 8 block spherical radius around it. Vibrations are caused by various events, such as a player and mobs walking, placing or breaking blocks, gliding with elytra, items falling on the ground, a piston extending or a wet wolf shaking itself off. While sneaking, a player is not detected. Walking, falling, dropping items, or shooting a projectile all trigger the sensor.

When a vibration is made within the range of a sculk sensor, a signal travels from the vibration source to the sensor at a speed of one block per game tick (20 blocks per second). When the signal arrives, the sensor is activated for 30 game ticks (1.5 seconds). The sensor cannot detect any other vibrations while activated or while a signal is traveling to it.

Sculk sensors have a cooldown period of 10 game ticks (0.5 seconds) after being placed or after deactivating. During this cooldown period, they cannot detect vibrations. This prevents a sensor from reactivating when a contraption it is powering (such as a piston) becomes unpowered.

Sculk sensors don't detect vibrations from other sculk sources or the warden in Java Edition.

Wool and carpets have a special interaction with sculk sensors. If a wool block is placed between a sensor and a vibration source, the sensor is not able to detect the placed wool nor vibrations behind it. Specifically, if the ray joining the cube centers of the sensor block and the vibration source passes through any wool blocks, the noise is muffled. If the ray passes diagonally through the edge between two blocks, either one or the other block may muffle it but not both. Sculk sensors are not able to detect footsteps or dropped items on wool blocks or carpet, and they are also unable to detect dropped items of wool and carpets.

Sculk sensors pass on the vibrations made by players to sculk shriekers within 8 blocks of the sensor. For example, an item dropped by a player triggers the shrieker, but an item dropped by a dispenser or from a broken block does not; a player flying around with elytra triggers the shrieker, but a bat flying around does not. Alarms can be blocked by wool placed in between the sensor and shrieker, similar to how wool can block vibrations from reaching the sensor itself.

### Redstone emission
Sculk sensors emit a redstone signal when they are activated. The strength of the redstone signal is inversely proportional to the distance the vibration signal traveled – the closer the vibration is to the sculk sensor, the stronger the redstone signal is, so it reaches the maximum redstone signal strength when the vibration is directly on top of the sensor.

#### Vibration frequencies

  

This section needs expansion. 
You can help by expanding it.Instructions: Bedrock Edition values


Each vibration in the game falls under a certain frequency value. This value can be measured with a comparator. With the right contraption, the player could detect if a certain action has occurred or is occurring nearby.

| Output | Vibration type       | Game event                     | Description                                                                                    |
|--------|----------------------|--------------------------------|------------------------------------------------------------------------------------------------|
| 1      | Step                 | minecraft:step                 | Player or entity steps                                                                         |
|        | Swim                 | minecraft:swim                 | Player or entity swims, boat paddles                                                           |
|        | Flap                 | minecraft:flap                 | Entity flaps (bat)                                                                             |
|        | Resonate 1           | minecraft:resonate_1           |                                                                                                |
| 2      | Projectile Land      | minecraft:projectile_land      | Projectile lands (snowball)                                                                    |
|        | Hit Ground           | minecraft:hit_ground           | Player or entity hits ground post-jump or fall                                                 |
|        | Splash               | minecraft:splash               | Player or entity splashes. Entity enters water or bubble column                                |
|        | Resonate 2           | minecraft:resonate_2           |                                                                                                |
| 3      | Item Interact Finish | minecraft:item_interact_finish | Item interaction (shield, spyglass, bone meal)                                                 |
|        | Projectile Shoot     | minecraft:projectile_shoot     | Projectile shoots (arrow, firework, etc.)                                                      |
|        | Instrument Play      | minecraft:instrument_play      | Goat horn plays                                                                                |
|        | Resonate 3           | minecraft:resonate_3           |                                                                                                |
| 4      | Entity Action        | minecraft:entity_action        | Entity roars (ravager), entity shakes (wolf after swimming), villager holds item, sniffer digs |
|        | Elytra Glide         | minecraft:elytra_glide         | Player glides                                                                                  |
|        | Resonate 4           | minecraft:resonate_4           |                                                                                                |
| 5      | Entity Dismount      | minecraft:entity_dismount      | Player dismounts                                                                               |
|        | Equip                | minecraft:equip                | Armor equipped in armor slot or stand                                                          |
|        | Resonate 5           | minecraft:resonate_5           |                                                                                                |
| 6      | Entity Mount         | minecraft:entity_mount         | Player mounts (horse)                                                                          |
|        | Entity Interact      | minecraft:entity_interact      | Player interaction with entity (breeding)                                                      |
|        | Shear                | minecraft:shear                | Sheep being sheared                                                                            |
|        | Resonate 6           | minecraft:resonate_6           |                                                                                                |
| 7      | Entity Damage        | minecraft:entity_damage        | Damage or death to entities (except armor stand)                                               |
|        | Resonate 7           | minecraft:resonate_7           |                                                                                                |
| 8      | Drink                | minecraft:drink                | Entity drinks                                                                                  |
|        | Eat                  | minecraft:eat                  | Entity eats                                                                                    |
|        | Resonate 8           | minecraft:resonate_8           |                                                                                                |
| 9      | Container Close      | minecraft:container_close      | Container (chest, shulker box, hopper) closes                                                  |
|        | Block Close          | minecraft:block_close          | Door, trapdoor, or fence gate closes                                                           |
|        | Block Deactivate     | minecraft:block_deactivate     | Block deactivation (piston, button, lever, pressure plate)                                     |
|        | Block Detach         | minecraft:block_detach         | Tripwire detachment                                                                            |
|        | Resonate 9           | minecraft:resonate_9           |                                                                                                |
| 10     | Container Open       | minecraft:container_open       | Container opens                                                                                |
|        | Block Open           | minecraft:block_open           | Door opens                                                                                     |
|        | Block Activate       | minecraft:block_activate       | Block activation                                                                               |
|        | Block Attach         | minecraft:block_attach         | Attachment of tripwire hook                                                                    |
|        | Prime Fuse           | minecraft:prime_fuse           | TNT or creeper activates                                                                       |
|        | Note Block Play      | minecraft:note_block_play      | Note block sounds                                                                              |
|        | Resonate 10          | minecraft:resonate_10          |                                                                                                |
| 11     | Block Change         | minecraft:block_change         | Block change (chiseled bookshelf, lectern)                                                     |
|        | Resonate 11          | minecraft:resonate_11          |                                                                                                |
| 12     | Block Destroy        | minecraft:block_destroy        | Block destruction                                                                              |
|        | Fluid Pickup         | minecraft:fluid_pickup         | Gathered fluid (water, honey bottle, powdered snow)                                            |
|        | Resonate 12          | minecraft:resonate_12          |                                                                                                |
| 13     | Block Place          | minecraft:block_place          | Block placement                                                                                |
|        | Fluid Place          | minecraft:fluid_place          | Fluid placement                                                                                |
|        | Resonate 13          | minecraft:resonate_13          |                                                                                                |
| 14     | Entity Place         | minecraft:entity_place         | Entity placement via spawn-egg, mob spawner, or evoker magic                                   |
|        | Lightning Strike     | minecraft:lightning_strike     | Lightning strikes                                                                              |
|        | Teleport             | minecraft:teleport             | Endermen, chorus fruit, shulker, or ender pearl teleportation                                  |
|        | Resonate 14          | minecraft:resonate_14          |                                                                                                |
| 15     | Entity Die           | minecraft:entity_die           | Armor stand dies, firework finishes                                                            |
|        | Explode              | minecraft:explode              | TNT, end crystal, bed/respawn anchor, or creeperexplodes                                       |
|        | Resonate 15          | minecraft:resonate_15          |                                                                                                |

#### Vibration resonance
When a sculk sensor detects a vibration, any adjacent block of amethyst will reemit a vibration on the same frequency that the sculk sensor detected.

#### Things which are not detected
The following occurrences, despite presumably causing physical motion, do not produce vibrations and therefore cannot be detected: 

- Blocks destroyed by a fluid flowing into their space[1]
- Several blocks being destroyed due to their supporting block being removed:[2]
	- Rails
	- Powered rails
	- Detector rails
	- Activator rails
	- Redstone wire
	- Redstone repeaters
	- Redstone comparators
- Several cases where adispenserfails to perform an action:[3]
	- Flint and steel not creating fire
	- Bone meal not growing something
	- Heads and carved pumpkins, if not equipped on something or placed
	- Shulker boxes, if not placed
	- Shears, if there's nothing to shear
	- Glowstone, if it doesn't charge a respawn anchor
- Inserting aneye of enderinto anend portal frame[4][5]
- Eyes of ender breaking[6]
- Silverfishentering blocks[7]
- Waterandlavaflowing into existing spaces, or drying up[8]
- Changing the mode of aredstone comparator[9]
- Changing the delay on aredstone repeater[10]
- Changing the shape of a single unit ofredstone wire[11]
- Fireextinguished by rain[12]

The following cases have been confirmed to be intentional: 

- Axolotlsbeing bred via tropical fish buckets[13]
- Moss blocksreplacing existing blocks[14]

### Piston interactivity
Sculk sensors are immovable. Pistons cannot push them, and sticky pistons cannot push or pull them. Slime blocks and honey blocks do not stick to sculk sensors and have no effect whether the slime block or honey block is being pushed or pulled.

## Data values
### ID
Java Edition:

| Name         | Identifier   | Form         | Translation key              |
|--------------|--------------|--------------|------------------------------|
| Sculk Sensor | sculk_sensor | Block & Item | block.minecraft.sculk_sensor |

| Name         | Identifier   |
|--------------|--------------|
| Block entity | sculk_sensor |

Bedrock Edition:

| Name         | Identifier   | Numeric ID | Form                       | Item ID[i 1]   | Translation key        |
|--------------|--------------|------------|----------------------------|----------------|------------------------|
| Sculk Sensor | sculk_sensor | 562        | Block & Giveable Item[i 2] | Identical[i 3] | tile.sculk_sensor.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


| Name         | Savegame ID |
|--------------|-------------|
| Block entity | SculkSensor |

### Block states
See also: Block states

Java Edition:

| Name               | Default value | Allowed values         | Description                                                          |
|--------------------|---------------|------------------------|----------------------------------------------------------------------|
| power              | 0             | 0123456789101112131415 | The sculk sensor's current power level.                              |
| sculk_sensor_phase | inactive      | activecooldowninactive | Whether or not the sculk sensor is active.[more information needed]  |
| waterlogged        | false         | falsetrue              | Whether or not there's water in the same place as this sculk sensor. |

Bedrock Edition:

| Name               | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                      |
|--------------------|---------------|---------------|----------------|-------------------------|--------------------------------------------------|
| sculk_sensor_phase | Not Supported | 0             | 012            | Unsupported             | The sculk sensor phase.[more information needed] |



### Block data
A sculk sensor has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format


: Block entity data.
Tags common to all block entities
 last_vibration_frequency: The frequency of the last vibration.
 listener: The vibration event listener for this sculk shrieker, sculk sensor, or calibrated sculk sensor.
 event: Only exists if there is an incoming vibration.
 distance: The distance between this vibration's source and the block.
 game_event: The resource location of the vibration event that caused the current incoming vibration.
 pos: The coordinates of the source of this vibration.
: X coordinate.
: Y coordinate.
: Z coordinate.
 projectile_owner: If the vibration was caused by a projectile, this is the UUID of the entity that launched the projectile. Does not exist if vibration was not caused by a projectile.
 source: The UUID of the entity that caused the vibration. Does not exist if vibration was not caused by an entity.
 event_delay: How many ticks remain until triggered by the vibration. Set to 0 if there is no incoming vibration
 selector: The data of the vibration selector.[more information needed]
 tick: The game time when the vibration occurs, or -1 if there is no vibration to choose from.[more information needed]
 event: Candidate game event, with the same structure as the  event tag above.[more information needed]

Bedrock Edition:

See Bedrock Edition level format/Block entity format.
