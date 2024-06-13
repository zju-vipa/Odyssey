# End Portal (block)
The end portal block is a block generated when an end portal or exit portal is activated, which teleports the player between the Overworld and the End.

## Contents
- 1 Obtaining
- 2 Usage
	- 2.1 Properties
	- 2.2 Piston interactivity
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block data
- 5 History
	- 5.1 End portal "item"
		- 5.1.1 Appearances
		- 5.1.2 Names
- 6 Issues
- 7 Gallery
- 8 References

## Obtaining
The end portal block cannot be obtained as an item even by using the /give command. The item form is completely nonexistent in Java Edition, but it can be obtained through add-ons, external editors or by using bugs in Bedrock Edition.

The end portal block can be placed using commands such as /fill or /setblock or simply by building end portals. 

## Usage
End portal blocks can be used to teleport into and out of the End. When a player or other entity in the Overworld or the End touches an end portal block, it is instantly taken to the other dimension. If a single portal block is placed using commands, it can still be used to travel between dimensions.

All entities traveling to the End appear on the obsidian platform, recreating it if necessary. Players traveling to the Overworld appear at their individual spawn point, while other entities appear at the world spawn point.

### Properties
- End portal blocks can be destroyed in Creative mode. This does not affect adjacent end portal blocks.
- End portals do not reduce fall damage.‌[Java Edition  only]
- The top surface of an End portal is3⁄4the height of a full block.[verify]
- The end portal is one of the only blocks without a conventional texture or entity texture; it instead duplicates and layers a starfield pattern.
- IfTNTis detonated on an end portal, no blocks in its blast radius are destroyed.
- Ridden entities (and their riders) pass through the portal without being teleported.
- Ender dragonscannot teleport through portals.
- InJava Edition,witherscannot teleport through portals, but can do so inBedrock Edition.
- If/setblockis used to place an end portal block in theOverworld,Nether, or in acustom dimension, then it teleports the player to the End dimension. If the end portal block is placed inthe End, then it teleports the player to theirspawn point.
- If the end portal block is generated in the block grid using thedebug modeworld type, it teleports the player to the Overworld regardless of which dimension it is in.
- Items can fall through an end portal, including falling blocks, such asTNT. The items appear in the End dimension.

### Piston interactivity
End portal blocks cannot be pushed by pistons. They also cannot be pushed nor pulled by sticky pistons.

## Data values

  

This section is missing information about block tags. 
Please expand the section to include this information. Further details may exist on the talk page.


### ID
Java Edition:

| Name       | Identifier   | Form  | Block tags                                                                   | Translation key              |
|------------|--------------|-------|------------------------------------------------------------------------------|------------------------------|
| End Portal | `end_portal` | Block | `dragon_immune`<br/>`portals`<br/>`wither_immune`<br/>`invalid_spawn_inside` | `block.minecraft.end_portal` |

| Name         | Identifier   |
|--------------|--------------|
| Block entity | `end_portal` |

Bedrock Edition:

| Name       | Identifier   | Numeric ID | Form                         | Item ID[i 1]   | Translation key |
|------------|--------------|------------|------------------------------|----------------|-----------------|
| End Portal | `end_portal` | `119`      | Block & Ungiveable Item[i 2] | Identical[i 3] | —               |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Unavailable with /give command
3. ↑The block's direct item form has the same id as the block.

| Name         | Savegame ID |
|--------------|-------------|
| Block entity | `EndPortal` |

### Block data
An end portal block has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format

- Block entity data
	- 
	- Tags common to all block entities

Bedrock Edition:

SeeBedrock Edition level format/Block entity format.

