# Ender Pearl
An ender pearl is an item that can be thrown to teleport to where it lands, or used to craft eyes of ender, which are required to access the End.

## Contents
- 1 Obtaining
	- 1.1 Mob loot
	- 1.2 Chest loot
	- 1.3 Trading
	- 1.4 Bartering
- 2 Usage
	- 2.1 Stasis chamber
	- 2.2 Spawning endermites
	- 2.3 Crafting ingredient
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Entity Data
- 5 Achievements
- 6 Advancements
- 7 History
- 8 Issues
- 9 Trivia
- 10 Gallery
	- 10.1 Screenshots
	- 10.2 Concept artwork
- 11 References
- 12 See also

## Obtaining
### Mob loot
An enderman has a 50% chance to drop 1 ender pearl when killed. The drop is increased by 1 per level of Looting, with a maximum of 4 with Looting III.

| Source   | Roll Chance | Quantity (Roll Chance) |           |            |             |
|----------|-------------|------------------------|-----------|------------|-------------|
|          |             | Default                | Looting I | Looting II | Looting III |
| Enderman | 100%        | 0–1                    | 0–2       | 0–3        | 0–4         |

### Chest loot
| Item        | Structure      | Container      | Quantity | Chance          |
|-------------|----------------|----------------|----------|-----------------|
|             |                |                |          | Java Edition    |
| Ender Pearl | Stronghold     | Altar chest    | 1        | 23%             |
|             | Trial Chambers | Trial spawner  | 1        | 3.8%            |
|             |                | Corridor chest | 1–2      | 19.6%           |
|             |                |                |          | Bedrock Edition |
| Ender Pearl | Stronghold     | Altar chest    | 1        | 22.4%           |
|             | Trial Chambers | Corridor chest | 1–2      | 19.6%           |

A trapped chest always containing 2 ender pearls can be found in the "fake end portal" room of woodland mansions.

### Trading
In Java Edition, expert-level cleric villagers have a 2⁄3 chance to sell an ender pearl for 5 emeralds.

In Bedrock Edition, expert-level cleric villagers sell one ender pearl for 5 emeralds.

### Bartering
Piglins have a 10⁄459 (2.18%) chance to barter 2–4 ender pearls when given a gold ingot.

## Usage
Ender pearls can be thrown by pressing use. After it is thrown, the ender pearl is consumed, and the player teleports to where it lands, taking 5 fall damage. Wearing armor enchanted with Protection and/or Feather Falling reduces the damage taken from the ender pearl. 

Ender pearls have a small cone of travel; they do not all follow the same path when thrown in the same direction. The direction and velocity of ender pearl throws is slightly randomized. They can travel about 30 blocks‌[Java Edition  only]/45 blocks‌[Bedrock Edition  only] when thrown straight up, and up to 54 blocks forward when thrown at an optimum launch angle of ~35° (on even ground).

The thrower's vertical velocity influences the throw. Hence timing a throw with a jump can increase the throwing range to 42 blocks when thrown straight up and 64 blocks forward at a 35° angle. Throwing while falling significantly decreases the range. Ender pearls collide with all minecart types, boats, end crystals and nether portals, and travel through end portals. Ender pearls that fall into the void disappear, and do not trigger the player to teleport. However, ender pearl entities (instead of dropped items) are not destroyed by lava and teleport the player to the bottom of lava pools/lava oceans.

Ender pearls have a cooldown of one second before they can be used again. The cooldown is shown in the hotbar by a white overlay on the ender pearl that shrinks and must disappear before the player can use it again. If there are other inventory or hotbar slots containing ender pearls, they are covered with the white overlay as well.[1]

Ender pearls can be thrown into end gateways to reach the outer islands of the End. They can also be thrown into the exit portal to reach the player's spawn point.

Ender pearl teleportation does not occur across dimensions.

If the player throws an ender pearl and then dies while the pearl is in a loaded chunk before impact, the pearl disappears and the player is not teleported; in Java Edition, the pearl does not vanish upon the player's death if the game rule enderPearlsVanishOnDeath is set to false. Pearls in unloaded chunks do not disappear if their owner dies.

### Stasis chamber
Ender pearls are affected by bubble columns. An ender pearl can remain afloat on top of an upward bubble column, allowing it to be stored indefinitely. A mechanism can then be triggered to make the ender pearl hit a solid surface (e.g. by closing a trapdoor), teleporting the thrower back to the setup wherever they are.

### Spawning endermites
An ender pearl has a 5% chance to spawn an endermite when it lands. This is the only way through which endermites can spawn, without using cheats. The endermite spawns at the player's position when the pearl lands‌[Java Edition  only], or at the pearl's landing site‌[Bedrock Edition  only].

### Crafting ingredient
| Name         | Ingredients              | Crafting recipe |
|--------------|--------------------------|-----------------|
| Eye of Ender | Blaze Powder+Ender Pearl |                 |

## Data values
### ID
Java Edition:

| Item        | Identifier  | Form | Translation key            |
|-------------|-------------|------|----------------------------|
| Ender Pearl | ender_pearl | Item | item.minecraft.ender_pearl |

| Entity             | Identifier  | Translation key              |
|--------------------|-------------|------------------------------|
| Thrown Ender Pearl | ender_pearl | entity.minecraft.ender_pearl |

Bedrock Edition:

| Item        | Identifier  | Numeric ID | Form | Translation key       |
|-------------|-------------|------------|------|-----------------------|
| Ender Pearl | ender_pearl | 422        | Item | item.ender_pearl.name |

| Entity      | Identifier  | Numeric ID | Translation key         |
|-------------|-------------|------------|-------------------------|
| Ender Pearl | ender_pearl | 87         | entity.ender_pearl.name |

### Entity Data
Thrown ender pearls have entity data that define various properties of the entity.

Java Edition:

Main article: Entity format

 Entity data
Tags common to all entities
Tags common to all projectiles
 Item: The item to render as, may be absent.
Tags common to all items

Bedrock Edition:

See Bedrock Edition level format/Entity format.
