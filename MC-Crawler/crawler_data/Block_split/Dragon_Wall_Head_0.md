# Dragon Head
A dragon head is a block modeled after the head of the ender dragon.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
- 2 Usage
	- 2.1 Decoration
	- 2.2 Wearing
		- 2.2.1 Disguise
	- 2.3 Dispensers
	- 2.4 Crafting ingredient
	- 2.5 Enchantments
	- 2.6 Note blocks
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Metadata
	- 4.3 Block states
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Renders
	- 7.2 Screenshots
- 8 References

## Obtaining
### Breaking
A dragon head can be mined using any item,[1] and drops itself when broken.

| Block    | Dragon Head         |
|----------|---------------------|
| Hardness | 1                   |
|          | Breakingtime (secs) |
| Default  | 1.5                 |

If a dragon head is pushed by a piston or comes in contact with water or lava, it breaks off as an item.

When destroyed by an explosion, the dragon head always drops as an item.

### Natural generation
Dragon heads generate on end ships found in end cities.

## Usage
### Decoration
Dragon heads can be oriented in 16 different directions on top of a block, and 4 directions on the sides of blocks, similar to signs. They can be placed on top of, or beside each other by shift clicking.

When placed and powered by redstone, the dragon head opens and closes its mouth repeatedly (2 times per second). The same animation occurs when worn by a (horizontally) moving player, zombie, skeleton, or armor stand (note: the animation does not play if the NoGravity tag is set to 1)

### Wearing
See also:  § Renders

The player can wear dragon heads, similarly to pumpkins or helmets. This overlays the second layer of the player's skin.

#### Disguise
Unlike most other heads, wearing a dragon head does not impact the behavior of a corresponding mob: the ender dragon attacks the player as usual.

In Bedrock Edition, wearing a dragon head makes the player invisible to other players on a locator map.

### Dispensers
A dispenser can equip a dragon head on a player, mob, or armor stand with an empty helmet slot, within the block the dispenser is facing.

### Crafting ingredient
| Ingredients                   | Crafting recipe | Description         |
|-------------------------------|-----------------|---------------------|
| Dragon Head +Gunpowder+AnyDye |                 | Forms Creeper shape |

### Enchantments
Dragon heads can receive the following enchantments, but only through an anvil.

| Name               | Max level | Method |
|--------------------|-----------|--------|
| Curse of Binding   | I         | Anvil  |
| Curse of Vanishing | I         | Anvil  |

### Note blocks
Placing a dragon head above a note block causes the note block to play the ender dragon's ambient sound when activated.

The block below the note block does not affect the mob sound it creates.

## Data values
### ID
Java Edition:

| Name             | Identifier       | Form         | Translation key                  |
|------------------|------------------|--------------|----------------------------------|
| Dragon Head      | dragon_head      | Block & Item | block.minecraft.dragon_head      |
| Dragon Wall Head | dragon_wall_head | Block        | block.minecraft.dragon_wall_head |

| Name         | Identifier |
|--------------|------------|
| Block entity | skull      |

Bedrock Edition:

| Dragon Head | Identifier | Numeric ID | Form                         | Item ID[i 1] | Translation key        |
|-------------|------------|------------|------------------------------|--------------|------------------------|
| Block       | skull      | 144        | Block & Ungiveable Item[i 2] | item.skull   | —                      |
| Item        | skull      | 516        | Item                         | —            | item.skull.dragon.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Unavailable with /give command


| Name         | Savegame ID |
|--------------|-------------|
| Block entity | Skull       |

