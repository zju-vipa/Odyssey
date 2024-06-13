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



