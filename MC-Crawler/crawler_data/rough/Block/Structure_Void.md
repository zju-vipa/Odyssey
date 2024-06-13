# Structure Void
A structure void is an invisible block that allows existing blocks to remain unchanged rather than be overridden when using the structure block to load a structure.

A structure air is an unused variant of structure void in Bedrock Edition, which has the same behaviors with regular structure void.

## Contents
- 1 Obtaining
- 2 Usage
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Trivia

## Obtaining
Structure voids are available only using the /setblock, /fill, or /give commands.

In Java Edition, they are also available in the creative inventory if cheats and the operator items tab option in controls are enabled.

## Usage
The difference between air (top left) and structure void (top right) when "show invisible blocks" is enabled.
Structure voids can be placed as part of a structure and are ignored when the structure file is saved and loaded. This results in the blocks at the location where the structure is placed being maintained and not being overridden. For example, if a player saves a 2 block high structure with air at the top and a structure void at the bottom, and loads it into a 2 block high area of stone, the top block becomes air but the bottom stays stone.

In Java Edition, structure void blocks have no collision box but have a small hitbox. Additionally, they are invisible, but are displayed as pink cubes when "Show invisible blocks" is turned on in Save mode inside a Structure Block. Blocks can also replace structure voids similarly to snow and grass. A piston can move a structure void, but the structure void pushed by the piston turns into air.

In Bedrock Edition, structure void blocks' hitboxes are the same as a full block, and, similar to barriers, appear when held by the player. Unlike Java Edition, they can support blocks such as signs, torches, rails and redstone wire. A piston cannot move a structure void.

In Bedrock Edition, structure air blocks have the same behaviors with structure void blocks, but with another texture.

As there is no collision box, entities can pass through, although liquids cannot.

- Hitbox of structure void in Java Edition
- With "Show invisible blocks" on


## Data values
### ID
Java Edition:

| Name           | Identifier       | Form         | Translation key                  |
|----------------|------------------|--------------|----------------------------------|
| Structure Void | `structure_void` | Block & Item | `block.minecraft.structure_void` |

Bedrock Edition:

| Name           | Identifier       | Numeric ID | Form                       | Item ID[i 1]   | Translation key            |
|----------------|------------------|------------|----------------------------|----------------|----------------------------|
| Structure Void | `structure_void` | `217`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.structure_void.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Bedrock Edition:

| Name                | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description    |
|---------------------|---------------|---------------|----------------|-------------------------|----------------|
| structure_void_type | `0x1`         | `void`        | `air`          | `1`                     | Structure Air  |
|                     |               |               | `void`         | `0`                     | Structure Void |

