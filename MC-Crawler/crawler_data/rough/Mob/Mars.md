# Java Edition 22w13oneBlockAtATime
22w13oneBlockAtATime (known as 22w13oneblockatatime in the launcher) is an April Fools' joke snapshot, supposedly the first and only snapshot for the "One Block at a Time Update", released on April 1, 2022,[1] which overhauled the player's inventory as well as the game logic for blocks, items and entities, and redesigned relevant gameplay aspects such as controlling, breaking and crafting. This version is a fork of a commit between 1.18.2 and 22w11a, as it contains several blocks (not complete) from the deep dark biome.

## Contents
- 1 Additions
	- 1.1 Blocks
	- 1.2 Gameplay
	- 1.3 General
- 2 Changes
	- 2.1 Blocks
	- 2.2 Items
	- 2.3 Mobs
	- 2.4 Entities
	- 2.5 Gameplay
	- 2.6 World generation
	- 2.7 General
- 3 Issues
- 4 Trivia
- 5 Gallery
	- 5.1 Screenshots
	- 5.2 Official images
- 6 Video
- 7 See also
- 8 References

## Additions
### Blocks
** How did we get here? **
- All items are converted into item blocks.
- Has IDminecraft:generic_item_block
- Has anitemblock state that specifies the internal ID of the item to display with (0-1104).
	- item=0uses the model of whitecarpets.
- Waterloggable.
	- Indebug mode, all items and their waterlogged versions can be found.

### Gameplay
** Advancements **
- Added a new advancement:
	- Ride the End
		- Description reads "Extra Good luck"
		- Obtained for punching the ender dragon, causing the player to ride it; this is only possible once all end crystals are destroyed or with a dragon spawned by/summon.

** The End **
- Riding the ender dragon into the void teleports the player to the build limit in the Overworld.

** The Nether **
- Riding the ender dragon into the void teleports the player to the build limit in the Overworld.

### General
** Particles **
- Addedfootstepparticle, generated when player walks holding anything.

** Splashes **
- All regular splashes have been removed.
- Possible splashes are now "One!", "Block!", "At!", "A!", "Time!", or any possible arrangement of the words "One block at a time!".
- The special "<PLAYERNAME> IS YOU" splash has been changed to "<PLAYERNAME> IS ONE AT A TIME".

** Sounds **
- 2 new sounds were added
	- nothingtoseeheremovealong:awesome_introwhich is the intro sound.
		- Has 2 variations, one higher pitch and one normal pitch.
		- These sounds are located in theassets/nothingtoseeheremovealong/ananasfolder and are calledpapaya.ogg() andpapapaya.ogg().
	- nothingtoseeheremovealong:ooofwhich is the old hurt sound.
	- These sounds are bundled in the.jarfile.

## Changes
### Blocks
** General **
- Blocks will not drop in dropped item forms.
- When exploded, they are launched instead of dropped.

** Bedrock **
- Now breakable and obtainable in Survival.
	- Takes ~10.5 minutes to break with empty hands and aHasteII effect applied.[needs in-game testing]

** Chest **
- When loot chests generated in structures are broken, they emit explosion sound effects and particles, and explode out the loot items in falling block forms.

** Dispenser **
- When powered with aredstonesignal, the block it's facing will be dispensed with velocity in the direction of the dispenser as a falling block.
	- If the block is a fluid source, it turns into the form of buckets, and becomes fluid again when landing.

** Dripstone **
- Playstridentsound when thrown.

** Dropper **
- When powered with aredstonesignal, the block it's facing will be dispensed as a falling block.
	- Unlike dispensers, the converted falling block will drop straight downwards.
	- If the block is a fluid source, it turns into the form of buckets, and becomes fluid again when landing.

** End Portal Frame **
- Now breakable and obtainable in survival.
	- Takes ~37 seconds to break with empty hands and withoutHaste.[needs in-game testing]
- Can be found in chests insidenether fortresses.
- They can either be orientated vertically or horizontally.
	- When placed in a stronghold, it points up, like in normal versions, which allows to build end portals.
	- When placed outside a stronghold, it points to a stronghold.
	- When placed in a dimension without a stronghold, it points to a random direction.
- Has aneye of enderin place at all times.

** Fire **
- May convert nearbysmeltableitems to their smelted item, such as coal ore to coal.Soul firedoes not do this.
- Can be picked up, though it is invisible when held by the player.

** Glass and glass pane (including tinted and stained) **
- When thrown, they may break upon landing.
	- This applies to all blocks with#minecraft:fragiletag.

** Grass and fern **
- When thrown on a block that is not a grass block, they lay horizontally and change their variant to a gray one.

** Gravel **
- When thrown, it ignites grass, leaves and vines adjacent to where it lands.

** Ice **
- When thrown into lava, fire or onto magma blocks, they directly become water.

** Iron ore **
- Becomes ablock of ironwhen thrown into soul fire.

