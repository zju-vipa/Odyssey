#### Part 3: SpawnPotentials
Using the SpawnPotentials tag, you can create a mob spawner with multiple mobs in it. It will randomly pick one each time when the timer is reset (a second after spawning the previous mobs). Since these codes contain multiple mobs, they tend to be quite long codes. Here's a version of the SpawnPotentials code, that is easier on the eye:br>

/setblock ~ ~1 ~1 spawner{SpawnRange:6,RequiredPlayerRange:12,SpawnCount:1,MaxNearbyEntities:6,MinSpawnDelay:100,MaxSpawnDelay:600,SpawnData:{id:"zombie",HandItems:[{id:"wooden_sword",Count:1},{}],ArmorItems:[{id:"leather_boots",Count:1},{id:"leather_leggings",Count:1,tag:{display:{color:5013401}}},{id:"leather_chestplate",Count:1,tag:{display:{color:6717235}}},{id:"player_head",Count:1,tag:{SkullOwner:Reimac}}]},SpawnPotentials:[{Entity:{id:"zombie",HandItems:[{id:"wooden_sword",Count:1,tag:{Damage:58}},{}],ArmorItems:[{id:"leather_boots",Count:1},{id:"leather_leggings",Count:1,tag:{display:{color:5013401}}},{id:"leather_chestplate",Count:1,tag:{display:{color:6717235}}},{id:"player_head",Count:1,tag:{SkullOwner:Reimac}}]},Weight:4},{Entity:{id:"skeleton",HandItems:[{id:"iron_sword",Count:1},{}],ArmorItems:[{id:"leather_boots",Count:1,tag:{display:{color:1644825}}},{id:"leather_leggings",Count:1,tag:{display:{color:1644825}}},{id:"leather_chestplate",Count:1,tag:{display:{color:1644825}}},{id:"player_head",Count:1,tag:{SkullOwner:2insanepeople}}]},Weight:2},{Entity:{id:"zombie",HandItems:[{id:"stone_sword",Count:1},{}],ArmorItems:[{id:"chainmail_boots",Count:1,tag:{Enchantments:[{id:"protection"}]}},{id:"chainmail_leggings",Count:1,tag:{Enchantments:[{id:"protection"}]},{id:"chainmail_chestplate",Count:1,tag:{Enchantments:[{id:"protection"}]},{id:"player_head",Count:1,tag:{SkullOwner:Flixnore}}]},Weight:4},{Entity:{id:"zombie",Fire:2400,HandItems:[{id:"golden_sword",Count:1,tag:{Enchantments:[{id:"punch",lvl:1}]}},{}],ArmorItems:[{id:"golden_boots",Count:1},{id:"golden_leggings",Count:1},{id:"golden_chestplate",Count:1},{id:"carved_pumpkin",Count:1,tag:{Enchantments:[{id:"protection",lvl:2},{id:"fire_protection",lvl:10}]}}]},Weight:4},{Entity:{id:"zombie",HandItems:[{id:"iron_sword",Count:1,tag:{Enchantments:[{id:"sharpness",lvl:2}]}},{}],ArmorItems:[{id:"iron_boots",Count:1},{id:"iron_leggings",Count:1},{id:"iron_chestplate",Count:1},{id:"player_head",Count:1,tag:{ench:[{id:0,lvl:2}],SkullOwner:2zqa}}]},Weight:4},{Entity:{id:"zombie",HandItems:[{id:"diamond_pickaxe",Count:1,tag:{Enchantments:[{id:"sharpness",lvl:4},{id:"knockback",lvl:4},{id:"bane_of_arthropods",lvl:4},{id:"looting",lvl:3},{id:"unbreaking",lvl:3}]}},{}],ArmorItems:[{id:"diamond_boots",Count:1,tag:{Enchantments:[{id:"fire_protection",lvl:4},{id:"feather_falling",lvl:4}]}},{id:"diamond_leggings",Count:1,tag:{Enchantments:[{id:"blast_protection",lvl:4}]}},{id:"diamond_chestplate",Count:1,tag:{Enchantments:[{id:"protection",lvl:4}]}},{id:"player_head",Count:1,tag:{SkullOwner:MHF_Herobrine,Enchantments:[{id:"protection",lvl:4},{id:"fire_protection",lvl:4},{id:"blast_protection",lvl:4},{id:"thorns",lvl:3},{id:"respiration",lvl:1}]}}],CustomNameVisible:1,CustomName:'"Herobrine"',PersistenceRequired:1},Weight:1}]}
It contains a lot of codes, because of the fact that it is actually 6 separate mobs. In order we have:

- Before the "SpawnPotentials" tag: The starter, which will never pop up again after the first time. If you want to see him again, you have to include him a second time under SpawnPotentials. Its appearance is just a random person in blue jeans (blue dyed leather leg armor), and a green dye shirt (green dyed leather tunic), with a wooden sword. He's a zombie under that mob head of it, of course.
- Same thing, only this time, the wooden sword is 2 hits away from breaking.
- The next one has a ninja-like appearance. This one is a skeleton under its mask, but he's been given an iron sword. All of its leather armor is dyed ninja-black. Skeletons with swords close the gap quicker than zombies, so watch out.
- Zombie with a stone sword and chain armor, with Protection II on its mob head.
- The next one has a gold sword, golden armor, a pumpkin on its head, and he's on fire! The pumpkin is enchanted with Protection II and Fire Resistance X in a desperate attempt to keep him on its feet and threatening the player for more than 5 seconds. It works, but if the player plays keep away then the zombie does tend to burn to death. Its sword has fire aspect too.
- Iron Sword and Armor. Sharpness II on its sword, Protection II on its mob head.
- The final mob, fakeHerobrine, here has highly enchanted diamond armor (boots with Fire Protection IV and Feather Falling IV, leggings with Blast Protection IV, a chestplate with Protection IV, a mob head with Protection IV, Fire Protection IV, Blast Protection IV, Respiration III) and a diamond pickaxe enchanted with Sharpness IV, Smite IV, Bane of Arthropods IV, Looting III and Unbreaking III. Its also got the previously unseen CustomNameVisible (set to 1 for yes), a CustomName, and PersistenceRequired (set to 1 for yes). That last one will prevent it from ever despawning, although it can be killed normally. If you can get through that diamond armor and level 4 resistances.

Other than the ninja, it's a straight tour of the 5 tiers of swords and armor. Note that the Weight tag, used right after the Entity tag in each SpawnPotential. That determines how rarely it's picked. Specific numbers don't mean anything, just the ratios between the numbers. For example, if you want all the potentials to have an equal chance just set all the weights to 1. Changing them all to 8 wouldn't do anything different (they're still all the same size as each other), however, changing all but one to 8 would make that one 1/8th as likely as the rest. In this code, 4 is the default. The ninja only has a weight of 2 (making him half as likely to be picked) and fake Herobrine has a weight of 1 (making him 1/4th as likely to be picked, and thank god!)

#### Part 4: Rideable Monsters
Mobs can be ridden by using Minecarts or Boats on their heads. The command is fairly simple:

/setblock ~ ~1 ~ minecraft:spawner{SpawnPotentials:[{Entity:{id:"<Entity>",Passengers:[{id:"minecraft:minecart"(or "minecraft:boat")}]}}]}

Tips: 

- Bosses can also be spawned with a spawner. Adding aminecartis also possible.
- Hostile mobs with shooting abilities can and will use them against survival players. Watch out.
- Although the minecart would stuck in their head,ghastscan also be ridden. However, you may need anelytraor atridentenchanted with riptide to do that.
- Endermencannot be walked around, but they can be forced to teleport by shooting a projectile at them (e.g.; snowball).
- Ocelotsare some of the fastest mobs to ride, seeing they're trying to get away from you. They can also be partially controlled, by pointing away from the place you want to go.
- Spidersare the only mobs that slow down when ridden.
- Slimesand their Nether cousins,magma cubes, can have their sizes changed.

## More commands in fewer command blocks and recursion
There are several ways to combine groups of commands into just one command.

Use the following sets of commands for recursion:
/scoreboard objectives add counter dummy
/scoreboard players set target_count counter <target count>
/execute if score count counter < target_count counter <chained command>
/execute unless score count counter < target_count counter run scorebard objectives remove counter
/scoreboard players add count counter 1

To run multiple commands, summon a command-block minecart riding another command-block minecart riding another, with the commands in reverse order, on an activator rail. There are also commands called one-command tool that use this tactic.

## Using a map item as a scroll
A YouTuber called SethBling used a map as a scroll to perform commands (summon creatures, teleport). The player will have an empty map in the inventory and when the player uses it, it becomes a filled map which immediately disappears and a redstone task is done.

Pros

- Fast redstone interaction.
- Compact system.
- At-will triggered system, just right-click to activate it.
- Single use: the map disappears during the inventory check, but you can give it back through/give.

Cons

- There can only be one purpose for the scroll, i.e. players cannot do a scroll of teleporting and a scroll of strength without using complicated data values.
- The player may see the map animation when activating the map before it gets deleted.
- The player cannot use the map item during your playthrough (showing a text message, a path, a drawing, …).

Building the mechanism

The player can change the display name of an item to give the player a better understanding of the object and use the tooltip display. Use the following command to give the player a custom named map:
/give <player> map{display:{Name:"<displayName>",Lore:["<tooltip>"]}}

- player: the player you want to reach (@p, @a[arguments],...).
- displayName: the name displayed when you scroll in the hotbar or when you hover the item with your mouse.
- tooltip: the text below the item name when you hover it.

Detecting the activation of the map



- The two hoppers form a redstone clock. You can use other clocks shownhere.
- The Command block 1 contains the/givecommand described in the section above. It can be dismissed if the player doesn't want the scroll to come back after being activated.
- The Command block 2 contains the inventory check command:

/clear <player> filled_map

- The Command block 3 is the output in case of success. You can do whatever you want: give an effect to the player, teleport him somewhere,... You can also wire this output to a door, a piston,...

Going further
The /clear command can check for other interactive items:

- Check for aglass bottleif the player just drank a potion.
- Check for afishing rodwhen the line is reeled in. The/clearsyntax involves another argument, the damage value, after the item name:

/clear <player> fishing_rod{Damage:2}
Note that spamming the reel, or hooking a mob, may damage it more than 2, so make another one of these every 2.

