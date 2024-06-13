# Seagrass
Seagrass is a non-solid plant block that generates in all oceans, except frozen oceans.

Tall seagrass is a two-block high variety of seagrass.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Mob loot
	- 1.4 Post-generation
- 2 Usage
	- 2.1 Breeding
	- 2.2 Bone meal
	- 2.3 Composting
	- 2.4 Growing turtles
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Screenshots
- 8 References
- 9 External links

## Obtaining
### Breaking
Seagrass can be harvested only with shears. Using any other tool, item, or the player's fist destroys seagrass and causes it to drop nothing. When harvested with shears, regular seagrass drops itself as an item, and tall seagrass drops 2 seagrass items.

Tall seagrass cannot be obtained in item form without using Creative mode.

| Block    | Seagrass            |
|----------|---------------------|
| Hardness | 0                   |
|          | Breakingtime (secs) |
| Default  | 0.05                |
| Shears   | 0.05                |

### Natural generation
Seagrass generates in either its tall or small form in rivers, non-frozen oceans, underwater caves and swamps, replacing ice[1] and planks[2] as necessary. To generate seagrass, the water column it is in must have access to the sky.


### Mob loot
Turtles drop 0–2 seagrass when killed. Looting increases the maximum number of possible seagrass drops by 1 per level.

| Source | Roll Chance | Quantity (Roll Chance) |           |            |             |
|--------|-------------|------------------------|-----------|------------|-------------|
|        |             | Default                | Looting I | Looting II | Looting III |
| Turtle | 100%        | 0–2                    | 0–3       | 0–4        | 0–5         |

### Post-generation
Using bone meal on an opaque block‌[Java Edition  only], or dirt, coarse dirt, sand, red sand, gravel, or clay‌[Bedrock Edition  only] that is underwater generates seagrass on that block and its surrounding blocks. In order for this to work, there must be 2 water blocks above the block the bone meal is being used on, and the lower one must be non-flowing water. 

## Usage
The seagrass item can be placed only on opaque blocks. It breaks when opaque blocks move into its hitbox.

Like grass, snow layers, and other such blocks, placing blocks inside seagrass deletes the seagrass. However, seagrass prevents coral fan placement.‌[Bedrock Edition  only][3]

Tall seagrass has a hitbox considerably more appropriate for its size than other two-block-tall plants such as tall grass.[4]

Seagrass is completely resistant to lava trying to flow into it, allowing for lava to be floating on top of the water.[5]

### Breeding
Seagrass can be used to lead and breed turtles.

### Bone meal
Applying bone meal to a regular seagrass transforms it to tall seagrass if there is enough space. The bone meal is wasted if insufficient space exists.[6]

### Composting
Placing seagrass into a composter has a 30% chance of raising the compost level by 1.

### Growing turtles
Using seagrass on a baby turtle accelerates its growing time. When the turtle becomes an adult, it drops one scute.

## Data values
### ID
Java Edition:

| Name          | Identifier      | Form         | Block tags             | Translation key                 |
|---------------|-----------------|--------------|------------------------|---------------------------------|
| Seagrass      | `seagrass`      | Block & Item | `underwater_bonemeals` | `block.minecraft.seagrass`      |
| Tall Seagrass | `tall_seagrass` | Block        | None                   | `block.minecraft.tall_seagrass` |

Bedrock Edition:

| Name     | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key               |
|----------|------------|------------|----------------------------|----------------|-------------------------------|
| Seagrass | `seagrass` | `385`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.seagrass.seagrass.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:
Tall

| Name | Default value | Allowed values      | Description                                    |
|------|---------------|---------------------|------------------------------------------------|
| half | `lower`       | `lower`<br/>`upper` | The half of the plant contained in this block. |

Bedrock Edition:

| Name           | Metadata Bits   | Default value | Allowed values | Values forMetadata Bits | Description                               |
|----------------|-----------------|---------------|----------------|-------------------------|-------------------------------------------|
| sea_grass_type | `0x1`<br/>`0x2` | `default`     | `default`      | `0`                     | This is seagrass.                         |
|                |                 |               | `double_bot`   | `1`                     | This is the bottom half of tall seagrass. |
|                |                 |               | `double_top`   | `2`                     | This is the top half of tall seagrass.    |


