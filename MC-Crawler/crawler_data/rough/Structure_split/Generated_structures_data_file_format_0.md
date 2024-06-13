# Generated structures data file format
The Village.dat, Fortress.dat, Temple.dat, Mineshaft.dat, Stronghold.dat, Monument.dat, EndCity.dat, and Mansion.dat files are located in the data folder of a Minecraft level and store information about the generation of villages, Nether fortresses, desert and jungle pyramids and witch huts and Igloos, mineshafts, strongholds, ocean monuments, end cities, and woodland mansions respectively, in the level. The structure data is stored in the chunk data.

## NBT structure
As of Java Edition 1.12.

Note that many of the tags listed for the structure pieces apply only to specific piece types.

- : The root tag.
	- data
		- Features: List of features.
			- [X,Z]: A structure. Tag name contains the chunk coordinates of the structure's starting point.
				- id: Identifier for the structure type. Typically matches the file name.
				- ChunkX: Chunk X coordinate of the start of the structure.
				- ChunkZ: Chunk Z coordinate of the start of the structure.
				- BB: Bounding box of the entire structure. Value is 6 ints: the minimum X, Y, and Z coordinates followed by the maximum X, Y, and Z coordinates.
				- Valid: (Village only) Whether the village generated at least 3 non-roads. If 0, the village isn't actually generated.
				- Processed: (Monument only) List of chunks that have had their piece of the structure created.
					- 
						- X: Chunk X coordinate
						- Z: Chunk Z coordinate
				- Children: List of structure pieces making up this structure.
					- : Structure piece data.
						- id: Identifier for the structure piece. Typically a heavily abbreviated code rather than something human-readable.
						- GD: Appears to be some sort of measure of how far this piece is from the start.
						- O: Likely orientation of the structure piece.
						- BB: Bounding box of the structure piece. (Does not include the part of a village roof that can overhang the road.) Value is 6 ints: the minimum X, Y, and Z coordinates followed by the maximum X, Y, and Z coordinates.
						- Width: (Temples and huts) Width of the structure (X/Z).
						- Height: (Temples and huts) Height of the structure (Y).
						- Depth: (Temples and huts) Depth of the structure (X/Z).
						- HPos: (Temples and huts) Y level the structure was moved to in order to place it on the surface, or -1 if it hasn't been moved yet.
						- placedTrap1: (Jungle temple) Whether the hallway arrow trap dispenser was placed.
						- placedTrap2: (Jungle temple) Whether the chest arrow trap dispenser was placed.
						- placedMainChest: (Jungle temple) Whether the main chest was placed.
						- placedHiddenChest: (Jungle temple) Whether the hidden chest was placed.
						- hasPlacedChest0: (Desert temple) Whether chest was placed.
						- hasPlacedChest1: (Desert temple) Whether chest was placed.
						- hasPlacedChest2: (Desert temple) Whether chest was placed.
						- hasPlacedChest3: (Desert temple) Whether chest was placed.
						- Witch: (Witch hut) Whether the initial witch has been spawned for the hut.
						- hr: (Mineshaft "MSCorridor") Whether the corridor has rails.
						- sc: (Mineshaft "MSCorridor") Whether the corridor has cobwebs.
						- hps: (Mineshaft "MSCorridor") Whether the corridor has a cave spider spawner.
						- Num: (Mineshaft "MSCorridor") Corridor length.
						- tf: (Mineshaft "MSCrossing") Whether the crossing is two floors tall.
						- D: (Mineshaft "MSCrossing") Indicates the "incoming" direction for the crossing.
						- Entrances: (Mineshaft "MSRoom") List of exits from the room.
							- : Bounding box of the exit.
						- Chest: (Fortress "NeSCLT" and "NeSCRT") Whether this fortress piece should contain a chest but hasn't had one generated yet.
						- Mob: (Fortress "NeMT") Whether this fortress piece should contain a Blaze spawner but hasn't had one generated yet.
						- Seed: (Fortress "NeBEF") Random seed for the broken-bridge fortress piece.
						- EntryDoor: (Stronghold) The type of door at the entry to this piece.
						- Chest: (Stronghold "SHCC") Whether this chest in this stronghold piece was placed.
						- Steps: (Stronghold "SHFC") Length of the corridor
						- leftLow: (Stronghold "SH5C") Whether the 5-way crossing has an exit on the lower level on the side with the upward staircase.
						- rightLow: (Stronghold "SH5C") Whether the 5-way crossing has an exit on the lower level on the side with the downward staircase.
						- leftHigh: (Stronghold "SH5C") Whether the 5-way crossing has an exit on the upper level on the side with the upward staircase.
						- rightHigh: (Stronghold "SH5C") Whether the 5-way crossing has an exit on the upper level on the side with the downward staircase.
						- Tall: (Stronghold "SHLi") Whether the library has an upper level.
						- Mob: (Stronghold "SHPR") Whether the Silverfish spawner has been placed in this piece.
						- Type: (Stronghold "SHRC") Indicates whether the room contains a pillar with torches, a fountain, an upper level with a chest, or is just empty room.
						- Source: (Stronghold "SHSD") Whether the spiral staircase is the source of the Stronghold or was randomly generated.
						- Left: (Stronghold "SHS") Whether the corridor has an opening on the left.
						- Right: (Stronghold "SHS") Whether the corridor has an opening on the right.
						- Type: (Village) Village type: 0=plains, 1=desert, 2=savanna, 3=taiga.
						- Zombie: (Village) Whether this village generated as a zombie village.
						- VCount: (Village) Count of villagers spawned along with this piece.
						- HPos: (Village) Y level the piece was moved to in order to place it on the surface, or -1 if it hasn't been moved yet.
						- Chest: (Village "ViS") Whether the blacksmith chest has been generated.
						- CA: (Village "ViF" and "ViDF") Crop in the farm plot, as ablock ID(59=wheat, 141=carrots, 142=potatoes)
						- CB: (Village "ViF" and "ViDF") Crop in the farm plot.
						- CC: (Village "ViDF") Crop in the farm plot.
						- CD: (Village "ViDF") Crop in the farm plot.
						- Terrace: (Village "ViSH") Whether the house has a ladder to the roof and fencing.
						- T: (Village "ViSmH") Table: 0 is no table, 1 and 2 place it on either side of the hut.
						- C: (Village "ViSmH") Hut roof type.
						- Length: (Village "ViSR") Length of the road piece.

| Version history | Pre-Classic Classic Early Classic Creative Multiplayer Test  Survival Test Late Classic Creative Indev  Infdev Alpha Beta Full Release Development versions |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|

| .minecraft | client.jar version.json client.json launcher_profiles.json options.txt version_manifest.json |
|------------|----------------------------------------------------------------------------------------------|

| Development resources        | Anvil file format Chunk format Command storage format Entity format Generated structures format hotbar.nbt format Item format JSON Level format Map item format Model NBT format Obfuscation map ops.json format Pack format Player format raids.dat format Random sequence format Raw JSON text format Structure file format Schematic file format Scoreboard format Server list format sounds.json Subtitles |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Legacy development resources | Classic level format<br/>Classic server protocol<br/>Indev level format<br/>Alpha level format Infdev 20100624 level format<br/>Infdev 20100624 level format<br/>Region file format<br/>server_level.dat<br/>villages.dat format<br/>                                                                                                                                                                          |


