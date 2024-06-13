### Selecting an enchantment level
As enchantments offered depend on the enchantment level and the enchantment level depends on the number of active bookshelves, an easy way to change the enchantments offered is to disable bookshelves by placing torches between them and the enchanting table. That way one can still have the entire 'ring' of bookshelves around the table but get lower-level enchantments. Breaking the torches restores the effect of the bookshelves.

#### Bedrock Edition

With the layout shown here, enchantments with any number of bookshelves from 0 to 15 may be easily obtained:

|  |  |  |  | Active bookshelves |
|--|--|--|--|--------------------|
|  |  |  |  | 0                  |
|  |  |  |  | 1                  |
|  |  |  |  | 2                  |
|  |  |  |  | 3                  |
|  |  |  |  | 4                  |
|  |  |  |  | 5                  |
|  |  |  |  | 6                  |
|  |  |  |  | 7                  |
|  |  |  |  | 8                  |
|  |  |  |  | 9                  |
|  |  |  |  | 10                 |
|  |  |  |  | 11                 |
|  |  |  |  | 12                 |
|  |  |  |  | 13                 |
|  |  |  |  | 14                 |
|  |  |  |  | 15                 |

#### Java Edition

With the layout shown here, enchantments with any number of bookshelves from 0 to 15 may be easily obtained:

|  |  |  | Active bookshelves |
|--|--|--|--------------------|
|  |  |  | 0                  |
|  |  |  | 1                  |
|  |  |  | 2                  |
|  |  |  | 3                  |
|  |  |  | 4                  |
|  |  |  | 5                  |
|  |  |  | 6                  |
|  |  |  | 7                  |
|  |  |  | 8                  |
|  |  |  | 9                  |
|  |  |  | 10                 |
|  |  |  | 11                 |
|  |  |  | 12                 |
|  |  |  | 13                 |
|  |  |  | 14                 |
|  |  |  | 15                 |

## How enchantments are chosen
"Enchantment level" is the required experience level (the green number on the bottom-right).
"Enchantment power" is the strength of the particular enchantment. For example, "Sharpness IV" has a power of 4.
The enchantment algorithm uses a three-step process.

### 
The first thing that Minecraft does is apply two modifiers to the base enchantment level. Each modifier is restricted to a certain range, with numbers close to the middle of the range more common than those near the ends.

The first modifier is based on the item's "enchantability," which depends on the material and the type of the item (see the table below). Other enchantable items such as books, bows, crossbows, tridents, and fishing rods have an enchantability of 1 for this purpose. Minecraft picks a number between 0 and half the enchantability, then adds that number plus one to the enchantment level.  This random value follows a triangular distribution (like rolling a pair of dice and adding) so results close to a quarter of the enchantability are much more likely than results at the extremes.

The modified enchantment level is calculated with the following formula:

Modified enchantment level =B+R1+R2+ 1
Where:

- R1andR2are two individual randomly generated integers:
	- R1= randomInt(0, E / 4)
	- R2= randomInt(0, E / 4)
- Bis the base enchantment level.
- Eis the enchantability of the item.

Division is rounded down.

#### Enchantability
| Material  | Armor enchantability | Sword/Tool enchantability |
|-----------|----------------------|---------------------------|
| Wood      | N/A                  | 15                        |
| Leather   | 15                   | N/A                       |
| Stone     | N/A                  | 5                         |
| Chain     | 12                   | N/A                       |
| Iron      | 9                    | 14                        |
| Gold      | 25                   | 22                        |
| Diamond   | 10                   | 10                        |
| Turtle    | 9                    | N/A                       |
| Netherite | 15                   | 15                        |
| Other     | 1                    | 1                         |

Next, Minecraft picks a value between 0.85 and 1.15, again with a triangular distribution. The modified enchantment level is multiplied by this value (so it could increase or decrease by up to 15%) and then rounded to the nearest integer.

#### Step one pseudocode
// Returns a uniformly distributed random integer between 0 and n–1, inclusive
function randomInt(n);

// Returns a uniformly distributed random real (fractional) number between 0 (inclusive) and 1 (exclusive)
function randomFloat();

// Returns the real number n rounded to the nearest integer.
function round(n);


// Generate a random number between 1 and 1+(enchantability/2), with a triangular distribution
int rand_enchantability = 1 + randomInt(enchantability / 4 + 1) + randomInt(enchantability / 4 + 1);

// Choose the enchantment level
int k = chosen_enchantment_level + rand_enchantability;

// A random bonus, between .85 and 1.15
float rand_bonus_percent = 1 + (randomFloat() + randomFloat() - 1) * 0.15;

// Finally, we calculate the level
int final_level = round(k * rand_bonus_percent);
if ( final_level < 1 ) final_level = 1

The source is Minecraft 1.8 source code.

