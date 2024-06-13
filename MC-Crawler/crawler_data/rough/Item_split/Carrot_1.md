### Farming
See also: Crop farming

Carrots can be farmed and harvested on farmland. Planted carrots take 8 stages to grow, and go through 4 visually distinct stages. Planted carrots require a light level of 9 or greater to continue growing. If the light level is 7 or below, the crops instantly un-plant themselves ("pop off"). It is not possible to plant carrots if the light level is too low.

Crops grow faster if the farmland they are planted in is hydrated. Using bone meal on crops also increases the speed of growth by randomly increasing their growth stage by 2 to 5.

Crops break if pushed by a piston or if their supporting farmland breaks or turns to dirt (i.e. by being trampled), dropping their usual drops.

If /gamerule mobGriefing is true, rabbits find mature carrot crops‌[Java Edition  only] / carrot crops with growth stage greater than 1‌[Bedrock Edition  only]. This reduces the growth stages by one, removing the crop completely when the growth stage reaches 0.

### Breeding
Carrots can also be used to breed and attract pigs and rabbits.

Villagers can pick up carrot items to become willing, which allow them to breed. Villagers require 12 carrots to become willing.

### Trading
Novice-level farmer villagers have a 25% (1⁄4)‌[Bedrock Edition  only] or 40% (2⁄5)‌[Java Edition  only] chance to buy 22 carrots for an emerald.

### Crafting ingredient
| Name              | Ingredients                                                            | Crafting recipe | Description                                                                         |
|-------------------|------------------------------------------------------------------------|-----------------|-------------------------------------------------------------------------------------|
| Carrot on a Stick | Fishing Rodor<br/>DamagedFishing Rod+<br/>Carrot                       |                 | The fishing rod must be diagonally above the carrot to craft the carrot on a stick. |
| Golden Carrot     | Gold Nugget+<br/>Carrot                                                |                 |                                                                                     |
| Rabbit Stew       | Cooked Rabbit+<br/>Carrot+<br/>Baked Potato+<br/>AnyMushroom+<br/>Bowl |                 |                                                                                     |

### Composting
Placing a carrot into a composter has a 65% chance of raising the compost level by 1.

## Data values
### ID
Java Edition:

| Name    | Identifier | Form  | Block tags                  | Translation key           |
|---------|------------|-------|-----------------------------|---------------------------|
| Carrots | `carrots`  | Block | `bee_growables`<br/>`crops` | `block.minecraft.carrots` |
| Carrot  | `carrot`   | Item  | —                           | `item.minecraft.carrot`   |

Bedrock Edition:

| Name    | Identifier | Numeric ID | Form                         | Item ID[i 1]   | Translation key    |
|---------|------------|------------|------------------------------|----------------|--------------------|
| Carrots | `carrots`  | `141`      | Block & Ungiveable Item[i 2] | Identical[i 3] | —                  |
| Carrot  | `carrot`   | `279`      | Item                         | —              | `item.carrot.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Unavailable with /give command
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name | Default value | Allowed values      | Description  |
|------|---------------|---------------------|--------------|
| age  | `0`           | `0`<br/>`1`         |              |
|      |               | `2`<br/>`3`         |              |
|      |               | `4`<br/>`5`<br/>`6` |              |
|      |               | `7`                 | Fully grown. |

Bedrock Edition:

| Name   | Metadata Bits             | Default value | Allowed values      | Values forMetadata Bits | Description  |
|--------|---------------------------|---------------|---------------------|-------------------------|--------------|
| growth | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`         | `0`<br/>`1`             |              |
|        |                           |               | `2`<br/>`3`         | `2`<br/>`3`             |              |
|        |                           |               | `4`<br/>`5`<br/>`6` | `4`<br/>`5`<br/>`6`     |              |
|        |                           |               | `7`                 | `7`                     | Fully grown. |




