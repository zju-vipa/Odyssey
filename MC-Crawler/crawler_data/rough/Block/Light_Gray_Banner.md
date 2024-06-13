# Banner
Banners are tall decorative blocks, featuring a field that is highly customizable using dyes and banner patterns.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
	- 1.4 Trading
- 2 Usage
	- 2.1 Helmet
	- 2.2 Chestplate
	- 2.3 Crafting ingredient
	- 2.4 Copying
	- 2.5 Map marker
	- 2.6 Patterns
		- 2.6.1 Loom recipes
		- 2.6.2 Crafting recipes
	- 2.7 Renaming
	- 2.8 Fuel
	- 2.9 Note Blocks
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Metadata
		- 4.2.1 Item
	- 4.3 Item
	- 4.4 Block states
	- 4.5 Block data
		- 4.5.1 Pattern color
		- 4.5.2 Pattern
	- 4.6 Item data
- 5 Achievements
- 6 History
- 7 Issues
- 8 Trivia
- 9 Gallery
	- 9.1 Renders
		- 9.1.1 Banner
		- 9.1.2 Wall banner
	- 9.2 Screenshots
	- 9.3 Development images
	- 9.4 In other media
- 10 References

## Obtaining
### Breaking
Banners can be broken with or without a tool, but an axe is fastest.

| Block     | Banners               |
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

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

A banner also breaks and drops itself as an item if the block the banner is attached to is moved, removed, or destroyed.

### Natural generation
| Name              | Location                                                                         | Appearance | Design                                                      |
|-------------------|----------------------------------------------------------------------------------|------------|-------------------------------------------------------------|
| Magenta Banner    | Outside ofend cities.                                                            |            | Magenta BannerBlack Inverted Chevron<br/>Black Chevron<br/> |
| Gray Banner       | In banner room inwoodland mansions.                                              |            | Gray Banner                                                 |
| Light Gray Banner | In master bedroom inwoodland mansions.                                           |            | Light Gray BannerWhite Flower Charge<br/>                   |
| Brown Banner      | Outside of some houses, meeting points, and pillar fountains in savannavillages. |            | Brown Banner                                                |
| Black Banner      | In altar room inwoodland mansions.                                               |            | Black Banner                                                |

### Crafting
Banners can be crafted from six wool and a stick in a pattern resembling a sign.

| Name         | Ingredients             | Crafting recipe | Description                                                                                                                                                                           |
|--------------|-------------------------|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Banner       | MatchingWool+<br/>Stick |                 | Once the banner is crafted, its base color cannot be changed.‌[Java Edition  only]                                                                                                    |
| White Banner | AnyBanner+<br/>Bleach   |                 | Bleach can be used to remove the color of a banner, resulting in a white banner. This includes removing patterns from a white banner.‌[Bedrock Edition and Minecraft Education  only] |

### Trading
Expert-level cartographer villagers always offer to sell 1 or 2 blank banners of a random color for 3 emeralds. Expert-level shepherd villagers have a 2⁄7 chance of offering the same trade.‌[Java Edition  only]

In Bedrock Edition, expert-level cartographer and shepherd villagers both offer to sell one of 16 blank banners for 3 emeralds as part of their trades.

## Usage
Overlapping block on a banner.
Overlapping on a wall mounted banner.
There are 16 colored blank banners, and numerous patterns each available in each of the 16 colors. A banner can feature up to 6 different patterns. The top layer of a banner (or the last pattern added) can be washed off by using it on a cauldron containing water.

Banners, much like signs, can be placed both on the ground facing in any direction, or on a wall. They gently sway as if affected by a breeze, regardless of dimension or location. 

Banners have no collision mask as they are completely non-solid, so entities can move through them.

Other blocks (including other banners) can be placed on any edge of a banner's hitbox, which is only one block high despite the banner appearing as two blocks tall. This makes it possible to overlap another solid block on the top half of a banner for floor banners, or the bottom half of wall banners.

When a banner is placed on the side of a block, its position is set by the top block, and it is possible to place it so it appears half buried.

Banners can also be placed in item frames, where they simply appear as their item model.

Water and lava flow around banners. In Bedrock Edition, banners can be waterlogged.

- Water can be placed below wall banners
- Water flows around a banner on the ground

