# Tutorials/Block and item duplication
This page seeks to teach you how to clone items and blocks without building a separate farm for them, in vanilla Survival mode. It can be treated as an "everything farm," since it can "farm" things that can't normally be farmed, like block of diamonds, dragon eggs and other non-renewable blocks.

If any of these do get patched, you must either go back versions or use third-party applications in order to replicate them again. For Java Edition, this can happen in the Minecraft Launcher, but on Bedrock Edition, you must use third party applications in order to replicate these again. These third-party applications are NOT owned or endorsed by Mojang, so use at your own risk.

Note that these techniques are considered "cheating" by many people and Mojang tries to remove the ability to duplicate in Survival during almost every update, except for primed TNT duplication, which has been left in on purpose until a suitable replacement exists. On most servers, duping inventory items is a bannable offense.

The best way to duplicate a block is to turn it into an item first, then duplicate the item. However, there are other ways to duplicate the blocks themselves, though they only work for certain blocks. Shulker boxes make item duplication much easier because they allow for up to 1,729 items to be cloned at once (including the shulker box).

## Contents
- 1 Background
	- 1.1 Why duplicate
	- 1.2 How to use this guide
- 2 Legitimate Duplication
	- 2.1 Dirt Duplication
	- 2.2 Bone Meal Duplication
	- 2.3 Void Trading
- 3 Java Edition
	- 3.1 Unpatched/Working
		- 3.1.1 Singleplayer
			- 3.1.1.1 Basic Save File manipulation
			- 3.1.1.2 Alt+F4 v2.0 - Task Manager
		- 3.1.2 SP and MP
			- 3.1.2.1 Explosive fireworks + elytra duplication (MP only)
			- 3.1.2.2 Dirt Duplication
			- 3.1.2.3 Lead Duplication (note: does not work in 1.16.4)
			- 3.1.2.4 Book player-profile rollback glitch
			- 3.1.2.5 Piston-based duplication of rails and carpets (Patched on paper)
			- 3.1.2.6 Dragon's Breath Duplication
			- 3.1.2.7 Shulker Box breaking glitch
			- 3.1.2.8 Piston-based TNT Duplication
			- 3.1.2.9 Gravity Block Duplication
			- 3.1.2.10 Tripwire Hook Duplication
	- 3.2 Patched/Non-Working
		- 3.2.1 Singleplayer
			- 3.2.1.1 Alt + F4 Method (Patched 1.15)
		- 3.2.2 Multiplayer
			- 3.2.2.1 Deadly Method (Patched 1.15)
			- 3.2.2.2 Same Player Twice (Patched in virtually every server)
			- 3.2.2.3 Donkey Inventory Oversight (Patched in 20w16a and in Paper/Spigot 1.15.2)
		- 3.2.3 Both
			- 3.2.3.1 Bundle Duplication (20w45a to 20w48a)
			- 3.2.3.2 Baby Piglin Item Dupe (Patched in 1.16.3)
			- 3.2.3.3 Zombie/Drowned Method (Patched)
			- 3.2.3.4 Chunk memory overflow (Patched 1.15)
			- 3.2.3.5 Dropped Items (patched 1.13)
			- 3.2.3.6 Piston Duplication (patched 1.13)
			- 3.2.3.7 Crafting Dupe (Patched 1.12.1)
			- 3.2.3.8 Using Dolphins(Patched 1.17-pre2)
			- 3.2.3.9 All Item Duplication Glitch (patched 1.17.1)
			- 3.2.3.10 Enchanted Book Method (24w09a)
- 4 Bedrock Edition
	- 4.1 Unpatched
		- 4.1.1 Sand Duplication (Works 1.20.1+)
		- 4.1.2 Dirt Chest (works 1.16.1+)
		- 4.1.3 Chunk save stating
	- 4.2 Patched
		- 4.2.1 Fortune on Flowers (Patched in 1.20.70)
		- 4.2.2 Gravity Block Duplication (Patched on 1.16.200)
		- 4.2.3 Anvil Duplication (Patched in 1.16)
		- 4.2.4 Anvil Naming (Versions 1.5.1-1.16.0) (Patched)
		- 4.2.5 Donkey + Looting sword (patched 1.16)
		- 4.2.6 Piston Chest (Patched in 1.16)
		- 4.2.7 Rapid Dispenser (Versions 1.5.1-1.5.2+)
		- 4.2.8 Bed Duplication (Patched)
		- 4.2.9 Ore Duplication (Patched)
		- 4.2.10 Beacon + Pocket Edition (Patched)

## Background
### Why duplicate
- Duplicate your most valuable gear:if you lose them to lava or the Void, you can just pull a backup from your backup chest! More specifically, you make a duplicate from your backup, so you can go through the entire process if you lose them again.
- Duplicate Enchanted Books / Diamonds / Ancient Debris / Netherite Ingots / Emeralds:Once you have one, you'll have an infinite amount by duplicating it. Again, it is important to leave some stock as backup; you never know if you need more.
- Duplicate Enchanted tools / Blocks:You'll never have to worry about running out of your tool / block of choice, since you can just duplicate them as well. Duplicate in bulk for items/blocks that will be used in large quantities.
- Duplicate Shulker Boxes (with items inside):theoretically you can duplicate both the shulker box and the items it contains, since that info is stored within the shulker box itself. Use this to duplicate blocks in excessive quantities.
- Duplicate Enchanted Equipment:combined with a grindstone, you can farm an infinite amount of EXP by removing enchantments from duplicated enchanted gear. While a decent, safe and consistent method of getting exp, building an Enderman Farm is faster.
- Griefing servers (not endorsed):Item duplication is sometimes used to inflate a server's economy by duplicating valuable items and distributing them to other players. This type of behavior is most notably used against pay-to-win servers that sell in-game items or other advantages for real money. This is considered cheating and can get you banned on the server in question. In addition, most duplication glitches are patched using third-party plugins.

