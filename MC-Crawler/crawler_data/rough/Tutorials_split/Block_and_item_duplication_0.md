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

