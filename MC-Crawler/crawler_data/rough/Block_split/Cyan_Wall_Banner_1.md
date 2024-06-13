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

