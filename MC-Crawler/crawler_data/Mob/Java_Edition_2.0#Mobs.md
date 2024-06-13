# Java Edition 2.0
On April 1, 2013, Mojang released a hoax announcement for Minecraft 2.0, a new game they had supposedly been working on for two years, describing how it would "bring blocky simulation games to the next level." The post also contained a changelog comprised mostly of nonsensical changes, such as a new slab of TNT called the Etho slab, and the addition of coal blocks (which did not exist at the time).

## Contents
- 1 Additions
	- 1.1 Blocks
	- 1.2 Mobs
- 2 Changes
	- 2.1 Blocks
	- 2.2 Mobs
	- 2.3 General
- 3 Videos
- 4 Issues
- 5 Trivia
- 6 See also
- 7 Notes
- 8 References

## Additions

  

This section needs cleanup to comply with the style guide. [discuss]
Please help improve this page. The talk page may contain suggestions.


### Blocks
Etho Slab
- The data value is 160, although a variant with ID 159 (double Etho slab) also exists.
- Can be crafted with 3 TNT:



Ingredients
Crafting recipe


TNT

6


- Much like other slabs, it can be placed on the lower or upper half of a block.
- It has the same functions as a normal TNT; however, when it explodes, it spawns ananvilover entities in the explosion's range, including Players.
	- This and the block's name are references toEthosLab, a Minecraft YouTuber who often tries to kill players with fallinganvils.

Torch (Burnt-out)
- The data value is 161.
- Torchesnow burn out after a random amount of ticks.
- They can be relit withflint and steel.
- Burnt-out torches were originally supposed to be added in theHalloween Update, wherelanternswere supposed to be the new light source. However, this feature wasn't added to the Halloween Update before release and was later officially rejected.

Block of Coal
- The data value is 162.
- Just like the other mineral blocks, it is crafted with 3×3coal:



Ingredients
Crafting recipe


Coal




- However, when it is put into the crafting table to get back the coal, the coal obtained is not stackable with other coal, because it has a different item data value: 32767 instead of 0. This is likely an intentional bug.
- Was coded in as a joke, but was added later in the next update as an authentic block.
- Showed speech bubbles such as "Ouch" when punched, and eventually struck the ground with lightning if punched enough times.
- This block was later added into Minecraft inJava Edition 1.6.1with the same texture as from the April Fools version, but it was later retextured.

Tinted Glass
- Has a data value of 163.
- Is opaque.
- Glass can bedyedany color that the dye exists for, and yields 8 tinted glass of the corresponding color:

| Ingredients                                                                                                                                                                                      | Crafting recipe  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| Glass+Bone MealorLight Gray DyeorGray DyeorInk SacorPink DyeorRed DyeorOrange DyeorYellow DyeorLime DyeorGreen DyeorLight Blue DyeorCyan DyeorLapis LazuliorPurple DyeorMagenta DyeorCocoa Beans | 8888888888888888 |

- Containsblock datavalues ranging from 0–15 that specify the color of the glass.Wool's block data valuesproduce the same colors when used on tinted glass.
- InJava Edition 1.7.2, tinted glass was added to the game under the name stained glass.
	- At its first introduction,13w41a, it used the 2.0 textures, but it was changed in the next snapshot,13w42a.
- InJava Edition 1.17,tinted glasswas added. It is unlikely that the identical naming of these blocks was intentional.

- Etho slab
- Torch (Burnt-out)
- Block of Coal
- Tinted Glasses

### Mobs
The pink wither compared to the regular wither.
A large swarm of redstone bugs.
Aside from the Pink Wither, the mobs added are variants of preexisting mobs.

  Horses and Ponies
- Textures are calledpig_horse, andcow_horse.
- These "horses" and "ponies" can sometimes be obtained when cows or pigs are spawned withspawn eggs.
- They follow a player holding an apple or sugar, but they breed like normal horses.
- Were a joke, buthorseswere added as authentic mobs inthe next update.

 Pink wither
Main article: Pink Wither
- Attracted tosugar, restores health to all surrounding mobs, and appliesbone mealto all eligible neighboring blocks.
- It also has the ability to growroses,dandelions,grassandfernsongrass blocks, due to the bone meal.
- Starts off with one head. Feeding it sugar grows another head (up to three) and increase the range of these effects.
- Pink withers are spawned by placing pink wool, with aflower potcontaining a rose on top.
- Just like their evil counterpart, they dropnether stars.
- It is still classified as a hostile mob, though its behavior is not hostile.
- The pink wither is also considered undead, and is hurt bypotionsof Healing and healed by potions of Harming.
- Unlike the normal wither the pink wither can't fly and has no health bar.
- In the version.jarfile the texture is namedwither_pink.
- Pink withers were also seen in15w14a, another April Fools snapshot.

 Diamond chickens
Main article: Diamond Chicken
- Rarely spawns instead of a normal chicken.
- Laysdiamondsorlapis lazuli, or explodes instead of layingeggs.

 Redstone bug
Main article: Redstone Bug
- Has the appearance of asilverfish, but with a shade of red that is the same as theredstonethey spawned over.
- Same behaviour as silverfish.
- Spawns when a redstone error is activated, on the spot of the error.

## Changes
### Blocks
Dropper
- Has been renamed to floppers.
- Change anything they drop to araw fish.

