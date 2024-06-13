## Additional behavior

  

This section needs expansion. 
You can help by expanding it.


This section explains more complex behaviors of certain gamerules.

- disableRaids
	- Whentrue, theBad Omeneffect is not removed from a player when entering a village.
	- Stops a raid if set totruewhile a raid is in progress, but the existing raid mobs do not despawn.
- doEntityDrops
	- Whenfalse, removing items from item frames does not drop that item.
- doMobLoot
	- Does not affect drops not related to a mob's death, such aschickenlayingeggs, orsheepdroppingwoolwhensheared.
	- Does not affect the dropping ofwither roseswhen mobs are killed by thewither.[1][2]
- doMobSpawning
	- Affects only natural mob spawning. Mobs from structures,‌[Java Edition  only]monster spawners, and events still spawn when set tofalse.
- doTileDrops
	- Whenfalse, containers still drop their contents, but not themselves.
		- Shulker boxesdo not drop anything, causing the items in them to be lost.
	- Whenfalse, destroying an armor stand does not drop it nor any armor it had equipped.
	- Whenfalse, item frames still drop themselves and their items.
	- Whenfalse,infested blocksdo not spawnsilverfishwhen broken.
- drowningDamage
	- Whenfalse, the player still loses air, but does not take damage when the air is depleted.
- fireDamage
	- Whenfalse, the player may still be set on fire, but does not take damage when on fire.
- forgiveDeadPlayers
	- Every neutral mob that can be aggravated remain aggravated even after the offending player dies, with the exception of piglins when a player does not wear golden armor and iron golems when it is created from a village where the player isunpopular.
- keepInventory
	- Whentrue, players also retain their experience upon death.
	- Whentrue, health and hunger are still reset as normal upon death.
	- Whentrue, alleffectsare still removed upon death.[3]
	- Whentrue, items enchanted withCurse of Vanishingdonotdisappear upon death.[4]
- mobGriefing
	- Whenfalse, prevents all mobs from modifying the environment in any way. This includes trampling crops and turtle eggs, picking up items, destroying blocks, or moving blocks. Specifically, it prevents:
		- Allaysfrom picking up dropped items.
		- Blazesfrom creating fire or lightingcampfires.
		- Creepersfrom destroying blocks when they explode, although they still damage entities.
		- End crystalsfrom destroying blocks when they explode, although they still damage entities.
		- TheEnder dragonfrom destroying blocks, causing it to just fly through them instead.
		- Endermenfrom picking up or placing blocks.
		- Evokerfrom turning bluesheepred.‌[Java Edition  only]
		- Foxesfrom pickingsweet berriesfrom asweet berry bushand picking up dropped items.
		- Ghastfireballs from exploding blocks and creating fire. They still damage entities.
		- Piglinsfrom attempting tobarterby picking up dropped items; using the item on them still works.
		- Rabbitsfrom eatingcarrot crops.
		- Ravagersfrom destroying crops and leaves.
		- Sheepfrom turninggrass blocksintodirt, but does not prevent the regrowth of wool. They still act as if they are eating the grass and regrow their wool upon doing so, but the grass remains and the grass breaking sound does not play.
		- Silverfishfrom hiding ininfested blocksand destroying those blocks when hatching.
		- Snow golemsfrom creating snow trails.
		- Villagersfrom farming and picking up items. However, they can still open doors and throw items.
		- TheWitherand its heads from destroying blocks with their explosions. Entities are still damaged, and awither rosedrops as an item.
		- Zombiesfrom breaking doors, picking up items, and attackingturtle eggs.
	- Has no effect onbreezeor theplayer.
- playersSleepingPercentage
	- When set to0, at least one player is still required to sleep to skip the night.
	- When set to a number greater than100, night is not skipped no matter how many players are sleeping.
- randomTickSpeed
	- Does not affect:
		- Cauldronsfilling withwaterorpowder snowwhile raining or snowing.[5]
			- Still affects filling of water andlavain cauldrons belowpointed dripstone.
		- Death ofcoral blocks,coral, andcoral fan.
		- Hatching offrogspawn[6]andsniffer eggs[7].
- snowAccumulationHeight
	- When set to0, snow layers do not form at all.
	- When set to8or higher, snow forms up to the level of a full block, but no greater than that.
- universalAnger
	- Every neutral mob that can be aggravated targets all nearby players whenever they are aggravated.
	- Bees attack all nearby players when their beehive is broken, regardless of the setting of this gamerule.[8]
		- Bees becoming angry when attacked works as expected.


