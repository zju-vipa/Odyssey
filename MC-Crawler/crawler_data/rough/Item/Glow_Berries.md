# Glow Berries
Glow berries are a food item obtained from cave vines and can be used to plant them.

Cave vines are a climbable, bonemealable plant that hangs off ceilings and grows glow berries. Cave vines with glow berries produce light.

## Contents
- 1 Obtaining
	- 1.1 Natural generation
	- 1.2 Chest loot
	- 1.3 Post-generation
- 2 Usage
	- 2.1 Placement
	- 2.2 Growth
	- 2.3 Farming
	- 2.4 Food
	- 2.5 Light
	- 2.6 Composting
	- 2.7 Breeding
- 3 Sounds
	- 3.1 Glow berries
	- 3.2 Cave vines
		- 3.2.1 Generic
		- 3.2.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 Advancements
- 6 History
	- 6.1 Cave vines "item"
		- 6.1.1 Appearances
		- 6.1.2 Names
- 7 Issues
- 8 Gallery
	- 8.1 Renders

## Obtaining
### Natural generation
Cave vines can be found in lush caves, hanging from cave ceilings.


### Chest loot
| Item         | Structure      | Container     | Quantity | Chance          |
|--------------|----------------|---------------|----------|-----------------|
|              |                |               |          | Java Edition    |
| Glow Berries | Mineshaft      | Chest         | 3–6      | 38.7%           |
|              | Ancient City   | Chest         | 1–15     | 23.2%           |
|              | Trial Chambers | Trial spawner | 2–10     | 11.5%           |
|              |                | Supply chest  | 2–10     | 37.3%           |
|              |                |               |          | Bedrock Edition |
| Glow Berries | Mineshaft      | Chest         | 3–6      | 38.7%           |
|              | Ancient City   | Chest         | 1–15     | 23.2%           |
|              | Trial Chambers | Supply chest  | 2–10     | 37.3%           |

### Post-generation
A bunch (item) of glow berries can be collected from cave vines by using or breaking the vine. This yields one bunch of glow berries when the vine is bearing them and nothing when it is not. A cave vine also breaks if water runs over its location or if a piston extends or pushes a block into its location.

Fortune has no effect on the number of glow berries dropped.

## Usage
### Placement
Glow berries can be placed on and grown from the bottom of most blocks (any block whose bottom face covers the bottom of the entire block). They can also be placed on the bottom of a cave vine, extending the stack of vines by 1 block. They have no specific lighting requirements.

### Growth
Placing glow berries on the bottom of a block creates a cave vine that grows downward one block at a time as long as air is beneath it and its maximum height (2 to 26 blocks) has not been reached.

### Farming
Cave vines are functionally a crop, and glow berries are its seeds. However, it grows differently than farmland crops do. In Bedrock Edition, cave vines is technically an item on its own. In Java Edition there is no proper cave vines item, and glow berries is the closest thing to its item form.

Each newly-grown cave vine block has an 11% chance of bearing glow berries. Glow berries only grow on a newly produced cave vine, and only when it first grows. A cave vine bearing no berry does not naturally grow a berry, unlike sweet berry bushes ‌[Java Edition  only][more information needed].

Using bone meal on a cave vine produces a glow berry in the vine, if the vine was not bearing glow berries. 

In Java Edition, cave vines stop growing if shears are used on the bottom block of the stack.

In Bedrock Edition, in the Nether, cave vines can grow and bear glow berries.

The different types of cave vines actually have different block names and ids. Futhermore, there are 3 different item versions of the cave vines blocks in Bedrock Edition.

### Food
To eat glow berries, press and hold use while it is selected in the hotbar. This restores 2 () hunger and 0.4 hunger saturation points, like sweet berries.

### Light
When bearing glow berries, cave vines give off a light level of 14.

### Composting
Placing glow berries into a composter by using them on it has a 30% chance of raising the compost level by 1.

### Breeding
Glow berries can be fed to foxes to breed them.

Glow berries can be used on baby foxes to reduce the time until they grow by 10%.

## Data values
### ID
Java Edition:

| Name             | Identifier         | Form  | Block tags                                                                                | Item tags  | Translation key                    |
|------------------|--------------------|-------|-------------------------------------------------------------------------------------------|------------|------------------------------------|
| Cave Vines       | `cave_vines`       | Block | `mineable/axe`<br/>`bee_growables`<br/>`cave_vines`<br/>`climbable`<br/>`sword_efficient` | —          | `block.minecraft.cave_vines`       |
| Cave Vines Plant | `cave_vines_plant` | Block | `mineable/axe`<br/>`bee_growables`<br/>`cave_vines`<br/>`climbable`<br/>`sword_efficient` | —          | `block.minecraft.cave_vines_plant` |
| Glow Berries     | `glow_berries`     | Item  | —                                                                                         | `fox_food` | `item.minecraft.glow_berries`      |

Bedrock Edition:

| Name                         | Identifier                     | Numeric ID | Form                         | Item ID[i 1]   | Translation key                          |
|------------------------------|--------------------------------|------------|------------------------------|----------------|------------------------------------------|
| Cave Vines                   | `cave_vines`                   | `577`      | Block & Ungiveable Item[i 2] | Identical[i 3] | `tile.cave_vines.name`                   |
| Cave Vines Body With Berries | `cave_vines_body_with_berries` | `630`      | Block & Ungiveable Item[i 2] | Identical[i 3] | `tile.cave_vines_body_with_berries.name` |
| Cave Vines Head With Berries | `cave_vines_head_with_berries` | `631`      | Block & Ungiveable Item[i 2] | Identical[i 3] | `tile.cave_vines_head_with_berries.name` |
| Glow Berries                 | `glow_berries`                 | `638`      | Item                         | —              | `item.glow_berries.name`                 |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑ a b cUnavailable with /give command
3. ↑ a b cThe block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:
Cave Vines:

| Name    | Default value | Allowed values                                                                                                                                                                                                              | Description                         |
|---------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|
| berries | `false`       | `false`<br/>`true`                                                                                                                                                                                                          | Whether this cave vine has berries. |
| age     | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15`<br/>`16`<br/>`17`<br/>`18`<br/>`19`<br/>`20`<br/>`21`<br/>`22`<br/>`23`<br/>`24`<br/>`25` | How old this cave vine is.          |

Cave Vines Plant:

| Name    | Default value | Allowed values     | Description                         |
|---------|---------------|--------------------|-------------------------------------|
| berries | `false`       | `false`<br/>`true` | Whether this cave vine has berries. |

Bedrock Edition:
Cave Vines, Cave Vines Body With Berries, Cave Vines Head With Berries:

| Name              | Metadata Bits | Default value | Allowed values                                                                                                                                                                                                              | Values forMetadata Bits | Description                |
|-------------------|---------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|----------------------------|
| growing_plant_age | Not Supported | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15`<br/>`16`<br/>`17`<br/>`18`<br/>`19`<br/>`20`<br/>`21`<br/>`22`<br/>`23`<br/>`24`<br/>`25` | `Unsupported`           | How old this cave vine is. |



