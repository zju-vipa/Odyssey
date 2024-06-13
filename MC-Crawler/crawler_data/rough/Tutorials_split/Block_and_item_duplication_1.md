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

