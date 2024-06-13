# Conduit
A conduit is a beacon-like block that provides Conduit Power effect and attacks monsters underwater.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
- 2 Usage
	- 2.1 Conduit power
	- 2.2 Light source
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Block entity
- 5 Achievements
- 6 Advancements
- 7 History
- 8 Issues
- 9 Trivia
- 10 Gallery
	- 10.1 Renders
	- 10.2 Screenshots
- 11 Notes
- 12 See also
- 13 External links

## Obtaining
### Breaking
A conduit drops as an item when broken with any tool or by hand, but a pickaxe is the fastest way to break it.

Like other precious blocks such as beacons and shulker boxes, when destroyed by an explosion, a conduit always drops as an item.

| Block     | Conduit               |
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


### Crafting
| Ingredients                     | Crafting recipe |
|---------------------------------|-----------------|
| Nautilus Shell+Heart of the Sea |                 |

## Usage
### Conduit power



1



































2



































3



































4



































5




































Schematic of a conduit in an activation frame. Click the scale on the right to view the layers.The conduit and water are required. The frame must include 16-42 blocks of prismarine, dark prismarine, sea lanterns, and/or prismarine bricks. Unused frame-blocks and empty spaces can be anything.


When activated, conduits give the "Conduit Power" effect to all players in contact with rain or water, within a spherical range of 32-96 blocks. This effect restores oxygen, gives underwater night vision and increases mining speed by 16.7% (1/6th). Conduits also damage any hostile mobs, like drowned, guardians, and elder guardians, within a range of 8 blocks of the conduit. Conduits can be activated in any biome and at any height or depth.

To activate, a conduit needs to be in the center of a 3×3×3 volume of water (source blocks, flowing water, and/or waterlogged blocks), which itself must be enclosed within an activation frame. The frame is built out of blocks in three 5×5 open squares centered on the conduit, one around each axis. Only prismarine, dark prismarine, prismarine bricks, and sea lantern blocks in the frame contribute to activation. A minimum of 16 blocks are required and produce an effective range of 32 blocks. Prismarine-type slabs (including double slabs), stairs, and walls cannot be used to activate the conduit. Any blocks (of any type) that are not part of the activation frame itself but are in the 5×5×5 outer shell likewise have no effect. Once activated, removing any blocks away from the conduit (frame blocks) deactivates the conduit.[note 1]

The effective radius of the conduit is 16 blocks for every seven blocks in the frame, though the effect does not activate until the minimum of 16 blocks is included in the build. Thus, it extends to 48 at 21 blocks, 64 at 28 blocks, 80 at 35 blocks, and 96 with a complete frame of 42 blocks. When the frame is complete, the center of the conduit displays an orange iris-like shape. A complete frame also carries the additional advantage of attacking hostile mobs within 8 blocks of the conduit by 4 every 2 seconds, if they are in contact with water or rain.[note 2]

Monsters that are attacked by the conduit:


Blaze
Bogged‌[upcoming: JE 1.21 & BE 1.21]
Breeze‌[upcoming: JE 1.21 & BE 1.21]
Cave Spider
Creeper
Drowned
Elder Guardian
Ender Dragon
Enderman
Endermite
Evoker
Ghast
Giant ‌[JE  only]
Guardian
Hoglin
Husk
Illusioner ‌[JE  only]
Magma Cube
Phantom
Piglin
Piglin Brute
Pillager
Ravager
Shulker
Silverfish
Skeleton
Skeleton Horse ‌[BE  only]
Slime
Spider
Stray
Vex
Vindicator
Warden
Witch
Wither
Wither Skeleton
Zoglin
Zombie
Zombie Horse ‌[BE  only]
Zombie Villager
Zombified Piglin
### Light source
Conduits emit a light level of 15, the brightest light level in the game, whether activated or not, and even on land.

## Data values
### ID
Java Edition:

| Name    | Identifier | Form         | Block tags       | Translation key         |
|---------|------------|--------------|------------------|-------------------------|
| Conduit | conduit    | Block & Item | mineable/pickaxe | block.minecraft.conduit |

| Name         | Identifier |
|--------------|------------|
| Block entity | conduit    |

Bedrock Edition:

| Name    | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key   |
|---------|------------|------------|----------------------------|----------------|-------------------|
| Conduit | conduit    | 412        | Block & Giveable Item[i 2] | Identical[i 3] | tile.conduit.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


| Name         | Savegame ID |
|--------------|-------------|
| Block entity | Conduit     |

### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values | Description                                                     |
|-------------|---------------|----------------|-----------------------------------------------------------------|
| waterlogged | true          | falsetrue      | Whether or not there's water in the same place as this conduit. |

### Block entity
A conduit has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format


 Block entity data
Tags common to all block entities
 Target: The UUID of the hostile mob the conduit is currently attacking, stored as four ints. May not be present.

Bedrock Edition:

See Bedrock Edition level format/Block entity format.
## Notes

↑ Conduits can be activated only by full blocks by design; see MC-128661

↑ Completed conduits only damage one mob at a time; see MC-198923


## See also
- Beacon

