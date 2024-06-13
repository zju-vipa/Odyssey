# Soul Campfire
A soul campfire is a dimmer variant of the campfire with turquoise flames. Soul campfires deal more damage than normal campfires. Just like normal campfires, it can be used to cook food, pacify bees, act as a spread-proof light source, smoke signal or damaging trap block.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
- 2 Usage
	- 2.1 Particles and smoke signals
	- 2.2 Damage
	- 2.3 Cooking
	- 2.4 Hoppers
	- 2.5 Bees
	- 2.6 Piglins
	- 2.7 Light source
	- 2.8 Note blocks
	- 2.9 Converting soul sand to soul soil
	- 2.10 Piston interactivity
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Block data
- 5 Achievements
- 6 Advancements
- 7 History
- 8 Issues
- 9 References

## Obtaining
### Breaking
Soul campfires can be mined with any tool, or without a tool, but axes are the fastest. A soul campfire drops soul soil, as well as any items currently cooking on it. If mined with a tool enchanted with Silk Touch, the soul campfire instead drops itself as an item.

In Bedrock Edition, a soul campfire can also be broken by pushing it with a piston or sticky piston. Pistons cannot move or break soul campfires in Java Edition.

| Block     | Soul Campfire         |
|-----------|-----------------------|
| Hardness  | 2                     |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 3                     |
| Wooden    | 1.5                   |
| Stone     | 0.75                  |
| Iron      | 0.5                   |
| Diamond   | 0.4                   |
| Netherite | 0.35                  |
| Golden    | 0.25                  |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Crafting
| Name          | Ingredients                                                                                                             | Crafting recipe |
|---------------|-------------------------------------------------------------------------------------------------------------------------|-----------------|
| Soul Campfire | Stick+<br/>Soul Sand+<br/>AnyLogorStemor<br/>AnyStripped LogorStemor<br/>AnyWoodorHyphaeor<br/>AnyStripped WoodorHyphae |                 |
| Soul Campfire | Stick+<br/>Soul Soil+<br/>AnyLogorStemor<br/>AnyStripped LogorStemor<br/>AnyWoodorHyphaeor<br/>AnyStripped WoodorHyphae |                 |

## Usage
Lit soul campfires emit a light level of 10.

Soul campfires are lit by default when placed. Soul campfires can be manually lit by using or dispensing flint and steel on them, shooting it with a flaming arrow, or using or dispensing fire charges, blaze fireballs, and ghast fireballs when /gamerule mobGriefing is true. In Bedrock Edition, soul campfires can also be lit by using an item enchanted with fire aspect, or stepping on it while burning. 

Soul campfires can be extinguished by waterlogging it (placing water in the same block space), throwing a splash water bottle on it, or using a shovel on it. Soul campfires cannot be extinguished from their bottom face.‌[JE  only][1] In Bedrock Edition, soul campfires can also be extinguished by placing a water source or allowing water to flow in the space above the soul campfire. As with torches, rain does not extinguish soul campfires.[2]

Using flint and steel on the side of a waterlogged or lit soul campfire sets the adjacent air block on fire instead.

Any items cooking on a soul campfire always drop when the soul campfire block is broken.

### Particles and smoke signals
Unlike regular campfires, soul campfires do not emit embers.[3]

### Damage
Soul campfires damage mobs standing on top of them even if underwater (with exceptions such as shulkers, zombified piglins or guardians), but only if lit. Soul campfires deal 2 of damage every tick (although damage immunity reduces this to once every half-second). Soul campfires do not cause lasting burning or destroy items. Damage taken is considered fire damage and is reduced by armor (which loses durability), the Resistance potion effects, and the Protection and Fire Protection enchantments. The player can avoid being damaged at all, either by using a potion of fire resistance or wearing Frost Walker boots.

Regardless of height, all blocks prevent damage done to mobs or players above soul campfires. The soul campfire deals damage only to entities occupying its block.

### Cooking
Main article: Campfire § Cooking
### Hoppers
Soul campfires do not have an external inventory. Raw food cannot be loaded into the soul campfire with a hopper.

A hopper placed directly underneath a soul campfire pulls through any items dropped into the soul campfire. Any drops from a mob that dies in the soul campfire get pulled into the hopper.

### Bees
Placing a soul campfire under a beehive or bee nest allows players to harvest honey bottles or honeycomb without provoking the bees.
There must be unobstructed air between the soul campfire and the beehive or bee nest. Carpets are an exception.‌[Java Edition  only]

### Piglins
Lit soul campfires repel piglins that are not currently attacking. This occurs when the piglin is within an 8 block radius of the soul campfire.

### Light source
Soul campfires emit a light level of 10. Due to their lower light level, soul campfires do not melt snow or ice.

### Note blocks
Soul campfires can be placed under note blocks to produce "bass" sounds.

### Converting soul sand to soul soil
Soul campfires can be used to convert soul sand into soul soil. If a soul campfire is crafted using soul sand, placed, and then broken without Silk Touch, that soul campfire drops soul soil.[4]

### Piston interactivity
In Bedrock Edition, pushing a soul campfire with a piston or sticky piston breaks it. Soul campfires cannot be pulled by sticky pistons.

In Java Edition, pistons do not interact with soul campfires. Soul campfires neither move nor break when pushed or pulled by pistons.

## Data values
### ID
Java Edition:

| Name          | Identifier      | Form         | Block tags                          | Translation key                 |
|---------------|-----------------|--------------|-------------------------------------|---------------------------------|
| Soul Campfire | `soul_campfire` | Block & Item | `campfires`<br/>`piglin_repellents` | `block.minecraft.soul_campfire` |

| Name         | Identifier |
|--------------|------------|
| Block entity | `campfire` |

Bedrock Edition:

| Name  | Identifier      | Numeric ID | Form                         | Item ID[i 1]         | Translation key           |
|-------|-----------------|------------|------------------------------|----------------------|---------------------------|
| Block | `soul_campfire` | `545`      | Block & Ungiveable Item[i 2] | `item.soul_campfire` | `tile.soul_campfire.name` |
| Item  | `soul_campfire` | `622`      | Item                         | —                    | `tile.soul_campfire.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Unavailable with /give command

| Name         | Savegame ID |
|--------------|-------------|
| Block entity | `Campfire`  |

### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values                            | Description                                                                                                            |
|-------------|---------------|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| facing      | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the campfire is facing.<br/>The opposite from the direction the player faces while placing the campfire. |
| lit         | `true`        | `false`<br/>`true`                        | Whether the campfire is lit.                                                                                           |
| signal_fire | `false`       | `false`<br/>`true`                        | Whether the campfire has ahay balebelow it.                                                                            |
| waterlogged | `false`       | `false`<br/>`true`                        | Whether or not there's water in the same place as this campfire.                                                       |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                            |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|------------------------------------------------------------------------------------------------------------------------|
| extinguished                 | `0x4`         | `false`       | `false`<br/>`true`                        | `0`<br/>`1`             | Whether the campfire is put out.                                                                                       |
| minecraft:cardinal_direction | Not Supported | `south`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction the campfire is facing.<br/>The opposite from the direction the player faces while placing the campfire. |



### Block data
A soul campfire has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format

- Block entity data
	- 
	- Tags common to all block entities
	- CookingTimes: How long each item has been cooking, first index is slot 0, etc.
	- CookingTotalTimes: How long each item has to cook, first index is slot 0, etc.
	- Items: List of up to 4 items currently cooking.
		- 
		- Tags common to all items

Bedrock Edition:

SeeBedrock Edition level format/Block entity format.