Lava can create fire in air blocks next to banners as if the banners were flammable, but the banners do not burn (and cannot be burned by other methods). Banners also cannot be moved by pistons.

If a banner is renamed on an anvil, it retains its name when a pattern is added, but not when a pattern is removed.

### Helmet

  

This feature is exclusive to  Java Edition. 


While a banner cannot be equipped in the head slot in Survival mode, equipping it using commands causes it to appear on top of the player. This is how raid captains wear banners‌[JE  only].

### Chestplate

  

This feature is exclusive to  Bedrock Edition. 


While a banner cannot be equipped in the chestplate slot in Survival mode, equipping it using NBT editors causes it to appear on top of the player. This is how raid captains wear banners‌[BE & edu  only].

- 
- 

### Crafting ingredient
Shields can have patterns applied to them using banners. The shield pattern has a smaller resolution than the banner pattern, causing them to look different or offset. Banners that have more than six patterns, such as those obtained through inventory editors, are reduced to six patterns on the shield.

| Ingredients                | Crafting recipe | Description                                                                                                                                                                                |
|----------------------------|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Shield+<br/>MatchingBanner |                 | Applies the banner pattern to the shield. The banner is consumed.<br/>The shield must have no preexisting patterns.<br/>Does not change existing durability or enchantments on the shield. |

### Copying
Banners can be copied with a blank banner to make multiple identical banners. Banners with more than 6 patterns applied using commands cannot be copied in this manner.

| Ingredients    | Crafting recipe | Description                                                                                                                               |
|----------------|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| MatchingBanner |                 | Copies pattern; both banners must have the same base color, and the one having a pattern copied onto it must have no preexisting pattern. |

### Map marker
How every banner appears In Java Edition on a map, including named banners.

  

This feature is exclusive to  Java Edition. 


In Java Edition, using on a standing banner with a map selected places a marker of the banner's position on the selected map, and using on the banner again removes the marker. Note that wall banners cannot serve as map markers. The marker has the same color as the banner's base without decorations. The marker is removed if the banner is destroyed unless the map is locked using a cartography table. If the banner is renamed, the name appears below the marker.

### Patterns
See also: List of patterned banners

Example of a banner with more than 6 patterns, a result of using the /give command.
A banner may have up to six layers of patterns, which are overlaid with the last-crafted on top. A banner can have up to 16 layers of patterns with the use of commands. The total number of unique banners with at most 16 banner patterns is approximately 1.27 × 1046 (12.7 quattuordecillion), or exactly 12,696,344,039,844,551,126,101,565,750,244,757,433,489,827,856.

Any color banner can be used; the pattern overlays the color. In Java Edition, a loom is used to make patterns. However, in Bedrock Edition, the patterns can be made in a loom or a crafting table.

A banner can have more than six layers of patterns through the commands /give, /setblock or /fill. This only works in Java Edition, as Bedrock Edition doesn't have any NBT commands. Here is an example of a mining banner with seven different patterns. There is specific codes for the colors and patterns that you have to input. 

/give @p white_banner{display:{Name:"\"Mining Industries Banner\""},BlockEntityTag:{Patterns:[{Pattern:"cr",Color:15},{Pattern:"bs",Color:15},{Pattern:"sc",Color:12},{Pattern:"ms",Color:0},{Pattern:"hh",Color:15},{Pattern:"bo",Color:15},{Pattern:"tts",Color:8}]}} 1


Loom recipes
Main page: Template:Banner pattern loom recipes[edit]


Crafting recipes
Main article: Banner/Banner pattern crafting recipes[edit]

### Renaming
In Java Edition, a banner can be given a custom name that remains as the banner is placed and retrieved. The player can use an anvil to rename the banner item, or may change the CustomName tag using the /data command on the banner block.

### Fuel
Banners can be used as a fuel in furnaces, smelting 1.5 items per banner.

### Note Blocks
Banners can be placed under note blocks to produce "bass" sounds.

## Data values
### ID
Java Edition:

