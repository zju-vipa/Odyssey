# Villager (old)
Villagers are passive mobs that inhabit villages, work at their professions, breed, and interact with each other. Their clothing varies according to their occupation. A player can trade with villagers, using emeralds as currency. Villagers received a complete overhaul of both their appearance and their functionality in the Village & Pillage update; this page covers villagers as they appeared and behaved before the update.

## Contents
- 1 Spawning
	- 1.1 Spawn eggs
	- 1.2 Natural generation
	- 1.3 Baby villagers
	- 1.4 Curing
- 2 Drops
- 3 Behavior
	- 3.1 Movement patterns
	- 3.2 Picking up items
	- 3.3 Sharing food
	- 3.4 Farming
	- 3.5 Baby villager behavior
	- 3.6 Zombies
	- 3.7 Lightning
- 4 Breeding
	- 4.1 Willingness
- 5 Professions and careers
	- 5.1 Nitwit
- 6 Trading
	- 6.1 Regeneration
- 7 Sounds
- 8 Data values
	- 8.1 ID
	- 8.2 Entity data
- 9 Achievements
- 10 Advancements
- 11 History
- 12 Trivia
	- 12.1 April fools
- 13 Gallery
- 14 References

## Spawning
### Spawn eggs
In Bedrock Edition, the old villager spawn egg can still be obtained by /give spawn_egg 1 15. Using that spawn egg spawns an old villager with 0 health, which means it dies immediately upon spawning. A new villager spawns after it dies.

### Natural generation
In Java Edition, old villagers can only spawn in versions of Minecraft prior to 1.14. In Bedrock Edition, old villagers can only spawn if they existed from a template world prior to 1.11.0, and any old villager spawned after 1.11.0 outside a template world is converted into villager_v2.

### Baby villagers
Villagers breed autonomously, but need doors and need to be willing in order to spawn baby villagers. After exactly 20 minutes during which the baby villager is within render distance, the baby villager grows up to an adult. See this section for more information.

### Curing
Villagers spawn if a player uses a splash potion of weakness on a v1 zombie villager in template world and then feeds it a regular golden apple. It then shakes and turn into a villager within 0-5 minutes. During the change, the zombie villager can still burn in the sun.

## Drops
Villagers drop nothing upon death.

Trade: 3–6 xp
Trade while willing: 8–11 xp

## Behavior
### Movement patterns
Upon spawning, villagers leave their homes and begin to explore the village. Generally, they wander aimlessly inside the village during the day. They may go indoors or outdoors, and they periodically make mumbling sounds. Occasionally, two villagers may stop and turn to look at each other, in a behavior called socializing, in which they stare at another villager for 4-5 seconds at a time. In the case of players, they continuously stare at them as long as the player is close enough, unless the villager tries to get into a house at night, farm food, or flee from a zombie.

In Legacy Console Edition, when a player attacks a villager, the villager does not run away, but anger particles fly out from the villager if it is in a village. In Bedrock Edition, villagers do not stop continuously in front of players. They also sprint away if the player attacks them.

Villagers, like other mobs, find paths around obstructions, avoiding walking off cliffs and some blocks that cause harm. However, in crowded situations it is possible for one villager to push another off a cliff or into harm. Villagers also occasionally walk off of ledges high enough to cause fall damage.

At night or during rain, villagers run inside, closing doors behind them, and staying indoors until morning. In the morning they head outside and resume normal behavior.

Villagers flee from zombies, illagers and vexes within 8 blocks.

If a villager finds itself outside the village boundary, or a villager without a village detects a village boundary within 32 blocks, it moves quickly back within the boundary. A villager taken more than 32 blocks away from its village boundary forgets the village within about 6 seconds. Whether in a village or not, a villager is never prone to despawning.

Villagers cannot open trapdoors, fence gates, or iron doors.

There is evidence that villagers are prone to overcrowding certain areas of a village while leaving other areas completely empty. When moving inside, the AI prefers doors within 16 blocks (Euclidean distance). It also tends to prefer doors with fewer villagers nearby, however "nearby" in this case is only 1.5 blocks and, when moving inside, villagers prefer to move 2.5 blocks inside when the inside is to the south or east and therefore go out of range of this check. During the day, it has been observed that villagers tend to cluster near a trapped villager or any existing large cluster of villagers, likely due to the "socialize" AI routine overriding their inclination to wander.

