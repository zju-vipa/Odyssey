## Usage
### Farming
Main article: Tutorials/Crop farming
When farmed, potatoes require 8 stages to grow. However, there are four visible stages due to having only four distinct textures: every two stages have the same texture, except that growth stage 7 keeps the same appearance as stages 5–6, so that only stage 8 has the final, mature appearance. Planted potatoes require a light level of 9 or greater to continue growing. If the light level is 7 or below, the crops instantly un-plant themselves ("pop off"). It is not possible to plant potatoes if the light level is too low.

Crops grow faster if the farmland they are planted in is hydrated. Using bone meal on crops also increases the speed of growth by randomly increasing their growth stage by 2 to 5.

Crops break if pushed by a piston or if their supporting farmland breaks or turns to dirt (i.e. by being trampled), dropping their usual drops.

### Food
To eat a potato, press and hold use while it is selected in the hotbar. Eating a potato restores 1 () hunger and 0.6 saturation.

### Breeding
Pigs follow and can be bred by a player holding a potato.

Villagers can pick up potato items to become willing, which allow them to breed. Villagers require 12 potatoes to become willing.

### Smelting ingredient
| Name         | Ingredients    | Smelting recipe |
|--------------|----------------|-----------------|
| Baked Potato | Potato+Anyfuel | 0.35            |

### Trading
Novice-level farmer villagers have a 25%‌[Bedrock Edition  only] or 40%‌[Java Edition  only] chance to buy 26 potatoes for an emerald as part of their trade.

### Composting
Placing a potato into a composter has a 65% chance of raising the compost level by 1. This is less efficient than composting with baked potatoes, which has a higher success chance of 85%.

## Data values
### ID
Java Edition:

| Name     | Identifier | Form  | Block tags         | Translation key          |
|----------|------------|-------|--------------------|--------------------------|
| Potatoes | potatoes   | Block | bee_growablescrops | block.minecraft.potatoes |
| Potato   | potato     | Item  | —                  | item.minecraft.potato    |

Bedrock Edition:

| Name     | Identifier | Numeric ID | Form                         | Item ID[i 1]   | Translation key    |
|----------|------------|------------|------------------------------|----------------|--------------------|
| Potatoes | potatoes   | 142        | Block & Ungiveable Item[i 2] | Identical[i 3] | tile.potatoes.name |
| Potato   | potato     | 280        | Item                         | —              | item.potato.name   |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Unavailable with /give command

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:

| Name | Default value | Allowed values | Description  |
|------|---------------|----------------|--------------|
| age  | 0             | 01             |              |
|      |               | 23             |              |
|      |               | 456            |              |
|      |               | 7              | Fully grown. |

Bedrock Edition:

| Name   | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description  |
|--------|---------------|---------------|----------------|-------------------------|--------------|
| growth | 0x10x20x4     | 0             | 01             | 01                      |              |
|        |               |               | 23             | 23                      |              |
|        |               |               | 456            | 456                     |              |
|        |               |               | 7              | 7                       | Fully grown. |




