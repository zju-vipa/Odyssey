# Commands/item
Manipulate or copy items in the inventories of blocks (chests, furnaces, etc.) or entities (players or mobs).

## Contents
- 1 Syntax
- 2 Arguments
- 3 Result
- 4 Output
- 5 Examples
- 6 History
- 7 See also

## Syntax
item modify (block <pos>|entity <targets>) <slot> <modifier>Modifies the items in the specified slot with the specified modifier.
item replace (block <pos>|entity <targets>) <slot> with <item> [<count>]Replaces the items in the specified slot with the specified items.
item replace (block <pos>|entity <targets>) <slot> from (block <sourcePos>|entity <sourceTarget>) <sourceSlot> [<modifier>]Copies the source items to the target slot and optionally modifies it with the modifier.
Syntax displayed in various ways



Simplified tree:



item ...
... modify <TARGET> <slot> <modifier>
... replace <TARGET> <slot>
... with <item> [<count>]
... from <SOURCE> <sourceSlot> [<modifier>]
where substituted arguments are:
<TARGET> = (block <pos>|entity <targets>)
<SOURCE> = (block <sourcePos>|entity <sourceTarget>)



Minimised:



/item (modify (block <pos>|entity <targets>) <slot> <modifier>|replace (block <pos>|entity <targets>) <slot> (with <item> [<count>]|from (block <sourcePos>|entity <sourceTarget>) <sourceSlot> [<modifier>]))



Maximised:



item modify block <pos> <slot> <modifier>
item modify entity <targets> <slot> <modifier>
item replace block <pos> <slot> with <item> [<count>]
item replace block <pos> <slot> from block <sourcePos> <sourceSlot> [<modifier>]
item replace block <pos> <slot> from entity <sourceTarget> <sourceSlot> [<modifier>]
item replace entity <targets> <slot> with <item> [<count>]
item replace entity <targets> <slot> from block <sourcePos> <sourceSlot> [<modifier>]
item replace entity <targets> <slot> from entity <sourceTarget> <sourceSlot> [<modifier>]

## Arguments
<pos>: block_pos

Specifies the position of the block to be modified.
Must be ablock positioncomposed of<X>,<Y>and<Z>, each of which must be an integer or atilde and caret notation.
<targets>: entity

Specifies one or more entities to modify.
Must be a player name, atarget selectoror aUUID.
<slot>: item_slot

Specifies the inventory slot to be modified. Valid values depend on whether a block or an entity is being modified.
Must be a string notation that refer to certain slots in the inventory, which consists of "slot type" and optional "slot number", in the format of<slot_type>or<slot_type>.<slot_number>. SeeSlotfor details.
<modifier>: resource_location

Specifies theitem modifierto apply on the chosen item.
Must be aresource location, which is resolved during command execution into unregistered content, or sent to the client to resolve into a client-side content.
<item>: item_stack

Specifies the item to be placed in the block or entity's inventory slot.
It must be in the format ofitem_id{data_tags}(accepts item and block tags), in which data tags can be omitted when they are not needed.
<count>: integer

Specifies the number of items to be placed in the block or entity's inventory slot.
Must be a32-bit integer number (from -2147483648 (-231) to 2147483647 (231-1) ). And it must be between 1 and 64 (inclusive).
<sourcePos>: block_pos

Specifies the position of the block to copy items from.
Must be ablock positioncomposed of<X>,<Y>and<Z>, each of which must be an integer or atilde and caret notation.
<sourceTarget>: entity

Specifies an entity to copy items from.
Must be a player name, atarget selectoror aUUID.
<sourceSlot>: item_slot

Specifies the inventory slot to copy the items from. Valid values depend on whether the source is block or an entity. See<slot>argument above for more information.
## Result















| Command                                           | Trigger                                                                                                                                                                                                                                                                                 | Java Edition |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| Any                                               | The command is incomplete, or any argument is not specified correctly.                                                                                                                                                                                                                  | Unparseable  |
| `/item modify .../item ... from ...`              | The specified`<modifier>`doesn't exist.                                                                                                                                                                                                                                                 | Failed       |
| `/item modify block .../item replace block ...`   | `<pos>`is unloaded or out of the world.                                                                                                                                                                                                                                                 |              |
|                                                   | The block at the`<pos>`is not a container.                                                                                                                                                                                                                                              |              |
|                                                   | The block at the`<pos>`does not have the specified slot.                                                                                                                                                                                                                                |              |
| `/item modify entity .../item replace entity ...` | `<targets>`fails to resolve to one or more entities (named player must be online).                                                                                                                                                                                                      |              |
|                                                   | All selected entities meet one or more of the following conditions:It doesn't have the specified slot (for example, zombies have no horse.armor).<br/>Specified item cannot be placed into the specified slot of its (for example, to place a stone into armor.chest of a player).<br/> |              |
| `/... with <item> <count>`                        | `<count>`exceeds the stack limit of the specified item.                                                                                                                                                                                                                                 |              |
| `/... from block ...`                             | `<sourcePos>`is unloaded or out of the world.                                                                                                                                                                                                                                           |              |
|                                                   | The block at`<sourcePos>`is not a container.                                                                                                                                                                                                                                            |              |
|                                                   | The block at`<sourcePos>`does not have the specified slot.                                                                                                                                                                                                                              |              |
| `/... from entity ...`                            | `<sourceTarget>`fails to resolve to a single entity (named player must be online).                                                                                                                                                                                                      |              |
|                                                   | The`<sourceTarget>`doesn't have the specified slot (for example, zombies have no horse.armor).                                                                                                                                                                                          |              |
| Any                                               | Otherwise                                                                                                                                                                                                                                                                               | Successful   |

## Output




| Command                             | Edition      | Situation  | Success Count | /execute store success ... | /execute store result ...                                    |
|-------------------------------------|--------------|------------|---------------|----------------------------|--------------------------------------------------------------|
| Any                                 | Java Edition | On fail    | 0             | 0                          | 0                                                            |
| `/item (modify|replace) block ...`  |              | On success | 1             | 1                          | 1                                                            |
| `/item (modify|replace) entity ...` |              | On success | 1             | 1                          | the number of entities whose items are successfully replaced |

## Examples
- To replace the items in the bottom-right slot of a single chest two block above with four spruce saplings:
	- /item replace block ~ ~2 ~ container.26 with minecraft:spruce_sapling 4
- To replace the items in the rightmost hotbar slot of the nearest player with four spruce saplings:
	- /item replace entity @p hotbar.8 with minecraft:spruce_sapling 4
- To replace the item in the offhand of the selected player with the item in their main hand:
	- /item replace entity @s weapon.offhand from entity @s weapon.mainhand
- To put a brownbanneron a player's head
	- /item replace entity @s armor.head with minecraft:brown_banner
- To increase the count of the item in your main hand:
	- /item modify entity @s weapon.mainhand example:increase_count
	- file in a data pack:data/example/item_modifiers/increase_count.json{
  "function": "minecraft:set_count",
  "count": 1,
  "add": true
}

