# Egg
An egg is an item that can be used to craft food items, or thrown for a chance to spawn baby chickens on impact.

## Contents
- 1 Obtaining
	- 1.1 Mob loot
	- 1.2 Chest loot
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Combat
	- 2.3 Spawning chickens
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Entity data
- 5 Achievements
- 6 Advancements
- 7 Video
- 8 History
- 9 Issues
- 10 Trivia
- 11 References

## Obtaining
### Mob loot
See also: Tutorials/Egg farming

Every adult chicken lays an egg item every 5–10 minutes, except for those that are or were a part of chicken jockeys. The theoretical average would be expected at 1 egg every 7.5 minutes (9000 GT).

A fox has a 3% chance of spawning with an egg in its mouth, which it will drop upon death. Alternatively, a player dropping a food item causes the fox to drop the egg.

### Chest loot
| Item | Structure      | Container         | Quantity | Chance          |
|------|----------------|-------------------|----------|-----------------|
|      |                |                   |          | Java Edition    |
| Egg  | Trial Chambers | Chamber dispenser | 4–8      | 6.9%            |
|      | Village        | Fletcher's chest  | 1–3      | 23.3%           |
|      |                |                   |          | Bedrock Edition |
| Egg  | Village        | Fletcher's chest  | 1–3      | 23.3%           |

## Usage
### Crafting ingredient
| Name        | Ingredients                 | Crafting recipe | Description                                                      |
|-------------|-----------------------------|-----------------|------------------------------------------------------------------|
| Cake        | Milk Bucket+Sugar+Egg+Wheat |                 | Emptybucketsremain in the crafting grid after crafting the cake. |
| Pumpkin Pie | Pumpkin+Sugar+Egg           |                 |                                                                  |

### Combat
Players are able to throw eggs and deal knockback to mobs (but not other players‌[JE  only][1]‌[until JE Combat Tests]), but no damage is dealt, similar to a snowball. Likewise, throwing eggs at neutral mobs provokes them. Eggs can also be fired from dispensers and are affected by gravity.

### Spawning chickens
When thrown by a dispenser or by pressing the use button, an egg has a 1⁄8 (12.5%) chance of spawning a chick. If this occurs, there is a 1⁄32 (3.125%) chance of spawning three additional chicks (on average, 1 out of every 256 eggs spawns 4 chicks). In other words, whenever an egg is thrown, there is a 31⁄256 chance of spawning 1 chick and a 1⁄256 chance of spawning four chicks.

The expected value of the number of chicks an egg produces is 35⁄256 or 13.7%. This means that on average, a chick is spawned every 7.3 eggs, a stack of 16 eggs spawns 2.188 chicks, and a full inventory including the hotbar and off-hand (37 * 16 = 592 eggs) is expected to spawn approximately 81 chicks.

Accounting for all probabilities, the average chicken produces 1.09 chickens per hour when all the eggs it lays are thrown. The formula you can use to find any amount of chickens or time ranges is d=3600÷((450÷c)÷(³⁵⁄₂₅₆)), where d is the drops a chicken has (they both have a average drop of one per chicken slain) and c is the number of chickens laying eggs. 3600 is the number of seconds in an hour, and 450 is the number of average seconds per egg lain.

## Data values
### ID
Java Edition:

| Name | Identifier | Form | Translation key    |
|------|------------|------|--------------------|
| Egg  | egg        | Item | item.minecraft.egg |

| Name       | Identifier | Entity tags        | Translation key      |
|------------|------------|--------------------|----------------------|
| Thrown Egg | egg        | impact_projectiles | entity.minecraft.egg |

Bedrock Edition:

| Name | Identifier | Numeric ID | Form | Translation key |
|------|------------|------------|------|-----------------|
| Egg  | egg        | 390        | Item | item.egg.name   |

| Name | Identifier | Numeric ID | Translation key |
|------|------------|------------|-----------------|
| Egg  | egg        | 82         | entity.egg.name |

### Entity data
Thrown eggs have entity data that define various properties of the entity.

Java Edition:

Main article: Entity format

 Entity data
Tags common to all entities
Tags common to all projectiles
 Item: The item to render as, may be absent.
Tags common to all items

Bedrock Edition:

See Bedrock Edition level format/Entity format.
