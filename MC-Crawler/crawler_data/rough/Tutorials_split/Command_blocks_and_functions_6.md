### Making a Store
By using /give @p[level=<level>..] <item> <amount> and /experience add @p[level=<level>..] -<level> levels you can make a shop system that trades a certain amount of exp for items. For instance, if you made a command block with /give @p[level=5..] grass_block 64 and another with /experience add @p[level=5..] -5 levels connected to the same redstone current, it will take 5 levels from the player, and in return, give them 64 grass blocks.

- Subtracting experiencecanwork as a currency, by using the command/experience add @p[level=3..] -3 levels. The minimum experience for the command to work can be listed inside the brackets.

Custom villagers selling whatever you want can be created with command blocks. Custom villagers are not available through Minecraft: Bedrock Edition. 
e.g.: /summon villager ~-2 ~0 ~0 {Profession:3,CustomName:BLACKSMITH,CustomNameVisible:0,Offers:{Recipes:[
{maxUses:13,buy:{id:388,Count:5},sell:{id:283,Count:1,tag:{ench:[{id:16,lvl:9},{id:20,lvl:6}],display:{Name:Molten Gold Sword}}}},{maxUses:13,buy:{id:388,Count:1},sell:{id:280,Count:1,tag:{ench:[{id:16,lvl:5}],display:{Name:Whuppin Stick}}}},{maxUses:13,buy:{id:388,Count:2},sell:{id:369,Count:1,tag:{ench:[{id:16,lvl:5},{id:20,lvl:10}],display:{Name:Radioactive Whuppin Stick}}}},]}}

