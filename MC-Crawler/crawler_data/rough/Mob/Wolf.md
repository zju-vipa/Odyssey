# Wolf
A wolf is a neutral mob that can be tamed using bones. Tamed wolves defend their owners against attackers and can assist them in combat.

## Contents
- 1 Spawning
	- 1.1 Variants
- 2 Drops
- 3 Behavior
	- 3.1 Movement
	- 3.2 Teleportation
	- 3.3 Taming, health and feeding
	- 3.4 Wolf Armor
	- 3.5 Breeding
- 4 Sounds
- 5 Data values
	- 5.1 ID
	- 5.2 Entity data
- 6 Achievements
- 7 Advancements
- 8 Videos
- 9 History
- 10 Issues
- 11 Trivia
- 12 Gallery
	- 12.1 Renders
		- 12.1.1 Variants
		- 12.1.2 Tamed wolves
		- 12.1.3 Angry wolves
		- 12.1.4 Wolves wearing wolf armor
		- 12.1.5 Sitting wolves
		- 12.1.6 Pups
		- 12.1.7 Tamed pups
		- 12.1.8 Angry pups
	- 12.2 Screenshots
	- 12.3 Development images
	- 12.4 In other media
- 13 References

## Spawning
Wild wolves spawn naturally in forests, taigas, groves, old growth spruce taigas, old growth pine taigas, and snowy taigas on grass blocks, dirt, coarse dirt, snow‌[Bedrock Edition  only], snow blocks or podzol. They spawn in packs of 4, and 10% of wolves naturally spawn as pups.

Wolves spawned through breeding are automatically tamed by the player who bred them (see § Breeding).

### Variants

  

This section describes content that may be included in Java Edition and Bedrock Edition. 
This content has appeared in Java Edition 1.20.5 and Bedrock Edition 1.20.80 development versions, but the full update containing it has not been released yet.


Wolves have 9 color variants, each of which spawns in a different biome. Most variants spawn in packs, with some having larger or smaller packs.

| Variant  | Biome                   | Pack size |
|----------|-------------------------|-----------|
| Ashen    | Snowy Taiga             | 4         |
| Black    | Old Growth Pine Taiga   | 2-4       |
| Chestnut | Old Growth Spruce Taiga | 2-4       |
| Pale     | Taiga                   | 4         |
| Rusty    | Sparse Jungle           | 2-4       |
| Snowy    | Grove                   | 1         |
| Spotted  | Savanna Plateau         | 4-8       |
| Striped  | Wooded Badlands         | 4-8       |
| Woods    | Forest                  | 4         |

When a wolf pack spawns near a biome border, individual wolves of the pack might take on a different appearance if their spawn location is in a bordering biome.[1]

Wolves spawned in jungles or bamboo jungles (using spawn eggs, monster spawners, commands, or due to a wolf pack bordering these biomes) spawn as rusty wolves; wolves in savannas or windswept savannas spawn as spotted wolves; wolves in badlands or eroded badlands spawn as striped wolves. Wolves in all other biomes spawn as the pale wolf variant.

- All nine wolf variants. Order: snowy, striped, spotted, rusty, chestnut, black, ashen, woods, and pale.

For pictures of individual variants, see § Gallery.

## Drops
Adult wolves drop 1–3 experience orbs when killed by a player or tamed wolf. A tamed wolf that is killed by its owner still drops experience.

Wolves wearing wolf armor always drop their armor when they die, regardless of what kills them.‌[upcoming: JE 1.20.5 & BE 1.20.80]

Upon successful breeding, 1–7 are dropped.

Like other baby animals, a pup drops no experience when killed.

## Behavior


A tamed wolf "begging" the player for food.
Three tamed wolves following the player around.
Wolves exhibit three different states depending on how the user interacts with them:

