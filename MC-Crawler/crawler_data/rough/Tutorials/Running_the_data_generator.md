# Tutorials/Running the data generator
This tutorial shows how to run the data generator that is included in Java Edition client and server distributions since 1.13.

## Contents
- 1 Purpose
- 2 Getting Started
- 3 Generating data pack contents
- 4 Generating stringified server DAT files
	- 4.1 Stringify all DAT files:
- 5 References
- 6 See also

## Purpose
The data generator can:

- Convert G-Zip compressedNBT formatfiles with.nbtextensions (as used inStructurefiles) from and to String NBT format files with.snbtextensions.
- Generate all contents of the vanilla data pack
- CreateJSONreports of all block states, all registries, and the full vanilla command tree

## Getting Started
To launch the data generator, it is recommended that you download the official server distribution of the Minecraft version you desire.

Then, open a bash or command prompt in the directory where you have the server jar, and run (make sure you have Java installed)

java -DbundlerMainClass="net.minecraft.data.Main" -jar server.jar

If you have set up correctly, the command line will show a list of options and descriptions.

## Generating data pack contents
In the same command line interface, run

java -DbundlerMainClass="net.minecraft.data.Main" -jar server.jar --server

The contents of the vanilla data pack (except pack.mcmeta) will be generated to generated directory in the run directory of the command line interface.



## Generating stringified server DAT files
Many of the server data files located in the world directory of the game server bear the .dat extension.  Many of these files are actually saved in Named Binary Tag (NBT) format used widely throughout Minecraft.  Follow these steps to use the data generator tools distributed with the Minecraft server JAR to convert these files to a human-readable "stringified" format:

1. Open a terminal or command prompt of your choice on your game server
2. Create a new directory namedinputin the same directory as your game server JARmkdir input
3. Copyanyqualifying .dat filewhich is actually written in NBT format into theinputdirectory you created and re-save it with the.nbtextension# (linux-only)
cp world/level.dat input/level.nbt# (windows-only)
copy world\level.dat input\level.nbt
4. Use the--devflag to activate the development generator which is capable of converting a directory of NBT files into a directory of "stringified" NBT (SNBT) files[1]

java -DbundlerMainClass="net.minecraft.data.Main" -jar server.jar --dev --input "input"


If it worked, you'll get some output that looks like this
[17:17:17] [main/INFO]: Starting provider: NBT to SNBT
[17:17:17] [main/INFO]: NBT to SNBT finished after 3 ms
[17:17:17] [main/INFO]: All providers took: 34 ms

You should also have a new directory named generated in the current directory where you ran the command.  Inside will be the stringified version of each file you supplied as input.

1. Use command-line tools of your choice (e.g.caton linux systems) to view them immediately, or use a GUI text editor of your choice to open them

### Stringify all DAT files:
If you'd like to stringify every DAT file currently on your server (for experimentation, curiosity, or whatever):


For Linux:

1. Start from the same directory where yourinputdirectory is located, then run this command to recursively copy all the DAT files into it[2].Replace path/to/world/data with the relative path to the directory holding the world data in your game server.  By default, Minecraft creates this directory in the same directory as the server JAR, and names it world.  Unless you've changed the world name in server.json or moved this directory somewhere else, you can probably just replace that entire path with world# (linux-only)
find path/to/world/data -name \*.dat -exec cp {} input \;
2. Rename all of these files with the.nbtextension[3]:# (linux-only)
for file in input/*.dat; do mv "$file" "${file/.dat/.nbt}"; done
3. Re-run the data generator with the--devflag as described above in step 4 under "Generating stringified server DAT files".

For Windows:

1. Start from the same directory where yourinputdirectory is located, then run this command to copy all files in the save's folder with the .dat extension into the input folder, replacing .dat with .nbt.Replace path\to\world\data with the relative path to the directory holding the world data in your game server.  By default, Minecraft creates this directory in the same directory as the server JAR, and names it world.  Unless you've changed the world name in server.json or moved this directory somewhere else, you can probably just replace that entire path with world# (windows-only)
copy path\to\world\data\*.dat input\*.nbt
2. Re-run the data generator with the--devflag as described above in step 4 under "Generating stringified server DAT files".

