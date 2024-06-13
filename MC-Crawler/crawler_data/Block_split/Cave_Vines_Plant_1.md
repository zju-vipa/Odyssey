### Food
To eat glow berries, press and hold use while it is selected in the hotbar. This restores 2 () hunger and 0.4 hunger saturation points, like sweet berries.

### Light
When bearing glow berries, cave vines give off a light level of 14.

### Composting
Placing glow berries into a composter by using them on it has a 30% chance of raising the compost level by 1.

### Breeding
Glow berries can be fed to foxes to breed them.

Glow berries can be used on baby foxes to reduce the time until they grow by 10%.

## Data values
### ID
Java Edition:

| Name             | Identifier       | Form  | Block tags                                                  | Item tags | Translation key                  |
|------------------|------------------|-------|-------------------------------------------------------------|-----------|----------------------------------|
| Cave Vines       | cave_vines       | Block | mineable/axebee_growablescave_vinesclimbablesword_efficient | —         | block.minecraft.cave_vines       |
| Cave Vines Plant | cave_vines_plant | Block | mineable/axebee_growablescave_vinesclimbablesword_efficient | —         | block.minecraft.cave_vines_plant |
| Glow Berries     | glow_berries     | Item  | —                                                           | fox_food  | item.minecraft.glow_berries      |

Bedrock Edition:

| Name                         | Identifier                   | Numeric ID | Form                         | Item ID[i 1]   | Translation key                        |
|------------------------------|------------------------------|------------|------------------------------|----------------|----------------------------------------|
| Cave Vines                   | cave_vines                   | 577        | Block & Ungiveable Item[i 2] | Identical[i 3] | tile.cave_vines.name                   |
| Cave Vines Body With Berries | cave_vines_body_with_berries | 630        | Block & Ungiveable Item[i 2] | Identical[i 3] | tile.cave_vines_body_with_berries.name |
| Cave Vines Head With Berries | cave_vines_head_with_berries | 631        | Block & Ungiveable Item[i 2] | Identical[i 3] | tile.cave_vines_head_with_berries.name |
| Glow Berries                 | glow_berries                 | 638        | Item                         | —              | item.glow_berries.name                 |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ a b c Unavailable with /give command

↑ a b c The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:
Cave Vines:

| Name    | Default value | Allowed values                             | Description                         |
|---------|---------------|--------------------------------------------|-------------------------------------|
| berries | false         | falsetrue                                  | Whether this cave vine has berries. |
| age     | 0             | 012345678910111213141516171819202122232425 | How old this cave vine is.          |

Cave Vines Plant:

| Name    | Default value | Allowed values | Description                         |
|---------|---------------|----------------|-------------------------------------|
| berries | false         | falsetrue      | Whether this cave vine has berries. |

Bedrock Edition:
Cave Vines, Cave Vines Body With Berries, Cave Vines Head With Berries:

| Name              | Metadata Bits | Default value | Allowed values                             | Values forMetadata Bits | Description                |
|-------------------|---------------|---------------|--------------------------------------------|-------------------------|----------------------------|
| growing_plant_age | Not Supported | 0             | 012345678910111213141516171819202122232425 | Unsupported             | How old this cave vine is. |




