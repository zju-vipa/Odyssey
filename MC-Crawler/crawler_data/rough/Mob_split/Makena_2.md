## Username
Players in-game are referred to by a username. These are used to target the player with commands and differentiate other players.  

In Java Edition, usernames must be 3–16 characters, although there are exceptions for players with under 3 characters, who bought the game early in its development. Players can change their username no more than once every 30 days. When the player changes their username, the previous username is available for other users to claim after 37 days. Because players can change usernames every 30 days, a player can manage two usernames without anyone being able to take either of them. If the player has a username under 3 characters and changes it, the old sub-3-character username is permanently unable to be obtained again.[3] This also applies for symbol names.[4] The username can be changed on the preferences page of minecraft.net.

In Bedrock Edition, usernames chosen in-game must be 3–32 characters. Users can choose a username and change it unlimited times from Settings -> General -> Profile. Alternatively, users that sign in with a Microsoft account have the username set to match their Gamertag. Gamertags can be modified on the Choose your new gamertag page of xbox.com for a fee of US$9.99 except if changing from the gamertag generated upon account creation.[5]

Player names appear above their head as nameplates, typically in white letters within a dark transparent rectangle. Player nameplates can also be seen through solid blocks and other obstructions, although a player can sneak to dim the nameplate's visibility when in sight, or hide it completely when out of sight or in Bedrock Edition.

## Customization
The player height options in Bedrock Edition.
Main articles: Skin and Character Creator
In Java Edition, players can change skins on the preferences page of minecraft.net or the Minecraft Launcher by uploading a PNG image file, which then replaces the default skin. Players also have the option to have three or four pixel-wide arms on the character model.

In Bedrock Edition, players can change their character's appearance from the Main menu or Pause menu -> Character where 5 character slots are shown. Edit Character opens the Character Creator where a skin, which synchronizes between signed-in devices, can be created by selecting pre-made components, altering their height, and selecting a slim or wide arm width. Players alternatively have the option to select from Classic skins with Skin packs obtained from the Marketplace or, for the Windows 10, iOS/iPadOS, and Android versions of the game, import a PNG image file. Classic Skins do not synchronize between signed-in devices.
Players can also choose 4 Emotes per character slot and select or remove a cape.

## Data values
### ID
Java Edition:

| Name   | Identifier | Translation key           |
|--------|------------|---------------------------|
| Player | `player`   | `entity.minecraft.player` |

Bedrock Edition:

| Name   | Identifier | Numeric ID | Translation key      |
|--------|------------|------------|----------------------|
| Player | `player`   | `63`       | `entity.player.name` |

### Entity data
Main article: player.dat format
See also: Chunk format

Players have entity data associated with them that contain various properties.

