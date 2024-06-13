# Tutorials/Door-based iron golem farming
This tutorial describes iron golem farming as it works in the Legacy Console Edition (and as it formerly worked prior to Java Edition 1.14 and Bedrock Edition 1.11). These farms are based on the number and arrangement of doors and number of villagers, taking advantage of the fact that if a player creates enough "houses," which can be made with just a door and a block, iron golems can spawn. This tutorial describes door-based farms. For iron golem farming in Java and Bedrock editions, see Tutorials/Iron golem farming.

## Contents
- 1 Overview
- 2 General requirements
- 3 Video
- 4 Iron golem farm designs
	- 4.1 Easy 2-tier build
	- 4.2 Survival mode build: Iron golem village
	- 4.3 4 spawn modules 2-level
	- 4.4 Simpler JL2579 design
	- 4.5 The Iron Stream
	- 4.6 The Iron Head, a 100% Efficient Iron Farm
	- 4.7 Comet 107's 30 Village Iron Farm
	- 4.8 The Iron Casster
	- 4.9 Comet 107's Double Stacking 168 Village Iron Farm
	- 4.10 The Iron Bakery
	- 4.11 Iron Processing Unit (IPU-128)
	- 4.12 Iron Nucleus
	- 4.13 Flexible design
	- 4.14 The Iron Paradise
	- 4.15 Tower design

## Overview
An iron golem farm is commonly a player-made village (or several of them, spaced far enough apart to remain separate) in which golems are spawned and then either killed immediately, or moved to a holding cell (outside the village boundary, so that new ones can spawn in their place) for later killing. If you opt for the first method, you will either need to go AFK while camping out at the collection point, have a hopper collecting your items, or else check back periodically to collect your items before they despawn. This necessity can be avoided by using the holding cell method, which allows the golems to collect while you are working nearby, and then you can harvest them all at once when you are ready so that you don't miss any drops. 

If the farm is built inside the spawn chunk and fully automatic, it will operate at any time, making it highly efficient.  Iron farms also work in Minecraft Bedrock Edition.

## General requirements
Iron golems spawn naturally in villages (natural or player-made), provided there are 10 villagers and at least 21 houses (counted as doors). The chance of spawning is 1 in 7000 per tick, which averages around one every six minutes. 

There are several approaches to building an iron farm, but efficient farms tend to use two floors in the golem-spawning zone (16 blocks×6 blocks×16 blocks) and keep all doors and villagers outside the zone, either above and below the center or in an outer "ring" on the same level. This is in order to maximize the number of available spaces for the golems to spawn in, which in turn will reduce the number of failed attempts, and keep the spawning rate as high as possible. This is much more effective than simply increasing the villager count to raise the golem cap, which only matters for the few seconds between the time when a golem spawns and when it is flushed out and killed. To further increase your output rate, you can build several separate iron farms as long as they are more than 64 blocks apart, and bring the golems or their drops to a central collection area. The most powerful iron farms are ones that overlap many villages. Since golems are immune to falling or drowning damage, the available killing methods are lava, magma blocks, suffocation, or a combination of these. As a more convoluted option, you can position a group of evokers to attack the golems in a holding chamber.

Odds of a missed spawn occurring:
There are 512 valid spawn points in the 16×6×16 block spawn area. Making a farm with only 1⁄2 of the valid spawn points (256) does not reduce your chance of spawn by 1⁄2.  This is because the game randomly "tries" to find a valid place to put a golem 10 times each time an opportunity to spawn a golem comes up. So, your chances become 0.5 for each of the ten tries. Missing a spawn in this case is equivalent to flipping a coin ten times and have all ten come out tails. It is .510 or .00098 which is just about one in a thousand odds. A better suggestion would be to use some of the area of the zone to rapidly move golems out of the interference zone so they do not halt further spawning. This is a much more likely occurrence than missed spawns if the golems can't move out of the area quickly. This is not as rare of an occurrence as has been suggested.

When the number of valid spawn points is n, chances of a missed spawn are calculated as follows:

(1−n16×6×16)10×100%

So with 256 valid spawn points you will miss 16.2% of the spawns whereas 512 valid spawn points will only result in a loss of 1.7%.

Additionally, console players should note the 50 villager spawn limit, which will make difficult, though not impossible, the full population of certain farm designs. Also, due to changes 4J Studios made to door detection and addition in the December 2015 update that brought MCCE to approximate parity with PC 1.8.8 no stacked or chained village iron farms from the PC community will work on console. Console players should avoid using anything but single village designs at this point. 4J Studios has remained silent as to whether or not the change was intentional or if they plan to fix it. All bug report tickets on MCCE bug tracker have gone unassigned.

No designs are guaranteed to work with modded servers including bukkit/spigot/paper/sponge/etc. due to possible changes in mechanics.

