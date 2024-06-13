# Tutorials/Recover corrupted saved world data
At times Minecraft will hiccup and drop a saved world from the list of those available. The file is still there with the other saved worlds; it is just been corrupted. You can re-upload your application data and specifically your world from the settings in your PS4 menu. Go to application data and simply upload from your online back ups.

In the second case that there is no backup, the missing world, and all your effort there, is recoverable. The things you were wearing and carrying at the time the world got corrupted are not.

First, try creating a "new" world with the exact same name. If successful you will spawn back in the last place you were with your inventory intact.

## 
- Access your "saves" folder
	- %appdata%\.minecraft\saves
	- ~/Library/Application Support/minecraft/saves
	- :~/.minecraft/saves(runningMinecraftas root isnotrecommended)

You should see a folder for each of your saved worlds. For this example, let's say your corrupted world is calledLostWorld.
- Make a copy of the LostWorld folder and all files and folders inside it.

This copy can have any name you want. For this example we call itLostWorldCopy.
- Create a new world with the same seed and map generator settings (Generate Structures, Superflat, etc.) as LostWorld. We will call this world "BlankWorld"

This can easily be done by restoring and "Re-creating" a backup ofLostWorld. If no backup exists, you must manually create a new world. Make sure seed and map generator settings match those ofLostWorldto avoid chunk error.
The inventory (i.e. the things you were carrying) fromBlankWorldworld will be used. Since an inventory in a new world is empty, it will also be empty in the restored world. You can fake a restored inventory by makingBlankWorlda Creative world and putting everything you need into your inventory before closing the game. Don't forget your armor and any enchants on your armor and tools.
If you're not sure what the seed ofLostWorldis and you need to find it, you can do so by accessing your level.dat file using a programme likeNBTExplorer. Here's astep-by-step guideon how to find your seed using NBTExplorer.
- Go back to the .minecraft/saves folder

There will be a new folderBlankWorldfor the world you just created.
- Copy the following files in the BlankWorld folder to the LostWorldCopy folder:
	- level.dat
	- level.dat_mcr(not always present)
	- level.dat_old
	- session.lock

Take care not to copy any folders. Copying can be done with the normal methods for your system: Copy (or Cut) and Paste, select and drag, or other methods.
Here you are looking toreplacethe above files in theLostWorldCopyfolder with the files you've just copied over from theBlankWorldfolder.
- Restart Minecraft

You should see a world calledBlankWorld, withLostWorldCopyas the name of the folder in which it is saved. This is now your restored world.
There will also be aBlankWorldwithBlankWorldas the folder. Ignore this one.
- Test to make sure this world loads correctly.

You will start in a random location and have to find your way back to your settlement.
You might start underground and suffocate. If this happens you will lose all your items again (the ones you put into your inventory in Creative mode in BlankWorld). If you want to keep your stuff, start the whole procedure from the top. After filling your inventory in BlankWorld, make sure to put a stack ofender pearlsin the first slot. When you suffocate, try to escape by looking up and using the ender pearls. You can also try to put yourself at a higher altitude in BlankWorld. You may then die from fall damage, but your items will still be there after you respawn. Or, use the keep inventory cheat to make it easier. Although, you can turn this gamerule cheat off afterwards. If you find it too 'unnatural' for your Minecrafting standards.
- In the Minecraft world select screen, rename BlankWorld to LostWorld.

This will now be your restored world.
- To clean up, delete the BlankWorld world (the one that is saved in the BlankWorld folder).

The restoration will not be perfect. In particular:

- Any saved information about mods (e.g. Thaumcraft research) will be lost.
- Unless you used the 'fake restore' trick mentioned above, your inventory will be empty. You can also restore it with an NBT editor by copying the content of the root node from the file players/yourname.dat to the node "Player" in the file level.dat. (Directions needed)
- Ender chestcontents may be lost.