Furnace
- Has a new NBT tagHeatthat can reach from 0 to 700.
- The tag increases every tick the furnace is lit with a 50% probability.
- It decreases with a 25% probability every tick it is not lit.
- The furnace has a higher chance of spawning a large smoke particle the higher theHeattag is.
- WhenHeatreaches 700 the furnace has a 25% chance of exploding every tick.
- The explosion has a power of 5 and creates fire.

Torches
- Burn out over time, turning intoburnt-out torches.
- They can be relighted withflint and steel.

### Mobs
Chicken
- Are now aneutral mob, and spawn reinforcements with a 25% probability when killed.
- LikeEndermen, they attack when the player looks at them. This can be prevented by wearing a pumpkin. They have an attack strength of 4.

Pigs, Mooshrooms, Cows, Sheeps and Chickens.
- New NBT tagFatnesswith a default value of 0.
- Increases every time they are fed with the item to breed them.
- The size of body increases except for chickens.
- When theFatnessreaches 10 or higher the animal explodes without destroying any blocks.
- They drop up to two times theirFatnessitems.

Sheep
- Using agolden applemakes them fly.

Zombie Pigmen
- Now carry "Battlesigns".

### General
Mobs
- "Super Hostile Mode" is an occasional event (every 2–5 minutes on Purple version).
	- Consisting of a shower oflightningbolts around the player (and usually striking the player at least once), while spawning a large number of powerful monsters in the area and applying the Blindness status to the player. These spawns include not only heavily armed and armoredzombiesandskeletons, and multiplecharged creepers, but even the occasionalblazeand other monsters that don't usually spawn in the Overworld. This is a reference toVechs'Super Hostile series of maps. All of these are apparently triggered by "punching wood" or crafting anything. Naturally, these are some of the first things a Survival player needs to do.

Options
There is a new option for Super HD Graphics. When this option is turned on, it makes all textures monochrome except for recolored/secondary layer textures, such as grass side overlay or the colored glass. Super HD Graphics mode does not, however, make the game more laggy or glitchy.

Speech bubbles
Blocks and mobs can have speech bubbles containing text above their heads, simulating talking. All quotes:

- That hurts :(
- My eye!
- ..zzZZZ
- Why!?
- I'll be back!
- You didn't ....
- Oof
- (&%!@*#&%!@$#
- Ouch
- Hi there!
- That tickles
- Who's there!
- I thought we were friends
- You're mean!
- Whiiii
- Not dropping anything!
- I like you!
- I HATE you!
- YOU NO TAKE .. COBBLE!
- I'm diamond
- You punched me
- Stop punching me
- I'm dirt
- Mummy?
- SSSSSSST
- KABOOM?
- BULLY!
- I'm telling
- Creeper behind you!
- Did I do bad?
- Hello

- An overfed sheep.
- A sheared overfed sheep.
- A talking block of coal.
- Super Hostile mode.
- Super Hostile mode again, featuring more mobs.
- Fighting the enderdragon in super hostile mode.
- Fighting the enderdragon in super hostile mode.
- Fighting the enderdragon in super hostile mode.

## Videos
The update was intended to be given to the following YouTubers as trailer videos:[1]

- SethBling –MindCrack SMP – Ep 1: MineCraft 2.0 Pre-Release Review
- BlameTheController –Minecraft 2.0 Beta Ep 1: Multiplayer Dungeon World first
- Guude –Minecraft MindCrack - S4E1 - Minecraft 2.0
- Xisumavoid –Minecraft 2.0 Update Preview
- Keralis –Wife vs. Minecraft - Episode 30: Minecraft 2.0!
- Biffa2001 –Minecraft 2.0 One Life - "Death By Blue Chickens" (April Fools Humor/Comedy!)
- Docm77 –Minecraft 2.0 Closed Beta - Exclusive First Look
- W92Baj –Minecraft 2.0 - You wont believe what has been added - Mindcrack prelease overview.
- Mhykol –Mhykol Mines - Mindcrack - Episode 259 - Minecraft 2.0
- Generikb –Minecraft 2.0 FIRST LOOK!
- Vechs –Ep01 Minecraft 2.0 LP - A Fresh Start
- Paul Soares Jr –Minecraft 2.0 - Mindcrack EXCLUSIVE SNEAK PEEK!
- Pyropuncher –Minecraft 2.0 Footage!
- Pakratt0013 –Pakratt's Collections 55: First Impressions of 2.0
- AvidyaZen –MINECRAFT 2.0 - THE NDA HAS BEEN LIFTED!
- Joe Hills –Minecraft 2.0, now with more abominations!
- Millbee –Preview Of The Minecraft 2.0 Update!
- AnderZel –Minecraft 2.0 Update Pink Witter?
- ElRichMC –Minecraft Review, 2.0 (April Fools Day)

## See also
- Java Edition 15w14a(2015)
- Java Edition 1.RV-Pre1(2016)
- Java Edition 3D Shareware v1.34(2019)
- Java Edition 20w14infinite(2020)
- Java Edition 22w13oneBlockAtATime(2022)
- Java Edition 23w13a_or_b(2023)
- Java Edition 24w14potato(2024)

## Notes

↑ Includes all the announced features without Super Hostile mode.

↑ Super Hostile mode only.

↑ Includes all announced features, including Super Hostile mode.


