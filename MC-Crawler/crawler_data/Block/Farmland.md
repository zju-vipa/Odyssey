# Farmland
Farmland is a block created by using a hoe on most types of dirt, and cannot be obtained in the inventory in Survival mode. It is required to grow all types of seeds, as well as carrots and potatoes.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Post-generation
- 2 Usage
	- 2.1 Hydration
	- 2.2 Decay
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 Achievements
- 6 Advancements
- 7 History
- 8 Issues
- 9 Trivia
- 10 See also
- 11 References
- 12 External links

## Obtaining
### Breaking
When mined (even with a Silk Touch tool), farmland drops dirt. It can be obtained as an item only by using commands, via the Creative inventory or the pick block control in Creative mode.

| Block     | Farmland              |
|-----------|-----------------------|
| Hardness  | 0.6                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 0.9                   |
| Wooden    | 0.45                  |
| Stone     | 0.25                  |
| Iron      | 0.15                  |
| Diamond   | 0.15                  |
| Netherite | 0.1                   |
| Golden    | 0.1                   |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Natural generation
Farmland occurs naturally in villages where wheat, potatoes, carrots, beetroots, pumpkin stems, and melon stems are grown. Patches of farmland are surrounded by logs or sandstone, spruce trapdoor, and cobblestone. Farmland also naturally occurs in certain woodland mansion rooms.

### Post-generation
A player can create a block of farmland by using a hoe on a dirt block, grass block, or dirt path. Using a hoe on coarse dirt or rooted dirt turns them into regular dirt, which can then be tilled into farmland by using the hoe once more. Mycelium and podzol cannot be turned into farmland.[1]

## Usage
Farmland is required to grow most of the game's types of crops: wheat seeds, carrots, potatoes, beetroot seeds, melon seeds, pumpkin seeds, torchflower seeds, and pitcher pods.

Plants such as saplings[2], ferns, grass, and flowers,[3] and sweet berries may be planted on farmland. Mushrooms[4], sugar cane[5], bamboo[6], dead bushes[7], twisting vines[8] and cacti cannot be planted on farmland.

Wall-mounted blocks such as ladders and torches cannot be attached to the side of a farmland block. Farmland is a partial block (15/16th of a block in height) and so mobs cannot spawn on it.

### Hydration
Conditions in which farmland either is or isn't hydrated.
A farmland block is created dry, and eventually reverts back to dirt if not hydrated and nothing is planted on it.

For farmland to become hydrated, water must be present:

- up to four blocks away horizontally (including diagonally) from the farmland block.
- at the same level or one block above the farmland block level.

The blocks between the farmland block and the water make no difference. Whether the water is flowing or still also makes no difference.

The rate at which farmland becomes hydrated cannot be changed. Each farmland block within a 9×9 grid of farmland with a single water block in the middle has exactly the same chance of becoming hydrated as a single farmland block in an ocean.

Farmland can also be hydrated by rain.

Different types of seeds grow faster on hydrated farmland than on dry farmland. Hydrated farmland yields a fully developed wheat crop in a little over a single day/night cycle.

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

| Name     | Identifier | Form         | Block tags      | Translation key          |
|----------|------------|--------------|-----------------|--------------------------|
| Farmland | farmland   | Block & Item | mineable/shovel | block.minecraft.farmland |

Bedrock Edition:

| Name     | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key    |
|----------|------------|------------|----------------------------|----------------|--------------------|
| Farmland | farmland   | 60         | Block & Giveable Item[i 2] | Identical[i 3] | tile.farmland.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:

| Name     | Default value | Allowed values | Description                                                                                                                                                                                                |
|----------|---------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| moisture | 0             | 01234567       | Increasing levels of wetness. The wetness value counts down to 0 while the farmland does not have access to water. The wet texture is used only on level 7. Newly hydrated farmland jumps from 0 to 7.[11] |

Bedrock Edition:

| Name               | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                                                                                                                                                                            |
|--------------------|---------------|---------------|----------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| moisturized_amount | 0x10x20x4     | 0             | 01234567       | 01234567                | Increasing levels of wetness. The wetness value counts down to 0 while the farmland does not have access to water. The wet texture is used only on level 7. Newly hydrated farmland jumps from 0 to 7. |



## See also
- Farming