If you happen to be a speedrunner, duplication allowed in gliched categories can cut down a lot in your game time. One extreme example is the TAS Any% speedrun done in 29.19, complete with the dragon dead. Alt+F4 is usually used for this purpose.

### How to use this guide
This guide is in the process of restructuring. When it's done, all methods will have something like this in front:

| Java version range | Mod patched?           | Realms |
|--------------------|------------------------|--------|
| 1.x.x ~ 1.x.x      | Paper x.x.x build #xxx | Yes    |

| Bedrock version range | Realms |
|-----------------------|--------|
| 1.x.x ~ 1.x.x         | Yes    |

These tables are there to save you some time with testing no longer useful methods.

Why do we care about mods? Although we, being the official wiki, do not endorse the use of mods, mods are a fact of life we must accept. Servers commonly use them to fix the very glitches we are talking about here and, by some tweaking of the game, do whatever the server owner want the game to do.

- Spigot is one of the modded server softwares you will bump into. They are mostly focused on performance, but do fix a glitch or two from time to time.
- Paper is a server software that branched off Spigot. They too care about performance, but they take out glitches with a burning hatred. They even killed TNT duplication!

Why single out Realms? Realms works a bit differently from your normal multiplayer server, Java or Bedrock. As a result, different glitches may occur.

## Legitimate Duplication
These are not actually duplicating items, but instead are legitimate (or mostly legitimate) methods of obtaining certain items.

### Dirt Duplication
Start by obtaining at least 2 dirt and gravel from bartering. Next, craft coarse dirt using 2 dirt and 2 gravel for 4 coarse dirt, then till the dirt and mine it to obtain 2 extra dirt. With a bartering farm, a good hoe, and a good shovel, you can mass produce dirt in a matter of minutes.  However, this is not perfect duplication, as you will need a constant supply of gravel.

### Bone Meal Duplication
By using bone meal and composting the yield, the player gets bone meal back. Usually, this method yields significantly less bone meal than is used, and is therefore not profitable, but the following methods do duplicate bone meal:

- Using bone meal on amoss blockand composting the blocks produced.
	- The player should leave a moss block uncomposted, to repeat the cycle.
	- InBedrock Edition, the azaleas can be further grown into azalea trees, and one then composts the leaves. Again, this is less effective inJava Edition, due to the 45% success rate of bone meal.
- Using bone meal on asapling,azalea,mangrove propagule,mushroom, orfungus, and composting the blocks created.
	- This is less effective inJava Edition, since it generally takes multiple bone meal to grow a singletree/huge mushroom/huge fungus.[needs testing]
	- InBedrock Edition, this method is most effective for trees that have a lot of leaves, such ascherry.
	- Formangroves, the player must use bone meal to create and grow a propagule.
	- For trees, the player must break some of the leaves, preferably with aFortuneIIIhoe, to replenish saplings. Similarly, forhuge mushrooms, the player must break some of themushroom blocks, which have a significantly higher drop rate than leaves, but Fortune does not work.
	- For azalea trees and huge fungi, the player must obtain azaleas and fungi, respectively, preferably using the methods above.

### Void Trading

  

This tutorial is exclusive to  Java Edition. 


| Java version range | Mod patched? |
|--------------------|--------------|
| 1.16+              | Paper        |

"Void trading" is a way to trade with villagers and wandering traders without restocking. To do that, a player unloads the villager before closing the trading interface, so that the villager never "remembers" having been used for trading. Infinite trading is good for turning farmed items such as Sticks from a Bamboo farm into emeralds, or for buying things.

A few ways are possible:

- The original "void trading" involves going out into The End. By setting up a villager trading hall on the end of oneEnd gateway, the player can leave instantly and unload the villager. When the player comes back, the villager would have not remembered the trade.
- The rail-based method uses powered rails to leave the simulation range and can be set up in the overworld. See"Minecraft Elegance: Voidless Void Trading (Java 1.17-1.19)"– ianxofour on YouTube.
- The multiplayer method uses two players logging in and out to do the trading. See"1.16.4 PaperMC & Spigot Multiplayer Infinite Villager Trades Exploit! (Currently Unpatched)".

## Java Edition
### 
Currently, work as of the latest release of vanilla Minecraft. They may be patched in modified servers (such as Spigot, or Paper), which many servers use, but have been tested and they still work in unmodified conditions. In singleplayer, these will work but in multiplayer, these will usually not work. 

#### Singleplayer
##### Basic Save File manipulation
This method is safe and reliable. Needs only the desired items for duplication as well as a chest. You need to have access to save files so this is impractical on servers, where admins aren't giving FTP out like candy.

1. Have the desired items to be duplicated on you: whether it's in your inventory, on your hotbar or equipped doesn't matter.
2. Exit and save the game; returning to the main menu is quickest.
3. Navigate to your save folder. On Windows, it's at%appdata%\.minecraft\saves, on macOS it's at~/Library/Application Support/minecraft/saves, and on Linux, this is located at~/.minecraft/saves.
	1. Making a backup folder of the target world folder is advised but not obligatory.
4. Open the target world folder and duplicate thelevel.datandlevel.dat_oldfiles.
	1. It is advised you keep the duplicates in a place easy to access, usually the world save folder itself. This especially applies if you plan to duplicate items multiple times.
	2. Alternatively, have multiple folders on screen to simply select, copy and paste from one to another.
5. Enter the target world and deposit the desired items to be duplicated into a chest.
6. Exit the world and return to the main menu; the game should save.
7. Copy and paste the duplicatedlevel.datfiles back into the target world folder.
8. Enter the target world. The desired items should both be in the inventory and in the chest.

