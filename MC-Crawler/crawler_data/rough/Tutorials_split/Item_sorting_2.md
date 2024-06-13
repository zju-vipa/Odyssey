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




