# Daylight cycle
The daylight cycle is a 20-minute-long cycle between two main light settings.

## Contents
- 1 Behavior
- 2 Conversions
	- 2.1 Minecraft time to real time
	- 2.2 Real time to Minecraft time
- 3 24-hour Minecraft day
	- 3.1 Daytime
	- 3.2 Sunset/dusk
	- 3.3 Nighttime
	- 3.4 Sunrise/dawn
- 4 Clocks
- 5 Commands
	- 5.1 Set time
	- 5.2 Moon phases
- 6 Achievements
- 7 Video
- 8 Graph
- 9 History
- 10 Trivia
- 11 Gallery
	- 11.1 In other media
- 12 Notes
- 13 References

## Behavior
During the daylight cycle, the sun and moon appear to rotate around the player, appearing directly overhead at midday and midnight, respectively. The sun and moon always remain in the same position relative to the stars, and to each other. Solar eclipses are therefore impossible, and technically the moon would constantly be eclipsed by the world, even though it exhibits phases depending on the number of nights elapsed.

In Bedrock Edition, the daylight cycle never pauses unless the game is shut down. If the game is paused, the cycle continues. In Java Edition, the daylight cycle pauses when a single-player game is paused unless a GUI window (such as the inventory) is opened. In multiplayer, time proceeds normally as long as the server is running.

The daylight cycle continues while the player is in the Nether or The End, although the world itself does not change until the Overworld is loaded again. A village created in another dimension observes a normal village schedule.

## Conversions

In Minecraft, time is exactly 72 times faster than normal time. This can be easily calculated as the proportion 1440⁄20 = 72, since there are 1440 minutes (86400 seconds) in a real day (3600sec × 24hr) and 20 minutes (1200 seconds) in a full Minecraft day, assuming the tick speed is maintained at 20 ticks/second. A collection of time unit conversions is listed below:
A chart showing the approximations of Minecraft time to real time.
### Minecraft time to real time
| Minecraft time       | Minecraft ticks | Real time           |
|----------------------|-----------------|---------------------|
| 1 second             | 0.27            | 0.0138seconds       |
| 1 minute             | 16.6            | 0.83seconds         |
| 1 hour               | 1,000           | 50 seconds          |
| 1 day                | 24,000          | 20 minutes          |
| 1 week (7 days)      | 168,000         | 2.3hours (2h 20min) |
| 1lunar cycle(8 days) | 192,000         | 2.6hours (2h 40min) |

### Real time to Minecraft time
The approximation of real time to Minecraft time:

| Real time            | Minecraft time                                   |
|----------------------|--------------------------------------------------|
| 1 tick               | 3.6 seconds                                      |
| 1 second             | 1 minute and 12 seconds (72 seconds)             |
| 10 seconds           | 12 minutes (720 seconds)                         |
| 50 seconds           | 1 hour (60 minutes, 3600 seconds)                |
| 1 minute             | 1 hour and 12 minutes (72 minutes, 4320 seconds) |
| 20 minutes           | 1 day                                            |
| 1 hour               | 3 days                                           |
| 1 day                | 72 days                                          |
| 1 month              | 2,160 days                                       |
| 1 year (365.24 Days) | 26,297 days (To the nearest day)                 |