Extra info: these files also contain your current location and your exp. Theoretically, you can enchant some gear, deposit it in a chest, then load the level.dat file to preserve your level and keep the enchanted gear. Another potential use is to use up your inventory while building then load a backup to keep your progress and refill your inventory with the building material. You could even use this to try multiple times to kill the Ender Dragon / Wither without risking your gear and inventory.

Disclaimer: the environment and mobs are not saved with this method, do not attempt to summon the Wither near places of importance or important mobs. Instead, backup the entire target world folder and load it in event of failure. Perform test runs to ensure that this method works.

This method is unlikely to be patched, due to it requiring access to the save files, and not being an in-game mechanic.

##### 
Alt+F4 is patched, but using Task Manager to end the task, on the other hand, is NOT patched, and still works. This is very similar to the Alt+F4 method.
Steps:

1. Open task manager
2. Go into the world you want to dupe the items in
3. Make sure 'Pause on Lost Focus' is off. Do this by pressing F3+P until you see something like "[Debug] Pause on lost focus: disabled" in chat
4. Put the items that you would like to dupe in your inventory
5. Close the world and open it up again
6. When it loads drop the items on ground by pressing 'Q' on the item. Don't close your inventory.
7. Quickly press ALT+TAB or  CTRL+SHIFT+ESC to get into Task Manager
8. End the process "Java(TM) Platform SE Binary" or "OpenJDK Platform Binary"
9. Open Minecraft and load the world again
10. Collect your items

From testing, it doesn't always work. Try playing with different timings.


Video here:



#### SP and MP
##### 
| Java version range | Mod patched?  | Bedrock version range |
|--------------------|---------------|-----------------------|
| 1.16.5             | Paper, Spigot | none                  |


  

This section needs expansion. 
You can help by expanding it.


This duplication glitch works on 1.16.5 multiplayer. It requires an elytra and firework rockets that deal damage to the player. If the rockets do not damage the player, the duplication will not work. Video below: (duplication glitch starts at 0:33)




This is known to work in vanilla servers and realms, however Spigot has patched the bug and Paper has patched it long before its discovery.

##### Dirt Duplication
| Java version range | Mod patched? |
|--------------------|--------------|
| 1.16 snapshot      | ?            |

The mechanism for growing giant spruce trees is known to be glitched in JE 1.16 snapshot. Instead of growing a giant tree on the saplings, the game grows the tree on the first position where space is sufficient and a dirt block is present in the north-west position. When the tree is grown, all the dirt blocks are filled in. With bone meal and piston automation, a semi-auto dirt duplicator can be produced (YouTube by ilmango).

##### 
| Java version range | Mod patched? |
|--------------------|--------------|
| ? - 1.16.4         | ?            |

Bring an animal to the end, put a lead on it, and then lead it into the end portal. When you get back, it should have dropped two leads. Sometimes one of the leads ends up in the end, so make sure to check there. It may not always be in the end, though. This also works when bringing animals into the nether.

##### Book player-profile rollback glitch
| Java version range | Mod patched? |
|--------------------|--------------|
| ? - 1.18?          | ?            |

This duplication glitch works on Singleplayer and Multiplayer. All you have to do is place a chest in front of you and then leave the server as it saves your player data, then relog and put the items you want to dupe from your inventory in the chest, get a book and quill, overload the book with excessive characters and it will cause you to get kicked from the server and rolling back your player data to last save while server files stay the same. As a result, the items will be in both your inventory and the chest.

The book mod (requires fabric download and custom download to work) automates the process.

Video here: https://youtu.be/ml3HkqNfUH4

