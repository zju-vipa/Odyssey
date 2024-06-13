# Hero of the Village
Hero of the Village (or village hero) is a status effect granted to the player upon defeating a raid.

## Contents
- 1 Effect
	- 1.1 Animation
	- 1.2 Price decrement
	- 1.3 Gifts
- 2 Causes
- 3 Data values
	- 3.1 ID
- 4 Achievements
- 5 Advancements
- 6 History
- 7 Issues
- 8 References

## Effect
Players receive gifts‌[JE  only] and discounts from villager trades while under the effect, which lasts 40 minutes. It does not affect the wandering trader's trades.

### Animation
The Bedrock Edition animation for the Hero of the Village effect activating.
In Bedrock Edition, upon the effect being given a short animation of the effect icon appearing on the screen plays, similar to a Totem of Undying.

### Price decrement
Level I Hero of the Village decreases the cost of the first item in a trade by 30%; each additional level decreases the price by an additional 1⁄16 (6.25%). In Survival, the maximum level is V‌[JE  only] or I‌[BE  only], giving discounts of 55% and 30%, respectively. Nevertheless, one can use commands to give higher levels of the effect. Hero of the Village XII gives a discount of 98.75%, decreasing all prices to 1. No matter how large the discount is, the final item count in the trade is always at least one, never zero. In other cases, the decrement is the discount ratio multiplied by the original count rounded down or rounded up if the decrement is less than 1.

Example: Level III would give a 42.5% discount. For trade with 14 emeralds as the cost, the discount would be 5 emeralds (rounded down from 5.95 emeralds), for a final price of 9 emeralds.

The formula can be written as Discounted price = Initial price  - max[1, floor(Initial Price × (0.0625 × (Level  - 1) + 0.3))].

Hero of the Village is a status effect and can be removed through all conventional methods, such as drinking milk, using Totem of Undying, or dying.‌‌[Java Edition  only]

### Gifts

  

This feature is exclusive to  Java Edition. 


Upon obtaining the effect, villagers randomly throw items from a certain pool at the player as rewards, listed below. In order for a player to have gifts thrown to them, they must have Hero of the Village, the villager must be able to see them, and they must be within 5 blocks of the villager. After throwing a gift, a villager enters a cooldown lasting between 30 seconds and 5min 30 sec. Villagers give gifts only while idle, working, or meeting at the town center (bell). They do not give gifts during the night when they should be sleeping.

| Type of villager   | Gift pool                                                                                                                                                                                                                                                                                                                      |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Baby               | Poppy<br/>                                                                                                                                                                                                                                                                                                                     |
| Armorer            | Chainmail Helmet<br/>Chainmail Chestplate<br/>Chainmail Leggings<br/>Chainmail Boots<br/>                                                                                                                                                                                                                                      |
| Butcher            | Cooked Chicken<br/>Cooked Mutton<br/>Cooked Porkchop<br/>Cooked Rabbit<br/>Steak<br/>                                                                                                                                                                                                                                          |
| Cartographer       | Empty Map<br/>Paper<br/>                                                                                                                                                                                                                                                                                                       |
| Cleric             | Lapis Lazuli<br/>Redstone Dust<br/>                                                                                                                                                                                                                                                                                            |
| Farmer             | Bread<br/>Cookie<br/>Pumpkin Pie<br/>                                                                                                                                                                                                                                                                                          |
| Fisherman          | Raw Cod<br/>Raw Salmon<br/>                                                                                                                                                                                                                                                                                                    |
| Fletcher           | Arrow<br/>Arrow of Fire Resistance<br/>Arrow of Harming<br/>Arrow of Healing<br/>Arrow of Invisibility<br/>Arrow of Leaping<br/>Arrow of Night Vision<br/>Arrow of Poison<br/>Arrow of Regeneration<br/>Arrow of Slowness<br/>Arrow of Strength<br/>Arrow of Swiftness<br/>Arrow of Water Breathing<br/>Arrow of Weakness<br/> |
| Leatherworker      | Leather<br/>                                                                                                                                                                                                                                                                                                                   |
| Librarian          | Book<br/>                                                                                                                                                                                                                                                                                                                      |
| Mason              | Clay<br/>                                                                                                                                                                                                                                                                                                                      |
| Shepherd           | Wool<br/>                                                                                                                                                                                                                                                                                                                      |
| Toolsmith          | Stone Axe<br/>Stone Hoe<br/>Stone Pickaxe<br/>Stone Shovel<br/>                                                                                                                                                                                                                                                                |
| Weaponsmith        | Stone Axe<br/>Golden Axe<br/>Iron Axe<br/>                                                                                                                                                                                                                                                                                     |
| Nitwit, Unemployed | Wheat Seeds<br/>                                                                                                                                                                                                                                                                                                               |

If /gamerule mobGriefing is set to true, villagers might pick up seeds and bread that were thrown as gifts if a player doesn't get to them first.

## Causes
| Cause                                            | Potency         | Length | Notes                                                                                                                    |
|--------------------------------------------------|-----------------|--------|--------------------------------------------------------------------------------------------------------------------------|
| Allillagersin the final wave of araidare killed. | I–V ‌[JE  only] | 40:00  | The player must have killed at least one raider. The level is the same as the level ofBad Omenthe raid was started with. |
|                                                  | I ‌[BE  only]   | 40:00  | The player must have killed at least one raider.                                                                         |

Even using the /effect command can give the player the Hero of the Village effect and cause the villagers to decrease prices, give gifts, and increase the player's popularity.

## Data values
### ID
Java Edition:

| Name                | Identifier            | Numeric ID | Translation key                        |
|---------------------|-----------------------|------------|----------------------------------------|
| Hero of the Village | `hero_of_the_village` | `32`       | `effect.minecraft.hero_of_the_village` |

Bedrock Edition:

| Name                | Identifier     | Numeric ID | Translation key      |
|---------------------|----------------|------------|----------------------|
| Hero of the Village | `village_hero` | `29`       | `effect.villageHero` |


