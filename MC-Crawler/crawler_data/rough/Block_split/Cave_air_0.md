# Air
Air is an invisible block used to define empty space where any other blocks could otherwise exist. It is one of the few blocks in the game that players cannot normally interact with.

Cave air‌[Java Edition  only] is the underground air found in carver caves and some generated structures along with features like lava lakes.

Void air‌[Java Edition  only] is used internally for air above Y=319 and below Y=-64 in the Overworld, and air above Y=255 and below Y=0 in the Nether and End dimensions, and in unloaded chunks.

## Contents
- 1 Obtaining
- 2 Usage
- 3 Data values
	- 3.1 ID
- 4 History
	- 4.1 Data history
	- 4.2 Air "item"
		- 4.2.1 Appearances
		- 4.2.2 Names
- 5 Issues
- 6 See also
- 7 References

## Obtaining
In Bedrock Edition, air cannot be obtained in the inventory without editing. In Java Edition, the block is completely unobtainable. It cannot be obtained with the /give command. Air can be destroyed or created only by the placement or removal of other blocks respectively.

Upon world generation, all otherwise empty spaces are occupied by air. In Java Edition, carver caves and underground structures generate cave air, as well as mineshafts in badlands and lava lakes.[1][2] Void air is used in place of unloaded chunks and above or below the world's buildable area.‌[Java Edition  only]


## Usage
Air, shown at left, is represented by blue cubes within structures. Cave air and void air are also shown as such.
Air shares some properties with non-solid blocks, including allowing the player or mob to move within that space without suffocating, and also to catch their breath if they are drowning in water.

Air can be visualized with the use of structure blocks in save mode. With "Show invisible blocks" enabled, air is represented as small blue cubes. All air types are displayed identically.

Cave air and void air have no special properties; they function the same as normal air.

## Data values
### ID
Java Edition:

| Block    | Identifier | Form         | Translation key            |
|----------|------------|--------------|----------------------------|
| Air      | `air`      | Block & Item | `block.minecraft.air`      |
| Cave Air | `cave_air` | Block        | `block.minecraft.cave_air` |
| Void Air | `void_air` | Block        | `block.minecraft.void_air` |

| Fluid | Identifier |
|-------|------------|
| Empty | `empty`    |

Bedrock Edition:

| Name | Identifier | Form                       | Item ID[i 1]   | Translation key |
|------|------------|----------------------------|----------------|-----------------|
| Air  | `air`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.air.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.


