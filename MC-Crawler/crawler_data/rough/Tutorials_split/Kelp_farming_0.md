# Tutorials/Kelp farming
This tutorial seeks to explain common practices for farming kelp, a plant found naturally underwater.

## Contents
- 1 Uses
- 2 Mechanics
	- 2.1 Experimental testing
- 3 Manual farming
	- 3.1 Helpful equipment
	- 3.2 Infrastructure
- 4 Automatic farming
	- 4.1 Piston design
	- 4.2 Flying machine
	- 4.3 Bone meal design
	- 4.4 Review Techniques

## Uses
When smelted and crafted into dried kelp blocks, kelp can be used to smelt items. One kelp block can smelt 20 items, so a single undried kelp ends up smelting 1.22 items. This makes kelp useful as a renewable fuel source.

Smelting kelp also grants 0.1 experience. To put this into perspective, it would take about 3,060 smelted kelp to go from level 27 to level 30.

In addition, kelp can be composted, giving an average of 1 bone meal per 23.33 kelp. Dried kelp works the same way, so it would be possible to smelt kelp for the experience, and then compost it.

## Mechanics
Kelp grows similar to sugar cane. One stem block can be placed underwater, and then it spontaneously grows upward until the top of the kelp is one block below the water surface. When kelp is planted or the plant above is broken, it sets a random age from 0 to 24, which determines the maximum height the kelp is able to reach. When kelp grows, the plant adds 1 to the age from below. A kelp plant stops growing at age 25. This means that a kelp plant can grow between 2 and 26 blocks tall.

Kelp has a 14% chance of growing each random tick. This means that there is a 50% chance for the kelp to grow in the first 4.6 ticks, a 75% chance for it to grow within 9.19 ticks, and a 25% chance for later growth. For information on random tick timings, see block tick.

Gnembon kelp mechanics


Bone meal can be used to speed up the growth of kelp. One bone meal grows kelp by one block.

Additionally, the maximum growth of a kelp plant may be reset to the current height of the plant, hindering any further growth. Not even bone meal can make a kelp plant grow again if the maximum height becomes reset to current height.

### Experimental testing
Based on testing, a 20×20 square of kelp (400) down results in a rough 50% gain over the course of 1 minute, or about 600 kelp. This does not mean that half of the kelp grows 1 block; the random nature of the growth creates a negative logarithmic curve of how many plants reach certain heights. (L shaped curve)

Here is the results from a 256 kelp test over a period of 1 real-life minute (1,200 ticks)
All kelp were made to be less than age 20 for the trial, so age did not matter as none grew to 6 tall.

| Category                        | Data     |        |        |       |       |
|---------------------------------|----------|--------|--------|-------|-------|
| Height Of Kelp                  | 1        | 2      | 3      | 4     | 5     |
| Number Of Times Grown           | 0        | 1      | 2      | 3     | 4     |
| Number Of Kelp Plants           | 106      | 109    | 33     | 7     | 1     |
| Percentage of Kelp Plants       | 41.41%   | 42.58% | 12.90% | 2.73% | 0.38% |
| Percent that reached each stage | starting | 58.59% | 16.02% | 3.12% | 0.39% |

## Manual farming
Kelp can be manually farmed by placing kelp underwater, waiting for it to grow, and breaking it. Usually you want to break the block above the bottom kelp plant so as to allow continued growth. If you do not need a large amount of kelp, such as several double chests filled, it is possible that harvesting naturally grown kelp in the ocean is sufficient.

It is important to note that kelp may not always grow to max height due to the random age value mentioned above. As such, it may be desirable to harvest kelp more frequently to allow it to constantly grow. In Java Edition, this age value can be checked by pressing F3.

When harvesting kelp, you should swim down close to the base of the plants and sweep your view, breaking large amounts of kelp. Once you have broken a sufficient amount, swim to the surface to collect the items. Make sure to collect the items within 5 minutes before they despawn.

### Helpful equipment
Kelp only grows underwater, which creates some difficulties when trying to harvest. The difficulties can be alleviated through the use of the right equipment, however.

- Ahelmetenchanted withRespirationcan allow you to stay underwater for longer. Such a helmet allows for up to an entire minute of time underwater. ATurtle Shellhelmet would also be helpful as it allows you to instantly recover air when breaking the surface.
- Moving underwater can also be slow. This can be helped withbootsenchanted withDepth Strider. ARiptidetridentmay also be helpful. If mining out an area for a farm, you may also wantAqua Affinity.
- Some potions can also be helpful. A potion ofWater Breathingcan allow you to stay underwater indefinitely and a potion ofNight Visioncan allow you to see much better.
- A sword withSmitemay be helpful for fending offDrowned.
- UsingIceto create Water Sources with a Silk Touch Pickaxe is more convenient and effective than using water buckets to place water.

### Infrastructure
To help streamline the farming process, you can also build up the infrastructure within the farm itself.

- To increase visibility, you could light up the area withJack o'Lanternsorsea pickles.
- Constructing nearby air pockets allow the player to enter and replenish breath more easily.
- Aconduitis extremely helpful as it provides all players within a 32-96-block spherical range with water breathing and better vision. In addition, it also attacks nearby hostile mobs.

For the farm itself, you should probably clear out a large area and cover it with kelp. Ideally, make the area at least 25 blocks deep to allow the kelp maximum growth.

It is also possible to automate collection by placing flowing water at the top, flowing into hoppers. This can be tricky however, and the kelp must not be allowed to grow into the flowing water and break the stream.

