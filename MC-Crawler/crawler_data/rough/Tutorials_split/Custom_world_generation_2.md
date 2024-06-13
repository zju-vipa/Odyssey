### Notes
#### Basin
Basins (aka. erosions) existed in all biomes before the surface rules were added. When the surface depth is less than or equal to 0, the topmost layer of the terrain is directly removed, leaving a bare stone basin. However, after the surface rules were added, they are somehow limited to only two biomes, frozen ocean and deep frozen ocean, and there is a bug when judging the water surface. In previous basins, blocks above sea level (blocks with Y>=63) were air, otherwise they were ice or water (Note that there were no aquifers or noise caves at that time). In the current vanilla surface rules, it is air when there is no water above it, which can lead to flowing water along the coast.

#### Carver
Due to a mistake in the code about carver, the behavior of the minecraft:water condition during carver generation is inconsistent with that during terrain generation. When generating terrain, the offset value is relative to the air-liquid contact surface (i.e. the block position of the air block). While during carver generation, the offset value is relative to the block position of the top liquid block. And because during carver generation, surface rules are only applied to dirt below when carving grass blocks or mycelium. The game assumes that there is no water above grass blocks and mycelium. Then during carving, grass blocks and mycelium may be carved into water, so there is at most one block of water above the dirt being processed by surface rules. Therefore, the offset value during carver generation can also be said to be relative to the top surface of the processing dirt.

Therefore, when generating terrain, offset values of 0 and -1 have the same effect: only succeed when there is no liquid above. But When carvers generates, if the offset value is -1, the condition is always successful, regardless of whether there is liquid above.

When surface rules were first added into the game (21w41a), the developers were not aware of the mistake in carver code and set the offset value to -1 when checking whether there is water above. As a result, grass blocks can be generated underwater during carver generation. Afterwards (21w43a and 22w07a), in order to resolve this bug, additional redundant minecraft:water conditions with offset values of 0 was added to the blocks that should not be generated underwater. Therefore, the current overworld surface rules in the vanilla game are slightly chaotic, but they can basically work as expected.

For pack and mod creators, it is important to avoid setting offset value to -1 in minecraft:water to ensure that it behaves the same during carver generation and terrain generation.

## Biome source parameter list presets
Through running the data generator, biome source parameter list presets of the overworld and the nether can be obtained. They are located in generated/reports/biome_parameters/. The biome generation defined therein is explained in detail on the Biome page.


