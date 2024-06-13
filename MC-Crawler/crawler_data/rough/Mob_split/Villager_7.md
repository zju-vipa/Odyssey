### Supply and demand
For detailed information on Villager economics, see Trading § Economics.

The price of an item can rise and fall with changes in demand. The price of a traded item can rise when next resupplied, or fall from a risen price if not traded. Demand is stored per item, not per villager.

### Trade offering
Several villagers offering trade items to a player.
When a player holds an item near a villager who wants that item, the villager holds up an item it offers in exchange. For example, a farmer villager who buys 20 wheat for one emerald holds up an emerald, offering it to a player holding wheat. Villagers do not offer trades that are currently out of stock. If the villager has more than one trade for an item, it cycles through the trades, offering a different item every few seconds. This kind of trading interaction makes it easier to find villagers who offer a particular trade, but the player must still open the trading interface to complete the trade. Note that villagers do not hold items to offer trades during their gather or sleep phases, even though it is still possible to trade with them.

### Economic trade
Villagers have levels and require experience to unlock the next tiers of trade; level 1 is a novice, level 2 is apprentice, level 3 is journeyman, level 4 is expert, and level 5 is master. Villagers can resupply trades by themselves by working more at their job site block.

### Popularity or reputation
In Bedrock Edition, villagers increase their prices of trades if a player's popularity is low, (e.g. from damaging villagers), and decrease it if their popularity is high (e.g. from trading with multiple villagers). Curing a zombie villager also increases the player's popularity by 10.

In Java Edition, a villager's prices are affected by the player's reputation with that villager rather than by village popularity.

### Hero of the Village
Main article: Hero of the Village
When a player receives Hero of the Village, players receive discounted prices on all the items traded by villagers in both editions. The Hero of the Village also gets gifts.‌[Java Edition  only] Each villager throws gifts related to its profession, and nitwits and unemployed villagers throw wheat seeds instead. These gifts range in value from common (like seeds) to rare items (like chainmail armor). A player's popularity increases by 10 in Java Edition and doesn't increase in Bedrock Edition. Villagers also shoot off fireworks, with different colored fireworks with no pattern.

## Similar mobs
### Zombie villagers
An example of a zombie villager.
Main article: Zombie Villager
When a zombie kills a villager, it can turn the villager into a zombie villager, depending on the difficulty: 0% chance on Easy, 50% chance on Normal and 100% chance on Hard. Zombie villagers also spawn naturally in the Overworld in the same conditions as a normal zombie, although much less commonly, with a 5% chance. Zombie villagers also spawn in abandoned villages (zombie villages) and igloos. They do not spawn from the zombie monster spawner in Java Edition.

### Wandering trader
A wandering trader.
Main article: Wandering Trader
Wandering traders are passive mobs that spawn randomly close to the player in both editions, or periodically in village gathering sites in Bedrock Edition. Wandering traders also spawn near bells. Two trader llamas spawn leashed to the wandering trader when a wandering trader is naturally spawned, and in Bedrock Edition when summoned or spawned using a spawn egg.

Players may use emeralds to buy items from wandering traders without the need of unlocking the previous trade, but cannot trade items for emeralds. They also lock trades like villagers, but never unlock the trade, nor can they work at any job site blocks. Like villagers, wandering traders are attacked by most zombie variants (though they do not have a zombified form, they die if a zombie kills it, even on hard difficulty), illagers, ravagers‌[Java Edition  only], and vexes. 

Wandering traders also drink a Potion of Invisibility at night (or when they see a hostile mob such as an illager or zombie). They also drink a milk bucket in the morning to remove the Invisibility. They despawn after 40 minutes (even with a name tag or in a minecart or boat) with their llamas.

## Data values
### ID
Java Edition:

| Name     | Identifier | Translation key             |
|----------|------------|-----------------------------|
| Villager | `villager` | `entity.minecraft.villager` |

Bedrock Edition:

| Name           | Identifier    | Numeric ID | Translation key           |
|----------------|---------------|------------|---------------------------|
| Villager (old) | `villager`    | `15`       | `entity.villager.name`    |
| Villager (new) | `villager_v2` | `115`      | `entity.villager_v2.name` |

### Entity data
Villagers have entity data associated with them that contains various properties.

Java Edition:

Main article: Entity format
- Entity data
	- 
	- Additional fields for mobs that can breed
	- 
	- Tags common to all entities
	- 
	- Tags common to all mobs
	- 
	- Tags common to all villagers
	- Inventory: Each compound tag in this list is an item in the villager's inventory, up to a maximum of 8 slots. Items in two or more slots that can be stacked together are automatically condensed into one slot. If there are more than 8 slots, the last slot is removed until the total is 8. If there are 9 slots but two previous slots can be condensed, the last slot returns after the two other slots are combined.
		- An item in the inventory, excluding the Slot tag.
			- 
			- Tags common to all items
	- LastRestock: The last tick the villager went to their job site block to resupply their trades.
	- LastGossipDecay: The last tick all gossip of the villager has decreased strength naturally.
	- RestocksToday: The number of restocks a villager has done in 10 minutes from the last restock, or0if the villager has not restocked in the last 10 minutes. When a villager has restocked twice in less than 10 minutes, it waits at least 10 minutes for another restock.
	- Willing: 1 or 0 (true/false) – true if the villager is willing to mate. Becomes true after certain trades (those that would cause offers to be refreshed), and false after mating.


Villager type
Main article: Villager/DV[edit]


Villager profession
Main article: Villager/DV2[edit]

Bedrock Edition:

SeeBedrock Edition level format/Entity format.

