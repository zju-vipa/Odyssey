# Carved Pumpkin
A carved pumpkin is a carved version of a pumpkin that can be worn or used to spawn golems. It can be made by using shears on a pumpkin placed in the world.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Mob loot
	- 1.4 Post-generation
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Helmet
	- 2.3 Dispensers
	- 2.4 Building golems
	- 2.5 Enchantments
	- 2.6 Composting
	- 2.7 Note blocks
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 Achievements
- 6 Advancements
- 7 History
- 8 Issues
- 9 Trivia
- 10 Gallery
	- 10.1 Renders
		- 10.1.1 Java Edition
		- 10.1.2 Bedrock Edition
		- 10.1.3 Mobs
		- 10.1.4 Structure
	- 10.2 Screenshots
	- 10.3 In other media
- 11 References
- 12 External links

## Obtaining
### Breaking
Carved pumpkins can be mined using any tool, but axes are the quickest way.

| Block     | Carved Pumpkin        |
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

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

When a carved pumpkin is pushed by a piston, it breaks and drops as an item. It cannot be pulled.

### Natural generation
Carved pumpkins generate in rail rooms in woodland mansions, as well as in pillager outposts as a part of scarecrows.

### Mob loot
The carved pumpkin of a snow golem can be obtained by shearing its head, revealing the golem's face. The carved pumpkin cannot be put back on the golem.

### Post-generation
A carved pumpkin (and 4 pumpkin seeds in Java Edition or 1 unit of pumpkin seeds in Bedrock Edition) is obtained by using shears on an uncarved pumpkin. Once carved, a pumpkin cannot be changed back to uncarved. This changes the rotation of the top texture.[1]

## Usage
When placed, a carved pumpkin automatically faces the player.

### Crafting ingredient
| Name           | Ingredients               | Crafting recipe |
|----------------|---------------------------|-----------------|
| Jack o'Lantern | Carved Pumpkin+<br/>Torch |                 |

### Helmet


A carved pumpkin can be equipped as a helmet without any actual armor value. When worn, it limits the player's viewing area to a mask pattern that resembles the pumpkin's carved face. The pattern does not appear when using the third-person view (toggled by F5 by default). In Java Edition, it also doesn't appear when the heads-up display is disabled by pressing F1.[2]

A player wearing a carved pumpkin does not aggravate endermen when looking at them. In Bedrock Edition, wearing a carved pumpkin makes the player invisible to other players on a locator map.

### Dispensers
Dispensers can equip a carved pumpkin on a player, mob or armor stand with an empty helmet slot, within the block the dispenser is facing. It can also place the carved pumpkin as a block, if a snow or iron golem can be spawned after the pumpkin is placed.

### Building golems
Snow golem
Iron golem
Carved pumpkins can be used to make snow golems and iron golems as shown below. Snow golems require snow blocks for their bodies, while iron golems require iron blocks. The carved pumpkin must be placed last or the golem does not spawn. The orientation of the carved pumpkin does not matter while building an iron golem or snow golem.




















Iron golem build configuration















Snow golem build configuration


### Enchantments
Carved pumpkins can receive the following enchantments, but only through an anvil.

| Name               | Max level | Method |
|--------------------|-----------|--------|
| Curse of Binding   | I         | Anvil  |
| Curse of Vanishing | I         | Anvil  |

### Composting
Placing a carved pumpkin into a composter has a 65% chance of raising the compost level by 1.

### Note blocks
Carved pumpkins do not produce didgeridoo sounds when placed under a note block, unlike regular pumpkins.[3]

## Data values
### ID
Java Edition:

| Name           | Identifier       | Form         | Block tags                             | Translation key                  |
|----------------|------------------|--------------|----------------------------------------|----------------------------------|
| Carved Pumpkin | `carved_pumpkin` | Block & Item | `enderman_holdable`<br/>`mineable/axe` | `block.minecraft.carved_pumpkin` |

Bedrock Edition:

| Name           | Identifier       | Numeric ID | Form                       | Item ID[i 1]   | Translation key            |
|----------------|------------------|------------|----------------------------|----------------|----------------------------|
| Carved Pumpkin | `carved_pumpkin` | `410`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.carved_pumpkin.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:
Carved pumpkin:

| Name   | Default value | Allowed values                            | Description                                                                                                                        |
|--------|---------------|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the pumpkin's carved face is facing.<br/>The opposite from the direction the player faces while placing the pumpkin. |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                                                                                            |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | `south`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction the pumpkin and carved pumpkin are facing.<br/>The opposite from the direction the player faces while placing the pumpkins. Though it doesn't affect the pumpkin at all. |



