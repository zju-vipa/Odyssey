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

### Item transportation
There are multiple methods that can be used to carry items across the input hopper to potentially be picked up. The methods most frequently used are hopper pipes, item streams, and minecarts with chests or minecarts with hoppers.

A hopper pipe is simply a chain of hoppers all pointing at each other in a continuous line. This requires extra iron and may cause consistent lag on large scale. Another limitation in Bedrock Edition is that hopper pipes transferring a full load at full speed (for example, continuously moving items that have been stacked in an input chest) pushes a small percentage of items past filters without allowing them to be sorted.[1]

Item streams, on the other hand, are made by running water over the hoppers and dropping items into the flow with a dropper. Whenever the stream grows too weak, ice and blocks that stop water flow but not moving entities (such as signs, open fence gates, top slabs/trapdoors, buttons, etc.) are used to carry items across the breaks. This is a cheaper method, provided Silk Touch has been obtained. However, while items are flowing through the system, it may generate more lag than using hoppers. Additionally, if too many items move past a filter at one time there is a chance for items to skip over and not be sorted. Hoppers also have a collection cooldown that limits them to collecting only one group of items every 8 game ticks.

Chest-minecarts and hopper-minecarts can be used to deliver items to filter hoppers by moving them across rails on top of the filter hoppers. This method of delivering items is reliable but also typically much slower than hopper pipes or items streams.

### Variations
A couple of variations of the standard overflow-protected design exist that either sacrifice the overflow protection or require some input method other than a hopper pipe.

If you are looking at variations that are not overflow-proof because they hold back fewer of the sorted item, you may want to consider one of the hybrid designs with inherent overflow protection instead.


Show variations






















































Double-speed hopper item sorter
Top hopper contains 41 diamonds, which represent the item being sorted, and 4 cheap items stackable to 64 in the other slots. (Renaming the 4 items is recommended.)
Hopper below that contains a full stack of the item being sorted and 4 cheap different items. Those items can be anything that isn't being used in the top hopper.
41
64

1-wide, tileable, silentsimple overflow protectiontransfer rate: 5 ipsBOM = 10 RSD








































Compact hopper item sorter
Hopper I contains 1 diamond, which represents the item being sorted, and 21 cheap items stackable to 64 in the other slots. (Renaming the 21 items is recommended.) If sorting items that stack to 16 rather than 64, use only 15 cheap items instead.
18

1-wide, tileable, silentno overflow protectiontransfer rate: 2.5 ipsBOM = 9 RSD



### Hybrid design



































































Hybrid sorter "h-B"  redstone delay = 4



































































Hybrid sorter "h-A"  redstone delay = 3
A hybrid sorter
To use only one item in a sorter with overflow protection, total isolation of the circuit is required. To achieve this you can use a hybrid solution.
If you combine designs "h-A" and "h-B" (in ABABAB... configuration) then you get an item sorter with better overflow protection, because the signals are completely isolated from each other and never interfere with adjacent tiles.

** Specs **
- The top Hoppers contain only 1 diamond, which represent the item being sorted, and 21 cheap items stackable in the other slots. (Renaming the 21 items is recommended.)18
- 1-wide, tileable, silent, transfer rate: 2.5ips.
- overflow protected only with part "h-A" and "h-B" mixed in alternating order.

** BOM for a set ("h-A" + "h-B") **
- 3 comparators
- 2 repeaters
- 2 redstone torches
- 6 redstone dust

(= 23 RSD)

#### 
Note that types I-IV below are prone to redstone torch flicker burnout in Java 1.18+ when used in a storage sorting setting (with a steady stream of 2.5 item per second). The burnout may cause all the filter items to drain, breaking the sorting. The issue is not present on Bedrock due to different torch burnout mechanics and is unlikely to manifest in Java in a farm setting (since farms rarely provide a steady stream of items).

** Some Specs of type I / II **
- BOM: 12 redstone torches + 7, 8 or 10 dust.
- complete circuit isolation -> overflow protection.
- support for a sorter main on/off circuit.


OH type I and II

OH type I













M



























































M














M





Optimized hybrid sorter "oh-B"  redstone delay = 4













M



























































M














M

M