### Picking up items
Villagers have eight hidden inventory slots, which start empty whenever the villager is spawned. Villagers do not intentionally seek out items to pick up, but they collect any bread, carrots, potatoes, wheat, seeds, beetroot and beetroot seeds they happen to come within range of. These are the only items they are able to pick up, though the player may use the /replaceitem command to put an arbitrary item into a villager's inventory. If a player and a villager are in the pickup range of an item at the same time, the player always picks it up first.

Even when gamerule keepInventory is set to false, villagers that are killed with any of the available items above do not drop them once they are killed.

Any items in these slots are lost if a villager becomes a zombie villager; a zombie villager has no inventory slots.

If /gamerule mobGriefing is false, villagers do not pick up items.

A dispenser can be used, if adjacent to a villager, to place armor on it. While not visible in most cases (other than pumpkins and mob heads) the equipment is fully functional; for example, the Thorns enchantment hurts zombies that attack a villager with a piece of armor enchanted with the Thorns enchantment equipped.

### Sharing food
If a villager has enough food in one inventory stack (6 bread or 24 carrots, potatoes, beetroots, or 18 wheat for farmers only) and sees a villager without enough food in one inventory stack (3 bread or 12 carrots, potatoes or beetroot for non-farmers; 15 bread, 60 carrots, potatoes, or beetroot, or 45 wheat for Farmers), the villager may decide to share food with that villager.

To share, a villager finds its first inventory stack with at least 4 bread, carrots, potatoes, or beetroot or with at least 6 wheat, and then throws half the stack (rounded down) in the direction of the target villager. When wheat is shared, it is first crafted to bread which may result in 1 or 2 less than half the stack being shared.

### Farming
Adult and baby brown-robed villagers, both farmers and other careers, tend crops within the village boundary. Villagers far enough outside the boundary of any village also tend nearby crops.

Farmland to be tended is found by seeking for certain blocks up to 15 blocks away from the villager in X and Z and up to 1 away in Y (a 31×31×3 area total).

- If a brown-robed villager does not have enough food in one stack in its inventory (15 bread, 60 carrots, potatoes, or beetroot, or 45 wheat) and finds fully-grown wheat, carrots, potatoes or beetroot, it moves to the crop block and break it.
- If a brown-robed villager has any seeds, carrots, potatoes, or beetroot seeds in its inventory and finds an air block above farmland, it moves to it and plant a crop. They always plant from the first eligible slot in their inventory.
- If/gamerule mobGriefingisfalse, villagers cannot farm.

### Baby villager behavior
A group of baby villagers playing a game of tag.
Baby villagers sprint around, entering and leaving houses randomly. They sometimes stop sprinting to stare at an iron golem. If the iron golem is holding a poppy, it might attract any baby villagers near it.

Baby villagers in Bedrock/Legacy Console Editions have a slightly bigger head than in the Java Edition, this also can be seen in different baby mobs in the game as well.

Unlike other breed-able mobs, the parents and child have no personal interactions other than socializing.

### Zombies
Main articles: Siege and Zombie
Zombies try to find and attack villagers within a 42 block radius (even when the villager is invisible), and attempt to break down doors. Zombies successfully break doors only if the difficulty is set to hard, although only a fraction of zombies spawned in Hard mode have the capacity to break doors. This also applies to zombie pigmen if they path find through a door. Villagers flee from zombies, sometimes hiding in houses. The villager's only "natural" defense are the iron golems, which attack nearby hostile mobs. 

Zombies try to kill villagers, or convert them to v1 zombie villagers. The chance for a villager to become a zombie villager on death is 0% on Easy, 50% on Normal, and 100% on Hard. Baby villagers can be infected by zombies as well.

Villagers also flee from zombie pigmen, although the latter do not attack them.

Drowned chase and attack villagers in the same way as zombies, and villagers run from drowned in the same way they run from zombies. Drowned can also convert villagers to zombie villagers, even when attacking from a distance with a trident.

### Lightning
When lightning strikes within 3–4 blocks of a villager, it turns into a witch.

## Breeding
See also: Tutorials/Legacy Console village mechanics

Two villagers mating.
Villagers mate depending on the number of valid doors. If "willing" (see below), villagers mate as long as the population is less than 35% (Bedrock Edition: 100%) of valid doors, rounded down. The type of villager that spawns is independent of the villager's parents.

A valid door is any door within the village radius where the number of "outside" spaces within 5 blocks in a straight line on one side of the door is not the same as the number of "outside" spaces within 5 blocks on the other side of the door. A space is considered to be "outside" if it has nothing but transparent blocks above it all the way to the sky.

