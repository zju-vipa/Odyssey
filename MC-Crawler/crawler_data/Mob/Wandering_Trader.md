# Wandering Trader
The wandering trader is a passive mob that randomly spawns near the player. It can trade, making natural items more available, less dangerous to obtain, and in some cases, renewable.

## Contents
- 1 Spawning
	- 1.1 Despawning
- 2 Behavior
- 3 Trading
- 4 Drops
- 5 Sounds
- 6 Data values
	- 6.1 ID
	- 6.2 Entity data
- 7 Achievements
- 8 Advancements
- 9 History
- 10 Issues
- 11 Trivia
- 12 Gallery
	- 12.1 Screenshots
	- 12.2 In other media
- 13 Notes
- 14 References
- 15 External links

## Spawning
The wandering trader appears randomly in the Overworld with 2 leashed trader llamas. They typically spawn within a 48-block radius of a player. In Bedrock Edition, they also try to spawn by a claimed bell in a village. 

When the world is created (or updated from an older version), a counter is initialized to 24000 ticks (20 real-life minutes, or 1 Minecraft day). Each minute (1200 ticks), if /gamerule doTraderSpawning is set to true,‌[Java Edition  only] the counter is decreased by 1200. When the counter reaches 0 it is reset to 24000 and, if /gamerule doMobSpawning is set to true, an attempt may be made to spawn a wandering trader. The first time there is a 25% chance of making the attempt, which increases to 50% the second time and is 75% thereafter until a trader is spawned or no player is found for the attempt.

When attempting a spawn, a random player is selected. If no player is found, no trader is spawned but the chance for future attempts is reset to 25%. If a player is found, then 90% of the time the spawn attempt immediately fails.    

It should be noted, if there is a bell within 48 blocks of the player then the nearest such bell is used as the target location.

After either of the above conditions are met: ten attempts are made to find a valid mob spawning location on the uppermost block of a random X/Z position within -48/+47 of the target location on each axis. If spawning the trader succeeds, an additional ten attempts are made for each of two trader llamas to find a position within -4/+3 of the trader.[verify] Wandering traders can still spawn if the passive mob cap is full.

In Bedrock Edition, when using spawn eggs or the /summon command to spawn a wandering trader, llamas always spawn with it. Wandering traders never spawn if /mobevent minecraft:wandering_trader_event is set to false.

### Despawning
A wandering trader despawns after being loaded for 48000 ticks (40 minutes, or 2 full Minecraft days), although ticks spent with the trading UI open are not counted.[verify] Naming the wandering trader with a name tag or placing the wandering trader in a boat/minecart does not prevent it from despawning.[1] This also includes wandering traders as passengers of other mobs in Java Edition, where the wandering trader still despawns if summoned on top of another mob.

When a wandering trader is unloaded, either by moving into unloaded chunks or entering another dimension, its despawn timer freezes.

Wandering traders despawn sooner if all the trades are locked.‌[Bedrock Edition  only][verify]

## Behavior
The wandering trader has 6 random trades. New trades are not unlocked after trading with it.

After spawning, the wandering trader prefers to wander within 16 blocks of the initial spawning target location, even if that player leaves or the bell is removed, if not otherwise reacting to nearby players or mobs.[verify]

The wandering trader can sometimes form a caravan, due to wild llamas that follow the leashed trader llama(s).

Wandering traders drink a potion of invisibility during dusk and as needed to renew the effect during the night. They also drink milk if invisible during the day to remove the invisibility effect.

Wandering traders avoid zombies and their variants (zombie villagers, husks, drowned, zombified piglins, zoglins), all illager variants, ravagers, and vexes, staying at least 8 blocks away. Unlike other villagers, a wandering trader killed by zombies does not become a zombie villager.[2]

Wandering traders drink potions of invisibility if hurt by magic attacks or projectiles from hostile mobs (but not players), or when avoiding illagers, vexes, and zombies.‌[BE  only]

When attacked by a player, a wandering trader flees from the player as a villager would do. The llamas, however, attack the player by spitting if their master gets hit, except in Peaceful. The llamas stop attacking if the player is killed and respawns, if the llamas are leashed after the wandering trader is killed, or if the player gets far enough away from them for a short period of time. 

Despite their similarities to villagers, attacking or killing wandering traders does not anger iron golems.[3]

Unlike most other villager-like mobs, wandering traders do not visually sit down when riding objects such as boats and minecarts.[4]

## Trading
The trading UI of a wandering trader in Java Edition.
For the available trades for the wandering trader, see Trading § Wandering trader.

The trading system is a gameplay mechanic that allows players to buy items with emeralds, but from a wandering trader this time.

Pressing the use control on the wandering trader allows a player to view the items offered for sale, similar to a villager. Different offers are visible in a list, and clicking on one of the offers moves the corresponding items to the slots above the player's inventory. All offers involve emeralds as a currency.

Wandering traders typically sell items generated in the world or otherwise related to nature, such as plants, dyes, and buckets of fish. They can also trade less common items, such as coral blocks, blue ice, or nautilus shells. Overall, trades offered by wandering traders offer a way to obtain biome-specific materials, without having to travel to the specific biomes.

After the player purchases the same item several times, the wandering trader locks the trade, but unlike villagers, never unlocks the trade. The wandering trader can appear again around the player with new trades after a while.

Wandering traders do not have the novice-master trading system like villagers. Instead, the player can buy anything from the wandering trader without the need of unlocking the previous trades.

Wandering traders do not increase or decrease the prices of its items being sold if attacked by the player, or if the player has the Hero of the Village effect.

Unlike villagers, wandering traders only sell items, they do not buy items. Wandering traders do not have an experience bar and do not modify their offers or prices based on changing demand. This (the trade items or prices) can be changed by the player by editing the corresponding NBT data flag through the use of the /data‌[JE  only] command.

Wandering traders are the only renewable source of sand, red sand, coral blocks, and small dripleaves.

The wandering trader cannot work at a job site block and restock, even summoned with a villager profession or other villager data.

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


