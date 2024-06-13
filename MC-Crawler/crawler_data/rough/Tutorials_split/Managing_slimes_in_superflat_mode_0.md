# Tutorials/Managing slimes in superflat mode
On superflat maps, slimes spawn in enormous numbers, and dealing with them can become extremely tedious. Dealing with them can involve building walls or fences, slime pits or moats, or one can use a clock with a command block. These methods are described below.

If no slimes at all are desired, then in Java Edition the world can simply be generated with a surface y level above 40, which stops the slime spawns. For details, see how to create custom world generation presets.

## Contents
- 1 Slime pit
- 2 Slime cage
- 3 Moat
- 4 Command block auto-killer (Creative with cheats only)
- 5 Turning on Peaceful mode
- 6 Using the MobSpawning game rule

## Slime pit
5×5×3 slime pit
This slime pit is 5×5×3, and has been dug down to bedrock and given a one-block 'lip'. The lip ensures slimes already in the pit don't sometimes push new arrivals away before they can fall in. Recommended size is about 7×7. 4×4 is about the minimum practical size because otherwise larger slimes arriving at an angle won't fall in. Rather than making one enormous pit, it's usually better to make several medium-sized pits in different areas.

## Slime cage
Simple slime cage
This simple slime cage made of dirt blocks traps small and large slimes but not any other mob type. The one-block 'steps' that allow slimes to climb into the cage, but not back out again. Their only escape is to be destroyed or to despawn. If you want to use a slime cage to help keep an area slime-free, put the steps on the inside, then any slime that does appear inside can find its way out, but not back in again.

The key idea behind both trap types is to ensure the slimes are trapped rather than killed; once enough slimes are trapped, the mob spawn rate in that area is greatly reduced and new mobs — slime or not — largely stop spawning. When you want to do some mob farming, simply move 128+ meters away from the slime pit, at which point all the slimes in it despawn and mobs of all types then start reappearing elsewhere as they normally would. A good tip is to do this either shortly before nightfall or shortly before dawn to maximize the number of farmable non-slime mobs that appear. By this method you can roughly control the numbers of mobs appearing in an area by luring more or fewer slimes into your slime pits.

One minor tip is to ensure your slime pits are dug out of earshot of the areas you spend the most time in, otherwise the sound of dozens of constantly-jumping slimes can also become wearing.

Given the large area covered by a typical NPC village, if you enclose an entire village inside a single wall, it's highly probable for at least one slime-spawning chunk to be inside the village. You may wish to place blocks allowing slimes to exit certain areas and not re-enter them in order to keep their numbers manageable.

Using snowballs, the player can push a slime away from the village or other area, though this is most practical in creative mode. Slimes may also be pushed into lava pits.

## Moat
A moat uses the same principle as a slime pit, but it takes advantage of the fact that slimes cannot swim. For simply stopping slimes, a one-block deep moat freezes them in their tracks, but it drowns only the smallest (harmless but annoying) ones. To kill all kinds of slimes, make it three blocks wide and three blocks deep. A water moat has the advantage that it forms a complete barrier against slimes, but is completely harmless to the player and other mobs. Dry moats capture other mobs without killing the slimes. Moats are also easy to build and look nice. In 1.13 it is possible to use magma blocks to pull slimes and all other mobs down using bubble columns. If there are a lot of nearby villages, the player might be able to fill the moat with lava to kill mobs of all kinds although the only downside is that it destroys the items they drop and experience orbs unless they use hoppers.

## 
This simple trick can be achieved by using a repeating command block with the setting always active on. In the command block, use this simple command: /kill @e[type=minecraft:slime] or /tp @e[type=minecraft:slime] ~ -70 ~ (The second command stops slimeball drops by teleporting the slimes into the void)

The player can also type the following commands directly into the chatbox: /gamerule doMobSpawning false (This method prevents all mobs including slimes from spawning in the world)

## Turning on Peaceful mode
One alternative method is to turn monsters on 'peaceful' mode. This, however, prevents all hostile mobs from spawning, as well as other various in-game effects (such as starvation). 

Java: Visit the game menu and change the Difficulty box near the top-right corner by clicking on it. Note: this works only if the difficulty is not locked. 

Bedrock: Pause, go to options, and then find the 'game' tab. You should be able to change it from there. 

On both, though, you can do /difficulty peaceful