The part labeled "Buy" is what the villager is accepting as payment, the part that says "sell" is what he's giving in return. You can change the maxUses to 1000 if you never want the offer to run out, or to 1 if you want to make it a one-of-a-kind item. Note that the first item there (the gold sword) has an out of range enchantment (sharpness 9). Yes this works, but always research what exactly the enchantment does before making an out of range one as some stuff does nothing or even does negative effects (respiration's "see underwater" side effect makes everything a blinding white at high levels, as if you dove into slush-filled arctic waters). As for that gold sword, keep in mind that gold swords wear out insanely fast (there's a reason people call them butter swords after all). A level 10 Unbreaking enchantment should bring a gold sword up to a decent durability level. Also notice that the other 2 "weapons" are actually a Stick and a Blaze Rod with weapon enchantments on them. Using any non-weapon as a weapon does the same damage as an empty hand (1 damage, aka half a heart) but the enchantments on these ones make them the equal of an unenchanted sword. The advantage is that sticks, blaze rods, or other items is that you can use it infinitely. The same trick can be used with mob heads and respiration 3 to make an infinite durability scuba mask.

## Spawners
Command blocks can create spawners using the /setblock command, e.g.: /setblock ~1 ~-1 ~0 spawner{SpawnData:{id:zombie,HandItems:[{id:iron_sword,Count:1}]}} Anything that counts as an entity can be spawned (except a player), which includes all mobs, as well as minecarts, fireballs, arrows, snowballs, ender pearls, custom thrown potions, fireworks, primed TNT, falling sand, red sand, or gravel, paintings and item frames, experience orbs, and even dropped items of any type. 

Pig, cow, or chicken spawners can be placed in the butcher's backyard in a village to create a constant meat supply. E.g.: /setblock ~1 ~-1 ~0 spawner{MaxNearbyEntities:10,RequiredPlayerRange:16,SpawnCount:6,SpawnRange:2,MinSpawnDelay:50,MaxSpawnDelay:200,SpawnData:{id:pig,Passengers:[{id:chicken}]}} Note that the spawner in the last code example will spawn a chicken riding a pig. There doesn't seem to be a limit to how many levels of riders you can use. For example, you could create a chicken riding a pig riding a cow riding a horse riding a silverfish riding a villager ("Say, that's a mighty odd hat you have on, Farmer Brown"). 

Please note that if you want to use the RequiredPlayerRange tag you have to use the MaxNearbyEntities tag as well. The same thing applies to MinSpawnDelay and MaxSpawnDelay. Lastly, note that the y value used in both of those spawner example codes was ~-1, which (assuming the player are not flying) will put the spawner in the surface level of the ground at your feet.

If you don't want to target a specific player, you can use @a, @p, or @r instead of <player>. Keep in mind that you can use @p (which means closest player) in player issued commands as an easy to type 2 character replacement for your own name as the closest player to you will always be you.

#### Part 1: The Basics
This code will create a zombie spawner 2 blocks from you in the x direction. Note that the name given for mob spawners in this code (minecraft:spawner) is the long version and you can leave out the minecraft: part.

/setblock ~2 ~0 ~0 minecraft:spawner{SpawnData:{id:zombie}}

This next code is also pretty basic but it includes the 6 basic parameters that can be set.

/setblock ~0 ~-1 ~-3 spawner{SpawnRange:4,RequiredPlayerRange:16,SpawnCount:4,MaxNearbyEntities:6,MinSpawnDelay:200,MaxSpawnDelay:800,SpawnData:{id:skeleton}}

Notes:

- All times are in game ticks (20ths of a second). 200-800 is 10–40 seconds.

- Keep in mind that they are in groups of 2 and won't work if their partner is missing. SpawnRange requires RequiredPlayerRange (and vice-versa), MinSpawnDelay requires MaxSpawnDelay, and assuming SpawnCount needs MaxNearbyEntities.

- There is also a parameter called "Delay" which contains the amount of time before next spawn (20 ticks for the first time, whatever random number it picks between MaxSpawnDelay and MinSpawnDelay every other time).

- The coordinates given are ~0 ~-1 ~-3 (so 3 blocks in the negative Z direction from the commandblock's current position and 1 block down). This presumably will imbed it in the surface of the floor. Keep in mind that a spawners "SpawnRange" setting only applies horizontally not vertically. Vertically it will only spawn at the same height or 1 lower or higher, so imbedding it in the surface of the floor cuts the available spawn area by 2/3rds (but can help hide it). Naturally occurring spawners have their height cut by 1/3rd due to appearing 1 block above the floor instead of 2.

- All the values used here are the defaults.

#### Part 2: Custom monsters
The next thing to do is to modify the spawn data. Spawn data is what tells the spawner you want a non-standard version of a monster, such as a zombie with a diamond sword and a chain helmet.

/setblock ~ ~1 ~ spawner{SpawnData:{id:zombie,HandItems:[{id:diamond_sword,Count:1}],ArmorItems:[{},{},{},{id:chainmail_helmet,Count:1}]}}

Using ~ without any number after it in the coordinates counts as zero. Because of the fact that none of those 6 parameters from the last example are used, they will all be defaults.
Note that there are now two types of item slots, Hand and Armor. Hand items are in the order Mainhand, Offhand, while armor items go in the order Boots, Legs, Chest, Helmet. You must even specify empty slots (the { }, parts), unless they're after the last non-empty slot. So, if you want your custom mob to have a helmet, you have to specify all 5 slots, but if it's just boots, you can leave off the other 3. Likewise, if you want them to have leg armor. you have to specify the boot slot, but not chest and helmet slots.
Remember that creatures that burn in sunlight are safe if they have a helmet on, although it damages the helmet instead.
As for the count tag, most codes can get away with leaving it out; however, it is important. An item without a count tag is a stack of zero, better known in the community as a "Ghost Item". A player trying to use a ghost item will have it disappear out of their hands with its first use (which is a failure). While monsters can use ghost items without problem (hence why codes get away with leaving it out sometimes), if they drop the items the player who picks it up won't be able to use it, so it is highly recommended to use the count tag.

The next example of customized monsters, consists of a skeleton with an enchanted bow (Flame) with a custom mob head (Spider, internet connection required or it's just Steve) with Protection 2 riding a Skeleton Horse.

/setblock ~2 ~1 ~2 spawner{SpawnData:{id:skeleton_horse,Tame:1,Passengers:[{id:skeleton,HandItems:[{id:bow,Count:1,tag:{Enchantments:[{id:flame,lvl:1}]}}],ArmorItems:[{},{},{},{id:player_head,Count:1,tag:{Enchantments:[{id:protection,lvl:2}],SkullOwner:MHF_Spider}}]}]}} replace 

As of 1.12, passengers can control their mounts to an extent, which means that former issues with Zombie passengers are no longer extant. A more in-depth look at the behavior of passengers and mounts can be found at Tutorials/Summoning Jockeys. 
The skeleton horse has Tame set to 1 (yes). Note that there is currently an ongoing bug where summoned mobs riding horses with saddles cannot move, regardless of whether the horse is tame. Technically you can have multiple levels of riders, although this gets silly quickly.