** Lava **
- When a smeltable item or block is thrown onto a lava block, it is converted into its smelted counterpart which overrides the lava it was thrown onto.

** Mushroom block **
- Becomes ashroomlightwhen thrown into fire.

** Pumpkin **
- Becomes a carved pumpkin when thrown near a cactus.

** Seagrass **
- When thrown on a block that is not a leaf block, they will be placed as normal and will generate awaterblock on them.

** Vines **
- When thrown, they will lay horizontally and change their variant to a gray one.

### Items
** General **
- All items can be placed on the ground as blocks.
	- When trying to place an item anywhere that's not a block, it is thrown instead.
		- Throwing an item directly on the player's head will equip it in the helmet slot.
		- Throwing any smeltable item into lava or placing it near fire or lava will smelt it.
		- Thrown items are implemented asfalling_blockentities.
		- Thrown items (or indeed anyfalling_block) can be caught in midair by hitting it.
	- Items that do not have a block form are converted togeneric_item_blockwith the appropriate data.
- Items can be crafted by placing a recipe above at least one crafting table, throwing the last item (recipe patterns top facing away from the player, but defaulting to north when not thrown by a player)
	- Alternatively, the recipe can be placed and a crafting table can then be thrown to land on the recipe.
- Tools may be used but break with one use.
	- Tools break even in situations when they would not lose any durability.
- Certain items (e.g. top of the door, tall grass, etc) have "invalid" block data and will disappear when they land (as an item). It is still possible to place them, however.
- Food items cannot be eaten, even in Creative mode, since using them on a block places them, and using them otherwise throws them.
	- However, there exist special cases in the code for bamboo, carrots, and potatoes (see below).

** Bamboo **
- When a player is named "Ulraf", bamboo can now be eaten at any time.
- When a player is not named "Ulraf", bamboo can now be eaten while in the offhand slot of the player, when the player is looking at the side of a bamboo block.
- When bamboo is eaten, the player gainsAbsorptionIV for 2 minutes,RegenerationII for 20 seconds,Fire Resistancefor 5 minutes andResistancefor 5 minutes.

** Carrot **
- Can now only be eaten in Creative mode (not Survival since the hunger bar is always full), from the player's offhand slot, if the player is looking at carrots placed on farmland.

** Ender pearl **
- Can no longer teleport the player, as they cannot be thrown normally.

** Eye of ender **
- Can no longer lead the player to the neareststronghold, as they cannot be thrown normally.

** Potato **
- Can now only be eaten in Creative mode (not Survival since the hunger bar is always full), from the player's offhand slot, if the player is looking at potatoes placed on farmland.

** Potion **
- Any potion held uses the bottle texture.
- Any thrown potion uses uncraftable potion texture.
- Any potion placed on ground uses slow-falling potion texture.

** Powder snow bucket **
- Thrown as a powder snow block when thrown.

** Water bucket and lava bucket **
- Make water and lava when thrown, with the bucket disappearing.

### Mobs
** General **
- When trying to damage a mob, the player will pick it up instead.
	- When falling, the player holds onto the mob that they picked up.
	- Some mobs like the ender dragon behave like rideable entities.
	- Some mobs like the wither cannot be ridden or picked up.
- To damage mobs, the player has to:
	- Throw the mob
	- Throw any block, item or entity at the mob
		- Different blocks deal different amounts of damage based on their blast resistance and speed; the formula is speed*10*blast resistance.
		- Different mobs also deal different amounts of damage based on their height and speed; the formula is speed*5*height.
			- However, the player also throws mobs slower the taller it is.
	- Release them in a stacked group of two or more.
	- Some mobs like the ender dragon cannot take damage from any block, item or entity.
- Mobs that can hold items, like zombies, skeletons, etc. can steal the player's held item when damaging them, playingnothingtoseeheremovealong:ooof.
- Mobs can also be made to wear carved pumpkins or barrels when the blocks are thrown at them.

** Bee **
- When held by the player, they will cause the player to keep the momentum from when they picked up the bee, albeit a lot slower.
	- If the player was completely still before picking up the bee, the player will not be able to move up or down whatsoever.
	- The player will be unable to jump while doing so.

** Cave spider **
- When held by the player, the player will be able to climb blocks vertically.

** Chicken **
- When held by the player, they will cause the player to float down slowly after jumping, similar to theSlow Fallingeffect.
	- Whenjumpingrepeatedly, the player will be able to float upwards.

** Ender dragon **
- Now rideable byattackingher.
	- Only 30 health points are displayed in the HUD.
	- When riding, the player can control her by looking around.
		- When flying down to the void of the End or the Nether (at Y=-32), it descends to the build limit of the Overworld.
		- Flying down to the void of a custom dimension will also descend the player to the build limit of the Overworld.
	- When there is anend crystalnearby, the player will be forced off.

