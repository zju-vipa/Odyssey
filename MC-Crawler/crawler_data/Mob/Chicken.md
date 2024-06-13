# Chicken
A chicken is a passive mob found in grass biomes and the main source of raw chicken, feathers and eggs. This mob can be attached to a lead.

## Contents
- 1 Spawning
	- 1.1 Chicken jockey
		- 1.1.1 Java Edition
		- 1.1.2 Bedrock Edition
- 2 Drops
	- 2.1 Breeding
	- 2.2 On death
- 3 Behavior
	- 3.1 Breeding
	- 3.2 Eggs
- 4 Sounds
- 5 Data values
	- 5.1 ID
	- 5.2 Entity data
- 6 Achievements
- 7 Advancements
- 8 Video
- 9 History
- 10 Issues
- 11 Trivia
- 12 Gallery
	- 12.1 Renders
	- 12.2 Textures
	- 12.3 Screenshots
	- 12.4 In other media
- 13 References

## Spawning
Chickens spawn naturally in the Overworld in groups of four on grass blocks with 2 blocks of free space above it at a light level of 9 or more. They do not spawn in deserts, snowy plains, ice spikes, snowy slopes, meadows, wooded badlands, jagged peaks, frozen peaks and stony peaks. 
In Java Edition, chickens are more common in sparse jungles.

After the world generation, chickens spawn individually.

5% of chickens spawn as baby chickens. 

In Bedrock Edition, chickens require a light level of 7 or more to spawn and are found in groups of two to four.

### Chicken jockey
#### Java Edition
Main article: Chicken Jockey
All baby zombie variants and baby zombified piglins have a 5% chance to spawn riding a chicken, forming a chicken jockey. Because a baby zombie occurs from 5% of zombie spawns, the chicken jockey spawns consist of 0.25% of all zombie spawns in a chicken-free environment; if chickens are present, the chance increases to 0.4875%. A chicken jockey can also be spawned by using the following command: 

/summon minecraft:chicken ~ ~ ~ {IsChickenJockey:1b,Passengers:[{id:"minecraft:zombie",IsBaby:1b}]}

Chicken jockeys may spawn with items equipped. Baby zombified piglin versions of the chicken jockey always wield a golden sword. Harming or killing the chicken does not cause the zombified piglin to attack.

#### Bedrock Edition
Baby zombie jockeys do not spawn riding chickens, but check for nearby adult chickens to mount prior to attacking a player, wandering trader, adult villager, snow golem or iron golem.

## Drops
Main article: Tutorials/Chicken farming
Adult chickens that were not part of chicken jockeys lay an egg every five to ten minutes.

### Breeding
1–7 experience orbs upon a successful breeding.

### On death
| Item |                  | Roll Chance | Quantity (Roll Chance) |           |            |             |
|------|------------------|-------------|------------------------|-----------|------------|-------------|
|      |                  |             | Default                | Looting I | Looting II | Looting III |
|      | Feather          | 100%        | 0–2                    | 0–3       | 0–4        | 0–5         |
|      | Raw Chicken[d 1] | 100%        | 1                      | 1–2       | 1–3        | 1–4         |


↑ Dropped as cooked chicken if on fire when killed.


1–3 experience orbs are dropped when a chicken is killed by a player or tamed wolf or 10 if it was part of a chicken jockey.

Killing a baby chicken yields no items or experience.

## Behavior
A chicken wanders aimlessly but goes after players holding various seeds within a 6×4×6 cubic area, while a baby chicken follows adult chickens.

Some chickens going after a player holding wheat seeds.
Chickens avoid falling off cliffs and flap their wings when they are in middle air and fall slowly, thus chickens are immune to fall damage.  

When harmed, chickens flee around for a few seconds. 

Chickens uniquely attempt to jump up to climb stairs instead of climbing them normally.[1]

Ocelots, untamed cats‌[JE  only] and foxes pursue and attack chickens. 

While in a loaded chunk, an adult chicken lays an egg every five to ten minutes (6000–12000 ticks), unless it is, or was, a part of a chicken jockey. If the player is close enough to a chicken when it lays an egg, a pop sound is heard.

Chickens can stay underwater for 15 seconds or can swim, visibly flapping their wings and staying on the water surface. While swimming, a chicken needs only one block of air above its head.

A chicken is 11 pixels or 0.6875 blocks tall. A chick is 5.5 pixels tall or 0.34375 blocks tall.

### Breeding
Main article: Breeding
If two adult chickens are fed wheat seeds, beetroot seeds, melon seeds, pumpkin seeds, torchflower seeds, or pitcher pods, a baby chicken spawns. They cannot breed for 5 minutes afterward.

A baby chicken with its parents.
Chicks take 20 minutes to grow up, but the growth time can be accelerated by 10% each time it is fed seeds. A baby chick fed a seed once per second grows up in approximately 48 seconds using 47 seeds.

Chicks are smaller than a half-block and can unwillingly pass through openings smaller than a full block, but do not walk through half-block-tall spaces. A chick riding a minecart cannot be hit because it is completely inside the minecart's hitbox.

### Eggs
See also: Tutorials/Egg farming § chicken farm

Chickens are the only Overworld mob that can repopulate without breeding. Adult chickens lay eggs at random and an egg thrown at the ground by a player or a dispenser has a 1⁄8 chance of spawning a baby chicken. If a baby chicken spawns from a thrown egg, there is a further 1⁄32 chance to spawn three extra baby chickens, or 1⁄256 overall. It is theoretically possible for a stack of 16 eggs to yield 64 chickens if all spawn chances succeed for all eggs.

If the player throws an egg at a glass pane, the baby chicken can spawn on the far side of the pane.

## Data values
### ID
Java Edition:

| Name    | Identifier | Entity tags                            | Translation key          |
|---------|------------|----------------------------------------|--------------------------|
| Chicken | chicken    | dismounts_underwaterfall_damage_immune | entity.minecraft.chicken |

Bedrock Edition:

| Name    | Identifier | Numeric ID | Translation key     |
|---------|------------|------------|---------------------|
| Chicken | chicken    | 10         | entity.chicken.name |

### Entity data
Chickens have entity data associated with them that contain various properties.

Java Edition:

Main article: Entity format

 Entity data
Additional fields for mobs that can breed
Tags common to all entities
Tags common to all mobs
 EggLayTime: Number of ticks until the chicken lays its egg. Laying occurs at 0 and this timer gets reset to a new random value between 6000 and 12000.
 IsChickenJockey: 1 or 0 (true/false) - Whether or not the chicken is a jockey for a baby zombie. If true, the chicken can naturally despawn, drops 10 experience upon death instead of 1-3 and cannot lay eggs. Baby zombies can still control a ridden chicken even if this is set false.

Bedrock Edition:

See Bedrock Edition level format/Entity format.