- Untamedwolves have a drooping tail and their eyes consist of a white pixel and a black pixel for the pupil (on each side). They are neutral toward theplayer. They are hostile towardsheep,rabbits,foxes, babyturtles, andskeletonsand their variants, taking on their angry appearance while attacking these mobs, and changing back when the targeted mob dies or moves out of range. They chasebatsdespite being unable to reach them.[2]They avoidllamas, although wolves may attack a llama that spits on them. They do notdespawn, even if they are in an unloaded chunk, or 32 blocks away from theplayer. They can be ridden by babyzombievariants.‌[BE  only]
- Angrywolves are characterized by their constant growling and fearsome appearance. Wild wolves become hostile when they are either attacked by aplayerormob, if not killed in one hit[3]‌[JE  only], or when they see amobthey want to eat. Their tail is held out straight, their eyes become blood red, their mouth is raised in a slight snarl, and they have angry eyebrows. Angry wolves are hostile only to the players or mobs that attacked them, or to the mobs they are hunting. They can see attackers even if they are under the invisibility effect, but they cannot track the attacker down if they get out of their render distance, or the attacker was able to unload thechunkwhere the wolves were. Angry wolves cannot beleashed, but a wild wolf may become angry while it is still leashed without dropping the lead.
- Tamedwolves have friendlier-looking eyes. They have a default red collar around their neck, which can be dyed using any color ofdyeon the wolf by any player regardless of who owns the wolf. Pressinguseon the wolf makes it sit and remain in place, and not follow the player. Tamed wolves that are not sitting attack players or mobs that their owner attacks, or those that injure their owner unless the target has the same owner or is on the sameteam. They do not attackcreepers,ghasts, ortamedanimals, regardless of owner. Standing tamed wolves attack only skeletons and their variants without provocation. Kills by tamed wolves count as player kills: this means mobs killed by a tamed wolf can dropexperience,rare dropsorequipped items. Tamed wolves are always passive to theplayer, even if the player hits them or kills a tamed wolf on the same team.

A wolf becomes hostile to a player or other mob that attacks it unless the attacker is the wolf's owner, or is otherwise on the same team, or if killed in one hit.‌[JE  only] It also causes wild wolves and standing tamed wolves in a 33×33×21 cuboid centered on the attacked wolf to become hostile to the attacker, allowing coordination for attacks and team hunts (only in wild wolves).

In Java Edition, any tamed wolf attacked by a player/mob causes all standing wolves on that team to attack that player/mob who attacked the tamed wolf.

If damaged by a mob or entity other than a player or arrow, wolves of any type take roughly half of the original damage ((damage + 1) / 2).

Skeletons and their variants, foxes, baby turtles and passive rabbits actively avoid both tamed and wild wolves. Killer rabbits‌[JE  only] attack wolves actively. Sheep ignore wolves, but flee when attacked by one. Sheep ignore tamed wolves but also do not flee from them.

When a player within 8 blocks holds meat or bones near a wolf, the wolf tilts its head as if to 'beg' for the food for 2 to 4 seconds.

The behavior of pups is the same as tamed wolves. Pups have large heads, similar to other baby animals.

Wolves are 0.85‌[JE  only] or 0.8‌[BE  only] blocks tall and pups are 0.425‌[JE  only] or 0.4‌[BE  only] blocks tall.

The textures of the wolves are tinted dark gray once submerged in water.

In Peaceful difficulty, attacking a wild wolf aggravates the wolf and its group, but they deal no damage to the player.

### Movement
A tamed wolf shaking off water.
Standing tamed wolves wander randomly when near their owner, but follow if more than 10 blocks away and teleport to a nearby free block (if any) if more than 12 blocks away. Besides making travel easier, teleportation can be used to rescue them from lava, water or pits, as they immediately teleport to a safe area.

- Wolves can be told to "sit" by pressinguseon them and made to stand again with another press ofuse.
	- A wolf automatically sits when first tamed.‌[Java Edition  only]
	- While sitting, they do not follow the player. However, if their owner fights a mob near them, they are still likely to join the fight. When the fight is over, they go back to sitting (if in water, they do not sit until they are on dry land, telling the wolf to sit makes it stand). They sit at their new location instead of returning to wherever they were previously.
	- Wolves stand up and follow the player if it is pushed into water or injured while sitting.
