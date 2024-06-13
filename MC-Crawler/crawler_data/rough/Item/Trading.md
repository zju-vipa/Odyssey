# Trading
The trading system is a gameplay mechanic that allows players to trade principally emeralds for items and vice versa, with villagers and wandering traders.

## Contents
- 1 Mechanics
	- 1.1 Level
	- 1.2 Trades
	- 1.3 Sale prices
- 2 Non-trading villagers
	- 2.1 Nitwit
	- 2.2 Unemployed villager
- 3 Java Edition offers
	- 3.1 Armorer
		- 3.1.1 Villager Trade Rebalance
	- 3.2 Butcher
	- 3.3 Cartographer
		- 3.3.1 Villager Trade Rebalance
	- 3.4 Cleric
	- 3.5 Farmer
	- 3.6 Fisherman
	- 3.7 Fletcher
	- 3.8 Leatherworker
	- 3.9 Librarian
		- 3.9.1 Villager Trade Rebalance
	- 3.10 Mason
	- 3.11 Shepherd
	- 3.12 Toolsmith
	- 3.13 Weaponsmith
- 4 Bedrock Edition offers
	- 4.1 Armorer
	- 4.2 Butcher
	- 4.3 Cartographer
	- 4.4 Cleric
	- 4.5 Farmer
	- 4.6 Fisherman
	- 4.7 Fletcher
	- 4.8 Leatherworker
	- 4.9 Librarian
	- 4.10 Shepherd
	- 4.11 Stone mason
	- 4.12 Toolsmith
	- 4.13 Weaponsmith
- 5 Wandering trader sales
	- 5.1 Java Edition sales
		- 5.1.1 Villager Trade Rebalance
	- 5.2 Bedrock Edition sales
- 6 Notes
- 7 Achievements
- 8 Advancements
- 9 Video
- 10 History
- 11 Issues
- 12 Trivia
- 13 Gallery
	- 13.1 Renders
	- 13.2 Screenshots
	- 13.3 Development images
- 14 References

## Mechanics
Pressing use on an adult villager with a profession, or on a wandering trader, opens a menu, allowing a player to trade with the villager or wandering trader. This action pauses any pathfinding the entity was doing. If the entity takes damage while trading, the trading menu closes. The same thing happens if they walk or are transported far enough away.

All transactions involve emeralds. Villagers buy or sell goods for emeralds, and wandering traders sell items for emeralds but do not buy items. Trading is the only legitimate method of acquiring the globe banner pattern, woodland explorer maps, and ocean explorer maps in Survival mode. It is also the only renewable way to obtain bells, diamond gear[note 1], lapis lazuli‌[BE  only], bottles o' enchanting, glass, sand, red sand, coral blocks, and small dripleaves.


  


The rest of this section describes mechanics that only apply to villagers. For wandering trader mechics, see § Wandering Trader.


### Level
Villagers have five career levels that can be increased by trading with them. Each villager starts at the "novice" level. A villager's level can be seen in the trading menu. The badge they wear can also be identified: stone for a novice, iron for an apprentice, gold for a journeyman, emerald for an expert, and diamond for a master. Trading until the villager's trading bar gets full unlocks the next level of trades. When a player trades with a villager, both the villager and the player gain experience. All villager trades reward the player with 3–6 experience, plus an additional 5 experience if the villager levels up due to the trade. Trading with a wandering trader also rewards the player with some experience, although the trader does not have experience levels to gain. A villager levels up when its experience bar becomes full and gains up to two new trades, along with keeping their old ones. Additionally, a villager receives a Regeneration effect, and becomes surrounded by purple and green particles for ten seconds.

| Level | Badge | Name       | Total villager experience required |
|-------|-------|------------|------------------------------------|
| 1     |       | Novice     | Available from start               |
| 2     |       | Apprentice | 10                                 |
| 3     |       | Journeyman | 70                                 |
| 4     |       | Expert     | 150                                |
| 5     |       | Master     | 250                                |

In Java Edition, villagers have a maximum of 10 trades. Each level unlocks a maximum of two new trades. If a level has a pool of more than two trades, the two offered trades are chosen randomly from the set.

In Bedrock Edition, villagers have 7–10 trade slots. A slot with multiple possible trades might display only one trade; for example, farmer villagers have 4 potential trades in their first trade slot, so each trade has a 1⁄4 chance to be chosen.

A villager's profession dictates the trading pool used to determine its trades. For example, villagers wearing straw hats are farmers, so their trades are based on the Farmer trade pool. Each profession unlocks a pre-defined and finite set of offers. Different professions are assigned to each villager based on their job-site block. This profession is indicated by their appearance and in the trading interface. Novice villagers who have not traded can lose their profession and change back into unemployed villagers if their claimed job site block is removed. Removing and then replacing a job site block can alter the trades offered, and a villager with no experience resets its trades every so often. Once a player trades with a villager, the villager keeps its profession forever and subsequently locks in the offered trades.

### Trades
Villagers run out of stock after a certain number of trades, the exact number is different for each item and referenced in the tables below. When villagers work at their job site blocks, they activate their offers again, up to twice per day. In Bedrock Edition, villagers need to be linked to a bed to restock their trades, It's not necessary for them to sleep but required to have a bed nearby. When an offer is disabled, a red "X" appears in the trading interface, and the villager displays the same particle effect as an offer being created.

Villagers distinguish between data values, so damaged tools cannot be traded in place of fully repaired tools.‌[Bedrock Edition  only] NBT data, however, is ignored, so the content of a written book does not matter. However, written books can no longer be sold to villagers, and no villagers currently buy any tools that have durability.

Each trade can be used a maximum number of times, after which the trade becomes disabled. Once trades are disabled, villagers must work at their corresponding job site block to resupply their trades.

### Sale prices
Permanent discounts (observed prices may be higher or lower due to other temporary factors) Above image is no longer accurate from 1.20.2(Java) and 1.20.30(Bedrock)


For the default sale price of a specific trade, find the trade in the tables below.
The price of an item rises and falls depending on three factors. Items with a high price multiplier (0.2) are affected by these changes more than items with a low multiplier (0.05). All price fluctuations affect only the first item involved in trade; for example, for an initial trade of 32 sticks for 1 emerald, the price might be driven down to 1 stick or up to 64 sticks for 1 emerald, but never for 2 emeralds. Additionally, no quantity can go lower than 1 or higher than the stack size.

The first factor is demand. An item that was sold out gets a price increase for all players when resupplied. If a player does not trade for a higher-priced item, the price is reduced the next time the villager resupplies. Demand is tracked per item, not per villager, so a villager can offer a higher-priced trade for a single item while other items are cheaper. Trades that have a price multiplier of 0 are not affected by demand.

The second way to affect prices is the Hero of the Village effect, which temporarily reduces prices for the affected player depending on the level of the effect.

Finally, players get personal discounts or fines based on their reputation with that particular villager. A positive reputation is gained by curing zombie villagers (the villager that was cured gives a permanent discount much larger than the temporary discount in nearby villagers). To cure a zombie villager, a player must splash it with a splash potion or an arrow of Weakness and then feed it a golden apple. The permanent discount is capped at one cure, while the temporary discount is capped at 8 cures. In Java Edition, players can also gain negative reputation by hitting or killing villagers, and positive reputation by trading.

## Non-trading villagers
If the player attempts to trade with a non-trading villager in Java Edition, they grunt and shake their head.

### Nitwit
A nitwit shaking its head.
Nitwits are green-coated villagers. They cannot gain a profession.

While they can be used for breeding, it is not possible to get a baby nitwit by breeding, even if using two nitwits as adults.


### Unemployed villager
An unemployed villager shaking its head.
Villagers without a job overlay cannot trade. They only wear their biome outfits. An unemployed villager gains a profession by claiming an unclaimed job site block. For example, an unclaimed cartography table converts an unemployed villager into a cartographer when the villager claims it, and both the villager and the table emit green particles. An inaccessible (or destroyed) job site block causes the connected villager to lose its profession, but that does not affect the player's popularity in the village.


## Java Edition offers
For the trades before 1.8, see Trading/Before 1.8.

For the 1.13 trades, see Trading/Before Village & Pillage.

For the experimental rebalanced trades, see Villager Trade Rebalance.

The villager pictured on the right is from the plains biome. To see villager professions dressed for other biomes, see Villagers § Professions.

Starting from Novice, at each level two more trades become available, unless there is only one trade within that level. If there are more than two possible trades, two are randomly selected.

### Armorer
Job site block: Blast Furnace

Armorer
| Armorer economic trade |             |                  |                  |                                     |          |                       |                |
|------------------------|-------------|------------------|------------------|-------------------------------------|----------|-----------------------|----------------|
| Level                  | Item wanted | Default quantity | Price multiplier | Item given                          | Quantity | Trades until disabled | XP to villager |
| Novice                 | Coal        | 15               | 0.05             | Emerald                             | 1        | 16 trades             | 2              |
|                        | Emerald     | 7                | 0.2              | Iron Leggings                       | 1        | 12 trades             | 1              |
|                        | Emerald     | 4                | 0.2              | Iron Boots                          | 1        | 12 trades             | 1              |
|                        | Emerald     | 5                | 0.2              | Iron Helmet                         | 1        | 12 trades             | 1              |
|                        | Emerald     | 9                | 0.2              | Iron Chestplate                     | 1        | 12 trades             | 1              |
| Apprentice             | Iron Ingot  | 4                | 0.05             | Emerald                             | 1        | 12 trades             | 10             |
|                        | Emerald     | 36               | 0.2              | Bell                                | 1        | 12 trades             | 5              |
|                        | Emerald     | 1                | 0.2              | Chainmail Boots                     | 1        | 12 trades             | 5              |
|                        | Emerald     | 3                | 0.2              | Chainmail Leggings                  | 1        | 12 trades             | 5              |
| Journeyman             | Lava Bucket | 1                | 0.05             | Emerald                             | 1        | 12 trades             | 20             |
|                        | Diamond     | 1                | 0.05             | Emerald                             | 1        | 12 trades             | 20             |
|                        | Emerald     | 1                | 0.2              | Chainmail Helmet                    | 1        | 12 trades             | 10             |
|                        | Emerald     | 4                | 0.2              | Chainmail Chestplate                | 1        | 12 trades             | 10             |
|                        | Emerald     | 5                | 0.2              | Shield                              | 1        | 12 trades             | 10             |
| Expert                 | Emerald     | 19–33            | 0.2              | Enchanted[note 2]Diamond Leggings   | 1        | 3 trades              | 15             |
|                        | Emerald     | 13–27            | 0.2              | Enchanted[note 2]Diamond Boots      | 1        | 3 trades              | 15             |
| Master                 | Emerald     | 13–27            | 0.2              | Enchanted[note 2]Diamond Helmet     | 1        | 3 trades              | 30[note 3]     |
|                        | Emerald     | 21–35            | 0.2              | Enchanted[note 2]Diamond Chestplate | 1        | 3 trades              | 30[note 3]     |