## 24-hour Minecraft day
| Image | Minecrafttime of day | Minecraftticks                | Real time(minutes) | Event                                                                                                                                                             |
|-------|----------------------|-------------------------------|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|       | 06:00:00.0           | 0<br/>(24000)                 | 0:00<br/>(20:00)   | Beginning of the Minecraft day.<br/>Players and villagers awaken and rise from their beds.                                                                        |
|       | 06:10:01.2           | 167                           | 0:08.35            | The moon disappears on the horizon.                                                                                                                               |
|       | 07:00:00.0           | 1000                          | 0:50               | Time when using the`/time set day`command.                                                                                                                        |
|       | 08:00:00.0           | 2000                          | 1:40               | Villagers begin their workday.                                                                                                                                    |
|       | 11:43:22.8           | 5723                          | 4:46.15            | The clock starts showing exactly midday.                                                                                                                          |
|       | 12:00:00.0           | 6000                          | 5:00               | Noon; the sun is at its peak.                                                                                                                                     |
|       |                      |                               |                    | Time when using`/time set noon`.                                                                                                                                  |
|       | 15:00:00.0           | 9000                          | 7:30               | Villagers end their workday and begin socializing.                                                                                                                |
|       | 17:50:02.4           | 11834                         | 9:41.70            | The moon appears on the horizon.                                                                                                                                  |
|       | 18:00:00.0           | 12000                         | 10:00              | Beginning of the Minecraft sunset.Time when using the /time set sunset‌[Bedrock Edition  only] command. Villagers go to their beds and sleep.                     |
|       | 18:00:36.0           | 12010                         | 10:00.5            | In rainy weather, beds can be used at this point.In rainy weather, the internal sky-light level begins to decrease.                                               |
|       | 18:02:24.0           | 12040                         | 10:02              | In sunny weather, theinternal sky-light levelbegins to decrease.                                                                                                  |
|       | 18:32:31.2           | 12542                         | 10:27.1            | In clear weather, beds can be used at this point.<br/>In clear weather, bees enter the nest/hive for the night.<br/>In clear weather, undead mobs no longer burn. |
|       | 18:36:36.0           | 12610                         | 10:30.5            | The clock shows exactly dusk (day to night).                                                                                                                      |
|       | 18:47:09.6           | 12786                         | 10:39.3            | The solar zenith angle is 0. Horizon stops getting darker.                                                                                                        |
|       | 18:58:08.4           | 12969                         | 10:48.45           | First tick when monsters spawn outdoors in rainy weather.[note 1]                                                                                                 |
|       | 19:00:00.0           | 13000                         | 10:50              | Beginning of the Minecraft night.Time when using the /time set night command.                                                                                     |
|       | 19:11:16.8           | 13188                         | 10:59.4            | First tick when monsters spawn outdoors in clear weather.[note 1]                                                                                                 |
|       | 19:40:12.0           | 13670                         | 11:23.5            | Theinternal sky-lightlevel reaches 4, the minimum at night.                                                                                                       |
|       | 19:42:07.2           | 13702                         | 11:25.10           | The sun disappears on the horizon.                                                                                                                                |
|       | 23:50:34.8           | 17843                         | 14:52.7            | The clock starts showing exactly midnight.                                                                                                                        |
|       | 00:00:00.0           | 18000                         | 15:00              | Midnight; the moon is at its peak.                                                                                                                                |
|       |                      |                               |                    | Time when using the`/time set midnight`command.                                                                                                                   |
|       | 04:18:00.0           | 22300                         | 18:35              | The sun appears on the horizon.                                                                                                                                   |
|       | 04:19:51.8           | 22331                         | 18:36.55           | Theinternal sky-light levelbegins to increase.                                                                                                                    |
|       | 04:48:43.2           | 22812‌[Java Edition  only]    | 19:00.6            | Last tick when monsters spawn outdoors in clear weather.[note 1]                                                                                                  |
|       | 04:48:46.8           | 22813‌[Bedrock Edition  only] | 19:00.65           |                                                                                                                                                                   |
|       | 05:00:00.0           | 23000                         | 19:10              | Beginning of the Minecraft sunrise.Time when using the /time set sunrise‌[Bedrock Edition  only] command.                                                         |
|       | 05:01:51.6           | 23031                         | 19:11.55           | Last tick when monsters spawn outdoors in rainy weather.[note 1]                                                                                                  |
|       | 05:02:27.6           | 23041                         | 19:12.1            | The clock starts showing exactly dawn.                                                                                                                            |
|       | 05:12:57.6           | 23216                         | 19:20.8            | The solar zenith angle is 0.                                                                                                                                      |
|       | 05:27:36.0           | 23460                         | 19:33              | In clear weather, beds can no longer be used.<br/>In clear weather, bees leave the nest/hive.<br/>In clear weather, undead mobs begin to burn.                    |
|       | 05:57:39.6           | 23961                         | 19:58.1            | In sunny weather, theinternal sky-lightlevel reaches 15, the maximum. Horizon stops getting brighter.                                                             |
|       | 05:59:31.2           | 23992                         | 19:59.6            | In rainy weather, beds can no longer be used.In rainy weather, the internal sky-light level reaches 12, the maximum.                                              |