- Wolves can either attack (within 16 blocks) or flee (within 24 blocks) fromllamas. The wolves' speed is increased by 50% whereas they flee.
- Wolves find paths to their targets if attacking within 16 blocks, even in difficult terrain. They also navigate along the edges of cliffs and occasionally fall far enough to takedamageif they leap.
- Wolves attack their targets running about at the player's walking speed and by leaping at them in exactly the same manner asspiders, but cause no damage while in midair. Tamed wolves attack any animal the player starts to attack. They also can navigate and turn around in 1×1 horizontal tunnels.
- After emerging from water, a wolf shakes the water off their fur. This is represented by an animation and waterparticles.

### Teleportation
Tamed wolves teleport to their owner if they are more than 12 blocks away, with a few caveats.

- Teleporting resets the focus of a tamed wolf, so if a wolf is attacking a mob and teleports beside a player, it resumes following the player, as its tracking has been reset.
- It is possible for tamed wolves to teleport to an inaccessible location (e.g. underice) and be injured or die ofsuffocationas a result. This happens when the wolf considerstransparentblocks, such as glass, orhalf-blocks, to be open.
- It cannot teleport when it is sitting.

An angry or untamed wolf does not teleport.

Tamed wolves do not teleport if:

- The wolf has been ordered to sit.[4]
	- Exception: The wolf is likely to teleport if it is injured while sitting (it no longer sits after teleporting). An example is if a wolf that is sitting is hit by another player, it teleports to their owner.
	- Exception: If the wolf is in a loadedchunk, and the player gets damaged by a mob, there's a chance for the wolf to stop sitting, causing them to teleport if the player is far away, then attacking the player's attacker and sitting down afterward.
- The wolf is chasing after askeleton. This can lead to wolves standing and jumping in one place, such as over a cavern if a skeleton is near. The wolf teleports once the skeleton is killed.
- The wolf is in aminecartor aboat.
- The wolf has been attached to a fence post with a lead.
- The wolf is in an unloadedchunk.
- None of the blocks on the edge of a 5×1×5 region centered on the player aretransparentblockswith a solid block below and another transparent block above.
- The player is in another dimension; a wolf remains in its current dimension until the player returns. However, wolves can be transported to another dimension by pushing them into the portal first.
- The owner is not directly touching the ground (e.g. usingelytra, swimming, flying, in aboat).

Wolf teleportation is completely silent.[5]

### 
Many tamed wolves sitting.
A group of begging wolves.
A wolf can be tamed by feeding it bones. Once tamed, a wolf does not accept any more bones. Note that the number of bones required is random – each bone has a 1⁄3 chance of taming the wolf.[6] If the wolf is tamed, it receives a red collar and, in Java Edition, sits if not swimming. There is no limit[7] to the number of wolves the player can tame.

A wolf's tail rises and lowers depending on its health. The exact health of an individual wolf can be determined by measuring the angle between its hind legs and tail. The angle indicates the percentage of health that the wolf has. Tamed wolves whine when they have low health (below 10). Wild wolves have a maximum health of 8, so their tails always remain significantly lower than those of tamed wolves. Tamed wolves can be healed by feeding them any sort of meat (excluding fish and rabbit stew‌[Java Edition  only]); listed below, this restores as much of the wolf's health as the same food would restore hunger points when eaten by the player.

The wolf cannot be tamed if it is hostile or already tamed.

Wolves that are tamed by the same player can accidentally attack each other while attacking another mob, leading to a fight.



