# Ominous Banner
An ominous banner‌[JE  only], or illager banner‌[BE & edu  only], is a special uncraftable variant of the banner obtained from Illagers.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Mob loot
- 2 Usage
	- 2.1 Helmet
	- 2.2 Chestplate
	- 2.3 Crafting ingredient
	- 2.4 Copying
	- 2.5 Map marker
	- 2.6 Renaming
	- 2.7 Fuel
	- 2.8 Note blocks
	- 2.9 Looms
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Block data
		- 4.3.1 Pattern color
		- 4.3.2 Pattern
	- 4.4 Item data
- 5 Advancements
- 6 History
- 7 Issues
- 8 Trivia
- 9 Gallery
	- 9.1 Renders
		- 9.1.1 Ominous banner
	- 9.2 In other media
- 10 References

## Obtaining
### Breaking
Ominous banners can be broken with or without a tool, but an axe is fastest.

| Block     | Ominous Banner        |
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

A ominous banner also breaks and drops itself as an item if the block the banner is attached to is moved, removed, or destroyed.

### Natural generation
Ominous banners are carried by raid captains. They are located in pillager outposts.

In Java Edition, the ominous banner cannot be crafted or copied because the design uses 8 patterns.

In Bedrock Edition, the illager banner is a separate type that cannot be placed in a loom.

Ominous banners have the following pattern:




White banner‌[JE  only]

- Cyan Lozenge
- Light Gray Base
- Gray Pale
- Light Gray Bordure
- Black Fess
- Light Gray Per Fess
- Light Gray Roundel
- Black Bordure

Separate type entirely‌[BE  only]

### Mob loot
Illagers that spawn carrying an ominous banner‌[JE  only] / illager banner‌[BE & edu  only] always drop it upon death.

| Source     | Roll Chance | Quantity (Roll Chance) |           |            |             |
|------------|-------------|------------------------|-----------|------------|-------------|
|            |             | Default                | Looting I | Looting II | Looting III |
| Vindicator | 100%[d 1]   | 1                      | 1         | 1          | 1           |

1. ↑When holding an ominous banner.

## Usage
See also: Banner § Usage

Ominous banners are a special type of banner in the game as they have more than 6 patterns, and as such cannot be crafted. Ominous banners have the same placement functionality as regular banners.

### Helmet

  

This feature is exclusive to  Java Edition. 


While an ominous banner cannot be equipped in the head slot in Survival mode, equipping it using commands causes it to appear on top of the player. This is how raid captains wear banners‌[JE  only].

### Chestplate

  

This feature is exclusive to  Bedrock Edition. 


While an ominous banner cannot be equipped in the chestplate slot in Survival mode, equipping it using NBT editors causes it to appear on top of the player. This is how raid captains wear banners‌[BE & edu  only].

- 
- 
- 
- 

### Crafting ingredient
Since ominous banners have more than six patterns, adding it to the shield will cause the banner to be reduced to six patterns on the shield.

| Ingredients                | Crafting recipe | Description                                                                                                                                                                                 |
|----------------------------|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Shield+<br/>Ominous Banner |                 | Applies the banner pattern to the shield. The banner is consumed.<br/>The shield must have no pre-existing patterns.<br/>Does not change existing durability or enchantments on the shield. |

### Copying
Unlike normal banners, ominous banners cannot be copied to make additional copies of the ominous banner.

### Map marker

  

This feature is exclusive to  Java Edition. 


Like regular banners, ominous banners can also serve as a map marker, having the same functionality as regular banners when used for marking points on a map.

### Renaming
In Java Edition, an ominous banner can be given a custom name that remains as the ominous banner is placed and retrieved. The player can use an anvil to rename the ominous banner item, or may change the CustomName tag using the /data command on the ominous banner block.

### Fuel
Ominous banners can be used as a fuel in furnaces, smelting 1.5 items per banner.

### Note blocks
Ominous banners can be placed under note blocks to produce "bass" sounds.

### Looms
Unlike a regular banner, ominous banners can't be used in a loom to apply patterns.

## Data values
### ID
Java Edition:

| Name                | Identifier          | Form         | Block tags                         | Item tags | Translation key                  |
|---------------------|---------------------|--------------|------------------------------------|-----------|----------------------------------|
| Ominous Banner      | `white_banner`      | Block & Item | `banners`<br/>`wall_post_override` | `banners` | `block.minecraft.ominous_banner` |
| Ominous Wall Banner | `white_wall_banner` | Block        | `banners`<br/>`wall_post_override` | —         | `block.minecraft.ominous_banner` |

Bedrock Edition:

| Banner   | Identifier        | Numeric ID | Form                         | Item ID[i 1]   | Translation key                   |
|----------|-------------------|------------|------------------------------|----------------|-----------------------------------|
| Standing | `standing_banner` | `176`      | Block & Ungiveable Item[i 2] | Identical[i 3] | `tile.standing_banner.white.name` |
| Wall     | `wall_banner`     | `177`      | Block & Ungiveable Item[i 2] | Identical[i 3] | —                                 |
| Item     | `banner`          | `567`      | Item                         | —              | `item.banner.white.name`          |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑ a bUnavailable with /give command
3. ↑ a bThe block's direct item form has the same id as the block.

| Name         | Savegame ID |
|--------------|-------------|
| Block entity | `Banner`    |

