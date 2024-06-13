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