| Name                   | Identifier               | Form         | Block tags                         | Item tags | Translation key                     |
|------------------------|--------------------------|--------------|------------------------------------|-----------|-------------------------------------|
| White Banner           | `white_banner`           | Block & Item | `banners`<br/>`wall_post_override` | `banners` | `block.minecraft.white_banner`      |
| Orange Banner          | `orange_banner`          | Block & Item | `banners`<br/>`wall_post_override` | `banners` | `block.minecraft.orange_banner`     |
| Magenta Banner         | `magenta_banner`         | Block & Item | `banners`<br/>`wall_post_override` | `banners` | `block.minecraft.magenta_banner`    |
| Light Blue Banner      | `light_blue_banner`      | Block & Item | `banners`<br/>`wall_post_override` | `banners` | `block.minecraft.light_blue_banner` |
| Yellow Banner          | `yellow_banner`          | Block & Item | `banners`<br/>`wall_post_override` | `banners` | `block.minecraft.yellow_banner`     |
| Lime Banner            | `lime_banner`            | Block & Item | `banners`<br/>`wall_post_override` | `banners` | `block.minecraft.lime_banner`       |
| Pink Banner            | `pink_banner`            | Block & Item | `banners`<br/>`wall_post_override` | `banners` | `block.minecraft.pink_banner`       |
| Gray Banner            | `gray_banner`            | Block & Item | `banners`<br/>`wall_post_override` | `banners` | `block.minecraft.gray_banner`       |
| Light Gray Banner      | `light_gray_banner`      | Block & Item | `banners`<br/>`wall_post_override` | `banners` | `block.minecraft.light_gray_banner` |
| Cyan Banner            | `cyan_banner`            | Block & Item | `banners`<br/>`wall_post_override` | `banners` | `block.minecraft.cyan_banner`       |
| Purple Banner          | `purple_banner`          | Block & Item | `banners`<br/>`wall_post_override` | `banners` | `block.minecraft.purple_banner`     |
| Blue Banner            | `blue_banner`            | Block & Item | `banners`<br/>`wall_post_override` | `banners` | `block.minecraft.blue_banner`       |
| Brown Banner           | `brown_banner`           | Block & Item | `banners`<br/>`wall_post_override` | `banners` | `block.minecraft.brown_banner`      |
| Green Banner           | `green_banner`           | Block & Item | `banners`<br/>`wall_post_override` | `banners` | `block.minecraft.green_banner`      |
| Red Banner             | `red_banner`             | Block & Item | `banners`<br/>`wall_post_override` | `banners` | `block.minecraft.red_banner`        |
| Black Banner           | `black_banner`           | Block & Item | `banners`<br/>`wall_post_override` | `banners` | `block.minecraft.black_banner`      |
| White Wall Banner      | `white_wall_banner`      | Block        | `banners`<br/>`wall_post_override` | —         | `block.minecraft.white_banner`      |
| Orange Wall Banner     | `orange_wall_banner`     | Block        | `banners`<br/>`wall_post_override` | —         | `block.minecraft.orange_banner`     |
| Magenta Wall Banner    | `magenta_wall_banner`    | Block        | `banners`<br/>`wall_post_override` | —         | `block.minecraft.magenta_banner`    |
| Light Blue Wall Banner | `light_blue_wall_banner` | Block        | `banners`<br/>`wall_post_override` | —         | `block.minecraft.light_blue_banner` |
| Yellow Wall Banner     | `yellow_wall_banner`     | Block        | `banners`<br/>`wall_post_override` | —         | `block.minecraft.yellow_banner`     |
| Lime Wall Banner       | `lime_wall_banner`       | Block        | `banners`<br/>`wall_post_override` | —         | `block.minecraft.lime_banner`       |
| Pink Wall Banner       | `pink_wall_banner`       | Block        | `banners`<br/>`wall_post_override` | —         | `block.minecraft.pink_banner`       |
| Gray Wall Banner       | `gray_wall_banner`       | Block        | `banners`<br/>`wall_post_override` | —         | `block.minecraft.gray_banner`       |
| Light Gray Wall Banner | `light_gray_wall_banner` | Block        | `banners`<br/>`wall_post_override` | —         | `block.minecraft.light_gray_banner` |
| Cyan Wall Banner       | `cyan_wall_banner`       | Block        | `banners`<br/>`wall_post_override` | —         | `block.minecraft.cyan_banner`       |
| Purple Wall Banner     | `purple_wall_banner`     | Block        | `banners`<br/>`wall_post_override` | —         | `block.minecraft.purple_banner`     |
| Blue Wall Banner       | `blue_wall_banner`       | Block        | `banners`<br/>`wall_post_override` | —         | `block.minecraft.blue_banner`       |
| Brown Wall Banner      | `brown_wall_banner`      | Block        | `banners`<br/>`wall_post_override` | —         | `block.minecraft.brown_banner`      |
| Green Wall Banner      | `green_wall_banner`      | Block        | `banners`<br/>`wall_post_override` | —         | `block.minecraft.green_banner`      |
| Red Wall Banner        | `red_wall_banner`        | Block        | `banners`<br/>`wall_post_override` | —         | `block.minecraft.red_banner`        |
| Black Wall Banner      | `black_wall_banner`      | Block        | `banners`<br/>`wall_post_override` | —         | `block.minecraft.black_banner`      |

