# Decorated Pot
A decorated pot is a storage block crafted from bricks and/or pottery sherds, with the items used individually affecting the appearance of its four side faces. It can store a single inventory slot's worth of items, which cannot be seen or retrieved by hand without breaking the pot.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
	- 1.3 Natural generation
- 2 Usage
	- 2.1 Storage
- 3 Sounds
	- 3.1 Generic
		- 3.1.1 Popped
		- 3.1.2 Shattered
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Block data
- 5 Achievements
- 6 Advancements
- 7 History
- 8 Issues
- 9 Trivia
- 10 Gallery
	- 10.1 Renders
	- 10.2 Screenshots
	- 10.3 Concept artwork
	- 10.4 In other media
- 11 References
- 12 External links

## Obtaining
### Breaking
Decorated pots can be broken with any tool and are mined instantly. A decorated pot drops the four pottery sherds or bricks used to craft it when mined with a pickaxe, axe, shovel, hoe or sword not enchanted with Silk Touch. It drops itself when mined with anything else, including tools listed above enchanted with Silk Touch.

A decorated pot breaks when hit by one of the following projectiles, causing it to shatter into sherds or bricks:

- Arrow
- Tipped Arrow
- Spectral Arrow
- Trident
- Firework Rocket
- Snowball
- Egg
- Fireball
- Small Fireball
- Dragon Fireball
- Wither Skull
- Wind Charge‌[upcoming: JE 1.21 & BE 1.21.0]

A decorated pot drops itself if pushed by a piston. It also always drops itself when destroyed by an explosion, similar to other precious blocks such as beacons and shulker boxes.[1]

Stored items are dropped when the decorated pot is broken, regardless of whether the pot shatters into sherds or drops itself. Breaking a pot is the only way to access the stored items without using a hopper.

In Java Edition, if the cracked block state is set to true, a decorated pot always drops sherds or bricks regardless of the breaking method.

### Crafting
| Ingredients             | Crafting recipe | Description                                                        |
|-------------------------|-----------------|--------------------------------------------------------------------|
| AnyPottery SherdorBrick |                 | It is possible to use any combination of bricks andpottery sherds. |

The decorated pot's side textures correspond to the item used in the crafting. If a pottery sherd is used, that side bears the texture of that pottery sherd, if a brick is used, that side bears the default texture.

### Natural generation
Decorated pots naturally generate in trial chambers, with loot inside.‌[upcoming: JE 1.21 & BE 1.21.0] Decorated pots in the trial chambers are composed of either four bricks or three bricks either one flow, guster, or scrape pottery sherd.

## Usage
Decorated pots can be used for decoration. Due to the top part of the decorated pot having no collision, other blocks can be placed on top of them, including other decorated pots and regular flower pots, which are required to place a flower in the decorated pot.

Pressing the use control on a decorated pot causes it to play a wobble animation, triggering a vibration frequency of 11.

Decorated pots crafted without sherds can also serve as a temporary building block, similar to scaffolding and slime blocks, because they are easy to craft, stack to 64, and can be broken instantly by hand.

### Storage
A decorated pot can store up to a stack of a single type of item. Unlike other containers, decorated pots have no GUI; items are inserted by interacting with the pot or by using droppers or hoppers. The only ways to retrieve stored items is by breaking the pot or by using hoppers and minecarts with hopper.

Decorated pots crafted without sherds can also serve as compact storage for bricks, as they are stackable, each can be crafted from four bricks and can be broken down into four bricks.

A redstone comparator can be used to measure the number of stored items.

## Data values
### ID
Java Edition:

| Name          | Identifier    | Form         | Translation key               |
|---------------|---------------|--------------|-------------------------------|
| Decorated Pot | decorated_pot | Block & Item | block.minecraft.decorated_pot |

| Name         | Identifier    |
|--------------|---------------|
| Block entity | decorated_pot |

Bedrock Edition:

| Name          | Identifier    | Numeric ID | Form                       | Item ID[i 1]   | Translation key         |
|---------------|---------------|------------|----------------------------|----------------|-------------------------|
| Decorated Pot | decorated_pot | -551       | Block & Giveable Item[i 2] | Identical[i 3] | tile.decorated_pot.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


| Name         | Savegame ID  |
|--------------|--------------|
| Block entity | DecoratedPot |

### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values     | Description                                                                                                                       |
|-------------|---------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| facing      | north         | eastnorthsouthwest | The direction a decorated pot faces in.                                                                                           |
| cracked     | false         | falsetrue          | If true, the pot always makes shatter sounds upon breaking.The value is set to true immediately before being shattered by a tool. |
| waterlogged | false         | falsetrue          | Whether or not there's water in the same place as this decorated pot.                                                             |

Bedrock Edition: [more information needed]



### Block data
A decorated pot has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format


 Block entity data
Tags common to all block entities
 sherds: List of sherds on this decorated pot.
: Item ID of this face. Each value defaults to bricks's ID, and can be either a brick or any sherd.
 item: The item stored within the pot. A decorated pot does not use  Slot to describe its contents, even though it functionally has 1 item slot.
Tags common to all items
Tags common to all objects that use loot tables to produce items

Bedrock Edition:

See Bedrock Edition level format/Block entity format.