#### Villager Trade Rebalance
Main article: Villager_Trade_Rebalance § Gameplay
 The table below is incomplete, please check the main article. 

| Biomes and corresponding armor |                                   |                                      |                                             |                                      |                                              |                                                 |                                        |
|--------------------------------|-----------------------------------|--------------------------------------|---------------------------------------------|--------------------------------------|----------------------------------------------|-------------------------------------------------|----------------------------------------|
| Appearance                     | Desert                            | Plains                               | Savanna                                     | Snowy                                | Taiga                                        | Jungle                                          | Swamp                                  |
| Expert                         | Iron Leggings<br/>withThorns      | Iron Leggings<br/>withProtectionI    | Iron Leggings<br/>withCurse of Binding      | Iron Helmet<br/>withAqua Affinity    | Diamond Leggings                             | Chainmail Helmet<br/>withUnbreakingI            | Chainmail Helmet<br/>withMending       |
|                                | Iron Boots<br/>withThorns         | Iron Boots<br/>withProtectionI       | Iron Boots<br/>withCurse of Binding         |                                      | Diamond Boots                                | Chainmail Chestplate<br/>withUnbreakingI        | Chainmail Chestplate<br/>withMending   |
|                                | Iron Helmet<br/>withThorns        | Iron Helmet<br/>withProtectionI      | Iron Helmet<br/>withCurse of Binding        | Iron Boots<br/>withFrost WalkerI     | Diamond Helmet                               | Chainmail Leggings<br/>withUnbreakingI          | Chainmail Leggings<br/>withMending     |
|                                | Iron Chestplate<br/>withThorns    | Iron Chestplate<br/>withProtectionI  | Iron Chestplate<br/>withCurse of Binding    |                                      | Diamond Chestplate                           | Chainmail Boots<br/>withUnbreakingI             | Chainmail Boots<br/>withMending        |
| Master                         | Diamond Chestplate<br/>withThorns | Diamond Leggings<br/>withProtectionI | Diamond Helmet<br/>withCurse of Binding     | Diamond Helmet<br/>withAqua Affinity | Diamond Chestplate<br/>withBlast ProtectionI | Chainmail Helmet<br/>withProjectile ProtectionI | Chainmail Helmet<br/>withRespirationI  |
|                                | Diamond Leggings<br/>withThorns   | Diamond Boots<br/>withProtectionI    | Diamond Chestplate<br/>withCurse of Binding | Diamond Boots<br/>withFrost WalkerI  | Diamond Leggings<br/>withBlast ProtectionI   | Chainmail Boots<br/>withFeather FallingI        | Chainmail Boots<br/>withDepth StriderI |
|                                | Emerald                           | Emerald                              | Emerald                                     | Emerald                              | Emerald                                      | Emerald                                         | Emerald                                |

### Butcher
Job site block: Smoker

Butcher
| Butcher economic trade |                  |                  |                  |                 |          |                       |                |
|------------------------|------------------|------------------|------------------|-----------------|----------|-----------------------|----------------|
| Level                  | Item wanted      | Default quantity | Price multiplier | Item given      | Quantity | Trades until disabled | XP to villager |
| Novice                 | Raw Chicken      | 14               | 0.05             | Emerald         | 1        | 16 trades             | 2              |
|                        | Raw Porkchop     | 7                | 0.05             | Emerald         | 1        | 16 trades             | 2              |
|                        | Raw Rabbit       | 4                | 0.05             | Emerald         | 1        | 16 trades             | 2              |
|                        | Emerald          | 1                | 0.05             | Rabbit Stew     | 1        | 12 trades             | 1              |
| Apprentice             | Coal             | 15               | 0.05             | Emerald         | 1        | 16 trades             | 2              |
|                        | Emerald          | 1                | 0.05             | Cooked Porkchop | 5        | 16 trades             | 5              |
|                        | Emerald          | 1                | 0.05             | Cooked Chicken  | 8        | 16 trades             | 5              |
| Journeyman             | Raw Mutton       | 7                | 0.05             | Emerald         | 1        | 16 trades             | 20             |
|                        | Raw Beef         | 10               | 0.05             | Emerald         | 1        | 16 trades             | 20             |
| Expert                 | Dried Kelp Block | 10               | 0.05             | Emerald         | 1        | 12 trades             | 30             |
| Master                 | Sweet Berries    | 10               | 0.05             | Emerald         | 1        | 12 trades             | 30[note 3]     |

### Cartographer
Job site block: Cartography Table

Cartographer
| Cartographer economic trade |                     |                  |                  |                                                 |          |                       |                |
|-----------------------------|---------------------|------------------|------------------|-------------------------------------------------|----------|-----------------------|----------------|
| Level                       | Item wanted         | Default quantity | Price multiplier | Item given                                      | Quantity | Trades until disabled | XP to villager |
| Novice                      | Paper               | 24               | 0.05             | Emerald                                         | 1        | 16 trades             | 2              |
|                             | Emerald             | 7                | 0.05             | Empty Map                                       | 1        | 12 trades             | 1              |
| Apprentice                  | Glass Pane          | 11               | 0.05             | Emerald                                         | 1        | 16 trades             | 10             |
|                             | Emerald<br/>Compass | 13<br/>1         | 0.2              | Ocean Explorer Map[note 4]                      | 1        | 12 trades             | 5              |
| Journeyman                  | Compass             | 1                | 0.05             | Emerald                                         | 1        | 12 trades             | 20             |
|                             | Emerald<br/>Compass | 14<br/>1         | 0.2              | Woodland Explorer Map[note 4]Trial Chambers Map | 1        | 12 trades             | 10             |
| Expert                      | Emerald             | 7                | 0.05             | Item Frame                                      | 1        | 12 trades             | 15             |
|                             | Emerald             | 3                | 0.05             | Any color blank banner[note 5]                  | 1        | 12 trades             | 15             |
| Master                      | Emerald             | 8                | 0.05             | Globe Banner Pattern                            | 1        | 12 trades             | 30[note 3]     |

#### Villager Trade Rebalance
| Cartographer economic trade |                     |                  |                  |                                              |          |                       |                |
|-----------------------------|---------------------|------------------|------------------|----------------------------------------------|----------|-----------------------|----------------|
| Level                       | Item wanted         | Default quantity | Price multiplier | Item given                                   | Quantity | Trades until disabled | XP to villager |
| Novice                      | Paper               | 24               | 0.05             | Emerald                                      | 1        | 16 trades             | 2              |
|                             | Emerald             | 7                | 0.05             | Empty Map                                    | 1        | 12 trades             | 1              |
| Apprentice                  | Glass Pane          | 11               | 0.05             | Emerald                                      | 1        | 16 trades             | 10             |
|                             | Emerald<br/>Compass | 8<br/>1          | 0.2              | Biome dependent<br/>Map[note 6][note 4]      | 1        | 12 trades             | 5              |
| Journeyman                  | Compass             | 1                | 0.05             | Emerald                                      | 1        | 12 trades             | 20             |
|                             | Emerald<br/>Compass | 13<br/>1         | 0.2              | Ocean Explorer Map[note 4]Trial Chambers Map | 1        | 12 trades             | 10             |
| Expert                      | Emerald             | 7                | 0.05             | Item Frame                                   | 1        | 12 trades             | 15             |
|                             | Emerald             | 3                | 0.05             | Any color blank banner[note 5]               | 1        | 12 trades             | 15             |
| Master                      | Emerald             | 8                | 0.05             | Globe Banner Pattern                         | 1        | 12 trades             | 30[note 3]     |
|                             | Emerald<br/>Compass | 14<br/>1         | 0.2              | Woodland Explorer Map[note 4]                | 1        | 1 trade               | 30[note 3]     |

| Biomes and corresponding maps |                     |                     |                     |                    |                    |                     |                     |
|-------------------------------|---------------------|---------------------|---------------------|--------------------|--------------------|---------------------|---------------------|
| Appearance                    | Desert              | Plains              | Savanna             | Snowy              | Taiga              | Jungle              | Swamp               |
| Group 1                       | Savanna Village Map | Taiga Village Map   | Plains Village Map  | Plains Village Map | Snowy Village Map  | Savanna Village Map | Snowy Village Map   |
| Group 2                       | Plains Village Map  | Savanna Village Map | Desert Village Map  | Taiga Village Map  | Plains Village Map | Desert Village Map  | Taiga Village Map   |
| Group 3                       | Jungle Explorer Map | –                   | Jungle Explorer Map | Swamp Explorer Map | Swamp Explorer Map | Swamp Explorer Map  | Jungle Explorer Map |

### Cleric
Job site block: Brewing Stand

Cleric
| Cleric economic trade |               |                  |                  |                      |          |                       |                |
|-----------------------|---------------|------------------|------------------|----------------------|----------|-----------------------|----------------|
| Level                 | Item wanted   | Default quantity | Price multiplier | Item given           | Quantity | Trades until disabled | XP to villager |
| Novice                | Rotten Flesh  | 32               | 0.05             | Emerald              | 1        | 16 trades             | 2              |
|                       | Emerald       | 1                | 0.05             | Redstone Dust        | 2        | 12 trades             | 1              |
| Apprentice            | Gold Ingot    | 3                | 0.05             | Emerald              | 1        | 12 trades             | 10             |
|                       | Emerald       | 1                | 0.05             | Lapis Lazuli         | 1        | 12 trades             | 5              |
| Journeyman            | Rabbit's Foot | 2                | 0.05             | Emerald              | 1        | 12 trades             | 20             |
|                       | Emerald       | 4                | 0.05             | Glowstone            | 1        | 12 trades             | 10             |
| Expert                | Scute         | 4                | 0.05             | Emerald              | 1        | 12 trades             | 30             |
|                       | Glass Bottle  | 9                | 0.05             | Emerald              | 1        | 12 trades             | 30             |
|                       | Emerald       | 5                | 0.05             | Ender Pearl          | 1        | 12 trades             | 15             |
| Master                | Nether Wart   | 22               | 0.05             | Emerald              | 1        | 12 trades             | 30[note 3]     |
|                       | Emerald       | 3                | 0.05             | Bottle o' Enchanting | 1        | 12 trades             | 30[note 3]     |

### Farmer
Job site block: Composter

