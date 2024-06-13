# Education Edition 1.8.0
1.8.0 is a beta version for Education Edition 1.9 released on March 7, 2019. This version added Village and Pillage features from Bedrock Edition 1.8.0 and 1.9.0.[1]

## Contents
- 1 Additions
	- 1.1 Blocks
	- 1.2 Items
	- 1.3 Mobs
	- 1.4 World generation
	- 1.5 Command format
	- 1.6 Gameplay
	- 1.7 General
- 2 Changes
	- 2.1 Blocks
	- 2.2 Items
	- 2.3 Mobs
	- 2.4 World generation
	- 2.5 Gameplay
	- 2.6 Command format
	- 2.7 General
- 3 References

## Additions
### Blocks
** Bamboo **
- Can be found whilefishingin jungles and will appear in somechests
- Spawning naturally in the world will come in a future update.

** Scaffolding **
- A new climbableblockthat can becraftedusing bamboo.

** Barrel, Bell, Blast Furnace, Cartography Table and Smoker **
- Currently have no functionality.
- Only available through Experimental Gameplay.

** Fletching Table **
- Can be crafted in crafting table usingcrafting tableandarrow.
- Currently has no functionality.
- Only available through Experimental Gameplay.

** Flowers **
- Addedcornflower.
	- Givesblue dye.
	- Appears inplainsbiomes.
- Addedlily of the valley.
	- Giveswhite dye.
	- Appears inforestbiomes.

** Grindstone **
- Currently has no functionality.
- Only available through Experimental Gameplay.

** Lantern **
- Acts as a new light source.
- Can currently only be obtained from the creative inventory with Experimental Gameplay enabled.

** Signs **
- Now come in all different wood types: spruce, birch, acacia, jungle and dark oak.

** Smithing Table **
- Can be crafted in crafting table usingcrafting tableandcobblestone.
- Currently has no functionality.
- Only available through Experimental Gameplay.

** Smooth blocks **
- Addedsmooth stone, smooth sandstone, smooth red sandstone and smooth quartz block.

** Slabs **
- Added stone, andesite, polished andesite, diorite, polished diorite, granite, polished granite, mossy stone brick, mossy cobblestone, smooth sandstone, smooth red sandstone, smooth quartz, red nether brick, and end stone brick slabs.
- Added cut sandstone and cut red sandstone slabs.

** Stairs **
- Added stone, andesite, polished andesite, diorite, polished diorite, granite, polished granite, mossy stone brick, mossy cobblestone, smooth sandstone, smooth red sandstone, smooth quartz, red nether brick, and end stone brick stairs.

** Walls **
- Added brick, andesite, diorite, granite, prismarine, stone brick, mossy stone brick, sandstone, red sandstone, nether brick, red nether brick, and end stone brick walls.

### Items
** Crossbow **
- New weapon.
- Crossbows can be enchanted with three new enchantments
- Stronger than bow, but takes longer to recharge.
- Can be obtained when "Experimental Gameplay" is turned on in settings.

** New dye items **
- Addedwhite dye,blue dye,brown dyeandblack dye.
- Items previously used as dyes (bone meal,lapis lazuli,cocoa beansandink sacs) can still be used.

** Spawn eggs **
- Panda
- Cat
- Pillager

### Mobs
** Pandas **
- Spawn injungles.
- Eatbambooandcakeitems.
- Have different personalities – lazy, playful, aggressive or worried.
- Have a rare brown variant.

** Stray cats **
- Spawn invillages.
- Can be tamed usingfish.
- Bring gifts to the player.
- Have dyeable collars, like wolves.

** NPCs **
- Can be only summoned using/summoncommand.

** Pillagers **
- They are hostile mobs, considered a subset ofillagers.
- Have 24× 12health.
- They wieldcrossbows.
- Droparrowsand theircrossbowswhen killed (affected byLooting).
- They will raid, or take over,villages, killingvillagers.
- They can't equip armor of any type.
- Available only through Experimental Gameplay.



** Passive mobs **
- Now randomly enterlove mode.

### World generation
** Bamboo forests **
- Newbiomevariant ofjungles.
- It contains bamboo shoots,podzol, andpandas.
- Only available through Experimental Gameplay.

### Command format
** /particle command **
- Only the following particles are available (prefixminecraft:is necessary):[2]
	- minecraft:mobflame_emitter
	- minecraft:test_beziercurve
	- minecraft:test_bounce
	- minecraft:test_catmullromcurve
	- minecraft:test_colorcurve
	- minecraft:test_combocurve
	- minecraft:test_highrestitution
	- minecraft:test_linearcurve
	- minecraft:test_mule
	- minecraft:test_smoke_puff
	- minecraft:test_sphere
	- minecraft:test_spiral
	- minecraft:test_watertest
	- minecraft:test_flipbook
	- minecraft:test_vertexrandom
	- minecraft:balloon_gas_particle
	- minecraft:mobspell_emitter
	- minecraft:basic_crit_particle
	- minecraft:portal_directional
	- minecraft:bubble_column_down_particle
	- minecraft:portal_east_west
	- minecraft:portal_north_south
	- minecraft:bubble_column_up_particle
	- minecraft:crit_emitter
	- minecraft:splash_spell_emitter
	- minecraft:end_chest
	- minecraft:totem_particle
	- minecraft:evocation_fang_particle
	- minecraft:water_splash_particle
	- minecraft:evoker_spell
	- minecraft:water_wake_particle
	- minecraft:magnesium_salts_emitter
	- minecraft:wither_boss_invulnerable
	- minecraft:mob_portal

** /reload **
- Reloads all function files from all behavior packs.

- Addedminecraft:prefix for/summonto separate vanilla entities and add-on entities.
- Addedfunction.
- Added gamerulerandomtickspeed.

** showDeathMessages **
- Allows players to select whether a message appears in chat when a player or tamed mob dies.
- Has new "Immediate Respawn" option.

** /tellraw **
- Enables the use of raw text formatting to be able to send translatable text output to chat using JSON.

** Gamerules **
- The number of commands run through functions can be limited with a new gamerule (defaults to 10,000) to limit performance issues.

** Functions **
- Can now be run every tick creating an update loop.

** Tags **
- Custom tags can be applied to entities and players to create more flexible selector groupings.
- Addedhas_tagfilter in components to allow checks to see if an entity has a specified tag.
- Autocomplete can be used for tags.
- /killcommandnow kills creative mode players.

