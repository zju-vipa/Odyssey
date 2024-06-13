### Daytime
This is the start of a new day.
Daytime is the longest section of the cycle, lasting 10 minutes.

- Start: 0 ticks (06:00:00.0)
- Mid: 6000 ticks (12:00:00.0)
- End: 12000 ticks (18:00:00.0)

When a player first spawns in singleplayer, the daylight cycle always starts at the beginning of the daytime (0:00). Most multiplayer servers also start at the beginning of the daytime, but the daylight cycle continues regardless of any new players joining.

During the daytime, the sun rises up to its peak in a light blue sky. The exact color of the sky depends on the current biome; for example, desert skies are a lighter shade of blue than plains skies.

All blocks that are in direct vertical view of the sky receive sunlight at the internal sky-light level 15, which is the maximum. Sunlight provides ample light for the growth of saplings, grass blocks and crops. Most undead mobs (including zombies and skeletons) exposed to direct sunlight (and are not in shade, in water, or wearing helmets) are set on fire. Additionally, sunlight renders spiders neutral, unless they are currently chasing a player, and any endermen exposed to sunlight teleport randomly when near the player and randomly become neutral if having been aggressive for at least 30 seconds.



### 
Example sunset seen from a high spot on the map.
Sunset is the period between daytime and nighttime, and always lasts 50 seconds.

- Start: 12000 ticks (18:00:00.0)
- End: 13000 ticks (19:00:00.0)

During sunset, the Sun descends on the western horizon, and the Moon rises on the eastern horizon. The sky near the setting Sun glows a vibrant orange-red. The internal sky-light level decreases. Eventually, undead mobs exposed to direct sunlight are set not to burn.

Between dusk and dawn, players may sleep in a bed. In singleplayer mode, doing so advances the daylight cycle to dawn and sets the weather to clear. This also occurs in multiplayer as long as every player online is in a bed simultaneously. Time does not pass for other aspects of the world, however; for example, crops do not grow and furnaces do not cook or smelt as they would when players are awake.



A snowy tundra biome during the night; various mobs can be seen.
### Nighttime
"Night" redirects here.  For night in Minecraft Dungeons, see MCD:Night.
Nighttime lasts 8 minutes 20 seconds.

- Start: 13000 ticks (19:00:00.0)
- Mid: 18000 ticks (00:00:00.0)
- End: 23000 ticks (05:00:00.0)

During the night, the Moon rises to its peak in a dark blue sky dotted with small white stars. The stars appear to move with the Moon and can be first seen toward the end of the sunset.


During the nighttime, the world is covered in darkness; the internal sky-light level falls to a minimum of 4, which allows hostile mobs to spawn on the surface. The exact duration for which hostile mobs are able to spawn in exposed areas is 13188 ticks.[note 1] Regardless of the low light level, crops continue to grow during the night as long as one player is not sleeping.
Example of the Sun rising in the horizon.


### 
Sunrise is the period between nighttime and daytime, and always lasts 50 seconds.

- Start: 23000 ticks (05:00:00.0)
- End: 24000 (0) ticks (06:00:00.0)

During sunrise, the Moon sets on the western horizon and the Sun rises on the eastern horizon. The sky near the rising Sun glows orange.

The internal sky-light level increases. Eventually, the effects of sunlight return, dissipating the threat of most hostile mobs.


## Clocks
Main article: Clock
A clock allows players to determine Minecraft time. A clock is useful while underground where the current day/night cycle is not visible. A clock helps the player avoid mistakenly surfacing at night and falling prey to night-spawned mobs on the surface.

Clocks spin uselessly in the Nether and the End, because there is no daylight cycle in those dimensions.

## Commands
If commands are enabled, then it is possible to change the current time with the /time commands, as detailed below. To enable or disable the daylight cycle, use the following command: /gamerule doDaylightCycle true|false

### Set time
Specific times can be set with the /time set command.

Syntax:/time set <number|day|noon|sunset|night|midnight|sunrise>
Examples:

/time set 0– Sets the time to the beginning of the Minecraft day.
/time set day– Sets the time to 1000.
/time set 12000– Sets the time to dusk/sunset.
/time set sunrise‌[Bedrock Edition  only]- Sets the time to 23000.
/time set noon- Sets the time to 6000.
