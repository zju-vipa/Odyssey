# Goat Horn
A goat horn is an item dropped by goats. It has eight variants, and each plays a unique sound when used which can be heard by players in a large radius.

## Contents
- 1 Obtaining
	- 1.1 Mob loot
	- 1.2 Chest loot
- 2 Usage
- 3 Sounds
	- 3.1 Generic
	- 3.2 Playing
- 4 Data values
	- 4.1 ID
	- 4.2 Item data
		- 4.2.1 Java Edition
- 5 History
- 6 Issues
- 7 Trivia
- 8 Gallery
	- 8.1 Screenshots
- 9 Notes
- 10 References
- 11 External links

## Obtaining
### Mob loot
A horn is dropped when an adult goat rams a tree or any other hard block that occurs naturally where goats spawn. These include stone, coal ore, copper ore, iron ore, emerald ore, log, or packed ice. Goats do not ram other solid blocks. In Java Edition, these blocks are listed under the snaps_goat_horn tag, and can be modified by data packs.

Up to two horns can be dropped from an adult goat, or one horn if the goat spawned with only one horn. Regular goats may drop the Ponder, Sing, Seek, and Feel horns, while screaming goats drop the Admire, Call, Yearn, and Dream horns. A specific goat drops only one type of horn; that is, if a goat drops a Sing horn, its other horn is also a Sing horn.

### Chest loot
| Item         | Structure        | Container | Quantity | Chance          |
|--------------|------------------|-----------|----------|-----------------|
|              |                  |           |          | Java Edition    |
| Goat Horn[A] | Pillager Outpost | Chest     | 1        | 50%             |
|              |                  |           |          | Bedrock Edition |
| Goat Horn[A] | Pillager Outpost | Chest     | 1        | 50%             |

1. ↑ a bDoes not contain goat horn variants that drop from screaming goats.

Only the four variants from regular goats can be found here.

## Usage
When used, they play a loud sound that can be heard from up to 256 blocks, but are also limited by the server view distance. Each horn variant plays a unique sound. There are eight variants, four of which are exclusive to screaming goats.

There is a cooldown of seven seconds between each use of the horn. All goat horns are affected by this cooldown.

## Data values
### ID
Java Edition:

| Name      | Identifier  | Form | Translation key                                                                                                                                                                                                                                                                                                                                                                  |
|-----------|-------------|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Goat Horn | `goat_horn` | Item | `item.minecraft.goat_horn`<br/>`instrument.minecraft.ponder_goat_horn`<br/>`instrument.minecraft.sing_goat_horn`<br/>`instrument.minecraft.seek_goat_horn`<br/>`instrument.minecraft.feel_goat_horn`<br/>`instrument.minecraft.admire_goat_horn`<br/>`instrument.minecraft.call_goat_horn`<br/>`instrument.minecraft.yearn_goat_horn`<br/>`instrument.minecraft.dream_goat_horn` |

Bedrock Edition:

| Name      | Identifier  | Numeric ID | Form | Translation key                                                                                                                                                                                                                                                                                                                               |
|-----------|-------------|------------|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Goat Horn | `goat_horn` | `624`      | Item | `item.goat_horn.name`<br/>`item.minecraft.goat_horn.sound.0`<br/>`item.minecraft.goat_horn.sound.1`<br/>`item.minecraft.goat_horn.sound.2`<br/>`item.minecraft.goat_horn.sound.3`<br/>`item.minecraft.goat_horn.sound.4`<br/>`item.minecraft.goat_horn.sound.5`<br/>`item.minecraft.goat_horn.sound.6`<br/>`item.minecraft.goat_horn.sound.7` |

### Item data
#### Java Edition
- tag: The item'stagtag.

- 
	- instrument: The identifier of the goat horn variant.

Goat horns use the "instrument" tag to control which sound can be played when using a goat horn. The values of the tag (to be prefixed with minecraft:) are:

| Sound type | Identifier         |
|------------|--------------------|
| Ponder     | `ponder_goat_horn` |
| Sing       | `sing_goat_horn`   |
| Seek       | `seek_goat_horn`   |
| Feel       | `feel_goat_horn`   |
| Admire     | `admire_goat_horn` |
| Call       | `call_goat_horn`   |
| Yearn      | `yearn_goat_horn`  |
| Dream      | `dream_goat_horn`  |

## Notes
1. ↑ a b c d e f g hThese are dropped by screaming goats.