| Food            | Heals | Notes                                                                                               |
|-----------------|-------|-----------------------------------------------------------------------------------------------------|
| Pufferfish      | 1     | Pufferfish can be fed to wolves without inflictingHunger,Poison, andNausea.‌[Bedrock Edition  only] |
| Tropical Fish   |       |                                                                                                     |
| Raw Chicken     | 2     | Raw chicken can be fed to wolves without inflictingHunger.                                          |
| Raw Mutton      |       |                                                                                                     |
| Raw Cod         | 2     | ‌[Bedrock Edition  only]                                                                            |
| Raw Salmon      |       |                                                                                                     |
| Raw Porkchop    | 3     |                                                                                                     |
| Raw Beef        |       |                                                                                                     |
| Raw Rabbit      |       |                                                                                                     |
| Rotten Flesh    | 4     | Rotten flesh can be fed to wolves without inflictingHunger.                                         |
| Cooked Rabbit   | 5     |                                                                                                     |
| Cooked Cod      | 5     | ‌[Bedrock Edition  only]                                                                            |
| Cooked Mutton   | 6     |                                                                                                     |
| Cooked Chicken  |       |                                                                                                     |
| Cooked Salmon   | 6     | ‌[Bedrock Edition  only]                                                                            |
| Cooked Porkchop | 8     |                                                                                                     |
| Steak           |       |                                                                                                     |
| Rabbit Stew     | 10    | ‌[Bedrock Edition  only]                                                                            |

Wolves do not get food poisoning, so they can freely eat rotten flesh, pufferfish or raw chicken. Feeding a tamed wolf that is already at full health usually starts the "love mode" animation.

A tamed wolf's necklace/collar color can be changed by using a dye on the wolf.

### Wolf Armor
A wolf wearing wolf armor.
Main article: Wolf Armor

  

This section describes content that may be included in Java Edition. 
This content has appeared in Java Edition 1.20.5 development versions, but the full update containing it has not been released yet.



  

This section describes an experimental feature in Bedrock Edition. 
This feature is not enabled in-game by default and requires enabling the "Armadillo and Wolf Armor" setting in the "Experiments" section in Bedrock Edition.


Using wolf armor on a wolf that the player has tamed equips it onto the wolf.

Wolf armor absorbs all damage done to the wolf with some exceptions (see the list below), until its durability runs out. When the armor absorbs damage, the wolf does not produce a hurt noise.

Wolf armor does not absorb damage dealt by the following sources:

- Drowning
- Freezing
- Suffocating
- Magic
- Thorns
- TheWithereffect
- Void
- Being outside theworld border
- Entity cramming
- The/killcommand
- Warden's sonically-charged shriek

If the owner uses shears on a wolf that is wearing armor, the armor gets unequipped from the wolf.

If a wolf dies while equipped with wolf armor, the armor is dropped.

### Breeding
Main article: Breeding
A pup sitting.
Tamed wolves at full health can be bred with any type of meat, including rotten flesh and raw chicken without causing the hunger status effect. There is a 5-minute cooldown for breeding, during which the wolf does not accept meat.

The growth of pups can be slowly accelerated using any type of meat. Each use takes 10% off the remaining time to grow up. Unlike healing in Bedrock Edition, rabbit stew or any type of fish cannot be used for breeding or speeding up growth.

Breeding two wolves that recognize someone else as an owner causes the pup to also be owned by the owner of the original two wolves. If two tamed wolves have different owners, the pup is randomly assigned to one of their two owners as its permanent owner.

If the player attacks an untamed wolf and then feeds it, hearts appear as when entering breeding mode, although the wolf does not breed and remains aggressive toward the player.

## Data values
### ID
Java Edition:

| Name | Identifier | Translation key         |
|------|------------|-------------------------|
| Wolf | `wolf`     | `entity.minecraft.wolf` |

Bedrock Edition:

| Name | Identifier | Numeric ID | Translation key    |
|------|------------|------------|--------------------|
| Wolf | `wolf`     | `14`       | `entity.wolf.name` |

### Entity data
Wolves have entity data associated with them that contain various properties.

Java Edition:

Main article: Entity format
- Entity data
	- 
	- Additional fields for mobs that can become angry
	- 
	- Additional fields for mobs that can be tamed by players
	- 
	- Additional fields for mobs that can breed
	- 
	- Tags common to all entities
	- 
	- Tags common to all mobs
	- CollarColor: The color of the wolf's collar. Present even for wild wolves (but does not render); default value is 14.
	- variant: Which of the 9 variant textures the wolf renders with. Default value is "minecraft:pale".‌[upcoming: JE 1.20.5]


Collar color
Main article: Wolf/DV[edit]

Bedrock Edition:

SeeBedrock Edition level format/Entity format.