Farmer
| Farmer economic trade |             |                  |                  |                                               |          |                       |                |
|-----------------------|-------------|------------------|------------------|-----------------------------------------------|----------|-----------------------|----------------|
| Level                 | Item wanted | Default quantity | Price multiplier | Item given                                    | Quantity | Trades until disabled | XP to villager |
| Novice                | Wheat       | 20               | 0.05             | Emerald                                       | 1        | 16 trades             | 2              |
|                       | Potato      | 26               | 0.05             | Emerald                                       | 1        | 16 trades             | 2              |
|                       | Carrot      | 22               | 0.05             | Emerald                                       | 1        | 16 trades             | 2              |
|                       | Beetroot    | 15               | 0.05             | Emerald                                       | 1        | 16 trades             | 2              |
|                       | Emerald     | 1                | 0.05             | Bread                                         | 6        | 16 trades             | 1              |
| Apprentice            | Pumpkin     | 6                | 0.05             | Emerald                                       | 1        | 12 trades             | 10             |
|                       | Emerald     | 1                | 0.05             | Pumpkin Pie                                   | 4        | 12 trades             | 5              |
|                       | Emerald     | 1                | 0.05             | Apple                                         | 4        | 16 trades             | 5              |
| Journeyman            | Emerald     | 3                | 0.05             | Cookie                                        | 18       | 12 trades             | 10             |
|                       | Melon       | 4                | 0.05             | Emerald                                       | 1        | 12 trades             | 20             |
| Expert                | Emerald     | 1                | 0.05             | Cake                                          | 1        | 12 trades             | 15             |
|                       | Emerald     | 1                | 0.05             | Suspicious Stew<br/>5 seconds ofNight Vision  | 1        | 12 trades             | 15             |
|                       | Emerald     | 1                | 0.05             | Suspicious Stew<br/>8 seconds ofJump Boost    | 1        | 12 trades             | 15             |
|                       | Emerald     | 1                | 0.05             | Suspicious Stew<br/>7 seconds ofWeakness      | 1        | 12 trades             | 15             |
|                       | Emerald     | 1                | 0.05             | Suspicious Stew<br/>6 seconds ofBlindness     | 1        | 12 trades             | 15             |
|                       | Emerald     | 1                | 0.05             | Suspicious Stew<br/>14 seconds ofPoison       | 1        | 12 trades             | 15             |
|                       | Emerald     | 1                | 0.05             | Suspicious Stew<br/>0.35 seconds ofSaturation | 1        | 12 trades             | 15             |
| Master                | Emerald     | 3                | 0.05             | Golden Carrot                                 | 3        | 12 trades             | 30[note 3]     |
|                       | Emerald     | 4                | 0.05             | Glistering Melon Slice                        | 3        | 12 trades             | 30[note 3]     |

### Fisherman
Job site block: Barrel

Fisherman
| Fisherman economic trade |                            |                  |                  |                              |          |                       |                |
|--------------------------|----------------------------|------------------|------------------|------------------------------|----------|-----------------------|----------------|
| Level                    | Item wanted                | Default quantity | Price multiplier | Item given                   | Quantity | Trades until disabled | XP to villager |
| Novice                   | String                     | 20               | 0.05             | Emerald                      | 1        | 16 trades             | 2              |
|                          | Coal                       | 10               | 0.05             | Emerald                      | 1        | 16 trades             | 2              |
|                          | Emerald<br/>Raw Cod        | 1<br/>6          | 0.05             | Cooked Cod                   | 6        | 16 trades             | 1              |
|                          | Emerald                    | 3                | 0.05             | Bucket of Cod                | 1        | 16 trades             | 1              |
| Apprentice               | Raw Cod                    | 15               | 0.05             | Emerald                      | 1        | 16 trades             | 10             |
|                          | Emerald<br/>Raw Salmon     | 1<br/>6          | 0.05             | Cooked Salmon                | 6        | 16 trades             | 5              |
|                          | Emerald                    | 2                | 0.05             | Campfire                     | 1        | 12 trades             | 5              |
| Journeyman               | Raw Salmon                 | 13               | 0.05             | Emerald                      | 1        | 16 trades             | 20             |
|                          | Emerald                    | 8–22             | 0.2              | Enchanted[note 2]Fishing Rod | 1        | 3 trades              | 10             |
| Expert                   | Tropical Fish              | 6                | 0.05             | Emerald                      | 1        | 12 trades             | 30             |
| Master                   | Pufferfish                 | 4                | 0.05             | Emerald                      | 1        | 12 trades             | 30[note 3]     |
|                          | <br/>One of 5boats[note 7] | 1                | 0.05             | Emerald                      | 1        | 12 trades             | 30[note 3]     |

### Fletcher
Job site block: Fletching Table

Fletcher
| Fletcher economic trade |                    |                  |                  |                           |          |                       |                |
|-------------------------|--------------------|------------------|------------------|---------------------------|----------|-----------------------|----------------|
| Level                   | Item wanted        | Default quantity | Price multiplier | Item given                | Quantity | Trades until disabled | XP to villager |
| Novice                  | Stick              | 32               | 0.05             | Emerald                   | 1        | 16 trades             | 2              |
|                         | Emerald            | 1                | 0.05             | Arrow                     | 16       | 12 trades             | 1              |
|                         | Emerald<br/>Gravel | 1<br/>10         | 0.05             | Flint                     | 10       | 12 trades             | 1              |
| Apprentice              | Flint              | 26               | 0.05             | Emerald                   | 1        | 12 trades             | 10             |
|                         | Emerald            | 2                | 0.05             | Bow                       | 1        | 12 trades             | 5              |
| Journeyman              | String             | 14               | 0.05             | Emerald                   | 1        | 16 trades             | 20             |
|                         | Emerald            | 3                | 0.05             | Crossbow                  | 1        | 12 trades             | 10             |
| Expert                  | Feather            | 24               | 0.05             | Emerald                   | 1        | 16 trades             | 30             |
|                         | Emerald            | 7–21             | 0.05             | Enchanted[note 2]Bow      | 1        | 3 trades              | 15             |
| Master                  | Tripwire Hook      | 8                | 0.05             | Emerald                   | 1        | 12 trades             | 30[note 3]     |
|                         | Emerald            | 8–22             | 0.05             | Enchanted[note 2]Crossbow | 1        | 3 trades              | 15[note 3]     |
|                         | Emerald<br/>Arrow  | 2<br/>5          | 0.05             | Tipped arrow[note 8]      | 5        | 12 trades             | 30[note 3]     |

### Leatherworker
Job site block: Cauldron

Leatherworker
| Leatherworker economic trade |             |                  |                  |                             |          |                       |                |
|------------------------------|-------------|------------------|------------------|-----------------------------|----------|-----------------------|----------------|
| Level                        | Item wanted | Default quantity | Price multiplier | Item given                  | Quantity | Trades until disabled | XP to villager |
| Novice                       | Leather     | 6                | 0.05             | Emerald                     | 1        | 16 trades             | 2              |
|                              | Emerald     | 3                | 0.2              | Leather Pants[note 9]       | 1        | 12 trades             | 1              |
|                              | Emerald     | 7                | 0.2              | Leather Tunic[note 9]       | 1        | 12 trades             | 1              |
| Apprentice                   | Flint       | 26               | 0.05             | Emerald                     | 1        | 12 trades             | 10             |
|                              | Emerald     | 5                | 0.2              | Leather Cap[note 9]         | 1        | 12 trades             | 5              |
|                              | Emerald     | 4                | 0.2              | Leather Boots[note 9]       | 1        | 12 trades             | 5              |
| Journeyman                   | Rabbit Hide | 9                | 0.05             | Emerald                     | 1        | 12 trades             | 20             |
|                              | Emerald     | 7                | 0.2              | Leather Tunic[note 9]       | 1        | 12 trades             | 1[1]           |
| Expert                       | Scute       | 4                | 0.05             | Emerald                     | 1        | 12 trades             | 30             |
|                              | Emerald     | 6                | 0.2              | Leather Horse Armor[note 9] | 1        | 12 trades             | 15             |
| Master                       | Emerald     | 6                | 0.2              | Saddle                      | 1        | 12 trades             | 30[note 3]     |
|                              | Emerald     | 5                | 0.2              | Leather Cap[note 9]         | 1        | 12 trades             | 30[note 3]     |

### Librarian
Job site block: Lectern

Librarian
| Librarian economic trade |                  |                  |                  |                         |          |                       |                |
|--------------------------|------------------|------------------|------------------|-------------------------|----------|-----------------------|----------------|
| Level                    | Item wanted      | Default quantity | Price multiplier | Item given              | Quantity | Trades until disabled | XP to villager |
| Novice                   | Paper            | 24               | 0.05             | Emerald                 | 1        | 16 trades             | 2              |
|                          | Emerald<br/>Book | 5–64<br/>1       | 0.2              | Enchanted Book[note 10] | 1        | 12 trades             | 1              |
|                          | Emerald          | 9                | 0.05             | Bookshelf               | 1        | 12 trades             | 1              |
| Apprentice               | Book             | 4                | 0.05             | Emerald                 | 1        | 12 trades             | 10             |
|                          | Emerald<br/>Book | 5–64<br/>1       | 0.2              | Enchanted Book[note 10] | 1        | 12 trades             | 5              |
|                          | Emerald          | 1                | 0.05             | Lantern                 | 1        | 12 trades             | 5              |
| Journeyman               | Ink Sac          | 5                | 0.05             | Emerald                 | 1        | 12 trades             | 20             |
|                          | Emerald<br/>Book | 5–64<br/>1       | 0.2              | Enchanted Book[note 10] | 1        | 12 trades             | 10             |
|                          | Emerald          | 1                | 0.05             | Glass                   | 4        | 12 trades             | 10             |
| Expert                   | Book and Quill   | 2[note 11][2]    | 0.05             | Emerald                 | 1        | 12 trades             | 30             |
|                          | Emerald<br/>Book | 5–64<br/>1       | 0.2              | Enchanted Book[note 10] | 1        | 12 trades             | 15             |
|                          | Emerald          | 5                | 0.05             | Clock                   | 1        | 12 trades             | 15             |
|                          | Emerald          | 4                | 0.05             | Compass                 | 1        | 12 trades             | 15             |
| Master                   | Emerald          | 20               | 0.05             | Name Tag                | 1        | 12 trades             | 30[note 3]     |

