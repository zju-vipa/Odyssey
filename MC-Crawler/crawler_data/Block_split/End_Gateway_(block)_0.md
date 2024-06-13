# End Gateway (block)
The end gateway is a block that forms a part of end gateways, which teleport the player between the main island and the outer islands in the End.

## Contents
- 1 Obtaining
	- 1.1 Post-generation
	- 1.2 Natural generation
- 2 Usage
	- 2.1 Beam
	- 2.2 Piston interactivity
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block data
- 5 History
	- 5.1 End gateway "item"
		- 5.1.1 Appearances
		- 5.1.2 Names
- 6 Issues
- 7 Gallery
- 8 Trivia
- 9 References

## Obtaining
The command used to get an end gateway.
The end gateway block cannot be obtained as an item even by using the /give command. The item form is completely nonexistent in Java Edition, but it can be obtained through add-ons, external editors or by using bugs in Bedrock Edition.

The end gateway block can be placed using commands such as /fill or /setblock in Java Edition. It cannot be placed by such commands in Bedrock Edition, but it can be placed using structure blocks.

### Post-generation
An end gateway
End gateway blocks form the functional part of end gateways. Each time the ender dragon is defeated, one end gateway spawns around the central island in the End, up to 20 times. Activating each of them spawns one additional gateway in the outer islands.

### Natural generation
More naturally generated gateways that transport the player back to the obsidian platform can be found throughout the outer End islands.


## Usage
End gateway blocks in their original form can be used to teleport to the outer islands of the End. End gateway blocks can be used as a custom teleporter using NBT tags‌[Java Edition  only].

- ExitPortaltag holds a set of X/Y/Z coordinates to determine the general location the player can be "safely" teleported to when entering.
- SettingExactTeleportto 1 teleports entities to the specified coordinates exactly instead of at a safer location around those coordinates.
- Agedetermines how long the gateway has existed. This is used to determine when the beam is rendered.
- Example:/setblock ~ ~-1 ~1 minecraft:end_gateway{Age:180,ExactTeleport:1,ExitPortal:{X:1,Y:2,Z:3}} replace

When created in a dimension other than the End without ExitPortal NBT data, it does not teleport entities but still activates its beam effect when an entity enters.

In Bedrock Edition and Minecraft Education, when the gateway is placed and entered in the End, it teleports the user to coordinates 0, 0, 0, below the main island. In the Overworld or Nether, it acts as a solid block and cannot be entered.
Gateways have a small chance to teleport the player directly into the void at Y=0.

### Beam
When generated (either naturally as part of an end gateway, or through /setblock‌[Java Edition  only]), the block emits a  magenta beam of light vertically from its top and bottom, lasting for 200 game ticks (10 seconds) while fading in and out.

An end gateway block also emits a  purple beam of light vertically from the top and bottom when an entity enters it. During the 40 game ticks (2 seconds) this beam is visible, no additional entities can be teleported.

It also emits the  purple teleport beam every 2400 game ticks (2 minutes). This beam also lasts 40 game ticks (2 seconds) and disables teleportation of the gateway while it's visible[1].

The creation beam extends from around Y=0 through the block up to Y=256; the teleport beam goes 50 blocks above and below the gateway block. The beam is visible from roughly the same distance as a single ordinary stack of blocks. If a render distance of 16 chunks is set, the beam of light is visible from up to 255 blocks away. Unlike the beam of a beacon, this beam does not change color if the player puts stained glass over it.

It is not possible to disable either of the beams entirely. However, it is possible to edit the age of the block to a negative value, effectively delaying beam-emitting properties of the end gateway. You can change the age of the block by entering the command (for example) as follows: /setblock ~ ~ ~ minecraft:end_gateway{Age:-9223372036854775808L}. This will last for 14,993,257,186 years, effectively disabling the beam.

### Piston interactivity
End gateway blocks cannot be interacted with pistons or sticky pistons.

## Data values

  

This section is missing information about block tags. 
Please expand the section to include this information. Further details may exist on the talk page.


### ID
Java Edition:

| Name        | Identifier  | Form  | Block tags                                            | Translation key             |
|-------------|-------------|-------|-------------------------------------------------------|-----------------------------|
| End Gateway | end_gateway | Block | dragon_immuneportalswither_immuneinvalid_spawn_inside | block.minecraft.end_gateway |

| Name         | Identifier  |
|--------------|-------------|
| Block entity | end_gateway |

Bedrock Edition:

| Name        | Identifier  | Numeric ID | Form                         | Item ID[i 1]   | Translation key |
|-------------|-------------|------------|------------------------------|----------------|-----------------|
| End Gateway | end_gateway | 209        | Block & Ungiveable Item[i 2] | Identical[i 3] | —               |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Unavailable with /give command

↑ The block's direct item form has the same id as the block.


| Name         | Savegame ID |
|--------------|-------------|
| Block entity | EndGateway  |

### Block data
An end gateway block has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format


 Block entity data
Tags common to all block entities
 Age: Age of the portal, in ticks. This is used to determine when the beam is rendered.
 ExactTeleport: 1 or 0 (true/false) - Teleports entities directly to the ExitPortal coordinates instead of near them.
 ExitPortal: Location entities are teleported to when entering the portal.
 X: X coordinate of target location.
 Y: Y coordinate of target location.
 Z: Z coordinate of target location.

Bedrock Edition:

See Bedrock Edition level format/Block entity format.

