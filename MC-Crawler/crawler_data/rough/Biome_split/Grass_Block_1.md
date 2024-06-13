## Usage
Using bone meal on grass blocks causes short grass, tall grass,‌[Java Edition  only] ferns,‌[Bedrock Edition  only] and flowers to grow.

Passive mobs tend to wander toward grass blocks. They also wander toward light.

When a sheep eats a grass block, the block becomes dirt, and a sheared sheep regrows its wool. Baby sheep graze grass much more often than adults and mature 1 minute faster when grazing.

Tilling a grass block with a hoe converts it to a farmland block. 

Dirt paths can be created by using any type of shovel on the side or top of a grass block with air above it. The shovel loses 1 durability for each dirt path block created.

### Death
Grass dies and changes to dirt a random time (when a random tick lands on the block) after it has been covered by any opaque blocks. Transparent blocks can kill grass in a similar manner if they cause the light level above the grass block to be four or below (like water does), and the surrounding area is not otherwise sufficiently illuminated.

### Spawning
In Java Edition, animals occasionally spawn on grass blocks that have light level 9 or brighter in the space directly above. This is quite rare and requires that there be few other animals nearby or in the spawn chunks. Most animals are instead created along with the terrain.

In Bedrock Edition, most animals require surface grass blocks (grass blocks with no solid block anywhere above them at the same x, z coordinate) to spawn. Animals regularly spawn in most Overworld biomes on surface grass blocks that have light level 7 or brighter in the space directly above.

### Snowy grass block
A snowy grass block with snow on top of it.
Grass blocks turn into a snowy grass block if snow, powder snow or a snow block is placed on top of the block. Removing the snow layer turns the block into a normal grass block.

### Composting
In Bedrock Edition, placing grass blocks into a composter has a 30% chance of raising the compost level by 1.

## Data values
### ID
Java Edition:

| Name        | Identifier    | Form         | Block tags                                                                                                                                                                                                    | Translation key               |
|-------------|---------------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| Grass Block | `grass_block` | Block & Item | `animals_spawnable_on`<br/>`bamboo_plantable_on`<br/>`enderman_holdable`<br/>`valid_spawn`<br/>`moss_replaceable`<br/>`lush_ground_replaceable`<br/>`mineable/shovel`<br/>`dirt`<br/>`sniffer_diggable_block` | `block.minecraft.grass_block` |

Bedrock Edition:

| Name        | Identifier    | Alias ID | Numeric ID | Form                       | Item ID[i 1]   | Translation key   |
|-------------|---------------|----------|------------|----------------------------|----------------|-------------------|
| Grass Block | `grass_block` | `grass`  | `2`        | Block & Giveable Item[i 2] | Identical[i 3] | `tile.grass.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name  | Default value | Allowed values     | Description                                                                                                      |
|-------|---------------|--------------------|------------------------------------------------------------------------------------------------------------------|
| snowy | `false`       | `false`<br/>`true` | If true, the block uses a snowy side and top texture.<br/>In-game, this is true when asnow blockorsnowis on top. |


