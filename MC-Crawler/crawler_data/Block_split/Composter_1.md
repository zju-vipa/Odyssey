### Changing profession
If a village has a composter that has not been claimed by a villager, any resident villager who has not already chosen a job site block has a chance to change their profession to farmer.

### Redstone component
See also: Redstone circuit

A composter can act as a power source for a redstone comparator. With a composter behind it (either directly, or separated by an unpowered solid block), a comparator outputs a signal strength between 0 and 8, proportional to how full the composter is: 0 for empty, 1 for 1⁄7 full, 2 for 2⁄7 full, and so on to 6. 7 is for completely full but the bone meal is not ready to collect, and 8 for completely full and the bone meal is ready to collect. However, if there is a block between the composter and comparator, the comparator does not immediately update.

### Hoppers
Composters can interact with hoppers. A hopper directly below a composter pulls bone meal from it. A hopper or dropper facing downward directly above a composter pushes items into it. See Hopper § Redstone component for more details.

Hoppers cannot interact with the sides of a composter.

Composters are also often placed on top of hoppers when they don't need to suck items in from the world. This is because hoppers with containers on top of them don't look for item entities around them and the composter is the container with the least amount of information stored so this helps reducing lag.

### Fuel
A composter can be used as fuel in a furnace to smelt 1.5 items.

### Note blocks
Composters can be placed under note blocks to produce "bass" sounds.

## Data values
### ID
Java Edition:

| Name      | Identifier | Form         | Translation key           |
|-----------|------------|--------------|---------------------------|
| Composter | composter  | Block & Item | block.minecraft.composter |

Bedrock Edition:

| Name      | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key     |
|-----------|------------|------------|----------------------------|----------------|---------------------|
| Composter | composter  | 468        | Block & Giveable Item[i 2] | Identical[i 3] | tile.composter.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
Composter with different compost levels
- 
- 
- 
- 
- 
- 
- 
- 
- 

Java Edition:

| Name  | Default value | Allowed values | Description                                                            |
|-------|---------------|----------------|------------------------------------------------------------------------|
| level | 0             | 012345678      | When at level 8, bone meal is able to be collected from the composter. |

Bedrock Edition:

| Name                 | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                                            |
|----------------------|---------------|---------------|----------------|-------------------------|------------------------------------------------------------------------|
| composter_fill_level | 0x10x20x40x8  | 0             | 012345678      | 012345678               | When at level 8, bone meal is able to be collected from the composter. |




