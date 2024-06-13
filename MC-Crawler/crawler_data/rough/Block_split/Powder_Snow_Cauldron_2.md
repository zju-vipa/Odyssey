### Changing profession
If a village has a cauldron that has not been claimed by a villager, any villager that does not already have a profession or job site block may change their profession to leatherworker.

### Extinguishing fire
A cauldron with water or powder snow extinguishes entities on fire that fall into it and the entity emits black particles. This includes mobs, players, items (if they land in the cauldron before burning up), and flaming arrows‌[JE  only]. Flaming arrows stuck into the side are also extinguished. Entities must reach the water or powder snow in it. Each entity extinguished causes the substance in the cauldron to decrease by one level. If the cauldron is filled with powder snow, it then becomes a water cauldron.

### Redstone component
An example of a cauldron used in a redstone circuit.
See also: Redstone circuit

A cauldron can act as a power source for a redstone comparator. With a cauldron behind it (either directly, or separated by an unpowered solid block), a comparator outputs a signal strength proportional to how full the cauldron is: 0 for empty, 1 for one-third full, 2 for two-thirds full, and 3 for completely full or filled with lava. However, if there is a block between the cauldron and the comparator, the comparator does not immediately update.

## Data values
### ID
Java Edition:

| Name                 | Identifier             | Form         | Block tags  | Translation key                                          |
|----------------------|------------------------|--------------|-------------|----------------------------------------------------------|
| Cauldron             | `cauldron`             | Block & Item | `cauldrons` | `block.minecraft.cauldron`<br/>`item.minecraft.cauldron` |
| Lava Cauldron        | `lava_cauldron`        | Block        | `cauldrons` | `block.minecraft.lava_cauldron`                          |
| Powder Snow Cauldron | `powder_snow_cauldron` | Block        | `cauldrons` | `block.minecraft.powder_snow_cauldron`                   |
| Water Cauldron       | `water_cauldron`       | Block        | `cauldrons` | `block.minecraft.water_cauldron`                         |

Bedrock Edition:

| Cauldron | Identifier | Alias ID        | Numeric ID | Form                         | Item ID[i 1]    | Translation key      |
|----------|------------|-----------------|------------|------------------------------|-----------------|----------------------|
| Block    | `cauldron` | `lava_cauldron` | `118`      | Block & Ungiveable Item[i 2] | `item.cauldron` | `tile.cauldron.name` |
| Item     | `cauldron` | None            | `432`      | Item                         | —               | `item.cauldron.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Unavailable with /give command

| Name         | Savegame ID |
|--------------|-------------|
| Block entity | `Cauldron`  |

### Block states
See also: Block states

Java Edition:
Water cauldron and powder snow cauldron:

| Name  | Default value | Allowed values              | Description                                       |
|-------|---------------|-----------------------------|---------------------------------------------------|
| level | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | Fullness of a cauldron, 0 is empty and 3 is full. |

Bedrock Edition:

| Name            | Metadata Bits             | Default value | Allowed values                                      | Values forMetadata Bits                             | Description                                       |
|-----------------|---------------------------|---------------|-----------------------------------------------------|-----------------------------------------------------|---------------------------------------------------|
| fill_level      | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6` | Fullness of a cauldron, 0 is empty and 6 is full. |
| cauldron_liquid | `0x8`                     | `water`       | `water`                                             | `0`                                                 | The cauldron contains water.                      |
|                 |                           |               | `lava`                                              | `1`                                                 | The cauldron contains lava.                       |
|                 |                           |               | `powder_snow`                                       | `Unsupported [sic]`                                 | The cauldron contains powder snow.                |



### Block data
In Bedrock Edition, a cauldron has a block entity associated with it that holds additional data about the block.

See Bedrock Edition level format/Block entity format.