#### Villager Trade Rebalance
| Librarian economic trade |                  |                  |                  |                                                         |          |                       |                |
|--------------------------|------------------|------------------|------------------|---------------------------------------------------------|----------|-----------------------|----------------|
| Level                    | Item wanted      | Default quantity | Price multiplier | Item given                                              | Quantity | Trades until disabled | XP to villager |
| Novice                   | Paper            | 24               | 0.05             | Emerald                                                 | 1        | 16 trades             | 2              |
|                          | Emerald<br/>Book | 5–64<br/>1       | 0.2              | Biome dependent<br/>common<br/>Enchanted Book[note 12]  | 1        | 12 trades             | 1              |
|                          | Emerald          | 9                | 0.05             | Bookshelf                                               | 1        | 12 trades             | 1              |
| Apprentice               | Book             | 4                | 0.05             | Emerald                                                 | 1        | 12 trades             | 10             |
|                          | Emerald<br/>Book | 5–64<br/>1       | 0.2              | Biome dependent<br/>common<br/>Enchanted Book[note 12]  | 1        | 12 trades             | 5              |
|                          | Emerald          | 1                | 0.05             | Lantern                                                 | 1        | 12 trades             | 5              |
| Journeyman               | Ink Sac          | 5                | 0.05             | Emerald                                                 | 1        | 12 trades             | 20             |
|                          | Emerald<br/>Book | 5–64<br/>1       | 0.2              | Biome dependent<br/>common<br/>Enchanted Book[note 12]  | 1        | 12 trades             | 10             |
|                          | Emerald          | 1                | 0.05             | Glass                                                   | 4        | 12 trades             | 10             |
| Expert                   | Book and Quill   | 2[note 11][2]    | 0.05             | Emerald                                                 | 1        | 12 trades             | 30             |
|                          | Emerald          | 5                | 0.05             | Clock                                                   | 1        | 12 trades             | 15             |
|                          | Emerald          | 4                | 0.05             | Compass                                                 | 1        | 12 trades             | 15             |
| Master                   | Emerald<br/>Book | 5–45<br/>1       | 0.2              | Biome dependent<br/>special<br/>Enchanted Book[note 13] | 1        | 12 trades             | 30[note 3]     |
|                          | Emerald          | 20               | 0.05             | Name Tag                                                | 1        | 12 trades             | 30[note 3]     |

| Biomes and corresponding enchantments |                                         |                                        |                                                  |                                            |                                            |                                                     |                                                      |
|---------------------------------------|-----------------------------------------|----------------------------------------|--------------------------------------------------|--------------------------------------------|--------------------------------------------|-----------------------------------------------------|------------------------------------------------------|
| Appearance                            | Desert                                  | Plains                                 | Savanna                                          | Snowy                                      | Taiga                                      | Jungle                                              | Swamp                                                |
| Special                               | EfficiencyIII                           | ProtectionIII                          | SharpnessIII                                     | Silk Touch                                 | FortuneII                                  | UnbreakingII                                        | Mending                                              |
| Common                                | Fire Protection<br/>Thorns<br/>Infinity | Punch<br/>Smite<br/>Bane of Arthropods | Knockback<br/>Curse of Binding<br/>Sweeping Edge | Aqua Affinity<br/>Looting<br/>Frost Walker | Blast Protection<br/>Fire Aspect<br/>Flame | Feather Falling<br/>Projectile Protection<br/>Power | Depth Strider<br/>Respiration<br/>Curse of Vanishing |

### Mason
Job site block: Stonecutter

Mason
| Mason economic trade |               |                  |                  |                                      |          |                       |                    |  |
|----------------------|---------------|------------------|------------------|--------------------------------------|----------|-----------------------|--------------------|--|
| Level                | Item wanted   | Default quantity | Price multiplier | Item given                           | Quantity | Trades until disabled | XP to the villager |  |
| Novice               | Clay Ball     | 10               | 0.05             | Emerald                              | 1        | 16 trades             | 2                  |  |
|                      | Emerald       | 1                | 0.05             | Brick                                | 10       | 16 trades             | 1                  |  |
| Apprentice           | Stone         | 20               | 0.05             | Emerald                              | 1        | 16 trades             | 10                 |  |
|                      | Emerald       | 1                | 0.05             | Chiseled Stone Bricks                | 4        | 16 trades             | 5                  |  |
| Journeyman           | Granite       | 16               | 0.05             | Emerald                              | 1        | 16 trades             | 20                 |  |
|                      | Andesite      | 16               | 0.05             | Emerald                              | 1        | 16 trades             | 20                 |  |
|                      | Diorite       | 16               | 0.05             | Emerald                              | 1        | 16 trades             | 20                 |  |
|                      | Emerald       | 1                | 0.05             | Dripstone Block                      | 4        | 16 trades             | 10                 |  |
|                      | Emerald       | 1                | 0.05             | Polished Andesite                    | 4        | 16 trades             | 10                 |  |
|                      | Emerald       | 1                | 0.05             | Polished Diorite                     | 4        | 16 trades             | 10                 |  |
|                      | Emerald       | 1                | 0.05             | Polished Granite                     | 4        | 16 trades             | 10                 |  |
| Expert               | Nether Quartz | 12               | 0.05             | Emerald                              | 1        | 12 trades             | 30                 |  |
|                      | Emerald       | 1                | 0.05             | Any color stained terracotta[note 5] | 1        | 12 trades             | 15                 |  |
|                      | Emerald       | 1                | 0.05             | Any color glazed terracotta[note 5]  | 1        | 12 trades             | 15                 |  |
| Master               | Emerald       | 1                | 0.05             | Quartz Pillar                        | 1        | 12 trades             | 30[note 3]         |  |
|                      | Emerald       | 1                | 0.05             | Block of Quartz                      | 1        | 12 trades             | 30[note 3]         |  |

### Shepherd
Job site block: Loom

Shepherd
| Shepherd economic trade |                |                  |                  |                                |          |                       |                |
|-------------------------|----------------|------------------|------------------|--------------------------------|----------|-----------------------|----------------|
| Level                   | Item wanted    | Default quantity | Price multiplier | Item given                     | Quantity | Trades until disabled | XP to villager |
| Novice                  | White Wool     | 18               | 0.05             | Emerald                        | 1        | 16 trades             | 2              |
|                         | Brown Wool     | 18               | 0.05             | Emerald                        | 1        | 16 trades             | 2              |
|                         | Black Wool     | 18               | 0.05             | Emerald                        | 1        | 16 trades             | 2              |
|                         | Gray Wool      | 18               | 0.05             | Emerald                        | 1        | 16 trades             | 2              |
|                         | Emerald        | 2                | 0.05             | Shears                         | 1        | 12 trades             | 1              |
| Apprentice              | White Dye      | 12               | 0.05             | Emerald                        | 1        | 16 trades             | 10             |
|                         | Gray Dye       | 12               | 0.05             | Emerald                        | 1        | 16 trades             | 10             |
|                         | Black Dye      | 12               | 0.05             | Emerald                        | 1        | 16 trades             | 10             |
|                         | Light Blue Dye | 12               | 0.05             | Emerald                        | 1        | 16 trades             | 10             |
|                         | Lime Dye       | 12               | 0.05             | Emerald                        | 1        | 16 trades             | 10             |
|                         | Emerald        | 1                | 0.05             | Any color wool[note 5]         | 1        | 16 trades             | 5              |
|                         | Emerald        | 1                | 0.05             | Any color carpet[note 5]       | 4        | 16 trades             | 5              |
| Journeyman              | Yellow Dye     | 12               | 0.05             | Emerald                        | 1        | 16 trades             | 20             |
|                         | Light Gray Dye | 12               | 0.05             | Emerald                        | 1        | 16 trades             | 20             |
|                         | Orange Dye     | 12               | 0.05             | Emerald                        | 1        | 16 trades             | 20             |
|                         | Red Dye        | 12               | 0.05             | Emerald                        | 1        | 16 trades             | 20             |
|                         | Pink Dye       | 12               | 0.05             | Emerald                        | 1        | 16 trades             | 20             |
|                         | Emerald        | 3                | 0.05             | Any color bed[note 5]          | 1        | 12 trades             | 10             |
| Expert                  | Brown Dye      | 12               | 0.05             | Emerald                        | 1        | 16 trades             | 30             |
|                         | Purple Dye     | 12               | 0.05             | Emerald                        | 1        | 16 trades             | 30             |
|                         | Blue Dye       | 12               | 0.05             | Emerald                        | 1        | 16 trades             | 30             |
|                         | Green Dye      | 12               | 0.05             | Emerald                        | 1        | 16 trades             | 30             |
|                         | Magenta Dye    | 12               | 0.05             | Emerald                        | 1        | 16 trades             | 30             |
|                         | Cyan Dye       | 12               | 0.05             | Emerald                        | 1        | 16 trades             | 30             |
|                         | Emerald        | 3                | 0.05             | Any color blank banner[note 5] | 1        | 12 trades             | 15             |
| Master                  | Emerald        | 2                | 0.05             | Painting                       | 3        | 12 trades             | 30[note 3]     |

### Toolsmith
Job site block: Smithing Table

Toolsmith
| Toolsmith economic trade |             |                  |                  |                                  |          |                       |                |
|--------------------------|-------------|------------------|------------------|----------------------------------|----------|-----------------------|----------------|
| Level                    | Item wanted | Default quantity | Price multiplier | Item given                       | Quantity | Trades until disabled | XP to villager |
| Novice                   | Coal        | 15               | 0.05             | Emerald                          | 1        | 16 trades             | 2              |
|                          | Emerald     | 1                | 0.2              | Stone Axe                        | 1        | 12 trades             | 1              |
|                          | Emerald     | 1                | 0.2              | Stone Shovel                     | 1        | 12 trades             | 1              |
|                          | Emerald     | 1                | 0.2              | Stone Pickaxe                    | 1        | 12 trades             | 1              |
|                          | Emerald     | 1                | 0.2              | Stone Hoe                        | 1        | 12 trades             | 1              |
| Apprentice               | Iron Ingot  | 4                | 0.05             | Emerald                          | 1        | 12 trades             | 10             |
|                          | Emerald     | 36               | 0.2              | Bell                             | 1        | 12 trades             | 5              |
| Journeyman               | Flint       | 30               | 0.05             | Emerald                          | 1        | 12 trades             | 20             |
|                          | Emerald     | 6–20             | 0.2              | Enchanted[note 2]Iron Axe        | 1        | 3 trades              | 10             |
|                          | Emerald     | 7–21             | 0.2              | Enchanted[note 2]Iron Shovel     | 1        | 3 trades              | 10             |
|                          | Emerald     | 8–22             | 0.2              | Enchanted[note 2]Iron Pickaxe    | 1        | 3 trades              | 10             |
|                          | Emerald     | 4                | 0.2              | Diamond Hoe                      | 1        | 3 trades              | 10             |
| Expert                   | Diamond     | 1                | 0.05             | Emerald                          | 1        | 12 trades             | 30             |
|                          | Emerald     | 17–31            | 0.2              | Enchanted[note 2]Diamond Axe     | 1        | 3 trades              | 15             |
|                          | Emerald     | 10–24            | 0.2              | Enchanted[note 2]Diamond Shovel  | 1        | 3 trades              | 15             |
| Master                   | Emerald     | 18–32            | 0.2              | Enchanted[note 2]Diamond Pickaxe | 1        | 3 trades              | 30[note 3]     |

### Weaponsmith
Job site block: Grindstone

