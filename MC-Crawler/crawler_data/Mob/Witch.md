# Witch
 The witch is a hostile mob that uses potions in combat, using various splash potions for offense and drinkable potions for defense.

## Contents
- 1 Spawning
- 2 Drops
- 3 Behavior
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
	- 11.1 Screenshots
	- 11.2 In other media
- 12 References

## Spawning
Main article: Tutorials/Witch farming
A witch may spawn in the Overworld above opaque blocks at a light level of 0 in all biomes except for mushroom fields and deep dark. Witches always spawn individually. Witches are the only mobs that can spawn in the small area around a swamp hut. 

Swamp biomes feature witch hut structures: every swamp hut spawns a witch and a black-colored cat inside during the world generation, and both never despawn. After world generation, only witches can spawn in the hut, provided that the entire hut is inside a swamp biome. In Java Edition, only witches spawn in the 7×7×9 volume that is the hut, which is the size of the roof and one block over the porch, from one level below the floor of the hut to two blocks above the roof. In Bedrock Edition, the hut has a hardcoded spawn spot on which witches spawn: the spawn spot is the same for every hut.

Some witches always spawn as part of raids starting from wave 4 in Bedrock Edition or wave 3 or 4 in Java Edition depending on the world difficulty.

A villager transforms into a witch when lightning strikes within four blocks from it. The witch transformed from a villager does not despawn naturally and cannot be changed back into a villager. This witch attacks the player with its potions even if the player traded with it before.

- The rooftop and scale of a swamp hut, as well as the spawning zone from Minecraft: Java Edition. The spawn area matches the roof, plus the porch.
- The side of a swamp hut, showing the scale of it and its proper height (Java Edition).
- Witches spawn on the northwest corner of the spawn spot in Minecraft: Bedrock Edition, which is marked with a block of lapis lazuli in this picture.

## Drops
On death, a witch rolls its loot table between 1 and 3 times, selecting one of the following rows each time:

| Item |                | Roll Chance | Quantity (Roll Chance) |           |            |             |
|------|----------------|-------------|------------------------|-----------|------------|-------------|
|      |                |             | Default                | Looting I | Looting II | Looting III |
|      | Glowstone Dust | 1–3 × 1/8   | 0–2                    | 0–3       | 0–4        | 0–5         |
|      | Sugar          | 1–3 × 1/8   | 0–2                    | 0–3       | 0–4        | 0–5         |
|      | Redstone Dust  | 1–3 × 1/8   | 0–2                    | 0–3       | 0–4        | 0–5         |
|      | Spider Eye     | 1–3 × 1/8   | 0–2                    | 0–3       | 0–4        | 0–5         |
|      | Glass Bottle   | 1–3 × 1/8   | 0–2                    | 0–3       | 0–4        | 0–5         |
|      | Gunpowder      | 1–3 × 1/8   | 0–2                    | 0–3       | 0–4        | 0–5         |
|      | Stick          | 1–3 × 2/8   | 0–2                    | 0–3       | 0–4        | 0–5         |

As result, no Looting averages two items per kill, Looting I averages three, Looting II averages four and Looting III averages five. The likelihood of dropping the maximum amount of 15 items is 1⁄81 or 1.234% because of the complexity of the loot table.

5 experience is dropped when kill credit is given to the player.

One of four types of drinkable potion has an 8.5% chance of dropping if a witch is killed while drinking the potion. The chance is increased by 1% for every level of Looting. A witch drops one of the following potions in this case:

- Potion of Healing
- Potion of Fire Resistance
- Potion of Swiftness
- Potion of Water Breathing

