### See also
- Hopper + Item Frame = Item Filter; There is arequest on the official feedback pagefor turning the combination of a hopper and an item frame into a filter.
- Mods/Plugins for simpler sorters:
	- "HopperFilter 2.6" withFuzzyfilter option.
	- "Hopper Filter Vanilla-style Item Filters" with inverted filters (old MC versions only).

## Storage silos
See also: Tutorials/Storage_minecarts § Infinite_storage

































Connected storage silo

1-wide, tileable, expandabletransfer rate: 2.5 ips































Accessible storage silo

1-wide, tileable, expandabletransfer rate: 5 ips
It is sometimes necessary to store items in more than just one chest. Using hoppers, it is possible to store items in hundreds or even thousands of chests. This is usually done with either a connected design or an accessible design.

The connected design should be used when it is necessary to take items from a single output. Any items stored in this silo funnel down as the bottom chest is emptied. Since the chests are not all easily accessible, this is more helpful in automation rather than use by the player. However, if it is not necessary to remove a large number of items, it could work. Silos like this are commonly used to hold fuel, minecarts, and shulker boxes.

The accessible design should be used when the player uses the stored items, not redstone contraptions. When the bottom chest is emptied, only items stored in the adjacent hopper can fill it back up. Since the bottom chest is the only one that can be drained with a hopper, it is impractical to use this for automation. Silos like this are commonly used in combination with sorting systems.

The accessible design is slightly faster than the connected design since the hoppers are in a vertical line. If an item is still in the top hopper after the one below has grabbed another, it puts the item into the chest. If the upper chests become full, however, the speed slows down to the normal 2.5 items per second.

These designs are easily expandable to fit storage needs. The expandable design can easily be tiled upward and to one side, while the connected design can be expanded in all directions. Below are some schematics demonstrating some of these possibilities.


Expanded designs














































This can be vertically extended as much a wanted.


































































































































It can also be horizontally expanded. The section on the right contains 516 slots.



## Special item filters
Special item filters, while similar to item sorters, sort items using unique properties rather than item type and name. They are usually used to sort unstackable items such as armor, shulker boxes, and potions. As item filters do not work with every item type, they may be most useful in combination with item sorters rather than as a standalone.

### Unstackable items






















A










B










C



Unstackable item filter

1-wide, silent, item-safetransfer rate: 2.5 ips
An unstackable item filter can be used to separate unstackable items, such as armor, tools, potions, and enchanted books, from stackable items. This can be useful with mob farms where tools should be separated from everything else.

When an unstackable item enters input hopper A, it unlocks output hopper B. The unstackable item then goes into hopper B to be sorted elsewhere. If a normal item enters hopper A, hopper B remains locked and the item can be outputted from hopper A.

The optional hopper C can prevent valuable items such as shulker boxes and diamond armor from being temporarily stuck in the system. When hopper B is locked, there is usually an item left in it. Hopper C, however, can still pull the items from hopper B. In one of the tileable designs, hopper C is locked with hopper B and cannot do this.

Note that these designs are not overflow protected. Should the storage connected to hopper A fill up, items begin to flow into storage B. An overflow with a tileable design could cause similar issues with adjacent modules.


Tileable designs
The Bedrock Stackable Filter is exclusive to Bedrock Edition. In Java Edition, redstone signals cannot travel down transparent blocks.











A










B

























Tileable stackable filter

1-wide, tileable, silenttransfer rate: 2.5 ips






















A










B










C



Bedrock stackable filter

1-wide, tileable, silent, item-safetransfer rate: 2.5 ips



### Potions and shulker boxes





A








B












C









Special item filter

1-wide, silent, item-safetransfer rate: 2 ips
Note: There is a request on the official feedback page for furnaces to accept only smeltable items in their input slot. This could possibly make them useable as another filter.

This item filter uses certain containers that restrict the kind of items that can enter them. The two containers that do this are brewing stands and shulker boxes. These allows potions and shulker boxes to be separated from other items. This could be handy to sort potions to a storage or shulker boxes to be unloaded.

With this design, items are inputed through hopper A. Any items that are allowed to enter are outputted through hopper B and items that are restricted through hopper C. If a brewing stand is used, potions are allowed to enter the stand and go to output B. If a shulker box is used, shulker boxes are prevented from entering and go to output C.

This design has a circuit delay of 5 ticks, which is slower than the speed of hoppers at 4 ticks. To ensure that every item gets an attempt to be pushed into the container, the input rate must be throttled to at one item per 5 redstone ticks. This could be done with a dropper on a 5 tick clock.

When building, note that the redstone repeater should be on a 3 tick delay. Hopper C is optional as it is used only to make the design item-safe. If using a brewing stand, blaze powder can be pushed into it but not removed. This usually shouldn't be a problem, however it may be desirable to fill the stand beforehand.