Weaponsmith
| Weaponsmith economic trade |             |                  |                  |                                |          |                       |                |
|----------------------------|-------------|------------------|------------------|--------------------------------|----------|-----------------------|----------------|
| Level                      | Item wanted | Default quantity | Price multiplier | Item given                     | Quantity | Trades until disabled | XP to villager |
| Novice                     | Coal        | 15               | 0.05             | Emerald                        | 1        | 16 trades             | 2              |
|                            | Emerald     | 3                | 0.2              | Iron Axe                       | 1        | 12 trades             | 1              |
|                            | Emerald     | 7–21             | 0.05             | Enchanted[note 2]Iron Sword    | 1        | 3 trades              | 1              |
| Apprentice                 | Iron Ingot  | 4                | 0.05             | Emerald                        | 1        | 12 trades             | 10             |
|                            | Emerald     | 36               | 0.2              | Bell                           | 1        | 12 trades             | 5              |
| Journeyman                 | Flint       | 24               | 0.05             | Emerald                        | 1        | 12 trades             | 20             |
| Expert                     | Diamond     | 1                | 0.05             | Emerald                        | 1        | 12 trades             | 30             |
|                            | Emerald     | 17–31            | 0.2              | Enchanted[note 2]Diamond Axe   | 1        | 3 trades              | 15             |
| Master                     | Emerald     | 13–27            | 0.2              | Enchanted[note 2]Diamond Sword | 1        | 3 trades              | 30[note 3]     |

## Bedrock Edition offers
For the trades before 1.11, see Trading/Before Village & Pillage.

### Armorer
Job site block: Blast Furnace

An armorer.
| Armorer economic trade |            |             |                  |                  |                                     |          |                       |                      |
|------------------------|------------|-------------|------------------|------------------|-------------------------------------|----------|-----------------------|----------------------|
| Level                  | Trade slot | Item wanted | Default quantity | Price multiplier | Item given                          | Quantity | Trades until disabled | XP given to villager |
| Novice                 | 1          | Coal        | 15               | 0.05             | Emerald                             | 1        | 16 trades             | 2                    |
|                        | 2          | Emerald     | 5                | 0.2              | Iron Helmet                         | 1        | 12 trades             | 1                    |
|                        |            | Emerald     | 9                | 0.2              | Iron Chestplate                     | 1        | 12 trades             | 1                    |
|                        |            | Emerald     | 7                | 0.2              | Iron Leggings                       | 1        | 12 trades             | 1                    |
|                        |            | Emerald     | 4                | 0.2              | Iron Boots                          | 1        | 12 trades             | 1                    |
| Apprentice             | 3          | Iron Ingot  | 4                | 0.05             | Emerald                             | 1        | 12 trades             | 10                   |
|                        | 4          | Emerald     | 36               | 0.2              | Bell                                | 1        | 12 trades             | 5                    |
|                        |            | Emerald     | 3                | 0.2              | Chainmail Leggings                  | 1        | 12 trades             | 5                    |
|                        |            | Emerald     | 1                | 0.2              | Chainmail Boots                     | 1        | 12 trades             | 5                    |
| Journeyman             | 5          | Lava Bucket | 1                | 0.05             | Emerald                             | 1        | 12 trades             | 20                   |
|                        | 6          | Diamond     | 1                | 0.05             | Emerald                             | 1        | 12 trades             | 30                   |
|                        | 7          | Emerald     | 1                | 0.2              | Chainmail Helmet                    | 1        | 12 trades             | 10                   |
|                        |            | Emerald     | 4                | 0.2              | Chainmail Chestplate                | 1        | 12 trades             | 10                   |
|                        |            | Emerald     | 5                | 0.2              | Shield                              | 1        | 12 trades             | 10                   |
| Expert                 | 8          | Emerald     | 19-33            | 0.2              | Enchanted[note 2]Diamond Leggings   | 1        | 3 trades              | 15                   |
|                        |            | Emerald     | 13-27            | 0.2              | Enchanted[note 2]Diamond Boots      | 1        | 3 trades              | 15                   |
| Master                 | 9          | Emerald     | 13-27            | 0.2              | Enchanted[note 2]Diamond Helmet     | 1        | 3 trades              | 30[note 3]           |
|                        |            | Emerald     | 21-35            | 0.2              | Enchanted[note 2]Diamond Chestplate | 1        | 3 trades              | 30[note 3]           |

### Butcher
Job site block: Smoker

A butcher.
| Butcher economic trade |            |                  |                  |                  |                 |          |                       |                |
|------------------------|------------|------------------|------------------|------------------|-----------------|----------|-----------------------|----------------|
| Level                  | Trade slot | Item wanted      | Default quantity | Price multiplier | Item given      | Quantity | Trades until disabled | XP to villager |
| Novice                 | 1          | Raw Chicken      | 14               | 0.05             | Emerald         | 1        | 16 trades             | 2              |
|                        |            | Raw Rabbit       | 4                | 0.05             | Emerald         | 1        | 16 trades             | 2              |
|                        |            | Raw Porkchop     | 7                | 0.05             | Emerald         | 1        | 16 trades             | 2              |
|                        | 2          | Emerald          | 1                | 0.05             | Rabbit Stew     | 1        | 12 trades             | 1              |
| Apprentice             | 3          | Coal             | 15               | 0.05             | Emerald         | 1        | 16 trades             | 10             |
|                        | 4          | Emerald          | 1                | 0.05             | Cooked Chicken  | 8        | 16 trades             | 5              |
|                        |            | Emerald          | 1                | 0.05             | Cooked Porkchop | 5        | 16 trades             | 5              |
| Journeyman             | 5          | Raw Beef         | 10               | 0.05             | Emerald         | 1        | 16 trades             | 20             |
|                        |            | Raw Mutton       | 7                | 0.05             | Emerald         | 1        | 16 trades             | 20             |
| Expert                 | 6          | Dried Kelp Block | 10               | 0.05             | Emerald         | 1        | 12 trades             | 30             |
| Master                 | 7          | Sweet Berries    | 10               | 0.05             | Emerald         | 1        | 12 trades             | 30[note 3]     |

### Cartographer
Job site block: Cartography Table

A cartographer.
| Cartographer economic trade |            |                     |                  |                  |                                |          |                       |                |
|-----------------------------|------------|---------------------|------------------|------------------|--------------------------------|----------|-----------------------|----------------|
| Level                       | Trade slot | Item wanted         | Default quantity | Price multiplier | Item given                     | Quantity | Trades until disabled | XP to villager |
| Novice                      | 1          | Paper               | 24               | 0.05             | Emerald                        | 1        | 16 trades             | 2              |
|                             | 2          | Emerald             | 7                | 0.05             | Empty Map                      | 1        | 12 trades             | 1              |
| Apprentice                  | 3          | Glass Pane          | 11               | 0.05             | Emerald                        | 1        | 16 trades             | 10             |
|                             | 4          | Emerald<br/>Compass | 13<br/>1         | 0.2              | Ocean Explorer Map[note 14]    | 1        | 12 trades             | 5              |
| Journeyman                  | 5          | Compass             | 1                | 0.05             | Emerald                        | 1        | 12 trades             | 20             |
|                             | 6          | Emerald<br/>Compass | 14<br/>1         | 0.2              | Woodland Explorer Map[note 14] | 1        | 12 trades             | 10             |
| Expert                      | 7          | Emerald             | 7                | 0.05             | Item Frame                     | 1        | 12 trades             | 15             |
|                             | 8          | Emerald             | 3                | 0.05             | One of 16 blank banners        | 1        | 12 trades             | 15             |
| Master                      | 9          | Emerald             | 8                | 0.05             | Globe Banner Pattern           | 1        | 12 trades             | 30[note 3]     |

### Cleric
Job site block: Brewing Stand

A cleric.
| Cleric economic trade |            |               |                  |                  |                      |          |                       |                |
|-----------------------|------------|---------------|------------------|------------------|----------------------|----------|-----------------------|----------------|
| Level                 | Trade slot | Item wanted   | Default quantity | Price multiplier | Item given           | Quantity | Trades until disabled | XP to villager |
| Novice                | 1          | Rotten Flesh  | 32               | 0.05             | Emerald              | 1        | 16 trades             | 2              |
|                       | 2          | Emerald       | 1                | 0.05             | Redstone Dust        | 2        | 12 trades             | 1              |
| Apprentice            | 3          | Gold Ingot    | 3                | 0.05             | Emerald              | 1        | 12 trades             | 10             |
|                       | 4          | Emerald       | 1                | 0.05             | Lapis Lazuli         | 1        | 12 trades             | 5              |
| Journeyman            | 5          | Rabbit's Foot | 2                | 0.05             | Emerald              | 1        | 12 trades             | 20             |
|                       | 6          | Emerald       | 4                | 0.05             | Glowstone            | 1        | 12 trades             | 10             |
| Expert                | 7          | Scute         | 4                | 0.05             | Emerald              | 1        | 12 trades             | 30             |
|                       |            | Glass Bottle  | 9                | 0.05             | Emerald              | 1        | 12 trades             | 30             |
|                       | 8          | Emerald       | 5                | 0.05             | Ender Pearl          | 1        | 12 trades             | 15             |
| Master                | 9          | Nether Wart   | 22               | 0.05             | Emerald              | 1        | 12 trades             | 30[note 3]     |
|                       | 10         | Emerald       | 3                | 0.05             | Bottle o' Enchanting | 1        | 12 trades             | 30[note 3]     |

### Farmer
Job site block: Composter

A farmer.
| Farmer economic trade |            |             |                  |                  |                          |          |                       |                |
|-----------------------|------------|-------------|------------------|------------------|--------------------------|----------|-----------------------|----------------|
| Level                 | Trade slot | Item wanted | Default quantity | Price multiplier | Item given               | Quantity | Trades until disabled | XP to villager |
| Novice                | 1          | Wheat       | 20               | 0.05             | Emerald                  | 1        | 16 trades             | 2              |
|                       |            | Potato      | 26               | 0.05             | Emerald                  | 1        | 16 trades             | 2              |
|                       |            | Carrot      | 22               | 0.05             | Emerald                  | 1        | 16 trades             | 2              |
|                       |            | Beetroot    | 15               | 0.05             | Emerald                  | 1        | 16 trades             | 2              |
|                       | 2          | Emerald     | 1                | 0.05             | Bread                    | 6        | 16 trades             | 1              |
| Apprentice            | 3          | Pumpkin     | 6                | 0.05             | Emerald                  | 1        | 12 trades             | 10             |
|                       | 4          | Emerald     | 1                | 0.05             | Pumpkin Pie              | 4        | 12 trades             | 5              |
|                       |            | Emerald     | 1                | 0.05             | Apple                    | 4        | 16 trades             | 5              |
| Journeyman            | 5          | Melon       | 4                | 0.05             | Emerald                  | 1        | 12 trades             | 20             |
|                       | 6          | Emerald     | 3                | 0.05             | Cookie                   | 18       | 12 trades             | 10             |
| Expert                | 7          | Emerald     | 1                | 0.05             | Suspicious Stew[note 15] | 1        | 12 trades             | 15             |
|                       | 8          | Emerald     | 1                | 0.05             | Cake                     | 1        | 12 trades             | 15             |
| Master                | 9          | Emerald     | 3                | 0.05             | Golden Carrot            | 3        | 12 trades             | 30[note 3]     |
|                       |            | Emerald     | 4                | 0.05             | Glistering Melon Slice   | 3        | 12 trades             | 30[note 3]     |

