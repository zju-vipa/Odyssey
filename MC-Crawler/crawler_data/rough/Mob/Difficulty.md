# Difficulty
Difficulty is an option in Minecraft that has a direct impact on the ease of gameplay, allowing the game's challenges to be tailored to the player's skill level.

## Contents
- 1 World settings
	- 1.1 Peaceful
	- 1.2 Easy
	- 1.3 Normal
	- 1.4 Hard
	- 1.5 Hardcore mode
- 2 Moon phase
- 3 Regional difficulty
	- 3.1 Clamped regional difficulty
- 4 Effects
	- 4.1 Mob damage
	- 4.2 Other effects
- 5 Video
- 6 History
- 7 Issues
- 8 See also
- 9 Notes
- 10 References

## World settings

The difficulty button in the options menu.
There are four difficulty levels in the game: Peaceful, Easy, Normal and Hard. These can be changed when creating a world, in the settings, as well as with the /difficulty command.

While the difficulty settings modify the challenge in Survival mode, they also affect hostile mobs in Creative mode the same as in Survival; for example:

- Hostile mobs cannot spawn naturally in Creative Peaceful.
- Zombieshave the same difficulty-dependent chances as in Survival to convert villagers intozombie villagers(0% in Creative Easy, 50% in Creative Normal, 100% in Creative Hard).
- Hostile mobs killed bymob grindersin farms drop higher-value items in Creative Hard.

Survival mode is affected by difficulty as described in the sections below. 

### Peaceful
No hostile mobs can spawn naturally, except for shulkers, hoglins, piglins, piglin brutes‌[BE  only], and the ender dragon. No spiders, cave spiders, zombified piglins, endermen or drowned – neutral rather than hostile mobs – can spawn naturally. When any of these mobs attempt to spawn (whether naturally, through monster spawners, spawn eggs, or commands), they are removed from the game instantaneously. Skeleton horses are also not able to spawn naturally.[1] All mobs that can spawn (such as shulkers, piglins, or wolves) are completely peaceful and unable to harm the player - with the exception of the ender dragon. When the difficulty is switched from any other setting to Peaceful, all mobs that are not allowed to spawn on Peaceful are removed from the world. Players regain health rapidly over time. Despite this, it is still possible to die if damage is received quickly enough. TNT deals no direct damage to the player, but it does give knockback still, meaning a player can be killed by it if it launches them too far upward. The hunger bar never depletes; in Java Edition, players therefore cannot eat anything except golden apples, chorus fruits, milk buckets, honey bottles and suspicious stew, unless the player switched to Peaceful when their hunger bar was below the maximum. Players can eat normally in Bedrock Edition. Additionally, if the hunger bar is below the maximum, it regenerates quickly.

Because of the gameplay changes and the absence of many mob types, many blocks and items are unavailable to the player. A list can be found at Non-renewable_resource#Peaceful_difficulty. In addition, the player is unable to get many advancements and achievements. 

One major effect of the lack of certain resources is that end portals cannot be activated by the player in Peaceful difficulty, because it is impossible to acquire the eyes of ender necessary to activate an end portal.[note 1] However, it is possible for an end portal to be activated by naturally generating with an eye of ender already embedded within all 12 end portal frames. For any given end portal, there is a 1 in a trillion chance of this happening.[note 2]
However, because of the huge number of possible seeds, over 8 million seeds are known to generate such end portals.
[2]

### Easy
Hostile mobs spawn, but they deal 1⁄2 of the damage they would on Normal difficulty plus 1. The hunger bar can deplete, damaging the player until 10 remain if it drains completely. Cave spiders and bees cannot poison players on Easy difficulty, and the wither does not cause the Wither effect, although wither skeletons do. Lightning sets only the struck block on fire, not surrounding blocks. Zombies do not break down doors, and do not turn villagers into zombie villagers. Zombies and skeletons don't wear full sets of armor. Hostile mobs like zombies, skeletons, spiders, husks and strays deal about 1 or 2 damage.

