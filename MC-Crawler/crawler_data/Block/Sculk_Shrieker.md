# Sculk Shrieker
A sculk shrieker is a sculk block found in the deep dark that produces a "shrieking" noise when triggered. It can only be triggered by a player, either by standing on it (even while sneaking) or by triggering a nearby sculk sensor. Natural sculk shriekers also inflict Darkness and may summon a warden when triggered, but those placed by players or sculk catalysts are inert and unable to summon wardens or inflict Darkness under any circumstance.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Post-generation
- 2 Usage
	- 2.1 Spawning wardens
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Block data
- 5 Advancements
- 6 History
- 7 Issues
- 8 Trivia
- 9 Gallery
	- 9.1 Screenshots
- 10 References

## Obtaining
### Breaking
Sculk shriekers can be mined with any tool, but hoes are the quickest. It drops 5 experience when mined without Silk Touch. When a sculk shrieker is broken it loses the ability to summon wardens, even if mined with Silk Touch.

| Block     | Sculk Shrieker        |
|-----------|-----------------------|
| Hardness  | 3                     |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 4.5                   |
| Wooden    | 2.25                  |
| Stone     | 1.15                  |
| Iron      | 0.75                  |
| Diamond   | 0.6                   |
| Netherite | 0.5                   |
| Golden    | 0.4                   |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Natural generation
Sculk shriekers can be found infrequently within the deep dark biome, and they are much more common within ancient cities. These shriekers can summon wardens.


### Post-generation
A sculk catalyst has a 1% chance of generating a sculk shrieker on top of a sculk block. These shriekers do not summon wardens.

## Usage
The shriek particle.
Sculk shriekers "shriek" after being activated. A sculk shrieker activates when any player stands on the black part in the center of the block, even when sneaking. Sculk shriekers are also activated by any sculk sensor triggered within an 8-block spherical radius of itself, but only if the vibration was caused by a player. However, a sculk sensor cannot activate the sculk shrieker if the line between the two contains a wool block. The shrieker shrieks for exactly 90 game ticks (4.5 seconds). 

### Spawning wardens
A set of shriek particles emitted by a sculk shrieker.
Sculk shriekers that naturally generate in the deep dark biome are capable of inflicting the Darkness effect upon players and summoning wardens. If a sculk shrieker is placed by a player or generated via a sculk catalyst, the tag can_summon is set to false, and therefore a warden cannot be summoned and Darkness cannot be inflicted by that sculk shrieker[1]. Each time a naturally generated sculk shrieker is activated, it adds 1 to a "warning" level to alert a warden. The warning level is specific to each player, not each sculk shrieker, meaning that the same player can activate a different sculk shrieker for each of the four times, and a warden still spawns on the fourth activation, even though any particular shrieker had been activated once. If a player does not activate any sculk shrieker, the warning level decreases by 1 every 10 minutes (12000 ticks). After the shrieking ends, all players in Survival or Adventure mode within 40 blocks are given the Darkness effect for 12 seconds. After a warden is summoned, a player's warning level does not reset back to 0, meaning multiple wardens can be summoned.

Naturally generated sculk shriekers have a 10-second cooldown per player. This means that if a player triggers one shrieker, they are completely unable to trigger any other shrieker within 10 seconds. The cooldown period includes the 4.5-second shrieking, which means 5.5 seconds after the previous shrieking ends, the player can activate sculk shriekers again.

When a player's warning level reaches level 4, the sculk shrieker attempts to spawn a warden after its shrieking ends. If the shrieker is broken before it ends shrieking, a warden spawns immediately. Up to 20 attempts are made to spawn a warden within an 11×13×11 box centered on the shrieker. If there isn't another warden within 24 blocks, a warden emerges from the ground. The warden always spawns at the highest available block. If all 20 spawning attempts fail, a loud roaring sound is played.

In Java Edition, if the game rule doWardenSpawning is set to false, naturally generated sculk shriekers behave as if they are placed by a player: they do shriek, but there is no shrieking cooldown, the player's warning level does not increase, no Darkness effect is inflicted, and no warden spawns.

If the player that triggered the sculk shrieker is outside the shrieker's range when the shrieking ends, the sculk shrieker does not apply the Darkness effect to any player. The player's warning level still increases by 1.

It is possible to make a warden spawn from a distance, by shooting a projectile into the direction of known sensors that are near shriekers.

The warnings have unique subtitles at different levels of warning: 1) "Warden approaches." 2) "Warden advances." 3) "Warden draws close."

## Data values
### ID
Java Edition:

| Name           | Identifier     | Form         | Translation key                |
|----------------|----------------|--------------|--------------------------------|
| Sculk Shrieker | sculk_shrieker | Block & Item | block.minecraft.sculk_shrieker |

| Name         | Identifier     |
|--------------|----------------|
| Block entity | sculk_shrieker |

Bedrock Edition:

| Name           | Identifier     | Numeric ID | Form                       | Item ID[i 1]   | Translation key          |
|----------------|----------------|------------|----------------------------|----------------|--------------------------|
| Sculk Shrieker | sculk_shrieker | 716        | Block & Giveable Item[i 2] | Identical[i 3] | tile.sculk_shrieker.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


| Name         | Savegame ID   |
|--------------|---------------|
| Block entity | SculkShrieker |

### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values | Description                                                            |
|-------------|---------------|----------------|------------------------------------------------------------------------|
| can_summon  | false         | falsetrue      | If true, the sculk shrieker can summon thewarden.                      |
| shrieking   | false         | falsetrue      | Whether the sculk shrieker is shrieking or not.                        |
| waterlogged | false         | falsetrue      | Whether or not there's water in the same place as this sculk shrieker. |

Bedrock Edition:

| Name       | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                       |
|------------|---------------|---------------|----------------|-------------------------|---------------------------------------------------|
| active     | Not Supported | 0             | 01             | Unsupported             | Whether the sculk shrieker is shrieking or not.   |
| can_summon | Not Supported | false         | truefalse      | Unsupported             | If true, the sculk shrieker can summon thewarden. |



### Block data
A sculk shrieker has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format


: The block entity's root tag.
 VibrationListener: The vibration event listener of the sculk shrieker, sculk sensor, and calibrated sculk sensor.
 event: Unknown.
 pending: Unknown.
 distance: Unknown.
 source: Unknown.
 vibration: Unknown.
 x: Unknown.
 y: Unknown.
 z: Unknown.
 selector: Unknown.
 ticks: Unknown.

Bedrock Edition:

See Bedrock Edition level format/Block entity format.
