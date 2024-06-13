# Tutorials/Hopper
The hopper is a redstone component that can be used to manage items.

## Contents
- 1 Automatic smelting
- 2 Item sorter
	- 2.1 Storage
	- 2.2 Overflow protection
	- 2.3 Item transportation
	- 2.4 Variations
	- 2.5 Hybrid design
		- 2.5.1 Resource optimized hybrid (OH)
			- 2.5.1.1 OH type III
			- 2.5.1.2 OH type IV
			- 2.5.1.3 OH type V
		- 2.5.2 Hybrid with Bedrock Edition
	- 2.6 See also
- 3 Storage silos
- 4 Special item filters
	- 4.1 Unstackable items
	- 4.2 Potions and shulker boxes
		- 4.2.1 Alternate version
- 5 Hopper clocks
- 6 Item counter
- 7 See also
- 8 References

## Automatic smelting





A


B









C





Basic auto smelter

1-wide, tileabletransfer rate: 0.1 ips
Main article: Tutorials/Automatic smelting
To make the smelting process more efficient, it is possible to use hoppers to ensure a furnace is never left empty. In the shown schematic, chest A is for items such as uncooked meat, chest B is for fuel such as coal, and chest C holds the output. Since furnaces can hold fuel without a chest, chest B and its hopper are unnecessary. This type of system also works with the smoker and blast furnace.

As furnaces retain experience when items are removed by hoppers, multiple of these can be run for an extended period of time to make an experience farm. When one item is removed from a furnace, all experience is received immediately.

Using a hopper system like this greatly speeds up the process of smelting large numbers of items. Should it become necessary to smelt an even larger number however, it is possible to link multiple modules to create what is commonly called a "furnace array." These vary in size and can range from small to using close to a hundred furnaces.

| 23 Furnace Array (view on YouTube) |
|------------------------------------|
|                                    |

## Item sorter
















































Basic hopper item sorter
Hopper I contains 41 diamonds, which represent the item being sorted, and 4 cheap items stackable to 64 in the other slots. Renaming the 4 items is recommended.
41

1-wide, tileable, silentsimple overflow protectiontransfer rate: 2.5 ipsBOM = 10 RSD (lavish)
An item sorter example made from the "compact" design (no overflow protection, etc.)
An item sorter is a type of redstone mechanism that can be used to filter specific items into chests. They generally work using two hoppers, as shown in the schematic. The top hopper is filled as shown under the image. The hopper underneath is powered so that it cannot remove items from the top. The top hopper must be pointed away from the bottom hopper, otherwise it pushes items into the bottom hopper. When enough items fill the top hopper, the bottom hopper is unpowered so that it can remove the extra items. Note that some method of passing the items to be sorted along the top of a sorter chain may be necessary: this can be done with another hopper pipe transporting items over the top, or with water/ice streams.

This design relies on the fact that, inside of Minecraft's code, hoppers search for an item to be taken from the input side before outputting an item to another container.  This results in the bottom hoppers taking the filtered item(s) before the items currently running through the storage system are passed over to the next hopper.  However, because hoppers have a 0.4 second cooldown after transferring an item, bear in mind that both the input and output activate should there be more than 1 item available to pass. For example, if 2 iron ingots were in the same hopper, 1 of them would get taken by the hopper beneath, while the second one would get outputted to the side and continue along the sorting chain.

### Storage
Usually chests are placed sideways to the right of the bottom hopper. Additional hoppers can be added below or to the right of the bottom hopper to attach more chests. The bottom hopper is the only one that needs to be powered (though one immediately below it would also be powered by the redstone torch), so as many hoppers and chests as necessary can be added.

At the end of an item sorter, there is usually a chest to catch any items that didn't get sorted for some reason. This is helpful in case a valuable tool or such is accidentally dropped in. If a chest becomes full, it can also prevent the loss of items of that type. Sometimes large farms' storages use lava instead to prevent a buildup of items should the storage completely fill up.

### Overflow protection
See also: Hybrid designs with better inherent overflow protection (through circuit isolation).

When multiple sorters are tiled directly next to each other, it is usually desirable to have overflow protection. In an overflow safe sorter, even if the topmost hopper has filled up due to an "overflow," the redstone signal strength isn't great enough to interfere with adjacent sorters. In the sorter shown, 1 full stack of items and 4 junk items produce a signal strength of 3. This is just strong enough to unlock the bottom hopper without affecting adjacent hoppers. If the signal strength were to get up to 4 however, the adjacent hoppers would be unlocked causing the whole system to break down.

The first slot of the input hopper should contain the item being sorted out. The other slots should contain items that never go through the system. Named sticks, dirt, and cobblestone are all common 'junk' items used for this purpose. Only one junk item should be placed in each slot. Otherwise, the sorter does not have ensured overflow protection.

If such named 'junk' items accidentally get into the sorter anyway this simple overflow protection has no value, but hybrid designs remain protected.

Tip: Use named "junk" items in the first sorter row/tile to sort out normal un-named junk items of the same type. This way you can safely use that normal junk item in all other sorter rows. Add a safety overfill detector on the storage container attached to that first sorter that disables the input for the entire sorter for an additional layer of security.

It is possible to remove the center column of blocks from this "basic" sorter design. However, doing so turns it into the "compact" variation without overflow protection. If the input hopper fills up, it has a signal strength of 3, which unlocks adjacent hoppers.

