### Honeycombs
When a dispenser collects honey from a beehive or bee nest with shears in its inventory, 3 honeycombs are produced and the shears inside the dispenser lose 1 point of durability. In Java Edition the honeycombs are spawned inside hive block and can be collected by a hopper beneath the hive, while in Bedrock Edition they are produced at the edge of an adjacent block even if solid.

The dispenser should be filled with as many shears as possible to maximize the time the system can operate before refilling. You could even set up a way to automatically restock the dispenser with shears when the durability runs out. 

These schematics show a 1-block wide setup to activate a dispenser above the hive and collect the honeycombs with a hopper. A honey block indicates the bee hive or nest, with its front to the left.
























X






P








Java version. Hopper P represents a pipe connecting to centralized storage, although you could do that directly from hopper X if not combining with the honey farm below.





























X








P








Bedrock version. Hoppers "front" and "back" of hopper X may catch additional drops. You could instead put the pipe at X if not combining with the honey farm below.

The dispenser is triggered every time the honey level changes, to no effect if the hive is not yet full. Various other redstone mechanism components may be used in place of the trap door.

If the hive has become full and the dispenser has run out of shears, even after being resupplied it does not harvest the hive. In this case the trap door may be manually toggled to restart the farm.

Other designs, using comparators rather than observers:

- A 1-block wide setup that activates a dispenser above a beehive when it is ready for harvest.
- A 1-block wide setup that collects honeycombs and eject them into the same space the bees occupy, to be collected from below.

### Honey bottles
When a dispenser collects honey from a beehive or bee nest with a glass bottle in its inventory, a honey bottle is placed into its inventory. In order to extract the honey bottles from a dispenser in a lossless fashion, the best way to do so is to set up an item sorter underneath the dispenser to collect only honey bottles. 8 of the 9 slots of the dispenser should be filled with as many glass bottles as possible, leaving at least one space empty for the honey bottles. The more glass bottles that are loaded into the dispenser, the longer this system can run without restocking.  Naturally once you pick up the honey bottles, you can craft them into honey blocks, thus freeing up the bottles for reuse.

This schematic shows a 1-block wide setup that collects honey using a dispenser and extract the honey bottles with an item sorter. A honey block indicates the bee hive or nest, with its front to the left.


















































A








P





















Hopper A must have one honey bottle in the first slot and 15 junk items (something that stacks to 64) spread across the remaining slots. Hopper P represents a hopper pipe connecting to centralized storage.

The design also has one non-obvious failure state — if a hive becomes full and the dispenser has run out of bottles, even after being resupplied it does not harvest the hive. The solution here is to break and replace a piece of redstone dust on the hive's top-layer trail. This interrupts the comparator's signal and allows the dispenser to trigger on the full hive.  

Other designs:

- 1-block wide setup that activates a dispenser once a beehive is ready for harvest
- A 1-block wide setup that collects honey using a dispenser and extract the honey bottles with an item sorter
- 1-block wide setup that stores empty bottles in a dropper next to the dispenser. This negates the need for an item sorter

Note: Tiling the design as shown in the final two gallery images make the dispensers inaccessible — the grass block in front of the dispenser must be replaced with a slab, fence, or trapdoor so the dispenser can be refilled with empty bottles. The top hopper in each row must be set up with 2 honey bottles in the first slot, and 11-13 "junk" items (stackable to 64) spread across the other slots. As honey is collected, one bottle is kept in the lower hopper, but bottles after that are passed on to the output.  

### Videos
| Design 1 (view on YouTube) |
|----------------------------|
|                            |

| Design 3 (view on YouTube) |
|----------------------------|
|                            |

| Design 4 (view on YouTube) |
|----------------------------|
|                            |

| Design 5 (view on YouTube) |
|----------------------------|
|                            |

| Design 6 (view on YouTube) |
|----------------------------|
|                            |

| Design 7 (view on YouTube) |
|----------------------------|
|                            |