## Behavior
The magical effect made of purple particles that witches emit from time to time.
A witch is ocasionally covered by purple-colored morning stars. There is an 1.5% chance every second to spawn those 10 to 44 ornamental particles above their heads to represent shining stars named “witch” in Java Edition or “witchspell” in Bedrock Edition. In Java Edition, any witch is given the Glowing status effect for three seconds when the bell block is rung within 32 blocks of it regardless of whether it participates in raids or not. A witch is neither an illager nor a villager. A witch cannot use housing or the equipment in their swamp huts, and cannot open doors. Witches are peaceful toward villagers and wandering traders when not participating in raids, although their potions can hit one by accident. Witches that participate in a raid seek out illagers and ravagers to throw splash potions of Regeneration with a duration of 45 seconds near them or Instant Health if they have a low health of 4 points or less. The poison, instant damage, evoker fangs, warden's sonic boom and the Thorns enchantment magical sources are 85% less effective against witches. In Bedrock Edition, witches are immune to poison, fatal poison and to the instant damage (but not the knockback) caused by their own thrown harming potions.

A witch pursues the player within 16 blocks and uses potions of the first level in combat, throwing splash potions offensively and drinking potions defensively. These potions are the same as ones obtainable through brewing, with the same duration. A witch has an infinite stock of potions, even when transformed from a villager or not having had any potions equipped in their inventory. Each potion chosen by the witch depends on the circumstance and is thrown within ten blocks and in a three-second interval.

- The witch throws a splash potion ofSlownessif the player[1]is eight, nine or ten blocks away and does not already have the Slowness effect. This makes it harder for the player or mob to escape if they attempt to.
- The witch throws a splash potion ofPoisonif the player's health[1]is at least 8and is not already poisoned.
- The witch has a 25% chance of throwing a splash potion ofWeaknessif the player[1]is 3 or less blocks away and does not already have the Weakness effect. This is used to weaken the player or mob's melee attacks on the witch if they attempt to. The Weakness effect can be used to curezombie villagersinto villagers.
- If none of the above conditions are true, the witch defaults to using a splash potion ofHarming, which does 6magicaldamage.

A witch can choose to equip and drink a potion each game tick (1⁄20 second) if it is not already drinking a potion. Drinking the potion takes 1.6 seconds[2] and slows down its moving speed a little. The witch does not attack during this time.

- When thehitboxof the witch is 80% underwaterand the witch is lacking theWater Breathingstatus effect, there is a 15% chance of drinking a potion of Water Breathing.
- When the witch is on fire or the last damage taken by it in the past two seconds was fire damage, there is a 15% chance of drinking a potion ofFire Resistance.
- When the witch is not at full health, there is a 5% chance of drinking a potion ofHealingwhich heals 4.[3]
- When the witch is eleven or more blocks from a target and does not have theSpeedeffect, there is a 50% chance of drinking a potion of Swiftness.

As a result, witches are difficult to kill via suffocation or cacti due to their frequent use of healing potions, cannot drown underwater and require a long time to die in lava or fire.

If the witch, ravager or illager raid members kill all the villagers in a village or all the village beds are destroyed, witches jump and show unique sound effects in commemoration to their victory. 

In Bedrock Edition, witches attack iron golems and snow golems or any mob that attacks it, including other witches and illagers, throwing harmful splash potions.

In Java Edition, witches drink a beneficial potion, often an instant-health healing potion, when they are attacked by evoker fangs, illager mobs or harming potions from other witches and join an illager patrol if sufficiently near to the pillager, vindicator, evoker and illusioner patrol captain mobs. The witches that join a patrol are hostile toward villagers, wandering traders and iron golems if in their sight.  

In Java Edition, witches can ride any mob via commands, including boss mobs. In Bedrock Edition, witches cannot ride ravagers as a witch is not considered an illager.

## Data values
### ID
Java Edition:

| Name  | Identifier | Entity tags | Translation key        |
|-------|------------|-------------|------------------------|
| Witch | witch      | raiders     | entity.minecraft.witch |

Bedrock Edition:

| Name  | Identifier | Numeric ID | Translation key   |
|-------|------------|------------|-------------------|
| Witch | witch      | 45         | entity.witch.name |

### Entity data
Witches have entity data associated with them that contains various properties.
Java Edition:

Main article: Entity format

 Entity data
Tags common to all entities
Tags common to all mobs
Tags common to all mobs spawnable in raids

Bedrock Edition:

See Bedrock Edition level format/Entity format.