| Name         | Identifier |
|--------------|------------|
| Block entity | `banner`   |

Bedrock Edition:

| Banner   | Identifier        | Numeric ID | Form                         | Item ID[i 1]   | Translation key                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|----------|-------------------|------------|------------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Standing | `standing_banner` | `176`      | Block & Ungiveable Item[i 2] | Identical[i 3] | `tile.standing_banner.black.name`<br/>`tile.standing_banner.red.name`<br/>`tile.standing_banner.green.name`<br/>`tile.standing_banner.brown.name`<br/>`tile.standing_banner.blue.name`<br/>`tile.standing_banner.purple.name`<br/>`tile.standing_banner.cyan.name`<br/>`tile.standing_banner.silver.name`<br/>`tile.standing_banner.gray.name`<br/>`tile.standing_banner.pink.name`<br/>`tile.standing_banner.lime.name`<br/>`tile.standing_banner.yellow.name`<br/>`tile.standing_banner.lightBlue.name`<br/>`tile.standing_banner.magenta.name`<br/>`tile.standing_banner.orange.name`<br/>`tile.standing_banner.white.name` |
| Wall     | `wall_banner`     | `177`      | Block & Ungiveable Item[i 2] | Identical[i 3] | —                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Item     | `banner`          | `567`      | Item                         | —              | `item.banner.black.name`<br/>`item.banner.red.name`<br/>`item.banner.green.name`<br/>`item.banner.brown.name`<br/>`item.banner.blue.name`<br/>`item.banner.purple.name`<br/>`item.banner.cyan.name`<br/>`item.banner.silver.name`<br/>`item.banner.gray.name`<br/>`item.banner.pink.name`<br/>`item.banner.lime.name`<br/>`item.banner.yellow.name`<br/>`item.banner.lightBlue.name`<br/>`item.banner.magenta.name`<br/>`item.banner.orange.name`<br/>`item.banner.white.name`                                                                                                                                                 |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑ a bUnavailable with /give command
3. ↑ a bThe block's direct item form has the same id as the block.

| Name         | Savegame ID |
|--------------|-------------|
| Block entity | `Banner`    |

### Metadata
#### Item
In Bedrock Edition, banner items use the following data values:

| DV | Banner color |
|----|--------------|
| 0  | black        |
| 1  | red          |
| 2  | green        |
| 3  | brown        |
| 4  | blue         |
| 5  | purple       |
| 6  | cyan         |
| 7  | light gray   |
| 8  | gray         |
| 9  | pink         |
| 10 | lime         |
| 11 | yellow       |
| 12 | light blue   |
| 13 | magenta      |
| 14 | orange       |
| 15 | white        |

### Item
In Java Edition, banner items use the following data values:

| DV | Banner color |
|----|--------------|
| 15 | black        |
| 14 | red          |
| 13 | green        |
| 12 | brown        |
| 11 | blue         |
| 10 | purple       |
| 9  | cyan         |
| 8  | light gray   |
| 7  | gray         |
| 6  | pink         |
| 5  | lime         |
| 4  | yellow       |
| 3  | light blue   |
| 2  | magenta      |
| 1  | orange       |
| 0  | white        |

### Block states
See also: Block states

Java Edition:
Floor

