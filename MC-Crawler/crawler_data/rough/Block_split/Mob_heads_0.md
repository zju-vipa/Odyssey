# Head
A head or skull is a block modeled after the head of a specific entity.

## Contents
- 1 Variants
- 2 Obtaining
	- 2.1 Mob loot
	- 2.2 Natural generation
	- 2.3 Player head
- 3 Usage
	- 3.1 Decoration
	- 3.2 Wearing
	- 3.3 Dispensers
	- 3.4 Crafting ingredient
	- 3.5 Enchantments
	- 3.6 Note blocks
- 4 Sounds
	- 4.1 Generic
	- 4.2 Unique
- 5 Data values
	- 5.1 ID
	- 5.2 Metadata
	- 5.3 Block states
- 6 Achievements
- 7 Advancements
- 8 History
	- 8.1 Skull "item"
		- 8.1.1 Appearances
		- 8.1.2 Names
- 9 Trivia
- 10 Gallery
	- 10.1 Screenshots
	- 10.2 Development images
	- 10.3 In other media
- 11 References

## Variants
There are seven types of heads:

- Skeleton Skull
- Wither Skeleton Skull
- Zombie Head
- Player Head
- Creeper Head
- Piglin Head
- Dragon Head

## Obtaining
### Mob loot
The following heads drops when the corresponding mob gets killed by a charged creeper's explosion:

- Skeleton Skull
- Zombie Head
- Creeper Head
- Piglin Head
- Wither Skeleton Skull

If several mobs are killed by the explosion of a single charged creeper, only one random mob drops its head.‌[Java Edition  only]

A wither skeleton sometimes drops a Wither Skeleton Skull when killed.

### Natural generation
- Skeleton Skullsgenerate as part ofancient cities.
- A singleDragon Headgenerates at the front ofend ships.

### Player head
The Player Head is unobtainable in Survival.

## Usage
### Decoration
Heads can be oriented in 16 different directions on top of a block, and 4 directions on the sides of blocks, similar to signs. They can be placed on top of, or beside each other by shift clicking.

When placed and powered by redstone, the piglin and dragon heads play an animation. The piglin head flaps its ears (2 times per second for the right ear and 2.5 times per second for the left ear) while the dragon head opens and closes its mouth repeatedly (2 times per second). The same animation occurs when worn by a (horizontally) moving player, zombie, skeleton, or armor stand (note: the animation does not play if the NoGravity tag is set to 1)

### Wearing
The player can wear heads, similarly to pumpkins or helmets. This overlays the second layer of the player's skin.

Wearing the corresponding head reduces the detection range for skeletons (but not wither skeletons), creepers, zombies, and piglins to 50% of the normal range. This is similar to (and stacks with) the reductions in detection range from sneaking and from the Invisibility status effect.

In Bedrock Edition, wearing any head makes the player invisible to other players on a locator map.

### Dispensers
A dispenser can equip a head on a player, mob, or armor stand with an empty helmet slot, within the block the dispenser is facing.

Dispensers can summon a wither when placing wither skeleton skulls on soul sand.

### Crafting ingredient
| Name                   | Ingredients                        | Crafting recipe |
|------------------------|------------------------------------|-----------------|
| Banner Pattern Creeper | Paper+<br/>Creeper Head            |                 |
| Banner Pattern Skull   | Paper+<br/>Wither Skeleton Skull   |                 |
| Firework Star          | AnyHead+<br/>Gunpowder+<br/>AnyDye |                 |

### Enchantments
Heads can receive the following enchantments, but only through an anvil.

| Name               | Max level | Method |
|--------------------|-----------|--------|
| Curse of Binding   | I         | Anvil  |
| Curse of Vanishing | I         | Anvil  |

### Note blocks
Placing a head above a note block causes the note block to play the corresponding mob's ambient sound when activated. The only exception is the creeper head; as creepers don't make ambient sounds, the note block plays the primed (hissing) sound instead.

The block below the note block does not affect the mob sound it creates.

## Data values
### ID
Java Edition:

| Name                       | Identifier                   | Form         | Translation key                              |
|----------------------------|------------------------------|--------------|----------------------------------------------|
| Skeleton Skull             | `skeleton_skull`             | Block & Item | `block.minecraft.skeleton_skull`             |
| Wither Skeleton Skull      | `wither_skeleton_skull`      | Block & Item | `block.minecraft.wither_skeleton_skull`      |
| Zombie Head                | `zombie_head`                | Block & Item | `block.minecraft.zombie_head`                |
| Player Head                | `player_head`                | Block & Item | `block.minecraft.player_head`                |
| Creeper Head               | `creeper_head`               | Block & Item | `block.minecraft.creeper_head`               |
| Dragon Head                | `dragon_head`                | Block & Item | `block.minecraft.dragon_head`                |
| Piglin Head                | `piglin_head`                | Block & Item | `block.minecraft.piglin_head`                |
| Skeleton Wall Skull        | `skeleton_wall_skull`        | Block        | `block.minecraft.skeleton_wall_skull`        |
| Wither Skeleton Wall Skull | `wither_skeleton_wall_skull` | Block        | `block.minecraft.wither_skeleton_wall_skull` |
| Zombie Wall Head           | `zombie_wall_head`           | Block        | `block.minecraft.zombie_wall_head`           |
| Player Wall Head           | `player_wall_head`           | Block        | `block.minecraft.player_wall_head`           |
| Creeper Wall Head          | `creeper_wall_head`          | Block        | `block.minecraft.creeper_wall_head`          |
| Dragon Wall Head           | `dragon_wall_head`           | Block        | `block.minecraft.dragon_wall_head`           |
| Piglin Wall Head           | `piglin_wall_head`           | Block & Item | `block.minecraft.piglin_wall_head`           |

| Name         | Identifier |
|--------------|------------|
| Block entity | `skull`    |

Bedrock Edition:

| Head  | Identifier | Numeric ID | Form                         | Item ID[i 1] | Translation key                                                                                                                                                                                         |
|-------|------------|------------|------------------------------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Block | `skull`    | `144`      | Block & Ungiveable Item[i 2] | `item.skull` | —                                                                                                                                                                                                       |
| Item  | `skull`    | `516`      | Item                         | —            | `item.skull.skeleton.name`<br/>`item.skull.wither.name`<br/>`item.skull.zombie.name`<br/>`item.skull.char.name`<br/>`item.skull.creeper.name`<br/>`item.skull.dragon.name`<br/>`item.skull.piglin.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Unavailable with /give command

| Name         | Savegame ID |
|--------------|-------------|
| Block entity | `Skull`     |