### Normal
Hostile mobs spawn and deal standard damage. The hunger bar can deplete, damaging the player until 1 remains if it drains completely. Zombies do not break down doors, but villagers killed by zombies have a 50% chance of turning into zombie villagers. Zombies and skeletons rarely wear sets of enchanted armor. Vindicators can break doors.

### Hard
Hostile mobs deal approximately 11⁄2 times the damage they would deal on Normal difficulty, and in some cases drop higher-value items when killed. The hunger bar can deplete, not only damaging but also killing the player if it drains completely. Zombies can break through wooden doors and can spawn reinforcements when attacked. In Java Edition, spiders can spawn with a beneficial status effect (Speed, Strength, Regeneration, or Invisibility), with these effects having an infinite duration. Villagers killed by zombies always turn into zombie villagers. Pillagers spawn near the player, with their attacks dealing 4 damage. In Bedrock Edition, if the world type is infinite, they deal 5 damage.

### Hardcore mode

  

This feature is exclusive to  Java Edition. 



  

This article describes content that may be included in Bedrock Edition. 
This content has appeared in Bedrock Edition 1.21.0 development versions, but the full update containing it has not been released yet.


- Icon for Java Edition Hardcore mode.

Main article: Hardcore
In Java Edition, at the world creation screen, selecting Hardcore from among the game mode options causes the player to spawn in Hard difficulty, does not allow it to be changed, and allows the player only one life. In a single player world, a player who dies can choose to respawn in Spectator mode or return to the title screen. In multiplayer, upon death, the player's game mode is automatically set to Spectator mode.

The only way to change the difficulty of Hardcore is to use the Open to LAN feature in the pause menu to enable commands, or to use an .NBT editor on the world's .NBT file.

This difficulty is currently not available in Realms.

It is available in Bedrock Edition from version 1.21.0 and onward.

## Moon phase
The phase of the moon has effects on the spawning of slimes in swamp biomes, and contributes to the calculation of regional difficulty. The fuller the moon is, the greater the effect.

The moon does not actually have to be in the sky for this effect to take place, since the moon exists in daytime and across dimensions.

|  | Moon phase | Value | Percentage |
|--|------------|-------|------------|
|  | Full       | 1.0   | 100%       |
|  | Gibbous    | 0.75  | 75%        |
|  | Quarter    | 0.5   | 50%        |
|  | Crescent   | 0.25  | 25%        |
|  | New        | 0.0   | 0%         |

## Regional difficulty
Regional difficulty values shown on the debug screen
Regional difficulty or local difficulty is a value between 0.00 and 6.75 that the game calculates by considering not just the world difficulty setting, but also the inhabited time of a chunk, the total daytime in the world, and the phase of the moon. This value is shown on the debug screen as the first value listed after the heading "Local Difficulty". This value determines several aspects of the difficulty of gameplay (see below).

The inhabited time of a chunk increases for each tick a player spends with the chunk loaded. This is a cumulative measure of time—if 50 players spend a single hour in a chunk, it counts the same as if one player spent 50 hours there. The effect of inhabited time on regional difficulty is capped at 50 hours.

The total daytime in the world is the value from /time query daytime added to the "Day" on the F3 debug screen converted to ticks, i.e. daytime + (dayNumber * 24,000). This is not the same as the actual playtime in the world (the value from /time query gametime). It affects the regional difficulty after the first 3 in-game days, and has no additional effect after 63 in-game days.

In pseudocode, the calculation of regional difficulty is:

# DaytimeFactor, ChunkFactor, and RegionalDifficulty are floating-point variables
# MoonPhase is as in the table above.

if (difficulty is Peaceful) return 0

if (TotalDaytime > 63 in-game days) DaytimeFactor = 0.25
else if (TotalDaytime < 3 in-game days) DaytimeFactor = 0 
else DaytimeFactor = (TotalDaytimeInTicks − 72,000) / 5,760,000

if (ChunkInhabitedTime > 50 hours) ChunkFactor = 1
else ChunkFactor = ChunkInhabitedTimeInTicks / 3,600,000

if (difficulty is Normal or Easy) multiply ChunkFactor by 0.75

if (MoonPhase ÷ 4 > DaytimeFactor) add DaytimeFactor to ChunkFactor
else add (MoonPhase ÷ 4) to ChunkFactor

