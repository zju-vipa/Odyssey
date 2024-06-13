# Compass
A compass is an item used to point to the world spawn or to a lodestone.

## Contents
- 1 Obtaining
	- 1.1 Chest loot
	- 1.2 Crafting
	- 1.3 Trading
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Anvil usage
	- 2.3 Trading
	- 2.4 Enchantments
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Item data
- 5 Advancements
- 6 History
	- 6.1 Texture generation prior to Java Edition 13w02a
- 7 Issues
- 8 Gallery
	- 8.1 Screenshots
- 9 See also
- 10 External links
- 11 References

## Obtaining
### Chest loot
| Item    | Structure      | Container            | Quantity | Chance          |
|---------|----------------|----------------------|----------|-----------------|
|         |                |                      |          | Java Edition    |
| Compass | Ancient City   | Chest                | 1        | 16.1%           |
|         | Shipwreck      | Map chest            | 1        | 7.7%            |
|         | Stronghold     | Library chest        | 1        | 10.9%           |
|         | Trial Chambers | Intersection barrel  | 1        | 5.9%            |
|         | Village        | Cartographer's chest | 1        | 26.3%           |
|         |                |                      |          | Bedrock Edition |
| Compass | Ancient City   | Chest                | 1        | 16.1%           |
|         | Shipwreck      | Map chest            | 1        | 7.7%            |
|         | Stronghold     | Library chest        | 1        | 10.5%           |
|         | Trial Chambers | Intersection barrel  | 1        | 5.9%            |
|         | Village        | Cartographer's chest | 1        | 26.3%           |

### Crafting
| Ingredients                   | Crafting recipe |
|-------------------------------|-----------------|
| Iron Ingot+<br/>Redstone Dust |                 |

### Trading
In Java Edition, expert-level librarian villagers have a 50% chance to sell a single compass for 4 emeralds.

In Bedrock Edition, expert-level librarian villagers have a 1⁄3 chance to sell a single compass for 4 emeralds.

## Usage
Normally, the compass' needle points toward the world spawn point. The compass points to spawn when viewed in any way, including as a dropped item, in a player's hand, in an inventory or the crafting table, or in an item frame. The direction the needle points to is relative to the player who is viewing it.

In the Nether or the End, the compass' needle spins and points in random directions.

The compass can be used on a lodestone, after which it is named "Lodestone Compass" by default and points to that lodestone as long as the compass is in the same dimension as the lodestone, but if the compass is taken to a different dimension, it spins randomly, as a normal compass would in the Nether or the End. If the lodestone is destroyed, it also spins randomly, even if the lodestone is replaced afterward. However, if a lodestone compass is placed in storage, the lodestone can be broken and replaced without the compass losing the attunement, as long as the compass remains in storage while the lodestone is missing.

A lodestone compass appears enchanted, similar to the enchanted golden apple.

Using /setworldspawn to change the world spawn also changes where the compass points.

### Crafting ingredient
| Name                  | Ingredients                   | Crafting recipe | Description                                                                                                                                                                                                                    |
|-----------------------|-------------------------------|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Empty Map             | Paper+<br/>Compass            |                 | This map is called an "Empty Locator Map" inBedrock Edition, and an "Empty Map" inJava Edition. It has the same uses in both editions.                                                                                         |
| Map<br/>(with marker) | Mapor Empty Map +<br/>Compass |                 | ‌[Bedrock Edition  only]Maps crafted from only paper do not show the location marker; to add it, a compass must be added to the map. The map keeps its current zoom level, and remembers all of the terrain it has mapped out. |
| Recovery Compass      | Echo Shard+<br/>Compass       |                 |                                                                                                                                                                                                                                |

### Anvil usage
| Name        | Ingredients      | Anvil usage      | Description                                                                                                                      |
|-------------|------------------|------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Locator Map | Map+<br/>Compass | Repair & NameMap | Bedrock Editiononly.Maps crafted with only paper do not show the location marker; to add it, a compass must be added to the map. |



### Trading
A single compass can be sold to a journeyman-level cartographer villager for 1 emerald.‌[Java Edition  only]

A single compass can be sold to an expert-level cartographer villager for 1 emerald as their sixth trade.‌[Bedrock Edition  only]

A compass is also part of the cost of explorer maps:

- An ocean explorer map and‌[JE  only]/or‌[BE  only]a woodland explorer map can be bought from a journeyman-level cartographer for 12 emeralds and one compass, as part of their fifth trade.‌[Bedrock Edition  only]

- InJava Edition, apprentice-level cartographer villagers offer to sell an ocean explorer map for 13 emeralds and a compass, and journeyman-level cartographer villagers offer to sell a woodland explorer map for 14 emeralds and one compass.

### Enchantments
A compass can receive the following enchantments:

| Name               | Max Level | Method |
|--------------------|-----------|--------|
| Curse of Vanishing | I         |        |

## Data values
### ID
Java Edition:

| Name    | Identifier | Form | Translation key                                                 |
|---------|------------|------|-----------------------------------------------------------------|
| Compass | `compass`  | Item | `item.minecraft.compass`<br/>`item.minecraft.lodestone_compass` |

Bedrock Edition:

| Name              | Identifier          | Alias ID           | Numeric ID | Form | Translation key              |
|-------------------|---------------------|--------------------|------------|------|------------------------------|
| Compass           | `compass`           | None               | `391`      | Item | `item.compass.name`          |
| Lodestone Compass | `lodestone_compass` | `lodestonecompass` | `602`      | Item | `item.lodestonecompass.name` |

### Item data
Java Edition:

Main article: Item format
- tag: The item'stagtag.

- 
	- LodestoneTracked: Optional. 1 or 0 (true/false) - true if the compass is connected to alodestone. When false,LodestoneDimensionandLodestonePosis not automatically removed when the lodestone is destroyed, but the compass still points to that location.
	- LodestoneDimension: Optional. The dimension of the lodestone to which the compass is pointing.
	- LodestonePos: Optional. The coordinates of the lodestone to which the compass is pointing.
		- X: x coordinate
		- Y: y coordinate
		- Z: z coordinate

Bedrock Edition:

SeeBedrock Edition level format/Item format.

