# Classic 0.0.23a_01 (remake)
Minecraft Classic is a JavaScript remake of Classic 0.0.23a_01, made to celebrate 10 years of Minecraft and was uploaded to the Minecraft website (built with Babylon.js library).[1] This version can be played at classic.minecraft.net for free.

## Contents
- 1 Features
	- 1.1 Blocks
	- 1.2 Mobs
	- 1.3 World generation
	- 1.4 Gameplay
	- 1.5 General
	- 1.6 Pause screen
- 2 Bugs
- 3 Differences and inaccuracies from the original
- 4 Trivia
- 5 History
- 6 Gallery
- 7 References

## Features
The inventory with all available blocks
### Blocks
For data values of blocks in this version, see Classic remake data values.

- Air
- Grass Block
- Stone
- Dirt
- Planks
- Rose
- Dandelion
- Water
- Sapling
- Cobblestone
- Bedrock
- Sand
- Gravel
- Wood
- Leaves
- Red Mushroom
- Brown Mushroom
- Lava
- Gold Ore
- Iron Ore
- Coal Ore
- Block of Gold
- Sponge
- Glass
- RedCloth
- OrangeCloth
- YellowCloth
- ChartreuseCloth
- GreenCloth
- Spring GreenCloth
- CyanCloth
- CapriCloth
- UltramarineCloth
- VioletCloth
- PurpleCloth
- MagentaCloth
- RoseCloth
- Dark GrayCloth
- Light GrayCloth
- WhiteCloth

### Mobs
** Human **
- Spawned by pressingG.
- Oddly, they can walk past the world border. They will fall through the bedrock if they go too far.
- They are client-side only and will not show up for other players in multiplayer.
- The model is not made correctly and makes the human look short.

### World generation
** Terrain **
- Generated terrain with hills and lakes, with small caves under the surface.

** Generated structures **
- Trees, made oflogsandleaves.

** World Size **
World Size is limited.

### Gameplay
** Blocks **
- Placing and destroying blocks; switch between the two by pressinguse.
- Blocks don'twaterloglike the one on the right.

** Multiplayer **
- Available to play with up to nine other players, but was temporarily disabled on May 8, 2019 due to performance issues.[2]

** Inventory **
- PressBto open.
- Find and select all the different blocks available.

### General
- 2Dclouds.

### Pause screen
- Drained Ocean before flooding itAbility to copy the URL link to give to other players for them to join.
- For browsers that do not support WebRTC, the URL link and "Copy" button have been replaced with the "Save level" and "Load level" buttons.
	- Clicking on any of these buttons will show the text "<html>" instead of the buttons that allowed the player to save or load a level.

## Bugs
- When exiting and entering the world, the top textures of all blocks that were ataltitudebecame invisible.
- Drained Ocean after flooding it, I noted with red the peak of 1675 Chunk updates, but later there was a even higher peak of 2.5 million chunk updates.The human mob model is glitched.
- Unloaded chunks turned white.
- The sea level in the game world did not match the sea level outside the world, sometimes there still occur "drained" oceans, see images.
- The high peak...FPS counter is inaccurate on some browsers and will sometimes display bogus/random numbers.
- Zooming in and out will sometimes cause a huge drop on FPS, this will cause an performance impact, and this will make all blocks disappear, and display an error icon.
- The game can fail to load the player's current world and instead generates a new one. In this case, any modified blocks (even air) from the previous map are carried over to the newly-generated map, overwriting any otherwise-generated blocks.
- The music sometimes overlaps with other music and keeps building up to the point it is unbearable.

## Differences and inaccuracies from the original
- General
	- Since this is a remake and not a port, the code, apart from the terrain generation code which is the only ported code in the game, is completely different from the original and as such there may be many minor gameplay inaccuracies.
	- Grass blocksseem to turn intodirtwhen in shade.
	- Airexists as a block.
	- The remake version has an auto-save feature.
		- Because of this, reloading or exiting then reopening the website on the same browser will load the same world and seed, along with player-made modifications, provided that the browser cookies aren't cleared.
	- Physics are very different from the original.
	- New level format.
	- Block IDs in this remake do not line up with the original.
- Human mobs
	- They have a strange appearance compared to the original version's humans, likely unintentionally as the result of an update.
	- They have a different, less random and frantic AI.
	- They can cross the world border, revealing that unlike the original, the bedrock and water beyond the border are actually tangible and are actual blocks rather than a rendered flat plane.
		- They will fall through the world after going too far.
	- They can be spawned in multiplayer, although they will only appear on the client side.
- GUI
	- The blue gradient, seen in the inventory, pause menu and other menus in the original, is replaced with simply a transparent gray color, reminiscent of modern Minecraft.
	- The red gradient, seen on the crash/kicked from server screens in the original, is replaced with the same dirt background as seen on the generating level screen in both the original and the remake.
	- Thefontis different, and is also rendered anti-aliased on most browsers. This is because it is in a vector format (.woff).
- Graphics
	- Lighting is very different compared to the original, appearing more flat.
		- Oddly, blocks appear to have a slight shine when looking down at them.
	- The remake used thenoa Engine.
	- Anti-aliasing, making blocks look smoother.
	- Block textures are stored separately rather than on a terrain.png file.
		- Many filenames are different from the actual name.
	- Inventory/hotbar block previews are pre-rendered textures unlike the original.
		- Because of this, they appear pixelated at high resolutions.
	- Saplings do not show particles when broken.
- Sound
	- Sounds are stored in.mp3format rather than.oggformat.
	- Music can be enabled in settings.
		- Are the Volume Alpha soundtrack versions.[verify]
	- Many sound effects are missing.
		- There are no walking sound effects.
		- Breaking wool and glass uses the normal grass and stone sound effects respectively. The original used higher pitched versions of the grass and stone sound effects for those blocks.
	- Breaking leaves plays a new sound that was not heard before in the original.
- Multiplayer
	- There is a new menu when you start up the game, letting you choose a username, and gives you an invitation link to invite people to a server.
		- The invitation link also appears on the pause menu.
	- Other players take the same, glitched appearance as the human mobs.
		- The name tag above players is also more reminiscent of modern Minecraft rather than 0.0.23a.
	- The command set is highly limited compared to the original.
		- Consists of/list,/kick,/ban,/tp,/setspawn, and/help.
		- You can also use commands and chat in singleplayer, unlike the original version.