##### 
| Java version range | Mod patched?                                     |
|--------------------|--------------------------------------------------|
| ? (useful in 1.19) | Paper (1.15.2 Build #358, has option to disable) |

Carpets can be duplicated using a contraption made of two Slime Blocks, a Sticky Piston, and an Observer. This glitch gives infinite fuel and is very easy to automate give thousands of carpets per hour tutorial: https://www.youtube.com/watch?v=ezM2Hs_-hbE

Bottom Layer








Top Layer









https://www.youtube.com/watch?v=U-9ihB7EmKI
and
https://www.youtube.com/watch?v=mGQLDJ8dNGs&t=3s
are in-depth tutorials that show how to do so

##### 
| Java version range | Mod patched? |
|--------------------|--------------|
| ?                  | ?            |

Whenever the dragon lands on the end portal and releases the purple fog, be above or below the purple fog, look at the fog at a steep angle, and proceed to harvest the dragon's breath. The fog will first shrink as intended, but after it reaches the smallest size, it will expand with each bottle used, and keep expanding until the fog disappears as too much time passed. (YouTube by Underscored Frisk)

##### Shulker Box breaking glitch
| Java version range | Mod patched?  |
|--------------------|---------------|
| ?                  | Spigot, Paper |

Shulker Box dupe allows you to duplicate any item in Minecraft singleplayer or Realms. This glitch works with 2 players or with an auto mine mod. So you quickly spam your item in and out while it being broken. The key is to take the item out just before the shulker box breaks. This may take a few tries but eventually you will dupe your items.

You can also use autoclicker with these settings: time between clicks- 1sec 487milisecs. Then you bind the autoclicker to key n, and automine to key m and press n,m,right click at the same time. This opens shulker. Hover over item you want to duplicate; shulkerbox should break and item in it, and item on the ground.

Video here https://www.youtube.com/watch?v=6hLxebiG3EA

##### Piston-based TNT Duplication
| Java version range | Mod patched?                                     |
|--------------------|--------------------------------------------------|
| 1.14+              | Paper (1.15.2 Build #358, has option to disable) |

TNT duplication works in a similar way as rail duplication. A TNT block is BUD-powered, such that when the contraption is pushed by a piston, the TNT is updated and ignites into a primed TNT entity. Then, the piston moves the TNT from the list of TNT block left. This doesn't so much duplicate the TNT block as it creates free primed TNT entities from it without deleting it. Many TNT duplicators still work, but unless properly constructed will blow themselves up.

One common TNT duplication design uses a minecart on a detector rail to power the slime block it is placed on, and moves a TNT block next to a coral fan underneath, the combination of the TNT and the coral duplicates the TNT whenever the whole contraption is moved forward with a piston. For an indepth tutorial of this one checkout Cheesysponges video https://youtu.be/3Izrj2m6Li4





































Slice 1




































Slice 2
The second slice may be placed on either side, and the coral fan has been marked with vines. To prime the mechanism, the upper slime blocks must first be moved forward, pushing the TNT under the rail. After this, moving the whole assemblage forward with a piston will duplicate the TNT, spawning a lit TNT entity directly below the TNT block.

For a list of variations, see e.g. [1]. TNT duping as a glitch is notable in that it has been patched by Mojang Studios several times in the past but was ultimately allowed in the vanilla game due to its immense value to the technical community. In the words of Mikael Hedberg, "TNT dupers fill a slot in the game that the intended game mechanics still cannot."

##### Gravity Block Duplication
| Java version range | Mod patched?            |
|--------------------|-------------------------|
| 1.14+              | Paper 1.15.2 Build #358 |

There are many ways to do this, but the basic idea is the same.

A gravity-affected block is pushed toward an end portal. It becomes an entity as it falls into the portal, and it travels into the other dimension's "spawn point.", but before it's removed from the original dimension, it bounces off an entity in the portal (in a vehicle so it won't go through), and is caught by some pistons. It then turns into a block and is returned to its original location. This process can be looped using redstone. It works for any block that is affected by gravity, except for primed TNT because it would blow up the contraption and cannot become a block again in any case.

Dragon eggs and anvils fall differently from each other and other gravity-affected blocks such as sand, gravel, and concrete powder. Neither dragon eggs nor anvils work in a sand/gravel/concrete powder duplicator because of this. However, it is possible to create a machine that can duplicate dragon eggs and anvils but not sand/gravel/concrete powder. They both can be duplicated and sent into the End as either falling entities or items.

##### Tripwire Hook Duplication
| Java version range | Mod patched? |
|--------------------|--------------|
| 17w18a+            | Paper        |


  

This section needs expansion. 
You can help by expanding it.


Tripwire Hooks are duplicatable, but only in certain directions. It may work in some directions, but not others.




### 
These no longer work as of the latest release of vanilla minecraft, but worked on older versions.

#### Singleplayer
These are dupes that work(ed) only on singleplayer, either because you need access to manage the server, Paper/Spigot patches it, or a plugin is installed that patches it.

##### 
This method is a simple method and has been around since Indev. This method involves dropping the items you want to duplicate, and then saving and quitting. You would then reload the world, pick up the items and press the keyboard shortcut to close a window. Then relaunch the game and reload the world. The items should be duplicated.

#### Multiplayer
These are dupes that only work on multiplayer, commonly because they exploit an anti-dupe plugin (like the thousands of donkey dupes)

##### 
This method is extremely deadly, but not necessarily to the player. This method involves taking a mob that can carry items (e.g. a zombie, a donkey or a llama) down to very low health (i.e. half a heart or less). Using extremely precise timing, kill that mob as it travels through an end portal or nether portal. The items equipped and the mob should appear in the other dimension. It works by tricking the game into thinking the mob is alive on one end of the portal and dead on the other side. The live mob will travel through the portal still carrying the items, and the dead mob's items are also sent into the portal, allowing the player at the other end to collect the cloned items and the mob carrying them.

The deadly method used to automatically farm diamonds (currently the fastest theoretical means of automatically obtaining items in vanilla survival):




##### 
There is a way to trick the game into logging in the same player twice on one server. To do this, start two instances of Minecraft. This requires starting a new instance of the Launcher so that they don’t interfere with each other. Log them both on the same server at the same time. By doing this, the game will render two of the same player. You can then kill the copied player and double your inventory. Rarely servers may also duplicate players on accident or leave "ghosts" of logged out players which can be killed for the same effect. 



##### 
Working in 1.15.2 and in 1.16 snapshots up to 20w12a (Patched in 20w16a and in paper). You need a tamed donkey or llama equipped with a chest. If a player shift-clicks the donkey / llama, that player may view the donkey's inventory and place items. If a second player rides the donkey, the first player will continue to view the donkey's /llama's inventory, even though it is not normally possible to view a donkey's inventory when it is already being ridden by a player. If the second player disconnects, the donkey will disappear along with them, and the donkey's inventory will be considered by the game as part of that player's data. However, the game will keep a copy of the donkey's inventory and GUI temporarily loaded for the first player, who can then reclaim the items. When the second player reconnects, the donkey's inventory will contain what was originally in it before the second player disconnected. The items can once again be taken from the donkey's inventory, resulting in x2 duplication.

#### Both
These dupes work(ed) everywhere! Servers that don't use anti-dupe plugins, singleplayer, etc. 

##### 



For any crafting recipe that uses more than 1 of the same item, you can use this dupe. To use it, you put the items in the crafting grid, then use the bundles on the crafting slot. The resulting item will not disappear but you will save the item you just took from a bundle. For example, if you used 9 stacks of netherite ingots to make 1 stack of netherite blocks, you could use 9 bundles to take all the netherite away and get 1 stack of netherite blocks for no cost.



##### 
This dupe involves baby piglins. It is incredibly simple and it works in multiplayer. To perform this glitch find a baby piglin and drop his health down to a 1-hit kill (2 hits with a normal diamond sword should work). Then drop the item you want to duplicate to the piglin(e.g. a shulker box) then wait for the baby piglin to pick it up. After the piglin has picked up the item drop the piglin 1 gold ingot. While the piglin is admiring the gold, kill the piglin.






##### 
This method exploits the fact that zombies can transform into drowned while they are dying. If you coax a zombie to pick up an item by throwing one at it and then kill it right at the moment that it converts to a drowned, the zombie will die and drop what it was holding but the newly spawned drowned will be holding a duplicate of the item. This can also work with husks transforming into zombies.


Ilmango shows a simple implementation for survival:





##### 
When you overflow chunk memory, you will be able to freeze the chunk. What this means is that changes on this chunk will not be saved and after loading it again it will return to the previous state.
The best way to do this is to create books filled with about fifty pages of random Unicode characters and put it in a chest. There are mods for doing this automatically, but you can also do it manually by copying and pasting. You will need two different types of books for this to work.

1. Choose a chunk in which you want to duplicate and do everything only in this chunk (Press F3 + G to see chunk borders).
2. Get 22 books filled with random characters, name them "X" and 21 filled books but with other characters, name them "Y".
3. Place a chest and put the items you want to duplicate inside it.
4. Place a chest at the same chunk and put them in this pattern:X|Y|X|Y|X|Y|X|Y|X
Y|X|Y|X|Y|X|Y|X|Y
X|Y|X|Y|X|Y|X|Y|X
	- You will have 8 books of each type left.
5. Place a chest above it and put 8 of book X in slot 1 and 8 of book Y in slot 2 in that chest.
6. Reload chunk by reconnecting to the world(if you are on singleplayer) or going 200-300 blocks away and returning(if you are on multiplayer)
7. Move books from the second chest like this:X|Y|X|Y|X|Y|X|Y|X
Y|X|Y|X|Y|X|Y
8. Take out the items you wanted to duplicate into your inventory or put them in a chest at the other chunk.
9. Reload chunk again.
10. Now you have your item(s) in the chest and in your inventory. Books in a second chest are just like in [4].

In 1.14+:

1. Press F3+G to see the chunk border.
2. Place a chest in the chunk that you want to duplicate, then place another chest above it.
3. Then, put the items that you wanted to duplicate in the upper chest.
4. After that, put 5 book and quills that filled in with 100 pages of random unicode characters in the bottom chest like this.X = 1 book; Y = stack of 2 books
X|X|X|Y|
5. After that, press esc and select 'Save and Quit to title' to save the chunk (If you're in singleplayer) or walk 400 blocks away from the chunk (If you're in multiplayer, make sure of the other players were stayed in the nether else the duplication won't work). This method will save the chunk.
6. Then, log-in your world again (If you're in singleplayer) or walk back to the chunk (If you're in multiplayer).
7. Open the bottom chest and move the books like this:X|X|X|X|X|
8. Take your items away from the upper chest and move them to your inventory or put them in a chest at the other chunk.
9. Save that chunk again.
10. Go back to the chunk again.
11. Your items will reappear in the upper chest. The books will be reverted to the state in step 4. Duplication complete.




Discovered by Earthcomputer: 




Tutorial on YouTube by BarrenDome: 





##### 
Relogging at the same time as you drop items can dupe items. Needs very precise timing; exit the second you see the items but before you hear the sound of collecting items.

##### 
When an item frame is removed (broken by the player) from the rear of a piston as the piston is retracting, the correct timing will yield two items of the item that was within the frame. This will work with any blocks or items inside of the frame, with shulker boxes being able to duplicate multiple items at once. This method works in both singleplayer and multiplayer game modes.

##### 
This method can also be used to stack unstackable items, such as diamond swords.

1. Put 2-3 stacks of planks in your inventory.

2. Drop the item that you want to dupe on the ground. (Make sure that there is no item that it can stack within your inventory!)

3. Open your inventory and spam the crafting table recipe until you pick up the item you dropped. It should result in a stack of that item.

##### 
Put a dolphin in a nether portal as it absorbs an item. The original item will still be there, while the dolphin will carry a copy.

##### 
Fill your inventory with items. Repeatedly rename the item you want to duplicate on an anvil until the anvil breaks. When it does, you will drop double the renamed item. If it is not working look at how it's being done in this video: https://youtube.com/watch?v=oSdwwxBgWco (Original Finder)

##### 
See also: 24w09a and 24w10a § Fixes

This method is similar to Chunk memory overflow for 1.14+ singleplayer, with the following differences:

- For step 4, put twocurse of vanishingenchanted books instead of the book and quills.
- For step 7, take the enchanted books, combine them in agrindstone, and move them to your inventory and then to the bottom chest byShift+ clicking.

## Bedrock Edition
### Unpatched
#### 
This method works by using redstone torches to power large dripleaves with sand blocks placed above them to duplicate sand. It's recommended to build this in either the Nether or the End. 

1. Gather at least 2 sand blocks, 1 redstone torch, 1 dirt (or any other block dripleaf can be placed on) and 1 large dripleaf.

2. Build a Nether portal.

3. Secure the portal and either build a shelter or dig as many blocks down respective to the amount of sand you're using to safely house your duplication system.

4. Place the block(s) you're using to plant your dripleaf.

5. Place the redstone torch adjacent to your dripleaf to power it.

6. Place the sand on top of the dripleaf.

7. Leave the Nether.

8. Re-enter the Nether portal.

9. The sand should be duplicated once you re-enter the Nether.

Explanation: https://www.youtube.com/watch?v=noV9JczPFBM

#### 
When using this method there might be a chance the items will get deleted, so creating a backup is recommended.
This method will not work on Realms. 

1. Gather all the items you want to duplicate as well as a chest.

2. Place your chest, and make sure there is 4 dirt in front of the chest.

3. Save & Quit, and then rejoin the World. 

4. Place the items you want to duplicate in the chest and quickly break 4 dirt in front of the chest 1 y-level below it in a 2×2 square shape then count to 4.

5. Quickly forcibly close the application. 

6. Rejoin the game. One of three things will have happened; 
A) The items will have duplicated (both in inventory and chest), 
B) The items will have been removed (neither in inventory nor chest), 
C) Nothing will have happened (in chest or inventory).

Explanation/Source: https://www.youtube.com/watch?v=ptGpINSxhaA



#### Chunk save stating
This method works by causing the game to crash in a way that only the chunk you are standing in will not save correctly, this will cause the chunk you are standing in to revert to the last save, allowing you to dupe in that chunk. 

Explanation of how it works: https://youtu.be/XTkivXhbcMA



### Patched
To use the following methods, you will have to either not update past that point or revert to a previous update (if possible for your system, not all can, such as on Xbox One or Nintendo Switch).



#### 
This can be used to duplicate any 2 block tall flower.

Steps:

1: Get an item with Fortune (level 3 works best) and a 2 block tall flower.

2: Place the 2 block tall flower.

3: Break said flower.

The flowers should have at least duplicated. I think you can get up to 6!

#### 
Duplicates all gravity-affected block except dragon eggs

This video will explain how to duplicate any gravity-affected block. It works similarly to gravity block duplicators in Java Edition: by having a falling block enter an end portal and become a block on the same tick. 




The reason this design does not work for dragon eggs is that it relies on pistons being able to push blocks into their original position. This allows for the block to be duplicated repeatedly, every 6 redstone ticks. However, one can manually duplicate dragon eggs with a similar process:

| G | D |  |  |  |
|---|---|--|--|--|
| P |   |  |  |  |
|   |   |  |  |  |

In the above diagram, the G, D, and P denotes the grindstone, dragon egg, and portal, respectively. The repeater is necessary for the timing to work correctly, due to MCPE-15793. Like the automatic gravity block duplicator, one must use huge mushrooms to replace the End portal frames.

To use, deactivate the lever, and a second dragon egg will appear in The End. You can then re-activate the lever to break the dragon egg and place another one. This design can be used for other gravity blocks, but the automatic version is generally more efficient.

Another alternative to end portal based duping is end gateway based duping, however, it is not as fast as end portal based duping.



#### 
You will need two book & quill and an anvil. Write any text in one book & quill, and sign it. From then, copy the first book & quill by placing them next to each other in the crafting grid. Take the item you wish to duplicate and rename it to the name of the copied book. From here, you can shift-click the anvil result and duplicate your item.

#### 
When naming a stack of items in an anvil, you can use the "Take Half" option to receive the output items without depleting the original stack. As long as you do not take the final renamed item, you can go to the original stack and pick it up to start more or just leave the anvil interface if you are done.

- A way to speed this up is to hit "Take Half", then "Toss Item" while standing close to the anvil, so you can rapidly go through a full stack without having to manually move each selection.

Items duplicated this way won't work for quick use in a recipe, though certainly can be used for Classic crafting and any other use. However, if you wish to revert an item to the default name, you can do so by crafting it into another item then crafting it back to the original (such as redstone block -> redstone dust x9 -> redstone block), or by placing it as a block then breaking it back into an item.

- Sometimes a block won't lose its name when broken into anitem, such asshulker boxeswhich are meant to keep their name, or just randomly the name may stay with a regular block and repeating the process will remove the name. However, some items may break into different items, such as anender chestdroppingobsidian, and the obsidian will each retain the ender chest's name (this was likely a glitch).
- TNT Duplication
- 1. Put a TNT anywhere
- 2.Put a chest aside the TNT
- 3.Put the item that you want to duplicate in the chest
- 3.Light the TNT and at the same time the TNT explodes take out the item in the chest(this requires correct timing and good armor if you want to stay alive after the explosion)

#### 
1. Get a donkey

2. Get a Looting 3 sword

3. Put a chest on the donkey

4. Put your items in that chest 

5. Kill the donkey

The Looting 3 sword causes the donkey to drop more items than normal.

https://www.reddit.com/r/Minecraft/comments/g2k25b/this_bug_is_awesome_to_duplicate_your_items_put

#### 
(Duplicates all Items)

When a chest is pushed by a piston, the contents are backed up a split second before it is moved. If you are in the chest interface and quick-move an item to your inventory in that moment then you will receive the item and the chest will be moved with the item still in it as well.

The recommended build is not automatic. For the recommended build, you will need at least 1 lever, 1 sticky piston, a chest, 10 redstone repeaters (all set to maximum delay), 2 redstone dust, and a button, though there are simpler(thus cheaper) versions that require only a sticky piston, a chest and a button. The instructions are as follows:

The "simple" method of the piston dupe machine. It follows the same instructions as the more expensive, recommended method but uses less blocks.
1. Press the button.
2. Wait until the piston pushes the chest.
3. Open the chest, and immediately put your cursor on the block.
4. At the last second, shift-click on the item you want to dupe.

The "recommended" build of the Bedrock Edition piston-chest dupe method.
If done correctly, you should have an identical copy of the item you put in. 

- If you can not afford to make a sticky piston, this method also works with one regular piston on each side. One piston pushes the chest, and then you open it. You then continue as normal, shift-clicking the item at the last second before the other piston pushes the chest back to it's starting position.

- This method makes mass-duplication possible with the use of ashulker boxand moving the contents of one duplicated box to the other, thus doubling how much you get each time, until you are duplicating an entire box's worth of items.
	- This does run the risk of massive lag in your world, by creating too many shulker boxes with contents. The effect may be even greater in online worlds such asrealmservers. Be sure to transfer most items to regular chests after duplicating to avoid this.

#### 
(Duplicates some Stackable Items only) (patched)

This video will explain how to duplicate any item that can be crafted into a block using a dispenser and a redstone clock.




#### 
Due to how beds are made out of 2 blocks, an explosion near the bed can make the bed drop 2 bed items, meaning you can spawn 2 beds (4 bed blocks) when you had 1 (2 bed blocks). You can repeat this and get infinite beds.

#### 
Get an anvil and get either 9 iron ingot, 9 diamond, 9 coal, 9 gold ingot, 9 lapis lazuli, 9 redstone dust or 9 emerald. Rename 1 of the ores to something random, place it above the rest of the ores in your inventory and go to a crafting table. Craft a block of that ore and select 'craft all.' This will result in the player obtaining 1 block of (whatever ore you chose). The other 8 pieces will still be in your inventory.

#### 
This duplication is no longer possible on realms and only works with stackable items.

1. Get a beacon (It does not have to be activated).

2. Put items to duplicate in your Hotbar, the nine slots on your screen.

3. Open the beacon GUI.

4. Double-tap on the items you want to duplicate. You can't duplicate non-stackable items, and it only duplicates up to fill a full stack.

Note: This might only work if Settings > Video > UI Profile it is set to Pocket, not Classic.

| Introductory      |                                                                                                                                                                           |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Basics            | Menu screen<br/>Game terms<br/>                                                                                                                                           |
| Newcomer survival | The first day/beginner's guide<br/>The second day<br/>The third day<br/>Hunger management<br/>Things not to do<br/>Simple tips and tricks<br/>Your first ten minutes<br/> |
| Shelters          | Best biomes for homes<br/>Best building materials<br/>Building and construction<br/>Navigation<br/>Shelters<br/>Shelter types<br/>                                        |

| General                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| General                    | Achievement guide<br/>Advancement guide<br/>Best enchantments guide<br/>Breaking a fall<br/>Breaking bedrock<br/>Combat<br/>Complete main adventure<br/>Creating a village<br/>Downgrading<br/>Dual wielding<br/>End survival<br/>Exploring caverns<br/>Gathering resources on peaceful difficulty<br/>Getting food quickly<br/>Headless pistons<br/>Hitboxes<br/>Horses<br/>Indestructible end crystals<br/>Mapping<br/>Measuring distance<br/>Minecraft in education<br/>Mining Diamonds Fossils Ancient Debris<br/>Diamonds<br/>Fossils<br/>Ancient Debris<br/>Nether hub<br/>Nether portals<br/>Nether survival<br/>Organization<br/>Pillar jumping<br/>Playing with a controller<br/>PvP PvP bases<br/>PvP bases<br/>Spawn-proofing<br/>Summoning jockeys<br/>The Void<br/>Time-saving tips<br/>Thunderstorm survival<br/>Units of measure<br/>Village mechanics Trading<br/>Trading<br/>X-ray glitches<br/> |
| Enchanting<br/>andsmelting | Enchanting mechanics<br/>Anvil mechanics<br/>Automatic smelting<br/>Manual smelting<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

| Challenges                |                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| General                   | Acquiring a conduit<br/>Curing a zombie villager<br/>Defeating temples<br/>Defeating a village raid<br/>Defeating a Nether fortress<br/>Defeating a bastion remnant<br/>Defeating a monster room<br/>Defeating a pillager outpost<br/>Defeating a woodland mansion<br/>Defeating a monument<br/>Defeating an End city<br/>Defeating the Ender dragon<br/>Defeating the Wither<br/>Exploring an ancient city<br/>Obtaining every music disc<br/> |
| Non-standard<br/>survival | Adventure survival<br/>Half hearted hardcore<br/>Hardcore mode<br/>Surviving in a single area indefinitely<br/>Infinite desert survival<br/>Island survival<br/>Manhunt<br/>Mob switch<br/>Nomadic experience<br/>Skywars survival<br/>Superflat survival<br/>Flat survival<br/>Ultra hardcore survival<br/>                                                                                                                                    |
| Challenge maps            | Beating a challenge map<br/>Creating a challenge map<br/>                                                                                                                                                                                                                                                                                                                                                                                       |

| Constructions |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Constructions | Adding beauty to constructions<br/>Airlock<br/>Architectural terms<br/>Building a cruise ship<br/>Building a metropolis<br/>Building a rollercoaster<br/>Building safe homes<br/>Building water features<br/>Color palette<br/>Creating shapes<br/>Defense<br/>Desert shelter<br/>Elevators<br/>Endless circling pool<br/>Furniture<br/>Glazed terracotta patterns<br/>Making nice floors<br/>Pixel art<br/>Ranches<br/>Roof types Curved roofs Roof construction guidelines Roof decorations<br/>Curved roofs<br/>Roof construction guidelines<br/>Roof decorations<br/>Secret door<br/>Settlement guide<br/>Underwater home<br/>Walls and buttresses<br/>Water gate<br/>Water-powered boat transportation<br/> |
| Blockbreaking | Blast chamber<br/>Igniting TNT underwater<br/>Wither cage<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

| Farming        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Blocksanditems | Amethyst<br/>Armor<br/>Azalea<br/>Bamboo<br/>Basalt<br/>Bedrock<br/>Blaze rod<br/>Bone meal<br/>Cactus<br/>Chorus fruit<br/>Clay and mud<br/>Cobblestone<br/>Cocoa bean<br/>Copper<br/>Crops (Beetroot, Carrot, Potato, Wheat)<br/>Dirt<br/>Dragon's Breath<br/>Dripstone<br/>Egg<br/>Fern<br/>Fish<br/>Flower<br/>Froglight<br/>Glow berries<br/>Glow ink sac<br/>Glow lichen<br/>Goat horn<br/>Gold<br/>Hanging roots<br/>Honey<br/>Ice<br/>Iron<br/>Kelp<br/>Lava<br/>Meat<br/>Moss block<br/>Mushroom<br/>Music disc<br/>Nautilus shell<br/>Nether growth<br/>Nether vine<br/>Nether wart<br/>Obsidian<br/>Powder snow<br/>Pumpkin, Melon<br/>Rooted dirt<br/>Sculk growths<br/>Scute<br/>Seagrass<br/>Sea pickle<br/>Snow<br/>Soul soil<br/>Sugar cane<br/>Sweet berries<br/>Tree<br/>Trident<br/>Vine<br/>Villager trading hall<br/>Wither rose<br/>Wool<br/>Duplication<br/> |
| Mobs           | Mob farming<br/>Mob grinding<br/>Monster spawner traps<br/>Allay<br/>Animals<br/>Axolotl<br/>Blaze<br/>Cat<br/>Cave spider<br/>Creeper<br/>Drowned<br/>Ender dragon<br/>Enderman<br/>Frog<br/>Goat<br/>Guardian<br/>Hoglin<br/>Iron golem<br/>Magma cube<br/>Phantom<br/>Piglin bartering farm<br/>Raid<br/>Shulker<br/>Slime<br/>Squid<br/>Turtle<br/>Villager<br/>Wandering trader<br/>Warden<br/>Witch<br/>Wither<br/>Wither skeleton<br/>Zombie<br/>Zombie villager<br/>Zombified piglin<br/>                                                                                                                                                                                                                                                                                                                                                                                   |

| Mechanisms            |                                                                                                                                                                                                                                                                                                                                                                  |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Basicredstone         | Automatic respawn anchor recharger<br/>Basic logic gates<br/>Combination locks<br/>Command block<br/>Flying machines<br/>Hopper<br/>Item sorting<br/>Item transportation<br/>Mechanisms<br/>Observer stabilizer<br/>Randomizers<br/>Redstone music<br/>Redstone tips<br/>Rube Goldberg machine<br/>Shulker box storage<br/>Villager trading hall*Water tram<br/> |
| Detectors             | Block update detector<br/>Comparator update detector<br/>Daylight detector<br/>                                                                                                                                                                                                                                                                                  |
| Minecarts             | Train station<br/>Minecarts Storage Storage system<br/>Storage<br/>Storage system<br/>                                                                                                                                                                                                                                                                           |
| Traps                 | Snow golems<br/>TNT cannons<br/>Trapdoor uses<br/>Trap design<br/>Traps<br/>                                                                                                                                                                                                                                                                                     |
| Pistons               | Piston uses<br/>Piston circuits<br/>Quasi-connectivity<br/>Zero-ticking<br/>Instant repeaters<br/>                                                                                                                                                                                                                                                               |
| Advanced<br/>redstone | Advanced redstone circuits<br/>Arithmetic logic<br/>Calculator<br/>Command stats<br/>Hourly clock<br/>Morse code<br/>Printer<br/>Redstone computers<br/>Redstone telegraph<br/>                                                                                                                                                                                  |

| Servers      |                                                                                                                                                                                                                                                                      |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| General      | Playing on servers<br/>Multiplayer Survival<br/>Spawn jail<br/>Griefing prevention<br/>Joining a LAN world with alternate accounts<br/>                                                                                                                              |
| Server setup | Setting up a server<br/>Server startup script<br/>FreeBSD startup script<br/>OpenBSD startup script<br/>Ubuntu startup script<br/>Setting up a Hamachi server<br/>Setting up a Minecraft Forge server<br/>Setting up a Spigot server<br/>Ramdisk enabled server<br/> |

| Technical                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Technical                   | Improving frame rate<br/>Minecraft help FAQ (IRC channel)<br/>Running the data generator<br/>Update Java<br/>                                                                                                                                                                                                                                                                                                                                            |
| Maps                        | Custom maps<br/>Map downloads<br/>Command NBT tags<br/>Falling blocks<br/>Updating old terrain using MCEdit<br/>                                                                                                                                                                                                                                                                                                                                         |
| Resource packs              | Creating a resource pack<br/>Loading a resource pack<br/>Sound directory<br/>                                                                                                                                                                                                                                                                                                                                                                            |
| Data packs                  | Creating a data pack<br/>Installing a data pack<br/>Custom world generation<br/>                                                                                                                                                                                                                                                                                                                                                                         |
| Creating<br/>Minecraftmedia | Creating videos<br/>Livestreaming<br/>                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Game installation           | Installing snapshots<br/>Installing Minecraft Preview and beta versions<br/>How to get a crash report<br/>Installing Forge mods<br/>Custom Minecraft directory<br/>Playing and saving Minecraft on a thumb drive<br/>Playing and saving Minecraft on a thumb drive with the old launcher<br/>Recover corrupted saved world data<br/>Run Minecraft through Google Drive<br/>Save game data to Dropbox (world data only)<br/>Saved data Dropbox guide<br/> |

| Outdated |                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Outdated | Building micro shelters<br/>Custom texture packs<br/>Door-based iron golem farming<br/>End of light mob farms<br/>Far Lands<br/>How to get a crash report<br/>Installing mods<br/>Man-made lake<br/>Managing slimes in superflat mode<br/>Minecart booster<br/>Potion farming<br/>Repeater reboot system<br/>Survival with no enabled data packs<br/>Update LWJGL<br/>Update Minecraft<br/>Village chaining<br/>Water ladder<br/> |