### Fisherman
Job site block: Barrel

A fisherman.
| Fisherman economic trade |            |                            |                  |                  |                              |          |                       |                |
|--------------------------|------------|----------------------------|------------------|------------------|------------------------------|----------|-----------------------|----------------|
| Level                    | Trade slot | Item wanted                | Default quantity | Price multiplier | Item given                   | Quantity | Trades until disabled | XP to villager |
| Novice                   | 1          | String                     | 20               | 0.05             | Emerald                      | 1        | 16 trades             | 2              |
|                          |            | Coal                       | 10               | 0.05             | Emerald                      | 1        | 16 trades             | 2              |
|                          | 2          | Emerald                    | 3                | 0.05             | Bucket of Cod                | 1        | 16 trades             | 1              |
|                          |            | Emerald<br/>Raw Cod        | 1<br/>6          | 0.05<br/>0       | Cooked Cod                   | 6        | 16 trades             | 1              |
| Apprentice               | 3          | Raw Cod                    | 15               | 0.05             | Emerald                      | 1        | 16 trades             | 10             |
|                          | 4          | Emerald                    | 2                | 0.05             | Campfire                     | 1        | 12 trades             | 5              |
|                          |            | Emerald<br/>Raw Salmon     | 1<br/>6          | 0.05<br/>0       | Cooked Salmon                | 6        | 16 trades             | 5              |
| Journeyman               | 5          | Raw Salmon                 | 13               | 0.05             | Emerald                      | 1        | 16 trades             | 20             |
|                          | 6          | Emerald                    | 8-22             | 0.2              | Enchanted[note 2]Fishing Rod | 1        | 3 trades              | 10             |
| Expert                   | 7          | Tropical Fish              | 6                | 0.05             | Emerald                      | 1        | 12 trades             | 30             |
| Master                   | 8          | Pufferfish                 | 4                | 0.05             | Emerald                      | 1        | 12 trades             | 30[note 3]     |
|                          | 9          | <br/>One of 5boats[note 7] | 1                | 0.05             | Emerald                      | 1        | 12 trades             | 30[note 3]     |

### Fletcher
Job site block: Fletching Table

A fletcher.
| Fletcher economic trade |            |                    |                  |                  |                                |          |                       |                |
|-------------------------|------------|--------------------|------------------|------------------|--------------------------------|----------|-----------------------|----------------|
| Level                   | Trade slot | Item wanted        | Default quantity | Price multiplier | Item given                     | Quantity | Trades until disabled | XP to villager |
| Novice                  | 1          | Stick              | 32               | 0.05             | Emerald                        | 1        | 16 trades             | 2              |
|                         | 2          | Emerald            | 1                | 0.05             | Arrow                          | 16       | 12 trades             | 1              |
|                         |            | Emerald<br/>Gravel | 1<br/>10         | 0.05             | Flint                          | 10       | 12 trades             | 1              |
| Apprentice              | 3          | Flint              | 26               | 0.05             | Emerald                        | 1        | 12 trades             | 10             |
|                         | 4          | Emerald            | 2                | 0.05             | Bow                            | 1        | 12 trades             | 5              |
| Journeyman              | 5          | String             | 14               | 0.05             | Emerald                        | 1        | 16 trades             | 20             |
|                         | 6          | Emerald            | 3                | 0.05             | Crossbow                       | 1        | 12 trades             | 10             |
| Expert                  | 7          | Feather            | 24               | 0.05             | Emerald                        | 1        | 16 trades             | 30             |
|                         | 8          | Emerald            | 7-21             | 0.05             | Enchanted[note 2]Bow           | 1        | 3 trades              | 15             |
| Master                  | 9          | Tripwire Hook      | 8                | 0.05             | Emerald                        | 1        | 12 trades             | 30[note 3]     |
|                         | 10         | Emerald            | 8-22             | 0.05             | Enchanted[note 2]Crossbow      | 1        | 3 trades              | 15[note 3]     |
|                         |            | Emerald<br/>Arrow  | 2<br/>5          | 0.05             | 1 of 15 tipped arrows[note 16] | 5        | 12 trades             | 30[note 3]     |

### Leatherworker
Job site block: Cauldron

A leatherworker.
| Leatherworker economic trade |            |             |                  |                  |                             |          |                       |                |
|------------------------------|------------|-------------|------------------|------------------|-----------------------------|----------|-----------------------|----------------|
| Level                        | Trade slot | Item wanted | Default quantity | Price multiplier | Item given                  | Quantity | Trades until disabled | XP to villager |
| Novice                       | 1          | Leather     | 6                | 0.05             | Emerald                     | 1        | 16 trades             | 2              |
|                              | 2          | Emerald     | 3                | 0.2              | Leather Pants[note 9]       | 1        | 12 trades             | 1              |
|                              |            | Emerald     | 7                | 0.2              | Leather Tunic[note 9]       | 1        | 12 trades             | 1              |
| Apprentice                   | 3          | Flint       | 26               | 0.05             | Emerald                     | 1        | 12 trades             | 10             |
|                              | 4          | Emerald     | 5                | 0.2              | Leather Cap[note 9]         | 1        | 12 trades             | 5              |
|                              |            | Emerald     | 4                | 0.2              | Leather Boots[note 9]       | 1        | 12 trades             | 5              |
| Journeyman                   | 5          | Rabbit Hide | 9                | 0.05             | Emerald                     | 1        | 12 trades             | 20             |
|                              | 6          | Emerald     | 7                | 0.2              | Leather Tunic[note 9]       | 1        | 12 trades             | 10             |
| Expert                       | 7          | Scute       | 4                | 0.05             | Emerald                     | 1        | 12 trades             | 30             |
|                              | 8          | Emerald     | 6                | 0.2              | Leather Horse Armor[note 9] | 1        | 12 trades             | 15             |
| Master                       | 9          | Emerald     | 5                | 0.2              | Leather Cap[note 9]         | 1        | 12 trades             | 30[note 3]     |
|                              |            | Emerald     | 6                | 0.2              | Saddle                      | 1        | 12 trades             | 30[note 3]     |

### Librarian
Job site block: Lectern

A librarian.
| Librarian economic trade |            |                  |                  |                  |                         |          |                       |                |
|--------------------------|------------|------------------|------------------|------------------|-------------------------|----------|-----------------------|----------------|
| Level                    | Trade slot | Item wanted      | Default quantity | Price multiplier | Item given              | Quantity | Trades until disabled | XP to villager |
| Novice                   | 1          | Paper            | 24               | 0.05             | Emerald                 | 1        | 16 trades             | 2              |
|                          | 2          | Emerald          | 9                | 0.05             | Bookshelf               | 1        | 12 trades             | 1              |
|                          |            | Emerald<br/>Book | 5–64<br/>1       | 0.2              | Enchanted Book[note 10] | 1        | 12 trades             | 1              |
| Apprentice               | 3          | Book             | 4                | 0.05             | Emerald                 | 1        | 12 trades             | 10             |
|                          | 4          | Emerald          | 1                | 0.05             | Lantern                 | 1        | 12 trades             | 5              |
|                          |            | Emerald<br/>Book | 5–64<br/>1       | 0.2              | Enchanted Book[note 10] | 1        | 12 trades             | 5              |
| Journeyman               | 5          | Ink Sac          | 5                | 0.05             | Emerald                 | 1        | 12 trades             | 20             |
|                          | 6          | Emerald          | 1                | 0.05             | Glass                   | 4        | 12 trades             | 10             |
|                          |            | Emerald<br/>Book | 5–64<br/>1       | 0.2              | Enchanted Book[note 10] | 1        | 12 trades             | 10             |
| Expert                   | 7          | Book and Quill   | 2[note 17]       | 0.05             | Emerald                 | 1        | 12 trades             | 30             |
|                          | 8          | Emerald          | 4                | 0.05             | Compass                 | 1        | 12 trades             | 15             |
|                          |            | Emerald          | 5                | 0.05             | Clock                   | 1        | 12 trades             | 15             |
|                          |            | Emerald<br/>Book | 5–64<br/>1       | 0.2              | Enchanted Book[note 10] | 1        | 12 trades             | 15             |
| Master                   | 9          | Emerald          | 20               | 0.05             | Name Tag                | 1        | 12 trades             | 30[note 3]     |

### Shepherd
Job site block: Loom

A shepherd.
| Shepherd economic trade |            |                        |                  |                  |                         |          |                       |                |
|-------------------------|------------|------------------------|------------------|------------------|-------------------------|----------|-----------------------|----------------|
| Level                   | Trade slot | Item wanted            | Default quantity | Price multiplier | Item given              | Quantity | Trades until disabled | XP to villager |
| Novice                  | 1          | One of 4 types of wool | 18               | 0.05             | Emerald                 | 1        | 16 trades             | 2              |
|                         | 2          | Emerald                | 2                | 0.05             | Shears                  | 1        | 12 trades             | 1              |
| Apprentice              | 3          | One of 5 dyes          | 12               | 0.05             | Emerald                 | 1        | 16 trades             | 10             |
|                         | 4          | Emerald                | 1                | 0.05             | One of 16 types of wool | 1        | 16 trades             | 5              |
|                         |            | Emerald                | 1                | 0.05             | One of 16 carpets       | 4        | 16 trades             | 5              |
| Journeyman              | 5          | One of 5 dyes          | 12               | 0.05             | Emerald                 | 1        | 16 trades             | 20             |
|                         | 6          | Emerald                | 3                | 0.05             | One of 16 beds          | 1        | 12 trades             | 10             |
| Expert                  | 7          | One of 6 dyes          | 12               | 0.05             | Emerald                 | 1        | 16 trades             | 30             |
|                         | 8          | Emerald                | 3                | 0.05             | One of 16 blank banners | 1        | 12 trades             | 15             |
| Master                  | 9          | Emerald                | 2                | 0.05             | Painting                | 3        | 12 trades             | 30[note 3]     |

### Stone mason
Job site block: Stonecutter

