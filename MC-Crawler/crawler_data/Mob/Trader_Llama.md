# Llama
A llama is a tameable neutral mob used to transport large shipments of items.

## Contents
- 1 Spawning
- 2 Drops
	- 2.1 Breeding
	- 2.2 On death
- 3 Behavior
	- 3.1 Spitting
	- 3.2 Taming
	- 3.3 Breeding
	- 3.4 Caravans
	- 3.5 Storage
	- 3.6 Carpets
- 4 Sounds
- 5 Data values
	- 5.1 ID
	- 5.2 Entity data
- 6 Achievements
- 7 Advancements
- 8 History
- 9 Issues
- 10 Trivia
- 11 Gallery
	- 11.1 Renders
	- 11.2 Screenshots
	- 11.3 Development images
	- 11.4 In other media
- 12 References
- 13 External links

## Spawning
A llama spawns at a light level 7 or above on grass blocks in savanna plateau, savanna‌[BE  only][1] or windswept savanna‌[BE  only] biomes in herds of 4 llamas, and in windswept hills, windswept forest, and windswept gravelly hills biomes in herds of 4 to 6 llamas, coming in four coat colors: brown, cream, white or gray.

10% of llamas spawn as baby llamas.

Every wandering trader spawns with two leashed trader llamas. Trader llamas often despawn one tick before their trader does, because a trader llama has its DespawnDelay set to 47999 ticks. This value is decremented each tick that the llama is untamed, unleashed, and not being ridden by a player, and is reset to one tick less than the trader's own DespawnDelay if leashed to a trader. The llama despawns when the its DespawnDelay reaches zero ticks.

## Drops
### Breeding
1–7 upon successful breeding.

### On death
| Item |         | Roll Chance | Quantity (Roll Chance) |           |            |             |
|------|---------|-------------|------------------------|-----------|------------|-------------|
|      |         |             | Default                | Looting I | Looting II | Looting III |
|      | Leather | 100%        | 0–2                    | 0–3       | 0–4        | 0–5         |

- Any equippedcarpetsandchest.
- All items in theirinventory.
- 1–3experienceorbs if killed by aplayeror tamedwolf.

Like other baby animals, killing a baby llama yields no item or experience.

## Behavior
Llamas are neutral, but if a player or mob attacks one, it will retaliate. Sometimes their spit can miss their target and hit another llama, starting a fight within a group of llamas. Additionally, a wandering trader's llamas spit at mobs or players who attack the wandering trader.

Llamas are hostile toward wolves and spit without provocation, but they don't attack tamed wolves unless provoked. Wolves are fearful of llamas of strength 4 or 5 and always run away.[2] Wolves flee from weaker llamas less often.

Trader llamas are hostile toward wolves, and defend their wandering trader from illagers‌[Java Edition  only] and all zombie variants. 

Llamas and trader llamas are completely passive in Peaceful difficulty.

The llama floats when in water deeper than two blocks.

### Spitting


Main article: Llama spit
Llamas attack other mobs by spitting at them, which deals 1 damage.

### Taming
Llamas can be tamed by repetitively riding them until hearts are displayed, done by pressing use on the llama while holding nothing.

Taming success depends on the llama's Temper value. Temper is a positive trait, with higher values increasing the chance of successful taming. Llamas begin with a Temper value of 0 and a maximum of 30. When a player rides an untamed llama, a random number from 0 to 29 is chosen. The llama gets tamed successfully if this number is less than the Temper value, otherwise, the Temper is increased by 5 and the player is bucked off. Temper can also be increased by feeding the llama.

Naturally spawned trader llamas are untamed and cannot be ridden while being led by their wandering trader. If unleashed, they become tameable in Java Edition, or immediately tamed in Bedrock Edition. Tamed trader llamas do not despawn.

Tamed llamas do not spit at mobs that attack its owner, although it spits at any mob that attacks the llama. Tamed llamas can still retaliate at players should the player hit them.

Feeding a llama food can alter its behavior, increasing its temper value if untamed, restoring lost health or making a baby grow faster (babies ordinarily take around 20 minutes to mature to adults). The table below lists the effects of the 2 food items llamas accept.

A llama can be fed by holding a valid food item and pressing use while facing the llama. Llamas can be fed only when feeding would have an effect, similar to other animals. If the food is invalid, the player mounts the llama instead.

| Food     | Heals | Speeds growth by | Increases temper by | Notes                              |
|----------|-------|------------------|---------------------|------------------------------------|
| Wheat    | 2     | 10 sec           | +3                  |                                    |
| Hay Bale | 10    | 1:30 minutes     | +6                  | Activateslove modein tamed llamas. |

### Breeding
Adult tamed llamas can be bred by being fed a hay bale. The baby llama takes on the coat color of one parent at random. Its strength is chosen as a random integer between 1 and the strength of the stronger parent, inclusive. 3% of the time the resulting strength is increased by 1, but it is capped at 5.

When two trader llamas are bred, the offspring wears a rug.

