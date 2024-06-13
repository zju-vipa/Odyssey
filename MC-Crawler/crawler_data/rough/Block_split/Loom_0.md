# Loom
A loom is used to apply patterns to banners. It also serves as a shepherd's job site block.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Applying banner patterns
	- 2.2 Changing profession
	- 2.3 Fuel
	- 2.4 Note blocks
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Renders
- 8 External links

## Obtaining
### Breaking
A loom can be mined using any tool or by hand, but axes are the quickest. It always drops as an item.

| Block     | Loom                  |
|-----------|-----------------------|
| Hardness  | 2.5                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 3.75                  |
| Wooden    | 1.9                   |
| Stone     | 0.95                  |
| Iron      | 0.65                  |
| Diamond   | 0.5                   |
| Netherite | 0.45                  |
| Golden    | 0.35                  |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Looms can be found in village shepherd houses.

### Crafting
| Ingredients           | Crafting recipe |
|-----------------------|-----------------|
| String+<br/>AnyPlanks |                 |

## Usage
### Applying banner patterns
Interface for the loom in Java Edition.
Interface for the loom in Bedrock Edition.

Using on a loom opens its interface. It has 3 slots for a banner, a dye and an optional banner pattern item. When a banner is put in, a list of patterns appears in the center part. 8‌[Java Edition  only] or 10 patterns require the following banner patterns: Flower Charge, Creeper Charge, Skull Charge, Thing, Snout, Globe, Field Masoned,‌[Bedrock Edition  only]  Bordure Indented,‌[Bedrock Edition  only] Flow, ‌[upcoming: JE 1.21 & BE 1.21.0] and Guster ‌[upcoming: JE 1.21 & BE 1.21.0]. Putting a banner pattern in its respective slot makes the loom show only that pattern.

Selecting a pattern or using a banner pattern on the list shows the preview of the banner after applying, if a dye is present. To finish, the player must take the banner in the slot beneath the preview. The original banner and the dye disappear from their respective slots, but the banner pattern is not consumed.

### Changing profession
If a village has a loom that has not been claimed by a villager, any villager who hasn't already chosen a job site block has a chance to change their profession to shepherd.

### Fuel
A loom can be used as fuel in a furnace to smelt 1.5 items.

### Note blocks
Looms can be placed under note blocks to produce "bass" sounds.

## Data values
### ID
Java Edition:

| Name | Identifier | Form         | Translation key        |
|------|------------|--------------|------------------------|
| Loom | `loom`     | Block & Item | `block.minecraft.loom` |

Bedrock Edition:

| Name | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key  |
|------|------------|------------|----------------------------|----------------|------------------|
| Loom | `loom`     | `459`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.loom.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name   | Default value | Allowed values                            | Description                                                                                             |
|--------|---------------|-------------------------------------------|---------------------------------------------------------------------------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the loom is facing.<br/>Opposite from the direction the player faces when placing a loom. |

Bedrock Edition:

| Name      | Metadata Bits   | Default value | Allowed values              | Values forMetadata Bits     | Description                                                                                                                         |
|-----------|-----------------|---------------|-----------------------------|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| direction | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`1`<br/>`2`<br/>`3` | The direction the loom is facing.0: South facing loom<br/>1: West facing loom<br/>2: North facing loom<br/>3: East facing loom<br/> |