A stone mason.
Note: "Mason" is used in Java Edition and "Stone Mason" is used in Bedrock Edition.
| Stone mason economic trade |            |                              |                  |                  |                                                          |          |                       |                |
|----------------------------|------------|------------------------------|------------------|------------------|----------------------------------------------------------|----------|-----------------------|----------------|
| Level                      | Trade slot | Item wanted                  | Default quantity | Price multiplier | Item given                                               | Quantity | Trades until disabled | XP to villager |
| Novice                     | 1          | Clay                         | 10               | 0.05             | Emerald                                                  | 1        | 16 trades             | 2              |
|                            | 2          | Emerald                      | 1                | 0.05             | Brick                                                    | 10       | 16 trades             | 1              |
| Apprentice                 | 3          | Stone                        | 20               | 0.05             | Emerald                                                  | 1        | 16 trades             | 10             |
|                            | 4          | Emerald                      | 1                | 0.05             | Chiseled Stone Bricks                                    | 4        | 16 trades             | 5              |
| Journeyman                 | 5          | <br/>One of 3 stone variants | 16               | 0.05             | Emerald                                                  | 1        | 16 trades             | 20             |
|                            | 6          | Emerald                      | 1                | 0.05             | <br/>One of 3 polished stone variants ordripstone block  | 4        | 16 trades             | 10             |
| Expert                     | 7          | Nether Quartz                | 12               | 0.05             | Emerald                                                  | 1        | 12 trades             | 30             |
|                            | 8          | Emerald                      | 1                | 0.05             | 1 of 16 types of stained terracotta or glazed terracotta | 1        | 12 trades             | 15             |
| Master                     | 9          | Emerald                      | 1                | 0.05             | Block of QuartzorQuartz Pillar                           | 1        | 12 trades             | 30[note 3]     |

### Toolsmith
Job site block: Smithing Table

A toolsmith.
| Toolsmith economic trade |            |             |                  |                  |                                  |          |                       |                |
|--------------------------|------------|-------------|------------------|------------------|----------------------------------|----------|-----------------------|----------------|
| Level                    | Trade slot | Item wanted | Default quantity | Price multiplier | Item given                       | Quantity | Trades until disabled | XP to villager |
| Novice                   | 1          | Coal        | 15               | 0.05             | Emerald                          | 1        | 16 trades             | 2              |
|                          | 2          | Emerald     | 1                | 0.2              | Stone Axe                        | 1        | 12 trades             | 1              |
|                          |            | Emerald     | 1                | 0.2              | Stone Pickaxe                    | 1        | 12 trades             | 1              |
|                          |            | Emerald     | 1                | 0.2              | Stone Shovel                     | 1        | 12 trades             | 1              |
|                          |            | Emerald     | 1                | 0.2              | Stone Hoe                        | 1        | 12 trades             | 1              |
| Apprentice               | 3          | Iron Ingot  | 4                | 0.05             | Emerald                          | 1        | 12 trades             | 10             |
|                          | 4          | Emerald     | 36               | 0.2              | Bell                             | 1        | 12 trades             | 5              |
| Journeyman               | 5          | Flint       | 30               | 0.05             | Emerald                          | 1        | 12 trades             | 20             |
|                          | 6          | Emerald     | 6-20             | 0.2              | Enchanted[note 2]Iron Axe        | 1        | 3 trades              | 10             |
|                          |            | Emerald     | 7-21             | 0.2              | Enchanted[note 2]Iron Pickaxe    | 1        | 3 trades              | 10             |
|                          |            | Emerald     | 8-22             | 0.2              | Enchanted[note 2]Iron Shovel     | 1        | 3 trades              | 10             |
|                          |            | Emerald     | 4                | 0.2              | Diamond Hoe                      | 1        | 3 trades              | 10             |
| Expert                   | 7          | Diamond     | 1                | 0.05             | Emerald                          | 1        | 12 trades             | 30             |
|                          | 8          | Emerald     | 17-31            | 0.2              | Enchanted[note 2]Diamond Axe     | 1        | 3 trades              | 15             |
|                          |            | Emerald     | 10-24            | 0.2              | Enchanted[note 2]Diamond Shovel  | 1        | 3 trades              | 15             |
| Master                   | 9          | Emerald     | 18-32            | 0.2              | Enchanted[note 2]Diamond Pickaxe | 1        | 3 trades              | 30[note 3]     |

### Weaponsmith
Job site block: Grindstone

A weaponsmith.
| Weaponsmith economic trade |            |             |                  |                  |                                |          |                       |                |
|----------------------------|------------|-------------|------------------|------------------|--------------------------------|----------|-----------------------|----------------|
| Level                      | Trade slot | Item wanted | Default quantity | Price multiplier | Item given                     | Quantity | Trades until disabled | XP to villager |
| Novice                     | 1          | Coal        | 15               | 0.05             | Emerald                        | 1        | 16 trades             | 2              |
|                            | 2          | Emerald     | 3                | 0.2              | Iron Axe                       | 1        | 12 trades             | 1              |
|                            | 3          | Emerald     | 7-21             | 0.2              | Enchanted[note 2]Iron Sword    | 1        | 3 trades              | 5              |
| Apprentice                 | 4          | Iron Ingot  | 4                | 0.05             | Emerald                        | 1        | 12 trades             | 10             |
|                            | 5          | Emerald     | 36               | 0.2              | Bell                           | 1        | 12 trades             | 10             |
| Journeyman                 | 6          | Flint       | 24               | 0.05             | Emerald                        | 1        | 12 trades             | 20             |
| Expert                     | 7          | Diamond     | 1                | 0.05             | Emerald                        | 1        | 12 trades             | 30             |
|                            | 8          | Emerald     | 17-31            | 0.2              | Enchanted[note 2]Diamond Axe   | 1        | 3 trades              | 15             |
| Master                     | 9          | Emerald     | 13-27            | 0.2              | Enchanted[note 2]Diamond Sword | 1        | 3 trades              | 30[note 3]     |

## Wandering trader sales


Wandering Trader
Unlike villagers, the wandering trader does not buy items in exchange for emeralds – it only sells items, using emeralds as a currency. Therefore, the following tables' leftmost column is how many emeralds the player needs to give to receive the items listed in the middle column of the table.

### Java Edition sales
The wandering trader offers six trades in total: five random ordinary trades and one special trade. The five random trades are chosen from the list below.

| Price | Item                       | Trades untildisabled |
|-------|----------------------------|----------------------|
| 1     | Allium                     | 12                   |
| 1     | Azure Bluet                | 12                   |
| 1     | Blue Orchid                | 8                    |
| 1     | Cornflower                 | 12                   |
| 1     | Dandelion                  | 12                   |
| 1     | Lily of the Valley         | 7                    |
| 1     | Orange Tulip               | 12                   |
| 1     | Oxeye Daisy                | 12                   |
| 1     | Pink Tulip                 | 12                   |
| 1     | Poppy                      | 12                   |
| 1     | Red Tulip                  | 12                   |
| 1     | White Tulip                | 12                   |
| 1     | Fern                       | 12                   |
| 1     | Brown Mushroom             | 12                   |
| 1     | Red Mushroom               | 12                   |
| 1     | Beetroot Seeds             | 12                   |
| 1     | Melon Seeds                | 12                   |
| 1     | Pumpkin Seeds              | 12                   |
| 1     | Wheat Seeds                | 12                   |
| 1     | Pumpkin                    | 4                    |
| 1     | Sugar Cane                 | 8                    |
| 1     | Vines                      | 12                   |
| 1     | Lily Pad(×2)               | 5                    |
| 1     | Moss Block(×2)             | 5                    |
| 1     | Pointed Dripstone(×2)      | 5                    |
| 1     | Rooted Dirt(×2)            | 5                    |
| 1     | Small Dripleaf(×2)         | 5                    |
| 1     | Any color dye (×3)[note 5] | 12                   |
| 1     | Red Sand(×4)               | 6                    |
| 1     | Sand(×8)                   | 8                    |
| 2     | Glowstone                  | 5                    |
| 2     | Sea Pickle                 | 5                    |
| 3     | Cactus                     | 8                    |
| 3     | Brain Coral Block          | 8                    |
| 3     | Bubble Coral Block         | 8                    |
| 3     | Fire Coral Block           | 8                    |
| 3     | Horn Coral Block           | 8                    |
| 3     | Tube Coral Block           | 8                    |
| 3     | Kelp                       | 12                   |
| 4     | Slimeball                  | 5                    |
| 5     | Acacia Sapling             | 8                    |
| 5     | Birch Sapling              | 8                    |
| 5     | Dark Oak Sapling           | 8                    |
| 5     | Jungle Sapling             | 8                    |
| 5     | Oak Sapling                | 8                    |
| 5     | Spruce Sapling             | 8                    |
| 5     | Mangrove Propagule         | 8                    |
| 5     | Cherry Sapling             | 8                    |
| 5     | Nautilus Shell             | 5                    |

The one random special trade is chosen from the list below. It is always the wandering trader's final trade offer.

| Price | Items                   | Trades untildisabled |
|-------|-------------------------|----------------------|
| 1     | Gunpowder               | 8                    |
| 3     | Podzol(×3)              | 6                    |
| 3     | Packed Ice              | 6                    |
| 5     | Bucket of Pufferfish    | 4                    |
| 5     | Bucket of Tropical Fish | 4                    |
| 6     | Blue Ice                | 6                    |

#### Villager Trade Rebalance
The wandering trader offers nine trades in total: two random trades from purchasing table, two random trades from special selling table, and five random trades from ordinary trades table.

| Purchasing table     |          |       |                           |
|----------------------|----------|-------|---------------------------|
| Item wanted          | Quantity | Price | Trades until<br/>disabled |
| Water Bottle         | 1        | 1     | 1                         |
| Water Bucket         | 1        | 2     | 1                         |
| Milk Bucket          | 1        | 2     | 1                         |
| Fermented Spider Eye | 1        | 3     | 1                         |
| Baked Potato         | 4        | 1     | 1                         |
| Hay Bale             | 1        | 1     | 1                         |

| Selling table (special) |                                           |       |                           |
|-------------------------|-------------------------------------------|-------|---------------------------|
| Price                   | Item                                      | Count | Trades until<br/>disabled |
| 1                       | Packed Ice                                | 1     | 6                         |
|                         | Gunpowder                                 | 4     | 2                         |
|                         | <br/>Log[3]                               | 8     | 4                         |
| 3                       | Podzol                                    | 3     | 6                         |
| 5                       | Potion of Invisibility<br/>Duration: 8:00 | 1     | 1                         |
| 6                       | Blue Ice                                  | 1     | 6                         |
| 6-20                    | Enchanted[note 2]<br/>Iron Pickaxe        | 1     | 1                         |

