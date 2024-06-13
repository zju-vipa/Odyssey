## Drops
- Amilk bucket(8.5% chance, increased 1% per level ofLooting) if killed while holding or before finishing drinking.
- Apotion of invisibility(8.5% chance, increased 1% per level ofLooting) if killed while holding or before finishing drinking.

A wandering trader is also a source of leads, as it typically spawns with two leashed trader llamas. These leads break and drop (at the location of the llama) if either trader or llama dies or if they are separated.

Separating mobs upon leads have the connection broken, dropping the leads if they enter boats for example.  Unless they enter the same boat at the same time, every lead is always broken if at least one moves into a boat.

Wandering traders do not drop any loot when they despawn.

Wandering traders do not reward any experience when killed or when the player successfully trades with the wandering trader.

## Data values
### ID
Java Edition:

| Name             | Identifier       | Translation key                   |
|------------------|------------------|-----------------------------------|
| Wandering Trader | wandering_trader | entity.minecraft.wandering_trader |

Bedrock Edition:

| Name             | Identifier       | Numeric ID | Translation key              |
|------------------|------------------|------------|------------------------------|
| Wandering Trader | wandering_trader | 118        | entity.wandering_trader.name |

### Entity data
Wandering traders have entity data associated with them that contains various properties.

Java Edition:

Main article: Entity format

 Entity data
Additional fields for mobs that can breed
Tags common to all entities
Tags common to all mobs
 DespawnDelay: The number of ticks counted down until this wandering trader is forced to despawn. The wandering trader despawns when this value reaches 1.
 Offers: Is generated when the trading menu is opened for the first time.
 Recipes: List of trade options.
 A trade option.
 buy: The first 'cost' item, without the Slot tag.
Tags common to all items
 buyB: May not exist. The second 'cost' item, without the Slot tag.
Tags common to all items
 maxUses: The maximum number of times this trade can be used before it is disabled. Increases by a random amount from 2 to 12 when offers are refreshed.
 rewardExp: 1 or 0 (true/false) - true if this trade provides XP orb drops. All trades from naturally-generated villagers in Java Edition reward XP orbs.
 sell: The item being sold for each set of cost items, without the Slot tag.
Tags common to all items
 uses: The number of times this trade has been used. The trade becomes disabled when this is greater or equal to maxUses.
 WanderTarget: Destination toward where this trader wanders.
 X: The X coordinate to wander toward.
 Y: The Y coordinate to wander toward.
 Z: The Z coordinate to wander toward.
 Inventory: Each compound tag in this list is an item in the wandering trader's inventory, up to a maximum of 8 slots. Items in two or more slots that can be stacked together are automatically be condensed into one slot. If there are more than 8 slots, the last slot is removed until the total is 8. If there are 9 slots but two previous slots can be condensed, the last slot returns after the two other slots are combined. Wandering traders don't change their inventory automatically or drop items from it upon death. The inventory is currently unused.
 An item in the inventory, excluding the Slot tag.
Tags common to all items

Bedrock Edition:

See Bedrock Edition level format/Entity format.
## Notes

↑ Categorized as an NPC in the game code.



