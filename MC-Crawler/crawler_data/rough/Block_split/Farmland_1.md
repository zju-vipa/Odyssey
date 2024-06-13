### Decay
Farmland eventually decays into normal dirt if is dehydrated and nothing is planted in it. Additionally, a farmland block becomes a dirt block, regardless of its state of hydration, if any of the following occur:

- The player or any mob jumps/falls on the block (with a greater chance as falling speed increases).
	- The player can trample farmland even inAdventuremode.[9][10]
	- InJava Edition, mobs smaller than 0.512 cubic blocks cannot destroy farmland. This includesparrots,rabbits,chickens,bats,ocelots,cats,wolves,foxes,cave spiders,endermites,silverfish, baby mobs, smallslimes, and smallmagma cubes.
- Apistonarm is extended over a farmland block.
- A piston pushes a farmland block down.
- A solid block covers the top surface of the farmland block such as when pumpkin or melon blocks appear, or when trees grow.
- Anendermanteleports directly on top of a farmland block.

When farmland decays, any crops growing on the block are dropped as items, as if they were harvested.

A ravager does not turn farmland to dirt when stepping on it, but it does destroy all crops.

## Data values
### ID
Java Edition:

| Name     | Identifier | Form         | Block tags        | Translation key            |
|----------|------------|--------------|-------------------|----------------------------|
| Farmland | `farmland` | Block & Item | `mineable/shovel` | `block.minecraft.farmland` |

Bedrock Edition:

| Name     | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key      |
|----------|------------|------------|----------------------------|----------------|----------------------|
| Farmland | `farmland` | `60`       | Block & Giveable Item[i 2] | Identical[i 3] | `tile.farmland.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name     | Default value | Allowed values                                              | Description                                                                                                                                                                                                |
|----------|---------------|-------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| moisture | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7` | Increasing levels of wetness. The wetness value counts down to 0 while the farmland does not have access to water. The wet texture is used only on level 7. Newly hydrated farmland jumps from 0 to 7.[11] |

Bedrock Edition:

| Name               | Metadata Bits             | Default value | Allowed values                                              | Values forMetadata Bits                                     | Description                                                                                                                                                                                            |
|--------------------|---------------------------|---------------|-------------------------------------------------------------|-------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| moisturized_amount | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7` | Increasing levels of wetness. The wetness value counts down to 0 while the farmland does not have access to water. The wet texture is used only on level 7. Newly hydrated farmland jumps from 0 to 7. |