if (difficulty is Easy) multiply ChunkFactor by 0.5

RegionalDifficulty = 0.75 + DaytimeFactor + ChunkFactor

if (difficulty is Normal) multiply RegionalDifficulty by 2
if (difficulty is Hard) multiply RegionalDifficulty by 3

return RegionalDifficulty

The raw regional difficulty therefore is always 0.0 on Peaceful and ranges from 0.75 to 1.5 on Easy, 1.5 to 4.0 on Normal, and 2.25 to 6.75 on Hard.

### Clamped regional difficulty
How clamped regional difficulty relates to regional difficulty
The clamped regional difficulty (also known as special multiplier) also is a value between 0.00 and 1.00 based on regional difficulty. This value is shown on the debug screen as the second value listed after the heading "Local Difficulty". This is yet another value that affects the difficulty of gameplay (see below).

The regional difficulty value is clamped as follows:

if (RegionalDifficulty < 2.0) value = 0.0;
else if (RegionalDifficulty > 4.0) value = 1.0;
else value = (RegionalDifficulty − 2.0) / 2.0;

Thus, on Easy, where regional difficulty is never higher than 1.5, the clamped value is always zero.

On Normal, the effects reach the maximum after 63 in-game days (1512000 game ticks) in a fully-inhabited chunk on a full moon; and on Hard after 63 in-game days the effects reach the maximum in chunks inhabited 4 1⁄6 hours during a full moon and remain at maximum in chunks inhabited over 16 2⁄3 hours.[verify]

## Effects
### Mob damage
The damage mobs deal to players is affected by the difficulty setting of the world they are in. The below values represent the amount of damage taken per hit.

- A mob attackinganother mobalways deals the damage it would deal to a player on Normal difficulty, even if the current value of the difficulty setting is different.
- The values for acreeperand aghastassume the player is directly adjacent to the respective explosion.
- The damage ofslimesandmagma cubesdepends on their size. Tiny slimes, while hostile, are unable to do damage directly.
- Mobs deal no damage to players on peaceful.

