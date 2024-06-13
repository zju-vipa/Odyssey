#### Pathfinding
Villagers, like other mobs, can find paths around obstructions, avoid walking off cliffs of heights greater than 3 blocks, and avoid some blocks that cause harm. However, in crowded situations, one villager can push another off a cliff or into harm's way.

Villagers can open all wooden doors and find paths to blocks of interest behind the doors. However, they cannot open any trapdoors, fence gates, or iron doors. Villagers can climb ladders, but do not recognize them as paths and do not deliberately use them. Any climbing of ladders seems to be a side effect of them being pushed into the block by another mob (usually by other villagers).

#### Stranded villagers
Climbing a ladder can leave a villager stranded on the second floor and roof of some village structures, as they lack the necessary AI to intentionally descend ladders.[verify] A simple fix for these situations is for the player to manually push the villager back toward the ladder hole. Then the player can place a wooden trapdoor at the top, to stop the villager from ever getting up there again. However, the villager can still get stuck on the ladder underneath the trapdoor. Another solution is to break the first ladder touching the ground, completely preventing the villager from climbing the ladder. However, this means the player has to jump up one block to use the ladder.

#### Getting attacked
Villagers flee from zombies, zombie villagers, husks, drowned, zombified piglins ‌[Bedrock Edition  only], zoglins, vindicators, pillagers (even if their crossbow has been broken), ravagers, and vexes within 8 blocks, and evokers and illusioners within 12 blocks. Like other passive mobs, villagers sprint away when attacked. Villagers do not run away from skeletons (and their variants), spiders, or cave spiders since these hostile mobs are passive toward villagers, although a skeleton arrow might hit a villager by accident.

##### Preferred path

  

This feature is exclusive to  Bedrock Edition. 


When pathfinding, villagers prefer to stay on low cost blocks, such as dirt paths, cobblestone, bricks, and planks. They do this by trying to minimize the path cost of all of the blocks they walk across. They also avoid jumping, because it has a high path cost, but babies don't avoid it as much.

| Preferred path blocks                                                                                                                                                                                                                                                                                | Path cost      |               |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|---------------|
|                                                                                                                                                                                                                                                                                                      | Adult villager | Baby villager |
| Dirt Path                                                                                                                                                                                                                                                                                            |                | 0             |
| Cobblestone<br/>Stone Stone Bricks Sandstone Mossy Cobblestone Slabs Planks Bricks Nether Bricks Red Nether Bricks End Stone Bricks Red Sandstone Stained Glass Glass Glowstone Prismarine Block of Emerald Block of Diamond Block of Lapis Lazuli Block of Gold Block of Redstone Glazed Terracotta |                | 1             |
| Beds<br/>Lectern Composter Grindstone Blast Furnace Smoker Fletching Table Cartography Table Brewing Stand Smithing Table Cauldron Barrel Loom Stonecutter                                                                                                                                           |                | 50            |
| Other                                                                                                                                                                                                                                                                                                | 3              | 1.5           |
| Jump cost                                                                                                                                                                                                                                                                                            | 20             | 5             |

### Job site blocks
For a list of job site blocks and the professions they are required for, see  § Professions.

Unemployed villagers (other than babies and nitwits) seek employment at job site blocks (also referred to as workstations), and employed villagers use job site blocks to refresh their trades (see § Working). Villagers who have made their first trade must claim a site block that corresponds with their profession, whereas tradeless villagers may change their profession to match a site block. 

In Java Edition, an unemployed villager claims job site blocks by searching for the nearest unclaimed site in a 48-block sphere. When a suitable site block is detected, the villager starts pathfinding to it, staking a provisional claim. This can occur only while the villager is awake. A provisional claim is released if the villager cannot reach the block within 60 seconds, however the villager may try again immediately.[1] To fully claim the site and change profession, the villager must approach within a 2-block radius of the job site's center. When a job site block is fully claimed, its owner emits green particles, and no other villager can claim the block unless the owner relinquishes it. 

In Bedrock Edition, all villagers in a village search for unclaimed job sites in a 16 block radius and 4 block height. If a site block is found, it is added to a shared list of valid job site blocks for the whole village. An unemployed villager with a bed claims the first site block on that list and immediately acquires the profession to match, regardless of the distance or accessibility to the site block.[2] The villager can even claim the site block while sleeping. When a job site block is claimed, both the block and the villager making the claim emit green particles and the site block is removed from the list. If a villager cannot pathfind to its claimed site, both the site block and villager emit anger particles. The site block may need to be broken before the villager unclaims it.[verify]

A desert villager and a plains villager gossiping.
### Gossiping
Villagers can store memories about players in the form of gossip. These get spread to other villagers whenever they talk with each other. Each piece of gossip is one of five types, and it stores a value as well as a target. Gossips generate and increase in value as a result of various player actions. The target is the player who caused the gossip. Together the gossip values determine a player's reputation with each villager, which influence trading prices and the hostility of naturally spawned iron golems.

| Type           | Caused by | Amount gained | Decay | Share penalty | Max value | Reputation multiplier |
|----------------|-----------|---------------|-------|---------------|-----------|-----------------------|
| Major positive | Curing    | 20            | 0     | 100           | 20        | 5                     |
| Minor positive | Curing    | 25            | 1     | 5             | 200       | 1                     |
| Minor negative | Attacking | 25            | 20    | 20            | 200       | -1                    |
| Major negative | Killing   | 25            | 10    | 10            | 100       | -5                    |
| Trade          | Trading   | 2             | 2     | 20            | 25        | 1                     |

Trading with or curing a villager increase the value of the corresponding gossips for the targeted villager only. When a villager is attacked or killed, however, it instead generates the major negative gossip in every other villager it could see (eye-to-eye line of sight) inside a box extending 16 blocks from the villager in all coordinate directions.

When a piece of gossip is shared, it is received at a lower value than the sharer has it. Gossips also decay a certain amount (see Decay column) every 20 minutes. Since major positive gossip have a share penalty equal to its max value and a decay of 0, it cannot be shared and never decays.

A player's total reputation with a villager is determined by multiplying each gossip's value by its respective multiplier and adding the results together. For example, if a player has recently cured a villager for the first time but also attacked the villager twice, their reputation with that villager would be 5×20 + 25 - 50 = 75. After 40 minutes the gossips have decayed twice, making the player's reputation 5×20 + 23 - 10 = 113.

The prices of a villager's trades all get reduced by reputation times the price multiplier rounded down, meaning that a positive reputation lowers prices but a negative reputation increase them. The price multiplier is either 0.05 or 0.2 depending on the item, see trading. Prices can not get lower than 1 or higher than the item's stack size. The exact function to calculate the price affected by the gossips is y = x - floor((5a + b + c - d - 5e) × p), Where y is the final price, x is the base price, a is the value of major_positive, b is the value of minor_positive, c is the value of trading, d is the value of minor_negative, e is the value of major_negative, and p is the value of PriceMultiplier.

An iron golem that was not built by a player becomes hostile toward all players whose reputation with any nearby villager is -100 or lower. The golem checks all villagers inside a box centered on the golem and extending 10 blocks in every horizontal direction and 8 blocks in both vertical directions.

Players can set villagers on fire using flint and steel or lava without affecting gossips. The same is true for TNT activated by redstone or a dispenser. However, TNT ignited directly by a player (using flint and steel, fire charges or flaming arrows) does generate gossip for damaged or killed villagers, because the TNT's damage is attributed to the player.

