### Water and lava
Main article: Fluid § Mixing
Water and lava can produce stone, cobblestone, or obsidian based on how they interact. If water touches a lava source, the lava source turns to obsidian. If both touch each other while flowing, cobblestone is made and no sources are removed, and if lava flows downward onto water, the water turns to stone.

### Interactions with mobs
#### Direct contact
Water damages endermen, snow golems, striders and blazes, at a rate of 1 per half second. If water comes into contact with a shulker or an enderman, the mob teleports away.

#### Drowning
Main article: Damage § Drowning
Players and mobs (except aquatic mobs, undead mobs and iron golems) have a breath meter that lasts 15 seconds. After they run out of breath, they take 2 drowning damage every second until they die, surface, or enter bubble columns.

Dolphins are a special case when it comes to drowning: they take drowning damage when underwater for about 4 minutes, but also take suffocation damage when in air for about 2 minutes.

Each level of the Respiration enchantment adds 15 seconds to the breath meter and grants an x/(x+1) chance (where x is the Respiration level) of not taking damage after that time: 30 seconds and an average 1/second with Respiration I, 45 seconds and an average of 2⁄3 damage/second with Respiration II, and 60 seconds and an average of 1⁄2 damage/second with Respiration III.

If a husk drowns underwater, it starts to shake and eventually becomes a zombie. If a zombie drowns underwater, it starts to shake and eventually transforms into a drowned.

### Slower mining speed
Players with their head underwater require 5 times the normal amount of time to mine blocks while standing on the ground, or 25 times while not on the ground. If a player wears a helmet with the Aqua Affinity enchantment, then underwater mining speed while standing on the ground is the same as on land, and 5 times slower if not standing on the ground.

### Explosions
Water does not prevent explosions from activating. Water has a high blast resistance, causing it to absorb any normal blasts, with the exception of explosions from underwater TNT‌[Minecraft Education  only].

### Hardening concrete powder
When water comes into contact with concrete powder, the powder hardens into solid concrete.

### Sponges
When a dry sponge comes into contact with a water source or flowing block, it becomes a wet sponge, absorbing all water within 3 to 5 blocks in all directions. Kelp and lily pads within the absorbed water blocks are destroyed and drop as items, and seagrass is destroyed without dropping anything. Mobs that take damage out of water are affected as a side-effect. 

Sponges do not absorb water from waterlogged blocks, nor water that comes into contact by flowing back in from outside the area of absorption. For instance, placing a sponge 4 or more blocks from a single water source removes the flowing water in the area of effect, but as the flow from the source resumes it is not affected by the wet sponge.

A sponge instantly absorbs nearby water when it is placed next to water or when water comes into contact with it (by being placed next to the sponge, or by flowing toward it). A sponge absorbs water around itself (water source blocks or flowing water) out to a taxicab distance of 7 in all directions (including up and down), but won't absorb more than 65 blocks of water (water closest to the sponge is absorbed first). The absorption propagates only from water to water and does not "jump over" non-water blocks (including air).

### Dripping
Dripping water.
Water above a non-transparent block (except for stairs, fences, or slabs) produces dripping particles on the underside of that block. If a block of pointed dripstone hangs under any block directly beneath a water source, the drips can slowly fill up a cauldron placed underneath. Without the dripstone, a cauldron does not fill.

### Vertical transport
Bubble columns are created by placing magma blocks or soul sand under water. These can be used to transport mobs or items quickly vertically.

## Data values
### ID
Java Edition:

| Water | Identifier | Form  | Translation key         |
|-------|------------|-------|-------------------------|
| Block | `water`    | Block | `block.minecraft.water` |

| Water         | Identifier      | Fluid tags |
|---------------|-----------------|------------|
| Fluid         | `water`         | `water`    |
| Flowing Fluid | `flowing_water` | `water`    |

Bedrock Edition:

| Water      | Identifier      | Numeric ID | Form                         | Item ID[i 1]   | Translation key           |
|------------|-----------------|------------|------------------------------|----------------|---------------------------|
| Flowing    | `flowing_water` | `8`        | Block & Ungiveable Item[i 2] | Identical[i 3] | `tile.flowing_water.name` |
| Stationary | `water`         | `9`        | Block & Ungiveable Item[i 2] | Identical[i 3] | `tile.water.name`         |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑ a bUnavailable with /give command
3. ↑ a bThe block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name  | Default value | Allowed values                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| level | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | If bit 0x8 is set, this fluid is "falling" and spreads only downward. At this level, the lower bits are essentially ignored, since this block is then at its highest fluid level. This level is equal to the falling water above, equal to 8 plus the level of the non-falling water above it.The lower three bits are the fluid block's level. 0 is the highest fluid level (not necessarily filling the block - this depends on the neighboring fluid blocks above each upper corner of the block). Data values increase as the fluid level of the block drops: 1 is the next highest, 2 lower, on through 7, the lowest fluid level. Along a line on a flat plane, water drops one level per meter. |

Bedrock Edition:
Water and flowing water

| Name         | Metadata Bits                       | Default value | Allowed values                                                                                                                    | Values forMetadata Bits                                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|--------------|-------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| liquid_depth | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | If bit 0x8 is set, this fluid is "falling" and spreads only downward. At this level, the lower bits are essentially ignored, since this block is then at its highest fluid level. This level is equal to the falling water above, equal to 8 plus the level of the non-falling water above it.The lower three bits are the fluid block's level. 0 is the highest fluid level (not necessarily filling the block - this depends on the neighboring fluid blocks above each upper corner of the block). Data values increase as the fluid level of the block drops: 1 is the next highest, 2 lower, on through 7, the lowest fluid level. Along a line on a flat plane, water drops one level per meter. |



