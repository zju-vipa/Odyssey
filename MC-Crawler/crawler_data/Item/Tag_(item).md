# Tag (item)
Tags and Bits are items exclusive to the 23w13a_or_b April Fools' joke snapshot from 2023. They are used to craft in-game representations of NBT tags.

## Contents
- 1 Obtaining
- 2 Usage
- 3 Trivia
- 4 History
- 5 Gallery
	- 5.1 Renders
- 6 References

## Obtaining
A stonecutter can be used to cut a name tag into either 16 "Name" or 16 "Tag" items. These can be cut into 16 Bit items each.

| Name      | Ingredients | Cutting recipe | Description                                          |
|-----------|-------------|----------------|------------------------------------------------------|
| NameorTag | Name Tag    | 1616           | The resulting "Name" items must be named in ananvil. |
| Bit       | NameorTag   | 16             |                                                      |

To be able to proceed from here the nbt_crafting vote must be approved. Bits can be used in a crafting table to craft Left Curly, Right Curly, Left Square, and Right Square.

A crafting table can be used to convert a "Tag" item into a "Byte Tag." The amount of sticks added to the crafting recipe specifies the value of the Byte, as a signed 8-bit value. For example, a "Tag" and a full stack of sticks make a Byte with the value 64b, while 255 sticks result in -1b. Only one of the sticks is consumed. Two Bytes can be crafted into a "Short Tag" (equivalent to 16 bit), two Shorts into an "Int Tag" (equivalent to 32 bit), and two Ints into a "Long Tag" (equivalent to 64 bit). Many other combinations that form either 16, 32, or 64 bit are possible. For example, two Shorts and an Int make a Long. When combining values, their digits are stuck together in the given order, e.g. 1b and 0b make 256s (equivalent to 010016 in hexadecimal). Undoing any of these crafting actions in e.g. a stonecutter is not possible.

"Float" and "Double Tags" can be crafted by adding one or two boats to any numeric tag. A "String Tag" is crafted with a "Tag" and a piece of string.

| Name                                               | Ingredients                                    | Crafting recipe | Description                                                                                                                                   |
|----------------------------------------------------|------------------------------------------------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Right CurlyorLeft CurlyorLeft SquareorRight Square | Bit                                            |                 |                                                                                                                                               |
| String Tag                                         | Tag+String                                     |                 | String tags must be named in ananvilto set their value.                                                                                       |
| Byte Tag                                           | Tag+Stick                                      | 6463            | Only 1 stick is consumed. 128 and more sticks maketwo's complements:128 sticks = -128b 129 sticks = -127b ⋮ 254 sticks = -2b 255 sticks = -1b |
| Short TagorInt TagorLong Tag                       | Byte Tag                                       |                 | Shorts and Ints can be combined the same way, even mixed.Digits are appended, e.g. two 1b tags make 257s (010116 in hexadecimal).             |
| Float Tag                                          | Byte TagorShort TagorInt TagorLong Tag+AnyBoat |                 |                                                                                                                                               |
| Double Tag                                         | Byte TagorShort TagorInt TagorLong Tag+AnyBoat |                 |                                                                                                                                               |
| Compound Tag                                       | Left Curly+Name+Byte Tag+Right Curly           |                 | Instead of Bytes any other tag can be used, including other compound tags.                                                                    |
| List Tag                                           | Left Square+Byte Tag+Right Square              |                 | Instead of Bytes any other tag can be used, including other list tags.                                                                        |
| Compound TagorList Tag                             | Compound TagorList Tag                         |                 | Up to 9 can be combined.When compound tags contain identical names, only the latest of the corresponding values is used.                      |

"Name" and "String Tags" must be named in an anvil before they can be used. Unnamed Names and Strings always produce a "Sssyntax Error". None of the other tag items can be named.

All these items can be combined in a crafting table to form a short sequence of JSON code, as long as the resulting syntax is valid. For example: 

- A pair of Curlies that enclose a named "Name" item and some value, e.g. a Byte, create a "Compound Tag" with the content{Example:0b}.
	- Because of the limited size of the crafting table only 3 name-value pairs can be put between Curlies at a time. Compound Tags of any length can be created by concatenating two or more Compound Tags.
	- An empty pair of Curlies produces an empty Compound Tag with the content{}.
- A pair of Square brackets that enclose any number of values, e.g. 7 Bytes, create a "List Tag" with the content[0b,0b,0b,0b,0b,0b,0b].
	- Because of the limited size of the crafting table only 7 values can be put between Square brackets at a time. List Tags of any length can be created by concatenating two or more List Tags.
	- An empty pair of Square brackets produces an empty List with the content[].
	- "Name" items cannot be used in a List.

The resulting Compound and List Tags can be used as values in other Compound and List Tags, as deeply nested as you want.

## Usage
Tags appear to have no further functionality. They cannot be eaten or placed in the world, except in an item frame, as each other item can. However, Compound Tags with values like {Enchantments:[{id:"minecraft:sharpness",lvl:127b}]} will show the enchantment glint and actually act accordingly when used.[1] This appears to work with many weapon and tool enchantments.

In theory, an extremely lucky replace_recipe_output vote can change the crafting recipe for compound tags to output something else. When cheats are enabled you can test this with a command like /vote rule minecraft:replace_recipe_output approve {key:"minecraft:compound_tag",value:"minecraft:netherite_sword"}. However, as long as this vote is approved no other compound tag can be crafted. Use /vote rule minecraft:replace_recipe_output repeal * to undo all recipe replacements.

In combination with the midas_touch vote tag items can be converted into gold ingots. These retain their NBT data. When the world is loaded in another version of the game tag items disappear, but gold ingots persist.

