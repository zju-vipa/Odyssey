# Conductivity
Conductivity is a property of blocks that determines whether redstone signals can be conducted through them, meaning that redstone components are able to power other components touching another side of this block, though it also has a wide range of other effects on the game world.

Conductivity is usually determined by whether a block has a solid-blocking material and a collision box that takes up a full cube, with 5 exceptions:

## Properties
A lot of the effects of conductivity are non-obvious. Minecraft does not have a "solid" property for blocks, so conductivity is tested when a test for "solidity" would normally occur.

- Redstonebehavior (see also:Redstone circuitand its subpages):
	- Only conductive blocks can be powered by power components or transmission components (seelist of redstone components).
	- Conductive blocks overhead can preventredstone wiresfrom connecting to other redstone wire diagonally upward (and vice-versa for the wire connecting downward).
	- If a non-conductive block can support redstone wire, it acts as adiode, carrying power upward but not downward‌[Java Edition  only].
- Comparatorscan measure block state when it is separated from the measured block by a conductive block.
- Mobscannotspawninside conductive blocks. Conductive blocks also play a part in thepack spawningalgorithm‌[Java Edition  only].
- Minecartswhich on an activatedpowered railcan accelerates away from the conductive blocks on the other side.
- Chestscannot be opened if there is a conductive block on top of them. They are not affected by non-conductive blocks.
- Ghastfireball explosions start fires only on conductive blocks.
- Batscannot hang on non-conductive blocks.