| Mob                                    | Difficulty                 |                              |                                    | Status effect(s)                                                                                                                |
|----------------------------------------|----------------------------|------------------------------|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
|                                        | Easy                       | Normal                       | Hard                               |                                                                                                                                 |
| Axolotl                                |                            |                              | 2                                  | No                                                                                                                              |
| Bee                                    | 2                          | 2                            | 3                                  | Poisonfor 10 seconds on Normal difficulty and for 18 seconds on Hard difficulty                                                 |
| Blaze(melee)                           | 4                          | 6                            | 9                                  | No                                                                                                                              |
| Blaze fireball                         |                            |                              | 5+firefor 5 seconds                | No                                                                                                                              |
| Bogged arrow                           |                            |                              | 3to 5                              | Poisonfor 4 seconds                                                                                                             |
| Bogged(melee)                          |                            | 2                            | 3                                  | No                                                                                                                              |
| Breeze wind charge                     |                            | 1                            | 1.5× 0.75                          | No                                                                                                                              |
| Cat                                    |                            |                              | 3                                  | No                                                                                                                              |
| Cave Spider                            | 2                          | 2                            | 3                                  | Poisonfor 7 seconds on Normal difficulty and for 15 seconds on Hard difficulty                                                  |
| Creeper explosion(normal)              | 22.5× 11.25                | 43× 21.5                     | 64.5× 32.25                        | When exploding: NoIf having a potion effect when exploding, it leaves an effect cloud with the effect, like a lingering potion. |
| Creeper explosion(charged)             | 43.5× 21.75                | 85× 42.5                     | 127.5× 63.75                       |                                                                                                                                 |
| Dolphin                                | 2.5× 1.25                  | 3                            | 4.5× 2.25                          | No                                                                                                                              |
| Drowned                                |                            |                              |                                    | No                                                                                                                              |
| Drowned trident(Ranged)                | 7                          | 9                            | 12× 6                              | No                                                                                                                              |
| Drowned trident(Melee)‌[BE  only]      | 6                          | 11× 5.5                      | 16× 8                              | No                                                                                                                              |
| Elder Guardian(Laser)                  | 5                          | 8                            | 12× 6                              | InflictsMining FatigueIII for 5 minutes on nearby players                                                                       |
| Elder Guardian(Spikes)                 |                            | 2                            | 3                                  |                                                                                                                                 |
| Elder Guardian Ghost(Spikes)           |                            |                              | 2                                  |                                                                                                                                 |
| Ender Dragon(Melee)                    | 6                          | 10                           | 15× 7.5                            | No                                                                                                                              |
| Ender Dragon(Wings)                    | 3                          | 5                            | 7                                  | No                                                                                                                              |
| Ender Dragon(Breath)                   |                            |                              | 3per second                        | Area effect cloudofInstant Damage                                                                                               |
| Ender DragonDragon Fireball            |                            |                              | 6per second                        |                                                                                                                                 |
| Enderman                               | 4.5× 2.25                  | 7                            | 10.5× 5.25                         | No                                                                                                                              |
| Endermite                              |                            | 2                            | 3                                  | No                                                                                                                              |
| Evoker fangs‌[JE  only]                | 4                          | 6                            | 9                                  | No                                                                                                                              |
| Evoker fangs‌[BE  only]                |                            |                              | 6                                  | No                                                                                                                              |
| Fox                                    |                            | 2                            | 3                                  | No                                                                                                                              |
| Frog                                   |                            |                              | Target despawns after being pulled | No                                                                                                                              |
| Ghast fireball(Impact)                 | 4                          | 6                            | 9                                  | No                                                                                                                              |
| Ghast fireball(Explosion)              | 9.5× 4.75                  | 17× 8.5                      | 25.5× 12.75                        | No                                                                                                                              |
| Giant‌[JE  only]                       | 26× 13                     | 50× 25                       | 75× 37.5                           | No                                                                                                                              |
| Goat                                   |                            | 2                            | 3                                  | No                                                                                                                              |
| Goat(baby)                             |                            | 1                            | 1.5× 0.75                          | No                                                                                                                              |
| Guardian(Laser)                        | 4                          | 6                            | 9                                  | No                                                                                                                              |
| Guardian(Spikes)                       |                            | 2                            | 3                                  | No                                                                                                                              |
| Hoglin‌[JE  only]                      | 2.5× 1.25to 5              | 3to 8                        | 4.5× 2.25to 12× 6                  | No                                                                                                                              |
| Hoglin‌[BE  only]                      | 3                          | 6                            | 9                                  | No                                                                                                                              |
| Hoglin(baby)                           |                            | 0.5× 0.25                    | 0.75× 0.375                        | No                                                                                                                              |
| Husk                                   | 2.5× 1.25                  | 3                            | 4.5× 2.25                          | Hungerwhen attacking any mob for 7 × floor ofRDseconds                                                                          |
| Illusioner arrow‌[JE  only]            |                            | 2to 5                        | 3to 5                              | ThrowsBlindnessspells on the player, ifregional difficultyis 2 or greater                                                       |
| Iron Golem                             | 4.75× 2.375to 11.75× 5.875 | 7.5× 3.75to 21.5× 10.75      | 11.25× 5.625to 32.25× 16.125       | No                                                                                                                              |
| The Killer Bunny                       | 5                          | 8                            | 12× 6                              | No                                                                                                                              |
| Llama spit                             |                            | 1                            | 1.5× 0.75                          | No                                                                                                                              |
| Magma Cube(big)                        | 4                          | 6                            | 9                                  | No                                                                                                                              |
| Magma Cube(medium)                     | 3                          | 4                            | 6                                  | No                                                                                                                              |
| Magma Cube(small)                      | 2.5× 1.25                  | 3                            | 4.5× 2.25                          | No                                                                                                                              |
| Ocelot                                 |                            |                              | 3                                  | No                                                                                                                              |
| Old Zombie Villager                    | 2.5× 1.25                  | 3                            | 4.5× 2.25                          | No                                                                                                                              |
| Panda                                  | 4                          | 6                            | 9                                  | No                                                                                                                              |
| Phantom‌[JE  only]                     |                            | 2                            | 3                                  | No                                                                                                                              |
| Phantom‌[BE  only]                     | 4                          | 6                            | 9                                  | No                                                                                                                              |
| Piglin arrow‌[JE  only]                |                            | 2to 5                        | 3to 5                              | No                                                                                                                              |
| Piglin arrow‌[BE  only]                |                            | 2- 4                         | 2to 5                              | No                                                                                                                              |
| Piglin(Melee with Sword)‌[JE  only]    | 5                          | 8                            | 12× 6                              | No                                                                                                                              |
| Piglin(Melee with Sword)‌[BE  only]    | 5                          | 9                            | 13× 6.5                            | No                                                                                                                              |
| Piglin(Melee without Sword)‌[JE  only] | 3.5× 1.75                  | 5                            | 7.5× 3.75                          | No                                                                                                                              |
| Piglin Brute‌[JE  only]                | 7.5× 3.75                  | 13× 6.5                      | 19.5× 9.75                         | No                                                                                                                              |
| Piglin Brute‌[BE  only]                | 6                          | 10                           | 15× 7.5                            | No                                                                                                                              |
| Piglin Brute(Unarmed)                  | 4.5× 2.25                  | 7                            | 10.5× 5.25                         | No                                                                                                                              |
| Pillager arrow                         | 3.5× 1.75                  | 4                            | 5                                  | No                                                                                                                              |
| Pillager(Melee)‌[BE  only]             | 2                          | 3                            | 5                                  | No                                                                                                                              |
| Polar Bear                             | 4                          | 6                            | 9                                  | No                                                                                                                              |
| Pufferfish(Semi-puffed)                |                            | 2                            | 3                                  | Poisonfor 3 seconds                                                                                                             |
| Pufferfish(Fully Puffed)‌[JE  only]    | 2.5× 1.25                  | 3                            | 4.5× 2.25                          | Poisonfor 6 seconds                                                                                                             |
| Pufferfish(Fully Puffed)‌[BE  only]    |                            | 2                            | 3                                  | Poisonfor 10 seconds                                                                                                            |
| Ravager(Melee)                         | 7                          | 12× 6                        | 18× 9                              | No                                                                                                                              |
| Ravager(Roar)                          | 4                          | 6                            | 9                                  | No                                                                                                                              |
| Shulker bullet                         | 3                          | 4                            | 6                                  | Levitationfor 10 seconds                                                                                                        |
| Silverfish                             |                            | 1                            | 1.5× 0.75                          | No                                                                                                                              |
| Skeleton arrow‌[JE  only]              | 2to 4                      | 3to 4                        | 4to 5                              | No                                                                                                                              |
| Skeleton arrow‌[BE  only]              |                            | 1to 4, varies with proximity | 1to 5, varies with proximity       | No                                                                                                                              |
| Skeleton(melee)                        |                            | 2                            | 3                                  | No                                                                                                                              |
| Slime(big)                             | 3                          | 4                            | 6                                  | No                                                                                                                              |
| Slime(medium)                          |                            | 2                            | 3                                  | No                                                                                                                              |
| Slime(small)                           |                            |                              | 0                                  | No                                                                                                                              |
| Snow Golem snowball                    |                            |                              | 3toblazes                          | No                                                                                                                              |
| Spider                                 |                            | 2                            | 3                                  | No, but can spawn with effects                                                                                                  |
| Stray arrow‌[JE  only]                 |                            |                              | 3to 5                              | Slownessfor 30 seconds when their tipped arrow hits any mob (including another stray)                                           |
| Stray arrow‌[BE  only]                 |                            |                              | Damage varies with proximity       |                                                                                                                                 |
| Stray(melee)                           |                            | 2                            | 3                                  | No                                                                                                                              |
| Trader Llama spit                      |                            | 1                            | 1.5× 0.75                          | No                                                                                                                              |
| Vex                                    | 5.5× 2.75                  | 9                            | 13.5× 6.75                         | No                                                                                                                              |
| Vex(Unarmed)                           | 3                          | 4                            | 5                                  | No                                                                                                                              |
| Villager's firework rocket             | 5                          | 8                            | 12× 6                              | No                                                                                                                              |
| Vindicator                             | 7.5× 3.75                  | 13× 6.5                      | 19.5× 9.75                         | No                                                                                                                              |
| Vindicator(Unarmed)                    | 3.5× 1.75                  | 5                            | 7.5× 3.75                          | No                                                                                                                              |
| Warden(Melee)                          | 16× 8                      | 30× 15                       | 45× 22.5                           | No                                                                                                                              |
| Warden(Ranged)                         | 6                          | 10                           | 15× 7.5                            | No                                                                                                                              |
| Witch                                  |                            |                              | Deals damage by throwingpotions    | Throws splash potions ofPoison,Instant Damage,Slowness, andWeakness                                                             |
| Wither Skeleton                        | 5                          | 8                            | 12× 6                              | Witherfor 10 seconds                                                                                                            |
| Wither Skeleton(Unarmed)               | 2                          | 2                            | 3                                  | Witherfor 10 seconds                                                                                                            |
| Wither(birth explosion)                | 35.5× 17.75                | 69× 34.5                     | 103.5× 51.75                       | No                                                                                                                              |
| Wither Skull                           | 5                          | 8                            | 12× 6                              | WitherII for 10 seconds on Normal difficulty and 40 seconds on Hard difficulty                                                  |
| Wither(dash attack)<br/>‌[BE  only]    |                            |                              | 15× 7.5                            | No                                                                                                                              |
| Wolf                                   | 3                          | 4                            | 6                                  | No                                                                                                                              |
| Zoglin                                 | 3to 5                      | 3to 8                        | 4.5× 2.25to 12× 6                  | No                                                                                                                              |
| Zoglin(baby)                           | 0.25× 0.125                | 0.5× 0.25                    | 0.75× 0.375                        | No                                                                                                                              |
| Zombie                                 | 2.5× 1.25                  | 3                            | 4.5× 2.25                          | No                                                                                                                              |
| Zombified Piglin                       | 5                          | 8                            | 12× 6                              | No                                                                                                                              |
| Zombified Piglin(Unarmed)              | 3                          | 5                            | 7                                  | No                                                                                                                              |
| Zombie Villager                        | 2.5× 1.25                  | 3                            | 4.5× 2.25                          | No                                                                                                                              |
| Wither Skull(explosion)                |                            |                              | 5                                  |                                                                                                                                 |