Optimized hybrid sorter "oh-A"  redstone delay = 4
Specs
2/64 filter- plus 20 cheap items or 2/16 filter- plus 14 cheap items.  217 or 211
1-wide, tileable, silent, transfer rate 2.5 ips.
better overflow protection only when circuits "oh-A" and "oh-B" are mixed in alternating order (complete circuit isolation).
BOM for a set ("oh-A" + "oh-B")
2 comparators
6 redstone torches
10x redstone dust
(= 22 RSD)

Notes
The two unconnected "floating" solid blocks in circuit "oh-A" are required to keep both circuits isolated.
The stone slabs can be replaced with normal solid blocks.
The (redstone) components marked with an M on top, below and on the right of the hoppers are part of an optional main on/off circuit for the whole sorter array. It disables/enables all output hoppers on the bottom and the hopper transport pipe on top regardless of the individual sorter states. Useful for debugging, maintenance, changing the contents of the filter-hoppers and freezing the sorter mid-operation (mostly).
(improved by Nilbadimo)

OH Type II
























































²







Optimized hybrid sorter II "oh2-A" v2  redstone delay = 4 (3-6)  saves another redstone dust but master on/off circuit can't be added.











































M








²





M

M



Optimized hybrid sorter II "oh2-A"  redstone delay = 4 (3-6)



































²







M














M





Optimized hybrid sorter II "oh2-B"  redstone delay = 4 (3-6)
Specs
See Type I design above.

BOM for a set ("oh2-A" + "oh2-B")
2 comparators
2 repeaters
2 redstone torches
5 or 6 redstone dust
(= 19 or 20 RSD)

Notes
See Type I design above.



##### OH type III






















P¹






-



F










O



















P²





Optimized hybrid sorter III "oh3-B"  redstone delay = 4 
Only works as advertised if and only if combined with at least one "oh3-A" on one or the other side.
Note: The comparator is in subtraction mode.
























P¹










F










O






²












P²





Optimized hybrid sorter III "oh3-A"  redstone delay = 4 (3-6) 

Same as the "Compact" Variation
** Specs **
- 2/64 filter- plus 20 cheap items or 2/16 filter- plus 14 cheap items.217or211
- 1-wide, alternating tileable, silent, transfer rate 2.5ips.
- better overflow protection only when circuits "oh3-A" and "oh3-B" are mixed in alternating order (see notes below).

** BOM for a set ("oh3-A" + "oh3-B") **
- 2 comparators
- 1 repeater
- 4 redstone torches
- 4 redstone dust

(= 17 RSD, which is less then a set of two "compact" ones!) 

** Setup **
When initializing such a sorter array any "oh3-B" filter-hopper (F) can be be filled with filter and filler items only after at least one neighboring "oh3-A" has already been initialized. The "oh3-B" comparators need the adjacent comparators to output at least a power level of one to keep their own output-hoppers (O) locked and thus from puling the filter+filler from the filter-hopper (F).

** Notes **
- The composter on top of thehopper pipe(P¹) is there to reduce server load / lag (the hopper doesn't search the environment for collectable items, just the composter).
- Same goes for the furnace above the darkened second hopper pipe (P²). It's advised only if another sorter line is actually constructed below. Can be replaced with a normal solid block otherwise. (It's possible to stack three sorter lines of this making and reach all output chests from the same walkway.)
- The stone slabs can be replaced with normal solid blocks.
- Overflow: When a "oh3-A" sorter row/tile overflows it disables/locks the two adjacent "oh3-B" sorter tiles. They can still pull up to 62 items from the hopper transfer pipe but they cannot put those items into each corresponding storage until the overflow situation is fixed.But the overall sorter setup stays intact(no spreading chaos, filters stay working, etc.). -> The tiles are not completely isolated from each other but they only interact in a safe way (locking adjacent hoppers instead of unlocking them).
- A total redstone delay of 4 in each sorter row/tile ensures that the filtering hopper's comparator stays at the activation level while it's processing a stream of items and doesn't flip between active and inactive. In other words: The output-hopper (O) doesn't pull items from the filter-hopper until the later one is ready to pull a next item from the hopper pipe above (thus keeping a stable amount of 2+1 filter/to-be-sorted items in the filter-hopper). This reduces lag(?).

##### OH type IV
by r/Agantas























F










O

























Optimized hybrid sorter "oh4-B"






















F










O

