** Enderman **
- Every single enderman is now holding a random block. The random block can be any block in the game, including unobtainable blocks such ascommand blocks.
	- Each can have random properties, including being waterlogged.
	- Endermen can place waterlogged blocks in the Nether without the water disappearing.
- All of them are stuck in a holding pose if not holding any blocks.
- If an enderman holding a block attacks a player, the soundnothingtoseeheremovealong:ooofwill play, and the block is given to the player.
- When held by the player, the player and the enderman will teleport simultaneously.

** Illusioner **
- When held by the player, they will shoot arrows in the direction of the player.

** Iron golem **
- Appearance changes when named "billyballong", causing it to hold its hands in the air.
- Gives flowers to players named "maria", "alva", "neo", "hidetaka" or "miyazaki" (case-insensitive).

** Magma cube **
- When held by the player, the player will be immune to fire and lava damage.

** Pig **
- When held by the player, the pig is rendered upside-down and the holder will be magnetized to any block higher than two blocks above their head.
	- This will cause them to bounce up and down on the bottom side of the block.

** Piglin **
- When held by the player, they will shoot arrows in the direction of the player. If held by the player while the arrow is fired, their crossbows will break after firing. When hostile, they will damage the player even while held.

** Pillager **
- When held by the player, they will shoot arrows in the direction of the player. If held by the player while the arrow is fired, their crossbows will break after firing. Without their crossbows they stare at the player harmlessly and try to stay in crossbow range, despite not having a crossbow.

** Player **
- Leaves a trail of footprints while holding anything.
- When a player throws a block at another entity, the entity will be damaged.
- When a player throws a block at another player's head, the block will go into the helmet slot of the receiving player. Taking damage has a chance to remove it.[2]
	- When the block on the player's head issnow, asnow block,ice,packed ice, orblue ice, the player will begin freezing.
	- When the block on the player's head is amagma block, it will set the player on fire.
	- When the block on the player's head is abarrel, their vision becomes largely obstructed, leaving only a narrow window; and their model appears as if they are hiding under it and moving only with their legs visible.
		- Sneaking while under a barrel will disguise the player as a barrel block.
- The hunger bar does not deplete, meaning the player is always able to sprint and regenerate health.
- InSpectatormode, the two hands of the player are visible.

** Sheep **
- Are now sheared when they take damage or are thrown, dropping wool.
- When with wool, when thrown a wool block, the wool color of the sheep will be replaced, dropping the wool of the previous color.
- When without wool, when thrown a wool block, the wool will be put on the sheep.

** Skeleton **
- Skeletons can spawn with two spyglasses with unknown chance.[more information needed]They can also wear spyglasses when thrown, up to two.
- When held by the player, they will shoot arrows in the direction of the player.
- Based onXilefian's idea.[3]

** Spider **
- When held by the player, the player will be able to climb blocks vertically.

** Stray **
- When held by the player, they will shoot arrows in the direction of the player.

** Villager **
- Now have different trades.
	- Seems to have multiple trades, based on their profession and level. They gain more trades by leveling up by trading with them. The trade always includes emerald_ore blocks as for buying or selling.
		- Can now also trade mobs.
	- The player can trade with them by right clicking on the villager withemerald ore.
	- Their normal trading GUI is now inaccessible.
	- These changes also apply towandering traders.

** Witch **
- When held, if targeting the player, they will shoot potions in the direction of the player.

** Wolf **
- Naming a tamed wolf 'Mars' will give it a unique texture.

### Entities
** Fireball **
- Player can hold aghast's fireball, but when released, it will return to its original vector.

** Eye of ender **
- When summoned via commands, it will move to the origin point (X=0, Z=0) with its vector depending on its distance from the center of the world.

### Gameplay
** Explosion **
- Blocks that would be destroyed by an explosion are launched instead of destroyed.
	- Blocks launched represents the form of falling blocks before they land, and sometimes stuck in blocks without turning to normal blocks, causing possiblez-fighting.
	- The explosion will apply randomstonecutterrecipes to some blocks around it.

** Inventory **
- The inventory interface, hotbar, hunger bar and armor bar have been removed.
- The health bar is now centered at the bottom of the screen.
- The oxygen bar now appears at the bottom right corner of the screen.

** GUI **
- Every single inventory for any kind of container block has been removed.
	- With the exception of the horse inventory.
- Players now see both hands on the screen instead of just one.
	- Probably inspired by scrapped two-handed hold animation for skulls.[4]

### World generation
** Stronghold **
- End portal frames without eyes of ender inside of them do not generate.
	- To open the end portal, the player needs to place down end portal frames.

### General
** Debug screen **
- Mood in the debug screen has been changed to "Number of ghosts in world".

** Loading screen **
- The loading screen has been changed.
	- Practically similar to20w14∞'s loading screen, but with different textures.
	- Plays a sound saying "Mojang Studios", similar to 20w14∞ and3D Shareware v1.34.
	- The silhouette inside the logo is a "Mojang" that resembles a Crewmate from the gameAmong Us.

