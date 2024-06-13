#### Collecting items
A hopper collects items dropped on top of it if the space above the hopper not occupied by a storage block, as well as items landing inside the hopper block itself, regardless of the block above. Items are gathered from the entire 1 block space above the hopper, meaning that items sitting on partial blocks such as soul sand directly above a hopper can be collected.[1] It is also possible for a hopper to collect items from inside a full, solid block, a situation that might come from items rising up through solid blocks or being summoned. Item entities are not collected when they are outside of the collection area however; for example, items on top of a stone block directly above a hopper are not collected. Collected items are placed in the leftmost empty slot of a hopper's inventory.

In Java Edition, if there is no container above the hopper, then the hopper collects dropped items in the order in which they landed on the hopper. This order is remembered even while a hopper is locked. For instance, if a hopper is locked under a carpet while a fully equipped armor stand is broken above it, then it always collects items in this order when it is unlocked: armor stand, boots, leggings, chestplates, helmets. This is due to the order in which these items land.[verify] In Bedrock Edition, hoppers do not remember the order in which items land on the hopper. Instead, hoppers with multiple dropped items above them collect the items in the order in which they entered the chunk in which the hopper is located. Items that drop from a broken armor stand are collected in a random order.[2]

Hoppers usually check for dropped items every game tick and they can collect items even before they are picked up by a player[verify] or destroyed by lava. However, in Bedrock Edition hoppers have a "collection cooldown" time. After collecting an item (or stack of items), a hopper waits 4 redstone ticks (0.4 seconds, barring lag) before attempting to collect again.

Hoppers collect groups of items all at once rather than collecting them as single items one at a time. As a result, hoppers can collect item entities much faster than they can pull items from a container. Pulling from a moving minecart with chest or minecart with hopper is even slower, since the minecart is not always above the hopper.

#### Pushing and pulling items
A hopper with a storage container above it (such as a furnace, chest, dropper, composter, or another hopper) attempts to pull from the container instead of checking for floating items above it, and hence can not collect dropped items. A hopper always tries to push or pull items using the leftmost available slot. When a hopper is removing items from a chest, the items disappear from left to right. Similarly, when filling up a chest, the chest fills up from left to right. Hoppers prioritize pulling from the first slot of a container over pulling into the first hopper slot. If a hopper has stone in its first slot and nothing in its second while the container it is pulling from has chicken in its first slot but stone in the second, the hopper pulls the chicken from the first slot of the container into its empty second slot. However, if the hopper is unable to pull the chicken, such as if all slots are filled with stone, the hopper pulls the stone from the second slot of the container instead. Similarly, hoppers prioritize pushing from their first slot over pushing into the first slot of a container. If a hopper has stone in its first slot and chicken in its second while the container it is pushing to has chicken it its first slot but stone in the second, the hopper pushes stone from its first slot into the second slot of the container.

In Java Edition, the checks done by a hopper while pulling generally require less processing than the checks done by a hopper attempting collection. Therefore, a chain of hoppers topped with storage containers rather than air/solid blocks has better performance (measured as milliseconds of processing per tick) and lower potential for processing lag. [3] The performance improvement achieved is correlated with the number of storage slots the container has. Placing composters (with no storage slots but still with custom output logic) on top of hoppers provide the greatest efficiency‌[until JE 1.20.5], while double chests actually degrade performance, even when sharing each double chest across two hoppers.[3] In Bedrock Edition, a chain of hoppers with air or non-container blocks on top has better performance than a chain of hoppers topped by container blocks.[4] This may be because, even though hoppers with containers on top do not check for items, they do check for hopper-minecarts and chest-minecarts to pull from, and that involves scanning the chunk entity list.[5]




A






B


Push then pull

Chest A is full of items while the hopper and chest B are empty.
Item pushes and pulls are processed in the same game tick, but pushes are processed before pulls. In the schematic, the empty hopper first pulls an item from chest A as it cannot push anything into chest B. After the cooldown, the hopper first pushes its item into chest B before pulling another item from chest A, both pushing and pulling in the same tick, and the process repeats. The hopper stops pulling when A is empty, and stops pushing when B becomes full.

Hoppers also have a "transfer cooldown" time. After pulling and/or pushing items, a hopper waits 4 redstone ticks (0.4 seconds, barring lag) before pulling or pushing again (a transfer rate of 2.5 items per second, barring lag). A hopper that has an item pushed into it from another hopper also starts a 4 tick cooldown period, regardless of whether it pushed or pulled items itself. Item entities can be collected at any time without affecting the transfer cooldown time. The transfer cooldown and the Bedrock Edition collection cooldown are independent of each other.

