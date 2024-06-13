### Items
** Armor **
- No longer turn red when a player gets hurt.

** Golden apples and enchanted apples **
- Now have rarity tooltips.

** Turtle egg **
- Now have a 2D texture in the inventory.

### Mobs and entities
** Illager captains **
- Converting a normal pillager to a captain with the tag command now displays the banner correctly.
- Now drop banners correctly even if the world is reloaded.
- TheBad Omeneffect is now only received when killing an illager captain, and not when dealing non-fatal damage with abowor damage potion.

** Villagers **
- Cartographers now require 11 glass panes for an emerald.
- Farmers now sellsuspicious stew.
- VillagertradingUI no longer opens and closes if the player is standing too far away.
- Clerics can now correctly pathfind to their job sites.
- Fletchers now sell 16arrowsinstead of 5.
- Butchers now sell 5cooked rabbitfor 1emeraldinstead of 5.
- Leatherworkers now sell 1saddlefor 6 emeralds instead of 10.
- Toolsmiths now sell 1diamond hoefor 4 emeralds instead of 9.
- Villagers that are actively trading with players no longer run and hide if theraidbell rings.
- Added a sound to indicate when a villager does not want to trade, such as during a raid.
- Cured villagers now keep the jobs they had before becoming azombie.

** Wandering trader and zombie villagers **
- Added new sounds.

### Gameplay
** Swimming **
- Players no longer start swimming in 1-block deep water.

### General
- Improved performance.
- Changed thechatfont to Segoe UI.

New Mojang Studios logo on the loading screen.
** Menu screen **
- UpdatedMojang Studioslogo.

** Add-ons **
- New items can now be added with add-ons.
- Mob events can now be enabled and disabled in world templates.
- Animations and particles can be added without being linked to entities.
- Inventory, armor, and hand containers can be adapted through scripting.
- Sound effects can now be triggered by animation events.
- Added new executeCommand to the Scripting API.
- Added Scripting events for interaction with items, for example:
	- Item picked up
	- Item dropped
	- Carried item changed
- Added One-shot animation support, allowing the ability to execute a single animation on an entity.
- Particle emitters can now trigger scripting events.
- Updated documentation of actor events, to document client-side usage of actor events in resource packs.
- "Add block" components now use JSON schemas.
- Added a screen to view content log errors.
	- The log screen can be opened usingCtrl+H, or by going to Settings and then Profile.
- Added code to allow static validation scripts to be run locally.
- Custom blocks can now be added through Scripting.
	- This is currently still a "work in progress" feature, and more functionality will be added in future updates.
- Custom blocks can currently only be added through additional JSON scripting.
	- Custom blocks can only be placed with slash commands.
- Added new data-driven particles:
	- Llama Spit
	- Large Explosions
	- Colored Flames
	- Redstone Dust
	- Falling Dust
	- Lava
	- Enchanting Table
	- Conduit
- Added new data-driven animations:
	- Wolves
	- Fang Attack
	- Arrows
	- Shulker Bullets
	- Bows
	- Water
- Updated documentation to include a breaking changes section
- Basic item related events have been exposed to the scripting API. This includes:
	- actor_acquired_item
	- actor_carried_item_changed
	- actor_dropped_item
	- actor_use_item
	- actor_equipped_armor
- Basic inventory events have been exposed to the scripting API. This includes:
	- inventory_container
	- armor_container
	- hand_container
	- hotbar_container
- New block events and two new APIs have been included to query for blocks. This includes:
	- APIs
	- getBlock(Ticking Area, x, y, z)
	- getBlock(Ticking Area, PositionObject)
	- getBlocks(Ticking Area, x min, y min, z min, x max, y max, z max)
	- getBlocks(Ticking Area, Minimum PositionObject, Maximum PositionObject)
	- Events:
		- block_destruction_started
		- block_destruction_stopped
		- piston_moved_block
		- player_destroyed_block
		- player_placed_block
		- executeCommand API
	- Allows the scripting API to get the result of a slash command.
- Event data API:
	- Allows creators to create event data, register and pass it to the event function.
- Updated demo pack.
- Biome generation is now customizable via behavior packs.

** Music **
- Now still plays when the keyboard is being used.

** Menu screen **
- The "Store" button has been renamed to "Marketplace".
- TheVillage & Pillagepanorama should now properly appear instead of1.8.0orUpdate Aquatic.

** Realms **
- Realm owners can now set relevant permissions for players invited to their Realm.
	- Default settings can be set for all new members entering a Realm.
	- The owner can set permissions for an invited player to either visitor, member or operator.
	- When resetting a world, or uploading a new world, already set permissions stay in place.

** Splashes **
- Removed the following splashes:
	- "[snapshot intensifies]!"
	- "There's no stopping the Trollmaso."

** Sounds **
- Increased the frequency and volume of the ambient mob sounds made during raids, to make them easier to locate.

** Player positioning **
- The player's position now adjusts to the gap they are within:
	- 1.5 blocks: sneaking posture
	- <1 block: swimming animation
- Being forced into an area under two blocks high causes the player to adopt the appropriate posture.