### Other effects
| Attribute                                                                                                                                                  | Notes                                                                                                                                                           | Condition        |                          |                                   |                 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|--------------------------|-----------------------------------|-----------------|
|                                                                                                                                                            |                                                                                                                                                                 | World difficulty | Regional difficulty (RD) | Clamped regional difficulty (CRD) | Moon phase only |
| Mobs and explosions do higher damage to players.                                                                                                           | $Peaceful: No damageEasy:of Normal damage + 1 (never higher than Normal damage)Hard: 1\frac{1}{2}$times Normal damage                                           | Yes              | No                       | No                                | No              |
| Guardians (both types) have higher laser magic damage.                                                                                                     | Hard: + 2, added before calculating the difficulty-scaled mob damage                                                                                            | Yes              | No                       | No                                | No              |
| Starvation more harshly affects health.                                                                                                                    | Easy/Normal/Hard: starvation brings health down to 10/1/0 HP                                                                                                    | Yes              | No                       | No                                | No              |
| Mobs that spawn with armor are more likely to have more armor.                                                                                             | Easy & Normal: 75%/56%/42% of having 2/3/4 pieces;<br/>Hard: 90%/81%/73% of having 2/3/4 pieces                                                                 | Yes              | No                       | No                                | No              |
| Zombies are more likely to spawn with weapons.                                                                                                             | 1% on Easy and Normal,<br/>5% on Hard                                                                                                                           | Yes              | No                       | No                                | No              |
| Zombies are able to spawn reinforcements.                                                                                                                  | Hard only                                                                                                                                                       | Yes              | No                       | No                                | No              |
| Zombies are more likely to be able to break wooden doors.                                                                                                  | A zombie having the ability to break a door: (10×CRD)%The door actually breaking: Hard only                                                                     | Yes              | No                       | Yes                               | No              |
| Villagers killed by zombies have a greater chance of becoming zombie villagers.                                                                            | 0% on Easy,<br/>50% on Normal,<br/>100% on Hard                                                                                                                 | Yes              | No                       | No                                | No              |
| Zombified piglins spawn from nether portals in the Overworld more often.                                                                                   | $peron Easy,on Normal,\frac{3}{2000}$on Hard                                                                                                                    | Yes              | No                       | No                                | No              |
| A skeleton or stray does not wait as long between bow & arrow attacks.                                                                                     | Easy/Normal: 2s cooldown<br/>Hard: 1s                                                                                                                           | Yes              | No                       | No                                | No              |
| A skeleton or stray is more accurate in ranged attacks with its bow.                                                                                       | Easy/Normal/Hard "inaccuracy" value is 10/6/2                                                                                                                   | Yes              | No                       | No                                | No              |
| Damage from arrows slightly increases.                                                                                                                     | Easy/Normal/Hard damage bonus = +0.11 / +0.22 / +0.33                                                                                                           | Yes              | No                       | No                                | No              |
| Phantomsspawn more frequently.                                                                                                                             | A spawn attempt succeeds if the local difficulty is greater than a random value between 0.0 and 3.0.                                                            | No               | Yes                      | No                                | No              |
| Phantomsspawn in larger groups.                                                                                                                            | Easy: 1-2<br/>Normal: 1-3<br/>Hard: 1-4                                                                                                                         | Yes              | No                       | No                                | No              |
| Spiders can naturally spawn withstatus effects.                                                                                                            | Hard(10×CRD)%                                                                                                                                                   | Yes              | No                       | Yes                               | No              |
| ThePoisoneffect given by acave spiderlasts longer.                                                                                                         | Normal/Hard: 7s/15s                                                                                                                                             | Yes              | No                       | No                                | No              |
| ThePoisoneffect given by abeelasts longer.                                                                                                                 | Normal/Hard: 10s/18s                                                                                                                                            | Yes              | No                       | No                                | No              |
| TheWithereffect given by awither skulllasts longer.                                                                                                        | Normal/Hard: 10s/40s                                                                                                                                            | Yes              | No                       | No                                | No              |
| A wither shoots wither skulls when idle.                                                                                                                   | Normal/Hard only                                                                                                                                                | Yes              | No                       | No                                | No              |
| A wither spawns 3–4 wither skeletons when brought below half health.‌[Bedrock Edition  only]                                                               | Normal/Hard only                                                                                                                                                | Yes              | No                       | No                                | No              |
| Lightning can cause fires in the surrounding blocks, not just the block struck.                                                                            | Normal/Hard only                                                                                                                                                | Yes              | No                       | No                                | No              |
| Fire lingers for a bit longer.                                                                                                                             | The rawencouragementvalue of blocks surrounding fire gets a bonus of (Easy/Normal/Hard) +47 / +54 / +61, before being adjusted for fire age, humidity and rain. | Yes              | No                       | No                                | No              |
| Mobs are more willing to take fall damage when pursuing a target.[note 3]                                                                                  | Easy: 33% + 8<br/>Normal: 33% + 4<br/>Hard: 33%                                                                                                                 | Yes              | No                       | No                                | No              |
| Lightningstrikes are more likely to spawn askeleton trap horse.                                                                                            | Chance = (RD)%(0.75–1.5% on Easy, 1.5–4% on Normal, 2.25–6.75% on Hard)                                                                                         | No               | Yes                      | No                                | No              |
| Burning zombies are more likely to set their target on fire, and the burn duration is longer.                                                              | Chance = (30×RD)%Burn time = 2 ×RDseconds                                                                                                                       | No               | Yes                      | No                                | No              |
| TheHungereffect caught from being attacked by ahusklasts longer.                                                                                           | Effect time = 7 ×RDseconds                                                                                                                                      | No               | Yes                      | No                                | No              |
| Illusioners can castblindness.                                                                                                                             | IfRD> 2.                                                                                                                                                        | No               | Yes                      | No                                | No              |
| Skeletons can shoot flaming arrows.                                                                                                                        | IfRD> 3.                                                                                                                                                        | No               | Yes                      | No                                | No              |
| Skeletons and zombies are more likely to have the ability to pick up dropped items.                                                                        | Having the ability: (55×CRD)%                                                                                                                                   | No               | No                       | Yes                               | No              |
| Zombies are more likely to have a greater follow distance.                                                                                                 | if (random # in range 0–1.5) ×CRDis greater than 1, that becomes a bonus multiplier on the follow distance.                                                     | No               | No                       | Yes                               | No              |
| Zombies are more likely to be "leader zombies" (gaining a bonus to max HP, a bonus to the chance to spawn reinforcements, and the ability to break doors). | Any given zombie being a "leader": (5×CRD)%                                                                                                                     | No               | No                       | Yes                               | No              |
| Mobs are more likely to spawn with armor.                                                                                                                  | Chance of getting any armor at all: (15×CRD)%                                                                                                                   | No               | No                       | Yes                               | No              |
| Mobs that spawn with weapons are more likely to have enchantments.                                                                                         | Chance for the main hand item = (25×CRD)%                                                                                                                       | No               | No                       | Yes                               | No              |
| Mobs that spawn with armor are more likely to have enchantments.                                                                                           | Chance per armor item = (50×CRD)%                                                                                                                               | No               | No                       | Yes                               | No              |
| Mobs that spawn with enchanted equipment havehigher levels of enchantments.                                                                                | Level = 5 + randInt(0,18)×CRDwhere randInt(0,18) is a random integer between 0 and 17.                                                                          | No               | No                       | Yes                               | No              |
| Slimesare more likely to be bigger.                                                                                                                        | Small: ((33×(1-CRD)/2)+16.5)%<br/>Medium: 34%<br/>Big: ((33×(1+CRD)/2)+16.5)%in other words:<br/>Small/Medium/Big: 16.5%–33% / 34% / 33%–49.5%                  | No               | No                       | Yes                               | No              |
| Slimes are more likely to spawn in swamp biomes.                                                                                                           | Seeabove                                                                                                                                                        | No               | No                       | No                                | Yes             |
| Raidhas more waves                                                                                                                                         | Easy: 3 waves<br/>Normal: 5 waves Hard: 7 waves                                                                                                                 | Yes              | No                       | No                                | No              |
| Illager patrolsize                                                                                                                                         | RD+ 1 illagers (rounded up)                                                                                                                                     | No               | Yes                      | No                                | No              |
| Illager patrol can spawn vindicator‌[Bedrock Edition  only]                                                                                                | Easy and Normal: 100% pillager<br/>Hard: 80% pillager, 20% vindicator                                                                                           | Yes              | No                       | No                                | No              |
| Illager patrol can spawn on any light level‌[Bedrock Edition  only]                                                                                        | Easy: Light level 0-7<br/>Normal and Hard: Any light level                                                                                                      | Yes              | No                       | No                                | No              |
| VindicatorandPillagerspawn from raids having higher chance to dropspecial loot.‌[Bedrock Edition  only]                                                    | Normal: 65% chance<br/>Hard: 80% chance                                                                                                                         | Yes              | No                       | No                                | No              |
| Vindicatorare able to break downWooden Door                                                                                                                | Peaceful and Easy: unable to break door<br/>Normal and Hard: can break door                                                                                     | Yes              | No                       | No                                | No              |

## Notes
1. ↑An eye of ender requires blaze powder to craft, which can be crafted only from blaze rods; but a blaze rod can be obtained only as a drop from a blaze, which is a hostile mob that cannot spawn in Peaceful.
2. ↑Since each end portal frame has a 1⁄10 chance of being filled, there is a (1⁄10)12 = 1⁄1 trillion chance of all 12 end portal frames being filled.
3. ↑Mobs accept fall damage if their health would not be reduced below 33% of their maximum health (rounded up to the nearest 1), plus a constant reserve based on difficulty. This even applies to ground-based mobs immune to fall damage.