| Stronger parent's strength | Offspring's strength |        |        |     |       |
|----------------------------|----------------------|--------|--------|-----|-------|
|                            | 1                    | 2      | 3      | 4   | 5     |
| 1                          | 97%                  | 3%     |        |     |       |
| 2                          | 48.5%                | 50%    | 1.5%   |     |       |
| 3                          | 32.33%               | 33.33% | 33.33% | 1%  |       |
| 4                          | 24.25%               | 25%    | 25%    | 25% | 0.75% |
| 5                          | 19.4%                | 20%    | 20%    | 20% | 20.6% |

Select a row based on the stronger parent. The column shows the probability of the resulting offspring having a given strength.  

A llama's base health (15 × 7.5 to 30 × 15) is calculated based on that of its parents, in the same way as a horse's.

### Caravans
Llamas form a caravan when one of them is leashed by a player.

Leashing a llama signals up to 9 nearby llamas that are not already in a caravan to follow each other, forming a caravan of up to ten llamas. When multiple llamas are leashed, each leashed llama can form a separate caravan of up to ten separate llamas. Each caravan cannot have two or more leashed llamas in it, and there is no limit to the number of caravans a player can lead.

### Storage
The GUI of a llama with strength 4 and with a chest.
A tamed llama can be equipped with a chest by pressing the use control on it while holding a chest. The chest gives the llama 3 to 15 slots of inventory space, depending on its strength (see table below). Once equipped, its contents can be accessed by pressing the use control on the llama while sneaking, or by opening the inventory while riding the llama. The chest itself cannot be retrieved without killing the llama.

| Strength distribution in wild llamas |  |          |                                                      |                              |
|--------------------------------------|--|----------|------------------------------------------------------|------------------------------|
|                                      |  | Strength | Probability of spawning with that amount of strength | Number of slots in inventory |
|                                      |  | 1        | 32.8%                                                | 3                            |
|                                      |  | 2        | 32.8%                                                | 6                            |
|                                      |  | 3        | 32.8%                                                | 9                            |
|                                      |  | 4        | 0.8%                                                 | 12                           |
|                                      |  | 5        | 0.8%                                                 | 15                           |

### Carpets
All llama carpet patterns.
A llama can be equipped with a wool carpet in its carpet slot. Each carpet color shows as a different patterned rug when on the llama's back. This can be useful for color-coding the llamas as storage containers, like dyed shulker boxes.

A trader llama that does not have a carpet wears a blue rug design. This design can be replaced with a carpet but not removed. When given carpets, all types of llamas look the same, except for their fur colors. In Java Edition, a llama's carpet decoration, including the default blue rug of a trader llama, remains visible when the llama is under the effect of Invisibility;[3] in Bedrock Edition, it becomes invisible.

For the purposes of the /item command, a llama carries its carpet in the horse.armor slot.

## Data values
### ID
Java Edition:

| Name         | Identifier   | Entity tags          | Translation key               |
|--------------|--------------|----------------------|-------------------------------|
| Llama        | llama        | dismounts_underwater | entity.minecraft.llama        |
| Trader Llama | trader_llama | dismounts_underwater | entity.minecraft.trader_llama |

Bedrock Edition:

| Name         | Identifier   | Numeric ID | Translation key          |
|--------------|--------------|------------|--------------------------|
| Llama        | llama        | 29         | entity.llama.name        |
| Trader Llama | trader_llama | 157        | entity.trader_llama.name |

### Entity data
Java Edition:

Main article: Entity format
Llamas have entity data associated with them that contain various properties.


 Entity data
Additional fields for mobs that can breed
Tags common to all entities
Tags common to all mobs
 Bred: 1 or 0 (true/false) - Unknown. Remains 0 after breeding. If true, causes it to stay near other llamas with this flag set.
 ChestedHorse: 1 or 0 (true/false) - true if the llama has chests.
 DecorItem: The item the llama is wearing, without the Slot tag. Typically a carpet.‌[until JE 1.20.5]
Tags common to all items
 DespawnDelay: A timer for trader llamas to despawn, present only in trader_llama. The trader llama despawns when this value reaches 0.
 EatingHaystack: 1 or 0 (true/false) - true if grazing.
 Items: List of items. Exists only if ChestedHorse is true.
 An item, including the Slot tag.
Tags common to all items
 Owner: The UUID of the player that tamed the llama, stored as four ints. Has no effect on behavior. Does not exist if there is no owner.
 Variant: The variant of the llama. 0 = Creamy, 1 = White, 2 = Brown, 3 = Gray.
 Strength: Ranges from 1 to 5, defaults to 3.  Determines the number of items the llama can carry (items = 3 × strength).  Also increases the tendency of wolves to run away when attacked by llama spit. Strengths 4 and 5 always causes a wolf to flee.
 Tame: 1 or 0 (true/false) - true if the llama is tamed.
 Temper: Ranges from 0 to 100; increases with feeding. Higher values make a llama easier to tame.


Llama Variant
Main article: Llama/DV[edit]

Bedrock Edition:

See Bedrock Edition level format/Entity format.