| Name     | Default value | Allowed values | Description                          |
|----------|---------------|----------------|--------------------------------------|
| rotation | `0`           | `0`            | The block is facing south.           |
|          |               | `1`            | The block is facing south-southwest. |
|          |               | `2`            | The block is facing southwest.       |
|          |               | `3`            | The block is facing west-southwest.  |
|          |               | `4`            | The block is facing west.            |
|          |               | `5`            | The block is facing west-northwest.  |
|          |               | `6`            | The block is facing northwest.       |
|          |               | `7`            | The block is facing north-northwest. |
|          |               | `8`            | The block is facing north.           |
|          |               | `9`            | The block is facing north-northeast. |
|          |               | `10`           | The block is facing northeast.       |
|          |               | `11`           | The block is facing east-northeast.  |
|          |               | `12`           | The block is facing east.            |
|          |               | `13`           | The block is facing east-southeast.  |
|          |               | `14`           | The block is facing southeast.       |
|          |               | `15`           | The block is facing south-southeast. |

Wall

| Name   | Default value | Allowed values                            | Description                                                                                                                                                                    |
|--------|---------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the block is facing. For example, a block facing east is attached to a block to its west.<br/>Opposite from the direction a player faces when placing the block. |

Bedrock Edition:

** Standing **
| Name                  | Metadata Bits                       | Default value | Allowed values | Values forMetadata Bits | Description                          |
|-----------------------|-------------------------------------|---------------|----------------|-------------------------|--------------------------------------|
| ground_sign_direction | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`            | `0`                     | The block is facing south.           |
|                       |                                     |               | `1`            | `1`                     | The block is facing south-southwest. |
|                       |                                     |               | `2`            | `2`                     | The block is facing southwest.       |
|                       |                                     |               | `3`            | `3`                     | The block is facing west-southwest.  |
|                       |                                     |               | `4`            | `4`                     | The block is facing west.            |
|                       |                                     |               | `5`            | `5`                     | The block is facing west-northwest.  |
|                       |                                     |               | `6`            | `6`                     | The block is facing northwest.       |
|                       |                                     |               | `7`            | `7`                     | The block is facing north-northwest. |
|                       |                                     |               | `8`            | `8`                     | The block is facing north.           |
|                       |                                     |               | `9`            | `9`                     | The block is facing north-northeast. |
|                       |                                     |               | `10`           | `10`                    | The block is facing northeast.       |
|                       |                                     |               | `11`           | `11`                    | The block is facing east-northeast.  |
|                       |                                     |               | `12`           | `12`                    | The block is facing east.            |
|                       |                                     |               | `13`           | `13`                    | The block is facing east-southeast.  |
|                       |                                     |               | `14`           | `14`                    | The block is facing southeast.       |
|                       |                                     |               | `15`           | `15`                    | The block is facing south-southeast. |

** Wall **
| Name             | Metadata Bits             | Default value | Allowed values              | Values forMetadata Bits     | Description                                                                                                                                               |
|------------------|---------------------------|---------------|-----------------------------|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `2`<br/>`3`<br/>`4`<br/>`5` | `2`<br/>`3`<br/>`4`<br/>`5` | The direction the block is facing. For example, a block facing east is attached to a block to its west.2: north<br/>3: south<br/>4: west<br/>5: east<br/> |
|                  |                           |               | `0`<br/>`1`                 | `0`<br/>`1`                 | Unused                                                                                                                                                    |

### Block data
A banner has a block entity associated with it that holds additional data about the block. 

Bedrock Edition:

SeeBedrock Edition level format/Block entity format.
Java Edition:

See also: Block entity format

- Block entity data
	- 
	- Tags common to all block entities
	- CustomName: Optional. The name of this banner in JSON text component, which is used for showing the banner on a map.
	- Patterns: List of all patterns applied to the banner.
		- : An individual pattern.
			- Color: Color of the section.
			- Pattern: The banner pattern code the color is applied to.


Pattern color
Main article: Banner/DV[edit]


Pattern
Main article: Banner/Patterns[edit]

### Item data
Java Edition:

Main article: Item format
Banners, as items, use an NBT tag BlockEntityTag to indicate the patterns and details when it is placed.

- Item: The item
	- tag: Additional information about the item. This tag is optional for most items.
		- BlockEntityTag: The details of the banner.
			- All block data, except tags common to all block entities.

Bedrock Edition:

SeeBedrock Edition level format/Item format.