A census is periodically taken to determine the current population of the village. All villagers within the horizontal boundary of the village and within 5 vertical blocks (Bedrock Edition: no apparent height limit) of the center is counted as part of the population to determine if continued villager mating is allowed. However, any villager within the horizontal boundary of the village and within the spherical boundary of the village attempts to enter mating mode as long as there is at least one villager within the boundary. If two villagers simultaneously enter mating mode while they are close to one another, they mate with each other and produce a child.

### Willingness
Additionally, villagers must be "willing" in order to breed. After mating, they are no longer willing, and must be made willing again.

Villagers can become willing by having either 3 bread, 12 carrots, 12 potatoes, or 12 beetroots in one stack in their inventory. Any villager with an excess of food (usually farmers) throw food to other villagers, allowing them to pick it up and obtain enough food to become willing. The player can also throw bread, carrots, beetroots, or potatoes at the villagers themselves to encourage breeding. Villagers consume the required food upon becoming willing. 

Villagers may also become willing when the player trades with them. Willingness is granted the first time a new offer is traded, or at a one-in-five chance on subsequent trades. Most of the time, villagers becomes willing after the second or third trade. Green particles appear if the villager becomes willing by trading. This does not cause them to immediately seek out a mate, however.

Before Java Edition 1.8, willingness was not implemented. The only factor needed is enough valid doors.

## Professions and careers
Each villager has a profession, which can be identified by their clothing. Villagers also have careers specific to their profession. The player can identify a villager's career by reading the title at the top of the trading interface.

Below is a table listing the various villagers, with their careers in relation to their professions, as well as the IDs specifying these. While each profession has a 1 in 6 chance (16.67%) of occurring, the probabilities for individual careers to occur are more diversified. They are listed in the table as well.

| Clothing | Profession    | Profession ID | Career        | Career ID | Probability           | Combined Probability  |
|----------|---------------|---------------|---------------|-----------|-----------------------|-----------------------|
|          | Farmer        | 0             | Farmer        | 1         | $\frac{1}{24}$(4.17%) | $\frac{1}{6}$(16.67%) |
|          |               |               | Fisherman     | 2         | $\frac{1}{24}$(4.17%) |                       |
|          |               |               | Shepherd      | 3         | $\frac{1}{24}$(4.17%) |                       |
|          |               |               | Fletcher      | 4         | $\frac{1}{24}$(4.17%) |                       |
|          | Librarian     | 1             | Librarian     | 1         | $\frac{1}{12}$(8.33%) | $\frac{1}{6}$(16.67%) |
|          |               |               | Cartographer  | 2         | $\frac{1}{12}$(8.33%) |                       |
|          | Priest/Cleric | 2             | Cleric        | 1         | $\frac{1}{6}$(16.67%) | $\frac{1}{6}$(16.67%) |
|          | Blacksmith    | 3             | Armorer       | 1         | $\frac{1}{18}$(5.56%) | $\frac{1}{6}$(16.67%) |
|          |               |               | Weapon Smith  | 2         | $\frac{1}{18}$(5.56%) |                       |
|          |               |               | Tool Smith    | 3         | $\frac{1}{18}$(5.56%) |                       |
|          | Butcher       | 4             | Butcher       | 1         | $\frac{1}{12}$(8.33%) | $\frac{1}{6}$(16.67%) |
|          |               |               | Leatherworker | 2         | $\frac{1}{12}$(8.33%) |                       |
|          | Nitwit        | 5             | Nitwit        | 1         | $\frac{1}{6}$(16.67%) | $\frac{1}{6}$(16.67%) |

When a villager is transformed into a zombie villager, the profession of the zombie villager remains unchanged. However, the career is reset and randomly picked again if the zombie villager is cured, allowing for the player to get a villager with a new career and new trade offers. Old trade offers disappear, even if the same career is chosen again.

### Nitwit
|  | “ | It started because players could summon villagers without a career by using commands: it was the only way to get villagers with green robes. Whenever we discover we have a bug which is used by the community we just see it as 'undefined behaviour' - and 'fix' it by making it a feature. In this case we just needed a profession for the green-robed villager. I don't remember what name we came up with first - I think it was 'unemployed' or something, but it doesn't really fit in the world, because I don't really think the other villagers are employed by anyone either. So I think the next suggestion was 'village idiot' but I thought 'nitwit' was a more fun name. | „ |
|--|---|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
|  |   | — Jeb about the Nitwit[1]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |   |

The nitwit villager is a villager that wears a green robe and cannot be traded with.