- The root tag. Inlevel.datfiles, this tag is calledPlayer.
	- 
	- Tags common to all entities
	- except forthe tags:CustomNameandCustomNameVisible.
	- 
	- Tags common to all mobs
	- except forthe tags:HandItems,ArmorItems,HandDropChances,ArmorDropChances,CanPickUpLoot,PersistenceRequired,Leash.
	- abilities: The abilities this player has.
		- flying: 1 or 0 (true/false) -trueif the player is currently flying.
		- flySpeed: The flying speed, set to0.05.
		- instabuild: 1 or 0 (true/false) - Iftrue, the player can place blocks without depleting them. This istruefor Creative mode, andfalsefor other game modes.
		- invulnerable: 1 or 0 (true/false) - Behavior is not the same as the invulnerable tag on other entities. Iftrue, the player is immune to all damage and harmful effects except forvoiddamage and/kill. Also, all mobs, whether hostile or not, are passive to the player.truewhen in Creative or Spectator mode, andfalsewhen in Survival or Adventure mode.
		- mayBuild: 1 or 0 (true/false) - Iftrue, the player can place blocks.truewhen in Creative or Survival mode, andfalsewhen in Spectator or Adventure mode.
		- mayfly: 1 or 0 (true/false) - Iftrue, the player can fly and doesn't take fall damage.truewhen in Creative and Spectator modes, andfalsewhen in Survival and Adventure modes.
		- walkSpeed: The walking speed, set to0.1.
	- DataVersion: Version of the player NBT structure. Is increased with every new snapshot and release. SeeData version.
	- Dimension: TheIDof the dimension the player is in. Used to store the players last known location along withPos.
	- EnderItems: Each compound tag in this list is an item in the player's 27-slot ender chest inventory. When empty, list type may haveunexpected value.
		- An item in the inventory.
			- Includes theSlottag - slots are numbered0–26, inclusive.
			- SeeItem_format § NBT_structure.
	- enteredNetherPosition: May not exist. A compound of 3 doubles, describing theOverworldposition from which the player entered theNether. Used by thenether_traveladvancementtrigger. Set every time the player passes througha portalfrom the Overworld to the Nether. When entering a dimension other than the nether(not by respawning)this tag is removed. Entering the Nether without using a portal does not update this tag.
		- x: The X coordinate in the Overworld.
		- y: The Y coordinate in the Overworld.
		- z: The Z coordinate in the Overworld.
	- foodExhaustionLevel: SeeHunger § Mechanics.
	- foodLevel: The value of the hunger bar. Referred to ashunger. SeeHunger.
	- foodSaturationLevel: Referred to assaturation. SeeHunger § Mechanics.
	- foodTickTimer: SeeHunger.
	- Inventory: Each compound tag in this list is an item in the player's inventory. (Note: when empty, list type may haveunexpected value.)
		- An item in the inventory.
			- SeeItem_format § NBT_structure.
	- LastDeathLocation: May not exist. Location of the player's last death.
		- dimension: Dimension of last death.
		- pos: Coordinates of last death.
	- playerGameType: The current game mode of the player.0meansSurvival,1meansCreative,2meansAdventure, and3meansSpectator.
	- previousPlayerGameType: The previous game mode of the player.
	- recipeBook: Contains a JSON object detailing recipes the player has unlocked.
		- 
		- Tags related to the recipe book
	- RootVehicle: May not exist. The root entity that the player is riding.
		- Attach: TheUUIDof the entity the player is riding, stored as four ints.
		- Entity: The NBT data of the root vehicle.
			- SeeEntity format.
	- Score: The score displayed upon death.
	- seenCredits: 1 or 0 (true/false) -trueif the player has entered theexit portalin theEndat least once.
	- SelectedItem: Data of the item currently being held by the player, excluding theSlottag. Only exists when using the /data command, this value is not saved in theplayer.dat format.
		- Seeitem format.
	- SelectedItemSlot: The selected hotbar slot of the player.
	- ShoulderEntityLeft: The entity that is on the player's left shoulder. Always displays as a parrot.
		- SeeEntity format.
	- ShoulderEntityRight: The entity that is on the player's right shoulder. Always displays as a parrot.
		- SeeEntity format.
	- SleepTimer: The number ofgame ticksthe player had been in bed.0when the player is not sleeping. When in bed, increases up to 100 ticks, then stops. Skips the night after enough players in beds have reached 100 (seeBed § Passing the night). When getting out of bed, instantly changes to 100 ticks and then increases for another 9 ticks (up to 109 ticks) before returning to 0 ticks.
	- SpawnDimension: May not exist. The dimension of the player's bed or respawn anchor. These tags are only removed if the player attempts to respawn with no valid bed or respawn anchor to spawn at at these coordinates. They are unaffected by breaking a bed or respawn anchor at these coordinates, and are unaffected by the player's death.
	- SpawnForced: 1 or 0 (true/false) - may not exist.trueif the player should spawn at the below coordinates even if no bed can be found.
	- SpawnX: May not exist. The X coordinate of the player's bed or respawn anchor. Removed when the player attempts to respawn with no valid bed or respawn anchor to spawn at at these coordinates. They are unaffected by breaking a bed or respawn anchor at these coordinates, and are unaffected by the player's death.
	- SpawnY: The Y coordinate of the spawn point.
	- SpawnZ: The Z coordinate of the spawn point.
	- warden_spawn_tracker: Contains data about thewardenspawning process for this player.
		- warning_level: A warning level between0, and3(inclusive). The warden spawns at level 3.
		- cooldown_ticks: The number of game ticks before thewarning_levelcan be increased again. Decreases by 1 every tick. It is set to 200 game ticks (10 seconds) every time the warning level is increased.
		- ticks_since_last_warning: The number of game ticks since the player was warned for warden spawning. Increases by 1 every tick. After 12000 game ticks (10 minutes) it resets to level 3, and thewarning_leveldecreases by 1 level.
	- XpLevel: The level shown on theexperiencebar.
	- XpP: The progress across the experience bar to the next level, stored as a percentage.[verify]
	- XpSeed: The seed used for the next enchantment inenchantment tables.
	- XpTotal: The total amount of experience the player has collected over time; used for the score upon death.

An interactive widget is being loaded. If this does not work for you, please reload the page or check if JavaScript is enabled.