Optimized hybrid sorter "oh4-A"
** Specs **
- 2/64 filter- plus 20 cheap items or 2/16 filter- plus 14 cheap items.217or211
- 1-wide, alternating tileable, silent, transfer rate 2.5ips.
- The A/B tiles are completely isolated and can be used independently from each other.

** BOM for a set ("oh4-A" + "oh4-B") **
- 2 comparators
- 1 repeater
- 2 redstone torches
- 5 redstone dust

(= 14 RSD)

##### OH type V
by r/Agantas



























F












O





























Optimized hybrid sorter "oh5-B"


























F












O





























Optimized hybrid sorter "oh5-A"
** Specs **
- 2/64 filter- plus 20 cheap items or 2/16 filter- plus 14 cheap items.217or211
- 1-wide, alternating tileable, silent, transfer rate 2.5ips.
- The A/B tiles are completely isolated and can be used independently from each other.
- Works in Java 1.18+ (no torch burnout since all torches are protected by repeaters). Also works in Bedrock!
- Can be setup for double hopper speed (5ips).

** BOM for a set ("oh5-A" + "oh5-B") **
- 2 comparators
- 3 repeaters
- 2 redstone torches
- 6 redstone dust

(= 23 RSD) 

** Notes **
- The unconnected "floating" solid block in circuit "oh5-A" is required to keep both circuits isolated.
- The glass block in "oh5-B" can be replaced with a top slab or even a regular solid block, but glass provides the easiest way to check that everything is configured properly.
- If you make the double speed version where you point the filter hopper down, have a full stack of items stuck in the first slot of the hopper below the filter and a different type of filler item in slots 2-5. Even 5 items stuck in the first slot of the filter hopper isn't safe for the double filler. 18 items in first slot is lag-safe, but it is somewhat overkill. Since the amount of items leaked due to lag is inconsistent, it is better to be safe than sorry.

#### Hybrid with Bedrock Edition
When using Dark Altair's design on the Bedrock Edition, you might have issues with the 21 non filter items in Item Sorter Part B. With 21 items the hopper tends to run the 1 item filter trough as well. 

In order to make it work you should put 20 non filter items in. This way you sometimes get 2 filter items, but generally it drains to 1 filter item. 

Part A = 21 non filter items
Part B = 20 non filter items
** Hybrid and items with stacks of 16 **
In order to have only 1 filter item when storing items that stack till 16, you need to decrease the number of non filter items.

Part A = 15 non filter items
Part B = 14 non filter items
Below here is a link to a video that shows the use of this design on Bedrock Edition and with stacks of 16.




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

#### Alternate version



























































Special item filter

(back layer)





A









































B

C









Special item filter

(front layer)2-wide, item-safetransfer rate: 2.5 ips
This hopper-speed version does not require an additional step to slow down the input stream. It comes from a video by ilmango about potion sorting. Inputs and outputs work the same way as in the 1-wide design. The input stream is fed into a dropper facing the brewing stand or shulker box, while a comparator circuit triggers the dropper and the locking and unlocking of hoppers.


## Hopper clocks
Main article: Clock circuit § Hopper clocks

























Delayed hopper clock
flat, silentclock period: 40 ticks to 256 seconds 

Five stacks of items are in the leftmost hopper.

















Looped hopper clock
flat, silentclock output: 4 ticks on, 12 ticks offclock period: 16 ticks

1 item is in one of the hoppers.
Hoppers are commonly used to create clocks and delay circuits. Since items can travel back and forth between two hoppers, this is an easy way to make a clock. It is more iron intensive, however.

The looped hopper clock works by having an item traveling in a "loop" between the four hoppers. Whenever the comparator detects the item in a hopper, it turns on. This clock can be adjusted by adding or removing hoppers and items.

The delayed hopper clock works by taking turns completely emptying each hopper. When the hopper on the left completely empties, the redstone torch turns on and the other hopper begins emptying. Note that exactly 5 stacks of items must be used with this design. To decrease the clock speed, use fewer stackable items. "Delayed hopper clock origin"


## Item counter























































Item counter 

1-widetransfer rate: 1.25 ipssize: 1×5×4
This is a mechanism that outputs a short redstone signal for every item that goes through the dropper. The mechanism slows down the items moving through the dropper and the hopper above to make the outputs comfortable to use for counting mechanisms.

The output of this counter can be used in combination with a counting mechanism such as the scoreboard command in a command block.


