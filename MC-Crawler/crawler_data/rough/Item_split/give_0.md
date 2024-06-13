# Commands/give
Gives an item to one or more players.

## Contents
- 1 Usage
- 2 Syntax
- 3 Arguments
- 4 Result
- 5 Output
- 6 Examples
- 7 History
- 8 See also

## Usage
Gives the specified item(s) to the target(s). If <targets> or player: target resolves to multiple targets, each receives the specified number of items.

If there is enough room in the player's inventory, or the player is in creative mode, gives the specified item(s). And in Java Edition, also summons a "fake" item entity, with its PickupDelay tag set to 32767 and its Age tag set to 5999, which would make it impossible to be picked up, and have it despawn within one tick.

If there is not enough room in the player's inventory, and the player is in creative mode, gives the specified item(s) until the inventory is full. And in Java Edition, also summons a "fake" item entity, with its PickupDelay tag set to 32767 and its Age tag set to 5999, which would make it impossible to be picked up, and have it despawn within one tick.

If there is not enough room in the player's inventory, and the player is not in creative mode, gives the specified item(s) until the inventory is full, and summons the rest items as a item entity dropped by the player. In Java Edition, the item's Owner tag is set to the target and its PickupDelay tag is set to 0 so that it can be picked up only by that player at any time. In Bedrock Edition, the item entity is dropped by the player as normal, having a 10-tick pickup delay and being able to be picked up by any entity. In Bedrock Edition, when dropping the item entity, the item using progress of the player is discarded. In Bedrock Edition, the "Use doors and switches" option (in the "Player Permission" screen) disables the player to drop any item entity, even caused by the /give command.

## Syntax
- Java Edition

give <target> <item> [<count>]
- Bedrock Edition

give <player: target> <itemName: Item> [amount: int] [data: int] [components: json]
## Arguments
JE: <targets>: entityBE: player: target: CommandSelector<Player>

Specifies the target(s) to give item(s) to.
Must be a player name, atarget selectoror aUUID‌[Java Edition  only].  And the target selector must‌[JE  only]/should‌[BE  only]be ofplayer type.
JE: <item>: item_stackBE: itemName: Item: enum

Specifies the item to give.
InJava Edition, it must be in the format ofitem_id{data_tags}(accepts item and block tags), in which data tags can be omitted when they are not needed. InBedrock Edition, it must be anitem idor ablock idfor which the item form exist.
JE: <count>: integerBE: amount: int: int

Specifies the number of items to give. If not specified, defaults to1.
Must be a32-bit integer number (from -2147483648 (-231) to 2147483647 (231-1) ). InJava Edition, it must be between 1 and 2147483647 (inclusive). InBedrock Edition, it should be between 1 and 32767 (inclusive).
BE: data: int: int

Specifies the itemdata valueof the given item(s). Values that are invalid for the specified item id revert to 0. If not specified, defaults to 0.
Must be a32-bit integer number (from -2147483648 (-231) to 2147483647 (231-1) ). It should be between 0 and 32767 (inclusive).
BE: components: json: Json::Value

Specifies theitem componentsof the given item(s). Like data tags but supports onlyminecraft:can_place_on,minecraft:can_destroy,minecraft:item_lock, andminecraft:keep_on_deathfunctions (see#Examples).
It must be aJSONObject.
## Result









| Command | Trigger                                                                      | Java Edition | Bedrock Edition |
|---------|------------------------------------------------------------------------------|--------------|-----------------|
| Any     | The command is incomplete, or any argument is not specified correctly.       | Unparseable  | Unparseable     |
|         | `player: target`is a target selector that is not ofplayer type.              | N/A          | Failed          |
|         | `amount: int`is not between 1 and 32767.                                     |              |                 |
|         | `data: int`is not between 0 and 32767.                                       |              |                 |
|         | `<targets>`or`player: target`fails to resolve to one or more online players. | Failed       |                 |
|         | `<item>`or`itemName: item`is an ungivable item.                              |              |                 |
|         | `<count>`is larger than 100 stack worth items.                               |              | N/A             |
|         | Otherwise                                                                    |              | Successful      |

## Output





| Command | Edition         | Situation  | Success Count                               | /execute store success ... | /execute store result ...      |
|---------|-----------------|------------|---------------------------------------------|----------------------------|--------------------------------|
| Any     | Java Edition    | On fail    | 0                                           | 0                          | N/A                            |
|         |                 | On success | 1                                           | 1                          | the number of targeted players |
|         | Bedrock Edition | On fail    | 0                                           | N/A                        | N/A                            |
|         |                 | On success | the number of players who are given item(s) | N/A                        | N/A                            |

## Examples
- To give the nearest player a diamond sword with Lore that says "A legendary weapon":
	- /give @p minecraft:diamond_sword{display:{Lore:["\"A legendary weapon\""]}} 1‌[Java Edition  only]
- To give all players a potion that has theNight Visioneffect:
	- /give @a potion{Potion:"minecraft:night_vision"} 1‌[Java Edition  only]
	- /give @a potion 1 5‌[Bedrock Edition  only]
- To give a random player aSharpnessX diamond sword:
	- /give @r diamond_sword{Enchantments:[{id:"minecraft:sharpness",lvl:10}]} 1‌[Java Edition  only]
- To give the player executing the command a block of diamond that can be placed on dirt and can break quartz blocks, even in adventure mode.
	- /give @s minecraft:diamond_block{CanPlaceOn:["minecraft:dirt"],CanDestroy:["minecraft:quartz_block"]} 1‌[Java Edition  only]
	- /give @s diamond_block 1 0 {"minecraft:can_place_on":{"blocks":["dirt"]},"minecraft:can_destroy":{"blocks":["quartz_block"]}}‌[Bedrock Edition  only]
- To give all players a level 2 Wither Potion withKnockbackX:
	- /give @a potion{Enchantments:[{id:"minecraft:knockback",lvl:10}],CustomPotionEffects:[{Id:20,Amplifier:1}]} 1‌[Java Edition  only]
- To give the nearest player a diamond sword that is not dropped upon death:
	- /give @p diamond_sword 1 0 {"keep_on_death": {}}‌[Bedrock Edition  only]
- To give all players a stick that cannot be dropped or crafted with:
	- /give @a stick 1 0 {"item_lock": {"mode": "lock_in_inventory"}}‌[Bedrock Edition  only]
- To give a random player a wooden shovel that cannot be moved from its slot, dropped, or crafted with:
	- /give @r wooden_shovel 1 0 {"item_lock": {"mode": "lock_in_slot"}}‌[Bedrock Edition  only]


