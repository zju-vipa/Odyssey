### Picking up items
Each villager has eight hidden inventory slots, which start empty whenever the villager is spawned. A villager can fill all 8 of its inventory slots with any set of items, which can be all the same, all different, or any other combination of items.

The villager does not intentionally seek out items to pick up, but it does collect any bread, carrots, potatoes, wheat, wheat seeds, beetroot, beetroot seeds, torchflower seeds, pitcher pods, and bone meal which happen to be in range. The listed items are the only items villagers can pick up, although the the /item replace command can put any arbitrary item into a villager's inventory. Also, bone meal can only be picked up by a farmer villager.

If a player and a villager are in the pickup range of an item at the same time, the player always picks it up first. If several villagers are next to an item, the same one picks up the item every time. This behavior prevents villagers from effectively sharing food (and thus breeding) in a small space.

When killed or converted to a zombie villager, any inventory item of the villager is lost, even when /gamerule keepInventory is set to true.

If /gamerule mobGriefing is false, villagers cannot pick up items, and farmer villagers cannot plant or harvest crops.

Like other mobs, villagers have four slots for worn armor, separate from their inventory slots. An adjacent dispenser can equip armor, elytra, mob heads or carved pumpkins to a villager, but the armor is not rendered (except for carved pumpkins and mob heads). The equipment functions as normal; for example, a villager wearing an armor piece enchanted with Thorns can inflict Thorns damage to attackers, and a villager wearing Frost Walker boots is able to create frosted ice. If a villager is converted into a zombie villager, the armor it was wearing is dropped, though it may be able to pick it up and equip it again.

### Sharing food
Villagers sharing carrots.
In Java Edition, villagers collect bread, carrots, potatoes, beetroots, wheat seeds, beetroot seeds, and wheat. If a villager has at least 24 of these items, it gives the extra amount to a villager with 4 or fewer of each these food items. That other villager can also do this until all villagers have shared all items they could (for example, on a group of three villagers one receives 60 bread, then it shares 36 to another villager to keep 24[3], and that same villager then shares 12 to the third villager).

In the case of wheat, villagers have a rather distinct behavior. They do the same as other crops, but if a villager has at least 32 wheat, it tries to give half of it to another villager, making both have 16 wheat.

If a villager has 8 full [more information needed] stacks of any kind of food or seeds and then tries to share with another villager, it will leave at least 24 items in each stack. Thus it can never really empty its inventory down to 0 and clear a slot to pick up other stuff, unless it uses the items when trying to breed or when farming if it is a farmer villager.[4][5] A bait villager can be used in a farm taking advantage of this mechanic to have a farmer villager collect and deposit crops.

In Bedrock Edition, if a villager has enough food in one inventory stack (6 bread or 24 carrots, potatoes, beetroots, or 18 wheat for farmers only) and sees a villager without enough food in one inventory stack (3 bread, 12 carrots, 12 potatoes, or 12 beetroots for non-farmers; 15 bread, 60 carrots, 60 potatoes, or 60 beetroots, or 45 wheat for farmers), the villager may decide to share food with that villager.

To share, a villager finds its first inventory stack with at least 4 bread, carrots, potatoes, or beetroot or with at least 6 wheat, and then throws half the stack (rounded down) in the direction of the target villager. When wheat is shared, it is first crafted to bread, which may result in 1 or 2 less than half the stack being shared.

### Farming
Farmer villager picking and planting carrots.
In Java Edition, during the "work" portion of their schedule farmers tend nearby crops. 

- Farmers sometimes move to randomfarmlandblocks they detect within ±4 on the X and Z axes and ±2 on the Y axis, rather than going to their jobsite.
- If there are fully-grown crop blocks or air above farmland within ±1 of the villager on each axis, the farmer spends 10 seconds tending them (not counting time spend walking to the next block), one per second. The block is harvested if necessary and (re-)planted if the farmer has any seeds.
	- If/gamerule mobGriefingisfalse, villagers cannot farm.
	- Harvesting is done regardless of the villager's current inventory, even if they lack space to pick up the results.
	- Planting is done as from the first eligible inventory slot.
- If there is at least one non-fully-grown crop block within ±1 of the farmer on each axis, the farmer hasbone meal, and it has been at least 8 seconds since the farmer last did some fertilization, then the farmer fertilizes up to four crop blocks (one every two seconds).
- When the farmer works at their composter, it composts excess wheat and beetroot seeds, and extracts bone meal if it is full. Up to 20 seeds are composted in one work session, but at least 10 of each type of seed are first kept. Inventory slots are checked in reverse order.

In Bedrock Edition, farmers tend crops within the village boundary. Villagers far enough outside the boundary of any village also tend nearby crops. Farmland to be tended is found by seeking for certain blocks up to 9 blocks away from the villager in the X and Z coordinates and up to 1 away in the Y coordinate (a 19×19×3 volume total).

- If a farmer villager does not have enough food in one stack in its inventory (15 bread, 60 carrots, 60 potatoes, 60 beetroots, or 45 wheat) and finds fully-grown wheat, carrots, potatoes, or beetroot, the villager moves to the crop block and harvests it.
- If a farmer villager has any seeds, carrots, potatoes, or beetroot seeds in its inventory and finds an air block above farmland, the villager moves to it and plants a crop. They always plant from the first eligible slot in their inventory.
- Farmer villagers use and pick upbone meal. They also fill theircomposterwithseeds.
- Farmer villagers start farming only if a crop is planted on farmland previously.
- Farmer villagers continue to plant on the farmland even if all crops are destroyed.

For both editions,

- Farmer villagerscannotturndirt,grass blocks, ordirt pathsinto farmland, nor they pick up any hoes to till the blocks.
- If a hoe is placed into a farmer villager's mainhand or offhand via commands, they still cannot till any blocks.
- Farmer villagers often share their crops and food with other villagers if they have any extras.