## Trading
Main article: Trading/Before Village and Pillage
The pre-1.14 trading interface displaying a trade of 35 paper for 1 emerald.
|  | “ | Right click on a villager and you can trade with them, offering them emeralds in exchange for better equipment, maps to notable treasures or food. Unless you are trying to trade with a nitwit, of course, in which case you're going to get squat. Who's the nitwit now? | „ |
|--|---|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
|  |   | — Marsh Davies[2]                                                                                                                                                                                                                                                          |   |

The trading system is a gameplay mechanic that allows players to trade emeralds for items and vice-versa with villagers. Their trades can be good or bad, depending on what the cost is and what items you might get. Trading is only available for adult villagers; the player cannot trade with baby villagers or the nitwit villager.

Right-clicking a villager allows a player to trade with them, and display their career. Villagers make offers based on their profession and career, and trade based on whatever offers they are making. Different offers may be viewed by pressing the left and right buttons next to the currently displayed offer. All offers involve emerald as a currency, and some item pertinent to the villager's profession and career. Trading allows the acquisition of rare items that would otherwise be fairly difficult to obtain, such as chain armor. The trading mechanic allows players to get bottle o' enchanting in survival mode. When villagers get a new trade, pink particles and green cross particles appear.

After trading a new offer once, the villager allows a new tier of offers. After 2-12 times an offer is repeated, the villager locks the trade offer. That is, the villager no longer offers this trade. When this happens, the player must use another new trade offer in the villager's window once (or several times if it is already used once), and then wait for a short time. If green particles appear, all trades unlock. That is, the villager starts offering all trades. There is a maximum number of tiers each villager can possess, varying by career. Once the villager has unlocked all tiers, it does not open any new ones. However, players can still renew all offers by trading.

### Regeneration
When a villager gives off particles from a new trade, they get 10 seconds of Regeneration I, which gives them 4.

Commands or external editors can help villagers get new trades. 

If a villager unintentionally picks up certain seeds or crops, it throws it to another villager to simulate trading between the villagers.

## Data values
### ID
Java Edition:

| Name     | Identifier | Translation key             |
|----------|------------|-----------------------------|
| Villager | `villager` | `entity.minecraft.villager` |

Bedrock Edition:

| Name     | Identifier | Numeric ID | Translation key        |
|----------|------------|------------|------------------------|
| Villager | `villager` | `15`       | `entity.villager.name` |

### Entity data
See also: Chunk format

Villagers have entity data associated with them that contains various properties.



- Entity data
	- 
	- Tags common to all entities
	- 
	- Tags common to all mobs
	- 
	- Additional fields for mobs that can breed
	- Profession: TheIDof the texture used for this villager. This also influences trading options.
	- Riches: Currently unused. Increases by the number of emeralds traded to a villager any time they are traded.
	- Career: TheIDof this villager's career. This also influences trading options and the villager's name in the GUI (if it does not have a CustomName). If 0, the next time offers are refreshed, the game assigns a new Career and resets CareerLevel to 1.
	- CareerLevel: The current level of this villager's trading options. Influences the trading options generated by the villager; if it is greater than their career's maximum level, no new offers are generated. Increments when a trade causes offers to be refreshed. If 0, the next trade to do this assigns a new Career and sets CareerLevel to 1. Set to a high enough level causes no new trades to release (Career must be set to 1 or above).
	- Willing: 1 or 0 (true/false) - true if the villager is willing to mate. Becomes true after certain trades (those which would cause offers to be refreshed), and false after mating.
	- Inventory: Each compound tag in this list is an item in the villager's inventory, up to a maximum of 8 slots. Items in two or more slots that can be stacked together are automatically condensed into one slot. If there are more than 8 slots, the last slot is removed until the total is 8. If there are 9 slots but two previous slots can be condensed, the last slot remains after the two other slots are combined.
		- An item in the inventory, excluding the Slot tag.
			- 
			- Tags common to all items
	- Offers: Is generated when the trading menu is opened for the first time.
		- Recipes: List of trade options.
			- A trade option.
				- rewardExp: 1 or 0 (true/false) - true if this trade provides XP orb drops. All trades from naturally-generated villagers in Java Edition reward XP orbs.
				- maxUses: The maximum number of times this trade can be used before it is disabled. Increases by a random amount from 2 to 12 when offers are refreshed.
				- uses: The number of times this trade has been used. The trade becomes disabled when this is greater or equal to maxUses.
				- buy: The first 'cost' item, without the Slot tag.
					- 
					- Tags common to all items
				- buyB: May not exist. The second 'cost' item, without the Slot tag.
					- 
					- Tags common to all items
				- sell: The item being sold for each set of cost items, without the Slot tag.
					- 
					- Tags common to all items