| Selling table (ordinary) |                                                                                                                                             |       |                           |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|-------|---------------------------|
| Price                    | Item                                                                                                                                        | Count | Trades until<br/>disabled |
| 1                        | Fern                                                                                                                                        | 1     | 12                        |
|                          | Sugar Cane                                                                                                                                  | 1     | 8                         |
|                          | Pumpkin                                                                                                                                     | 1     | 4                         |
|                          | Dandelion<br/>Poppy<br/>Allium<br/>Azure Bluet<br/>Red Tulip<br/>Orange Tulip<br/>White Tulip<br/>Pink Tulip<br/>Oxeye Daisy<br/>Cornflower | 1     | 12                        |
|                          | Blue Orchid                                                                                                                                 | 1     | 8                         |
|                          | Lily of the Valley                                                                                                                          | 1     | 7                         |
|                          | Wheat Seeds<br/>Beetroot Seeds<br/>Pumpkin Seeds<br/>Melon Seeds                                                                            | 1     | 12                        |
|                          | <br/><br/>One of 16dyes                                                                                                                     | 3     | 12                        |
|                          | Vines                                                                                                                                       | 3     | 4                         |
|                          | Brown Mushroom<br/>Red Mushroom                                                                                                             | 3     | 4                         |
|                          | Lily Pad                                                                                                                                    | 5     | 2                         |
|                          | Small Dripleaf                                                                                                                              | 2     | 5                         |
|                          | Sand                                                                                                                                        | 8     | 8                         |
|                          | Red Sand                                                                                                                                    | 4     | 6                         |
|                          | Pointed Dripstone                                                                                                                           | 2     | 5                         |
|                          | Rooted Dirt                                                                                                                                 | 2     | 5                         |
|                          | Moss Block                                                                                                                                  | 2     | 5                         |
| 2                        | Sea Pickle                                                                                                                                  | 1     | 5                         |
|                          | Glowstone                                                                                                                                   | 1     | 5                         |
| 3                        | Tropical Fish Bucket<br/>Pufferfish Bucket                                                                                                  | 1     | 4                         |
|                          | Kelp                                                                                                                                        | 1     | 12                        |
|                          | Cactus                                                                                                                                      | 1     | 8                         |
|                          | Brain Coral Block<br/>Bubble Coral Block<br/>Fire Coral Block<br/>Horn Coral Block<br/>Tube Coral Block                                     | 1     | 8                         |
| 4                        | Slimeball                                                                                                                                   | 1     | 5                         |
| 5                        | <br/>One of 8saplings                                                                                                                       | 1     | 8                         |
|                          | Nautilus Shell                                                                                                                              | 1     | 5                         |

### Bedrock Edition sales
In Bedrock Edition, wandering traders offers 6 random trades. Their trades are unaffected by demand.

Five of the random trades are shown in the table below:

| Price | Regular offer                                                                                                                                                                                                                                                                                                     | Single offer[note 18]                                                                                                                                                                                                                                                                                                    |        | Trades untildisabled |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|----------------------|
|       |                                                                                                                                                                                                                                                                                                                   | Grouped items                                                                                                                                                                                                                                                                                                            | Weight |                      |
| 1     | Fern<br/>Vines<br/>Dandelion<br/>Poppy<br/>Blue Orchid<br/>Allium<br/>Azure Bluet<br/>Red Tulip<br/>Orange Tulip<br/>Pink Tulip<br/>White Tulip<br/>Oxeye Daisy<br/>Cornflower<br/>Wheat Seeds[note 19]<br/>Beetroot Seeds[note 19]<br/>Pumpkin Seeds[note 19]<br/>Melon Seeds[note 19]<br/>Cocoa Beans (x3)<br/> | Wheat Seeds[note 19]<br/>Beetroot Seeds[note 19]<br/>Pumpkin Seeds[note 19]<br/>Melon Seeds[note 19]<br/>                                                                                                                                                                                                                | 4      | 12                   |
|       |                                                                                                                                                                                                                                                                                                                   | Red Dye (×3)<br/>Yellow Dye (×3)<br/>Orange Dye (×3)<br/>Lime Dye (×3)<br/>Green Dye (×3)<br/>Cyan Dye (×3)<br/>Light Blue Dye (×3)<br/>Purple Dye (×3)<br/>Magenta Dye (×3)<br/>Pink Dye (×3)<br/>Gray Dye (×3)<br/>Light Gray Dye (×3)<br/>Blue Dye (x3)<br/>Brown Dye (x3)<br/>White Dye (x3)<br/>Black Dye (x3)<br/> | 16     |                      |
|       |                                                                                                                                                                                                                                                                                                                   | Brown Mushroom<br/>Red Mushroom<br/>                                                                                                                                                                                                                                                                                     | 2      |                      |
|       | Sugar Cane<br/>Sand (×8)<br/>                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                          | –      | 8                    |
|       | Lily of the Valley<br/>                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                          |        | 7                    |
|       | Red Sand (×4)<br/>                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                          |        | 6                    |
|       | Lily Pad (×2)<br/>Pointed Dripstone (x2)<br/>Moss Block (x2)<br/>Rooted Dirt (x2)<br/>Small Dripleaf (x2)<br/>                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                          |        | 5                    |
|       | Pumpkin<br/>                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                          |        | 4                    |
| 2     | Sea Pickle<br/>                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                          |        | 5                    |
|       | Glowstone<br/>                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                          |        |                      |
| 3     | Kelp<br/>                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                          |        | 12                   |
|       | Cactus<br/>                                                                                                                                                                                                                                                                                                       | Brain Coral Block<br/>Bubble Coral Block<br/>Fire Coral Block<br/>Horn Coral Block<br/>Tube Coral Block<br/>                                                                                                                                                                                                             | 5      | 8                    |
| 4     | Slimeball<br/>                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                          | –      | 5                    |
| 5     | –                                                                                                                                                                                                                                                                                                                 | Saplings<br/>                                                                                                                                                                                                                                                                                                            | 7      | 8                    |
|       | Nautilus Shell<br/>                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                          | –      | 5                    |

The other random trade is shown below (these items are chosen for each wandering trader and always offered but only one of them):

| Price | Items                                                 | Trades untildisabled |
|-------|-------------------------------------------------------|----------------------|
| 1     | Gunpowder<br/>                                        | 8                    |
| 3     | Podzol (×3)<br/>Packed Ice<br/>                       | 6                    |
| 5     | Bucket of Pufferfish<br/>Bucket of Tropical Fish<br/> | 4                    |
| 6     | Blue Ice<br/>                                         | 6                    |

## Notes
1. ↑There is 0.04% chance for zombies and skeletons to spawn with diamond armor, but the chance is so negligible that it is infeasible to obtain diamond armor in this way.
2. ↑ a b c d e f g h i j k l m n o p q r s t u v w x y z aa ab ac ad ae af agWhen creating an enchantment offer, the game uses a random enchantment level from 5 – 19. The enchantments are never treasure enchantments.
3. ↑ a b c d e f g h i j k l m n o p q r s t u v w x y z aa ab ac ad ae af ag ah ai aj ak al am an ao ap aq ar asAs the villager cannot level up any further, they do not actually gain any experience.
4. ↑ a b c d eAll copies of the map traded by a particular villager lead to the same structure. In worlds that do not have the structure, this trade is not offered.
5. ↑ a b c d e f g h iThe list of possible offers contains individual offers for each color, so multiple colors may be offered by the same villager as separate trades.
6. ↑Available maps listed in the following table. They are divided into 3 groups, each of them is a individual offer, so multiple groups may be offered by the same villager as separate trades. Inside the group, trade is selected based on biomes.
7. ↑ a bThe type of boat trade depends on the biome outfit of the villager. Plains villagers buy oak boats, taiga and snowy villagers buy spruce boats, desert and jungle villagers buy jungle boats, savanna villagers buy acacia boats, and swamp villagers buy dark oak boats.
8. ↑The type of arrow is chosen randomly from all possible brewable potions with effects, including extended and strengthened versions. This is a single offer in the offer list (like enchanted books), not one offer per type (like various colored items).
9. ↑ a b c d e f g h i j k l m nThe leather armor has a random color created by two dyes (possibly the same dye twice.)
10. ↑ a b c d e f g hThe enchantment is chosen randomly with equal chance of any enchantment type occurring (except for Soul Speed and Swift Sneak) and equal chance to get any level of the enchantment, meaning high-level enchantments are as likely as low-level enchantments. It is possible for a librarian to sell the same book more than once.
The price in emeralds depends on the enchantment level and "treasure" status. The minimum price of a book is given by 2 + 3 * (enchantment level), while the maximum price is 6 + 13 * (enchantment level). The possible values are 5–19 emeralds for Lvl I, 8–32 for Lvl II, 11–45 for Lvl III, 14–58 for Lvl IV, and 17–71 for Lvl V. For treasure enchantments the price is doubled. The cost is capped at 64 emeralds. All values below this cap are equally probable.
11. ↑ a bThe trade is listed as two book and quill items, but because there is only one trading input slot, and books and quills cannot stack, the player needs to exchange only one book and quill in the trade.
12. ↑ a b cThe enchantment is chosen randomly from the "Common" enchantments listed on the table below according to the biome of the villagers. Every levels of these enchantment has equal chance to be chosen, meaning high-level enchantments are as likely as low-level enchantments. It is possible for a librarian to sell the same book more than once.
The price in emeralds depends on the enchantment level and "treasure" status. The minimum price of a book is given by 2 + 3 * (enchantment level), while the maximum price is 6 + 13 * (enchantment level). The possible values are 5–19 emeralds for Lvl I, 8–32 for Lvl II, 11–45 for Lvl III, 14–58 for Lvl IV, and 17–71 for Lvl V. For treasure enchantments the price is doubled. The cost is capped at 64 emeralds. All values below this cap are equally probable.
13. ↑The enchantment is set from the "Special" enchantments listed on the table below according to the biome of the villagers. Unlike common enchantments, the level of enchantment is also defined.
The price in emeralds depends on the enchantment level and "treasure" status. The minimum price of a book is given by 2 + 3 * (enchantment level), while the maximum price is 6 + 13 * (enchantment level). The possible values are 5–19 emeralds for Lvl I, 8–32 for Lvl II, 11–45 for Lvl III, 14–58 for Lvl IV, and 17–71 for Lvl V. For treasure enchantments the price is doubled. The cost is capped at 64 emeralds. All values below this cap are equally probable.
14. ↑ a bIf explorer maps are bought when in the Nether, the End or a superflat world, the explorer map does not show a destination structure, and buying it in an Old world causes the game to freeze
15. ↑The stew grants one of the following effects: 5-7 seconds of Blindness, 7-10 seconds of Jump Boost, 7-10 seconds of Night Vision, 10-20 seconds of Poison, 0.3-0.35 seconds of Saturation, or 6-8 seconds of Weakness.
16. ↑Potion level is always I, except for Arrow of Decay, which is always II
17. ↑Book and quill is offered in two item slots due to being non-stackable
18. ↑Only one item is offered (e.g. wandering trader cannot sell both brown dye and pink dye). Each group of single-offer trades has the same chance to be chosen as a normal trade based on weight. For example, each individual sapling does have the same chance of being offered as a slimeball, because the sapling group as a whole which consist of 4 items and has 4 weight (multiple saplings cannot be offered however).
19. ↑ a b c d e f g hCrop seeds offered in both grouped and individual trades



