### Caravans
Llamas form a caravan when one of them is leashed by a player.

Leashing a llama signals up to 9 nearby llamas that are not already in a caravan to follow each other, forming a caravan of up to ten llamas. When multiple llamas are leashed, each leashed llama can form a separate caravan of up to ten separate llamas. Each caravan cannot have two or more leashed llamas in it, and there is no limit to the number of caravans a player can lead.

### Storage
The GUI of a llama with strength 4 and with a chest.
A tamed llama can be equipped with a chest by pressing the use control on it while holding a chest. The chest gives the llama 3 to 15 slots of inventory space, depending on its strength (see table below). Once equipped, its contents can be accessed by pressing the use control on the llama while sneaking, or by opening the inventory while riding the llama. The chest itself cannot be retrieved without killing the llama.

| Strength distribution in wild llamas |                                                      |                              |  |  |
|--------------------------------------|------------------------------------------------------|------------------------------|--|--|
| Strength                             | Probability of spawning with that amount of strength | Number of slots in inventory |  |  |
| 1                                    | 32.8%                                                | 3                            |  |  |
| 2                                    | 32.8%                                                | 6                            |  |  |
| 3                                    | 32.8%                                                | 9                            |  |  |
| 4                                    | 0.8%                                                 | 12                           |  |  |
| 5                                    | 0.8%                                                 | 15                           |  |  |

### Carpets
All llama carpet patterns.
A llama can be equipped with a wool carpet in its carpet slot. Each carpet color shows as a different patterned rug when on the llama's back. This can be useful for color-coding the llamas as storage containers, like dyed shulker boxes.

A trader llama that does not have a carpet wears a blue rug design. This design can be replaced with a carpet but not removed. When given carpets, all types of llamas look the same, except for their fur colors. In Java Edition, a llama's carpet decoration, including the default blue rug of a trader llama, remains visible when the llama is under the effect of Invisibility;[3] in Bedrock Edition, it becomes invisible.

For the purposes of the /item command, a llama carries its carpet in the horse.armor slot.

## Data values
### ID
Java Edition:

| Name         | Identifier     | Entity tags            | Translation key                 |
|--------------|----------------|------------------------|---------------------------------|
| Llama        | `llama`        | `dismounts_underwater` | `entity.minecraft.llama`        |
| Trader Llama | `trader_llama` | `dismounts_underwater` | `entity.minecraft.trader_llama` |

Bedrock Edition:

| Name         | Identifier     | Numeric ID | Translation key            |
|--------------|----------------|------------|----------------------------|
| Llama        | `llama`        | `29`       | `entity.llama.name`        |
| Trader Llama | `trader_llama` | `157`      | `entity.trader_llama.name` |

### Entity data
Java Edition:

Main article: Entity format
Llamas have entity data associated with them that contain various properties.

- Entity data
	- 
	- Additional fields for mobs that can breed
	- 
	- Tags common to all entities
	- 
	- Tags common to all mobs
	- Bred: 1 or 0 (true/false) - Unknown. Remains 0 after breeding. If true, causes it to stay near other llamas with this flag set.
	- ChestedHorse: 1 or 0 (true/false) - true if the llama has chests.
	- DecorItem: The item the llama is wearing, without the Slot tag. Typically acarpet.‌[until JE 1.20.5]
		- 
		- Tags common to all items
	- DespawnDelay: A timer for trader llamas to despawn, present only intrader_llama. The trader llama despawns when this value reaches 0.
	- EatingHaystack: 1 or 0 (true/false) - true if grazing.
	- Items: List of items. Exists only ifChestedHorseis true.
		- An item, including the Slot tag.
			- 
			- Tags common to all items
	- Owner: TheUUIDof the player that tamed the llama, stored as four ints. Has no effect on behavior. Does not exist if there is no owner.
	- Variant: The variant of the llama. 0 = Creamy, 1 = White, 2 = Brown, 3 = Gray.
	- Strength: Ranges from 1 to 5, defaults to 3.  Determines the number of items the llama can carry (items = 3 × strength).  Also increases the tendency of wolves to run away when attacked by llama spit. Strengths 4 and 5 always causes a wolf to flee.
	- Tame: 1 or 0 (true/false) - true if the llama is tamed.
	- Temper: Ranges from 0 to 100; increases with feeding. Higher values make a llama easier to tame.


Llama Variant
Main article: Llama/DV[edit]

Bedrock Edition:

SeeBedrock Edition level format/Entity format.

