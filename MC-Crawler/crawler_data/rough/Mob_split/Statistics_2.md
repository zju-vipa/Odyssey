## Storage
Statistics are stored in .minecraft/saves/<world name>/stats/<uuid>.json (<world name>/stats/<uuid>.json on servers). They keep track of these stats. The file structure is JSON based and takes the following format:

- : The root tag.
	- DataVersion: Thedata versionof the game version the file was last saved in.
	- stats: The tag that stores the actual statistics.
		- <statisticType>: A compound that saves all statistics of this type.
			- <statisticName>: The value of the statistic specified in this tag's name.

For example, if a player walked only one block (statistic minecraft.custom:minecraft.walked_one_cm) and broke an oak log (statistic minecraft.mined:minecraft.oak_log), the player's stats would be:

{
  "stats": {
     "minecraft:mined": {
        "minecraft:oak_log": 1
     },
     "minecraft:custom": {
        "minecraft:walked_one_cm": 100
     }
  },
  "DataVersion": 3700
}

Statistics are stored in the stats-change section. All of these fields are empty unless they need updating. For example, until the player jumps, the number of times jumped is not recorded. Distance is stored in centimeters (where one block equals 100 centimeters), and time is stored in ticks (where one tick equals 0.05 seconds).


