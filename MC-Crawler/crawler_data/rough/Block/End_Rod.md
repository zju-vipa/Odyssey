# End Rod
An end rod is a decorative light source that emits white particles.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Helmet
	- 2.2 Light
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Renders
	- 7.2 Screenshots
- 8 See also

## Obtaining
### Breaking
End rods can be mined by any tool or by hand, and drop themselves when broken. They also drop as an item when water flows over them or when lava flows over them in Java Edition.

### Natural generation
End rods generate naturally all over end cities. They may spawn upright on the outside of towers, and they may spawn sideways inside of towers.

### Crafting
| Ingredients                        | Crafting recipe |
|------------------------------------|-----------------|
| Blaze Rod+<br/>Popped Chorus Fruit | 4               |

## Usage
End rods in various positions on purpur blocks.
End rods are primarily used as light sources and decoration. They can be placed on any surface of any block, including other end rods. They do not break if their supporting block is broken. Gravity-affected blocks like sand or gravel do not break if they fall onto an end rod oriented vertically, but they do break on a rod oriented horizontally. End rods can be pushed and pulled by pistons, no matter the orientation.

Inside some end city towers, they are positioned so the player may use them to climb the tower, similar to a spiral staircase.


### Helmet
 
While an end rod cannot be equipped in the head slot in Survival mode, equipping it using commands causes it to appear like a unicorn horn. This can be done with the /item replace command.

### Light
End rods emit a light level of 14 (equal to torches), melting snow layers and ice within a 2-block radius.

## Data values
### ID
Java Edition:

| Name    | Identifier | Form         | Translation key           |
|---------|------------|--------------|---------------------------|
| End Rod | `end_rod`  | Block & Item | `block.minecraft.end_rod` |

Bedrock Edition:

| Name    | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key     |
|---------|------------|------------|----------------------------|----------------|---------------------|
| End Rod | `end_rod`  | `208`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.end_rod.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name   | Default value | Allowed values                                                | Description                                                                                                                                                                                                         |
|--------|---------------|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing | `up`          | `down`<br/>`east`<br/>`north`<br/>`south`<br/>`up`<br/>`west` | The direction to the end rod, from the block it is attached to; also the direction the white end points.<br/>Opposite from the direction the player faces when placing an end rod, and opposite from the wider end. |

Bedrock Edition:

| Name             | Metadata Bits             | Default value | Allowed values                              | Values forMetadata Bits                     | Description                                                                                                                                                                                                                |
|------------------|---------------------------|---------------|---------------------------------------------|---------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | The direction to the end rod, from the block it is attached to; also the direction the white end points.0: Facing down<br/>1: Facing up<br/>2: Facing north<br/>3: Facing south<br/>4: Facing west<br/>5: Facing east<br/> |



