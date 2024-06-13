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

