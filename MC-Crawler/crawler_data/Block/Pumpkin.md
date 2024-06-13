# Pumpkin
A pumpkin is a fruit block that appears in patches in grassy biomes. Pumpkins have the same texture on all 4 sides.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Chest loot
	- 1.4 Trading
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Farming
	- 2.3 Carving
	- 2.4 Trading
	- 2.5 Composting
	- 2.6 Note blocks
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Screenshots
- 8 References

## Obtaining
### Breaking
Pumpkins can be mined using any tool, but axes are the quickest way.

| Block     | Pumpkin               |
|-----------|-----------------------|
| Hardness  | 1                     |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 1.5                   |
| Wooden    | 0.75                  |
| Stone     | 0.4                   |
| Iron      | 0.25                  |
| Diamond   | 0.2                   |
| Netherite | 0.2                   |
| Golden    | 0.15                  |
| Sword     | 1                     |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


When a pumpkin is pushed by a piston, it breaks and drops as an item. It cannot be pulled.

### Natural generation
Pumpkins naturally generate with the terrain in most biomes in the Overworld, in the form of random patches. They require only grass blocks with air above (clear of any plants such as flowers or short grass), and can generate regardless whether that grass block has a layer of snow cover. Practically speaking, this means that the occurrence of pumpkins in stony or sandy biomes, or in grassy biomes with few clear grass blocks, is comparatively rare. Each chunk has a 1⁄32 chance to generate a pumpkin patch, making naturally-generated pumpkins rarer than diamond ore. 

Pumpkins naturally generate in stem farm rooms in woodland mansions.

4 pumpkins generate naturally in woolen tents in pillager outposts.

Pumpkins generate naturally as pile (and in some farms) in taiga and snowy taiga‌[BE  only] villages.


### Chest loot
| Item    | Structure | Container    | Quantity | Chance                         |
|---------|-----------|--------------|----------|--------------------------------|
|         |           |              |          | Java EditionandBedrock Edition |
| Pumpkin | Shipwreck | Supply chest | 1–3      | 14.4%                          |

### Trading
Wandering traders can sell a pumpkin for one emerald.

## Usage
### Crafting ingredient
| Name          | Ingredients       | Crafting recipe |
|---------------|-------------------|-----------------|
| Pumpkin Pie   | Pumpkin+Sugar+Egg |                 |
| Pumpkin Seeds | Pumpkin           | 4               |

### Farming
Main article: Tutorials/Pumpkin and melon farming
Pumpkin farming strategies parallel those of melons. Planted pumpkin seeds grow a central stem that, after maturing, generates pumpkins randomly on adjacent vacant dirt-based blocks (dirt, coarse dirt, rooted dirt, grass block, farmland, podzol, mycelium, moss block, mud or muddy mangrove roots). If a pumpkin is harvested without also cutting the central stalk, another pumpkin generates afterward without requiring replanting or waiting for the stalk to mature again.

Pumpkin stems take around 10 to 30 minutes to fully develop. They require a light level of 9 or higher to grow. Bone meal can be used on pumpkin stems to become fully-grown, but this does not produce a pumpkin immediately.

### Carving
A placed pumpkin can be made into a carved pumpkin by using shears, which drops 4 pumpkin seeds on Java Edition and 1 on Bedrock Edition. The targeted side becomes the face of the carved pumpkin, unless the top or bottom face of the pumpkin are targeted, in which case the carved side is on the side facing the player.

### Trading
Apprentice-level farmer villagers buy 6 pumpkins for an emerald as part of their trades.‌[Bedrock Edition  only]

Apprentice-level farmer villagers have a 2⁄3 chance to buy 6 pumpkins for one emerald.‌[Java Edition  only]

### Composting
Placing a pumpkin or carved pumpkin into a composter has a 65% chance of raising the compost level by 1.

### Note blocks
Pumpkins can be placed under note blocks to produce didgeridoo sounds. This doesn't apply to carved pumpkins.[1]

## Data values
### ID
Java Edition:

| Name    | Identifier | Form         | Block tags                    | Translation key         |
|---------|------------|--------------|-------------------------------|-------------------------|
| Pumpkin | pumpkin    | Block & Item | enderman_holdablemineable/axe | block.minecraft.pumpkin |

Bedrock Edition:

| Name    | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key   |
|---------|------------|------------|----------------------------|----------------|-------------------|
| Pumpkin | pumpkin    | 86         | Block & Giveable Item[i 2] | Identical[i 3] | tile.pumpkin.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:
Carved pumpkin:

| Name   | Default value | Allowed values     | Description                                                                                                                   |
|--------|---------------|--------------------|-------------------------------------------------------------------------------------------------------------------------------|
| facing | north         | eastnorthsouthwest | The direction the pumpkin's carved face is facing.The opposite from the direction the player faces while placing the pumpkin. |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                                                                                                                                                                       |
|------------------------------|---------------|---------------|--------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | south         | eastnorthsouthwest | Unsupported             | The direction the pumpkin and carved pumpkin are facing.The opposite from the direction the player faces while placing the pumpkins. Though it doesn't affect the pumpkin at all. |



