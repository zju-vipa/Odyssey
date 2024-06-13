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
How did we get here?
- All items are converted into item blocks.
- Has IDminecraft:generic_item_block
- Has anitemblock state that specifies the internal ID of the item to display with (0-1104).
	- item=0uses the model of whitecarpets.
- Waterloggable.
	- Indebug mode, all items and their waterlogged versions can be found.

### Gameplay
Advancements
- Added a new advancement:
	- Ride the End
		- Description reads "Extra Good luck"
		- Obtained for punching the ender dragon, causing the player to ride it; this is only possible once all end crystals are destroyed or with a dragon spawned by/summon.

The End
- Riding the ender dragon into the void teleports the player to the build limit in the Overworld.

The Nether
- Riding the ender dragon into the void teleports the player to the build limit in the Overworld.

### General
Particles
- Addedfootstepparticle, generated when player walks holding anything.

Splashes
- All regular splashes have been removed.
- Possible splashes are now "One!", "Block!", "At!", "A!", "Time!", or any possible arrangement of the words "One block at a time!".
- The special "<PLAYERNAME> IS YOU" splash has been changed to "<PLAYERNAME> IS ONE AT A TIME".

Sounds
- 2 new sounds were added
	- nothingtoseeheremovealong:awesome_introwhich is the intro sound.
		- Has 2 variations, one higher pitch and one normal pitch.
		- These sounds are located in theassets/nothingtoseeheremovealong/ananasfolder and are calledpapaya.ogg() andpapapaya.ogg().
	- nothingtoseeheremovealong:ooofwhich is the old hurt sound.
	- These sounds are bundled in the.jarfile.

## Changes
### Blocks
General
- Blocks will not drop in dropped item forms.
- When exploded, they are launched instead of dropped.

Bedrock
- Now breakable and obtainable in Survival.
	- Takes ~10.5 minutes to break with empty hands and aHasteII effect applied.[needs in-game testing]

Chest
- When loot chests generated in structures are broken, they emit explosion sound effects and particles, and explode out the loot items in falling block forms.

Dispenser
- When powered with aredstonesignal, the block it's facing will be dispensed with velocity in the direction of the dispenser as a falling block.
	- If the block is a fluid source, it turns into the form of buckets, and becomes fluid again when landing.

Dripstone
- Playstridentsound when thrown.

Dropper
- When powered with aredstonesignal, the block it's facing will be dispensed as a falling block.
	- Unlike dispensers, the converted falling block will drop straight downwards.
	- If the block is a fluid source, it turns into the form of buckets, and becomes fluid again when landing.

End Portal Frame
- Now breakable and obtainable in survival.
	- Takes ~37 seconds to break with empty hands and withoutHaste.[needs in-game testing]
- Can be found in chests insidenether fortresses.
- They can either be orientated vertically or horizontally.
	- When placed in a stronghold, it points up, like in normal versions, which allows to build end portals.
	- When placed outside a stronghold, it points to a stronghold.
	- When placed in a dimension without a stronghold, it points to a random direction.
- Has aneye of enderin place at all times.

Fire
- May convert nearbysmeltableitems to their smelted item, such as coal ore to coal.Soul firedoes not do this.
- Can be picked up, though it is invisible when held by the player.

Glass and glass pane (including tinted and stained)
- When thrown, they may break upon landing.
	- This applies to all blocks with#minecraft:fragiletag.

Grass and fern
- When thrown on a block that is not a grass block, they lay horizontally and change their variant to a gray one.

Gravel
- When thrown, it ignites grass, leaves and vines adjacent to where it lands.

Ice
- When thrown into lava, fire or onto magma blocks, they directly become water.

Iron ore
- Becomes ablock of ironwhen thrown into soul fire.

Lava
- When a smeltable item or block is thrown onto a lava block, it is converted into its smelted counterpart which overrides the lava it was thrown onto.

Mushroom block
- Becomes ashroomlightwhen thrown into fire.

Pumpkin
- Becomes a carved pumpkin when thrown near a cactus.

Seagrass
- When thrown on a block that is not a leaf block, they will be placed as normal and will generate awaterblock on them.

Vines
- When thrown, they will lay horizontally and change their variant to a gray one.

### Items
General
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

Bamboo
- When a player is named "Ulraf", bamboo can now be eaten at any time.
- When a player is not named "Ulraf", bamboo can now be eaten while in the offhand slot of the player, when the player is looking at the side of a bamboo block.
- When bamboo is eaten, the player gainsAbsorptionIV for 2 minutes,RegenerationII for 20 seconds,Fire Resistancefor 5 minutes andResistancefor 5 minutes.

Carrot
- Can now only be eaten in Creative mode (not Survival since the hunger bar is always full), from the player's offhand slot, if the player is looking at carrots placed on farmland.

Ender pearl
- Can no longer teleport the player, as they cannot be thrown normally.

Eye of ender
- Can no longer lead the player to the neareststronghold, as they cannot be thrown normally.

Potato
- Can now only be eaten in Creative mode (not Survival since the hunger bar is always full), from the player's offhand slot, if the player is looking at potatoes placed on farmland.

Potion
- Any potion held uses the bottle texture.
- Any thrown potion uses uncraftable potion texture.
- Any potion placed on ground uses slow-falling potion texture.

Powder snow bucket
- Thrown as a powder snow block when thrown.

Water bucket and lava bucket
- Make water and lava when thrown, with the bucket disappearing.

