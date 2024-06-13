#### Despawning
Piglins that spawned in a bastion remnant during world generation, and piglins that have picked up or equipped items, do not despawn naturally.

### Zombification
A piglin turning into a zombified piglin.
When in the Overworld or the End, piglins transform into zombified piglins after 15 seconds, retaining their armor, held items and their name. However, they cannot shoot a crossbow, using it instead as a melee weapon. Upon transformation, the spawned zombified piglin has the Nausea effect for 10 seconds; this is just a cosmetic effect. When a piglin transforms into a zombified piglin, it drops anything except equipped weapons and armor in its inventory; other items in its inventory disappear. In Bedrock Edition, if the game is set to Peaceful difficulty, the piglin despawns instead of transforming because hostile mobs do not exist in Peaceful difficulty. A piglin that returns to the Nether before 15 seconds remains unchanged, although the 15-second portal cooldown usually prevents them from returning during that time.

A piglin does not zombify outside the Nether if its IsImmuneToZombification tag is set to true. Piglins with their NoAI tag set to true also do not zombify.

In Java Edition, if a piglin is inspecting/admiring a gold ingot or a gold-related item and then gets zombified while inspecting, it drops the gold ingot or the gold-related item.

## Data values
### ID
Java Edition:

| Name   | Identifier | Translation key         |
|--------|------------|-------------------------|
| Piglin | piglin     | entity.minecraft.piglin |

Bedrock Edition:

| Name   | Identifier | Numeric ID | Translation key    |
|--------|------------|------------|--------------------|
| Piglin | piglin     | 123        | entity.piglin.name |

### Entity data
Piglins have entity data associated with them that contains various properties.

Java Edition:

Main article: Entity format

 Entity data
Additional fields for mobs that can become angry
Tags common to all entities
Tags common to all mobs
 CannotHunt: 1 or 0 (true/false) – if true, the piglin does not attack hoglins. Set to true for piglins spawned as a part of bastion remnants.
 Inventory: Each compound tag in this list is an item in the piglin's inventory. It can hold a maximum of 8 items.
 An item in the inventory, excluding the Slot tag.
Tags common to all items
 IsBaby: 1 or 0 (true/false) – true if the piglin is a baby. May not exist.
 IsImmuneToZombification: 1 or 0 (true/false) – if true, the piglin does not transform to a zombified piglin when in the Overworld.
 TimeInOverworld: The number of ticks that the piglin has existed in the Overworld; the piglin converts to a zombified piglin when this is greater than 300.

Bedrock Edition:

See Bedrock Edition level format/Entity format.
## See also
- Piglin Brute
- Zombified Piglin
- Bartering


