# Tutorials/Traps
Traps are a common mechanism in multiplayer built by players to kill other players or mobs automatically. The following is a list of basic traps with a short tutorial that often assumes the reader has a working understanding of the basic concepts required to build the trap. Most traps are considered to be mechanisms, though some are not classified as such.

## Contents
- 1 Video
- 2 Overview
- 3 Trigger components
	- 3.1 Pressure plates
		- 3.1.1 Wooden
		- 3.1.2 Stone
		- 3.1.3 Light-weighted
		- 3.1.4 Heavy-weighted
	- 3.2 Observers
	- 3.3 String
		- 3.3.1 Tripwire hook
	- 3.4 Button
	- 3.5 Daylight sensor
	- 3.6 Lectern
- 4 Mechanism components
	- 4.1 TNT
	- 4.2 Pistons
	- 4.3 Dispensers
	- 4.4 Nether Portals
	- 4.5 Mobs
- 5 Explosive traps
	- 5.1 Lectern info bait
	- 5.2 Trick house trap
	- 5.3 Warehouse trap
	- 5.4 End portal trap
	- 5.5 Bog-standard landmine
	- 5.6 Instant landmine 1
	- 5.7 Instant landmine 2
	- 5.8 Instant landmine 3: Sculk proximity jubilee
	- 5.9 Tree trap
	- 5.10 Cake trap
	- 5.11 Death temple
	- 5.12 The hidden house
	- 5.13 TNT floor house
	- 5.14 Explosive house
	- 5.15 C4 trap
	- 5.16 Exploding furnace
	- 5.17 Inescapable arrow trap
- 6 Pitfall traps
	- 6.1 Sand trap
	- 6.2 Fence trap [verify]
	- 6.3 Chest pitfall [verify]
	- 6.4 Painting trap
	- 6.5 Fake chunk error
	- 6.6 Fake water pitfall
	- 6.7 Snowball trap
	- 6.8 Piston pit
	- 6.9 Fake elevator
	- 6.10 False-floor trap
	- 6.11 False door pit
- 7 Water traps
	- 7.1 Fake water elevator
	- 7.2 Retrieval trap
	- 7.3 Whirlpool trap
	- 7.4 Pufferfish pit
- 8 Lava traps
	- 8.1 Lava staircase trap
	- 8.2 Chest lava trap
	- 8.3 Lava pit
	- 8.4 Lava door
	- 8.5 Trapdoor lava pit
	- 8.6 Lava filler
- 9 Capture traps
	- 9.1 Curiosity trap
	- 9.2 Piston trap
	- 9.3 Door trap
	- 9.4 Shallow pitfall
	- 9.5 Trapping pool
	- 9.6 Slime trap
	- 9.7 Quicksand
	- 9.8 Netherite block live-capture trap
- 10 Piston traps
	- 10.1 Crushing trap
	- 10.2 Honeycomb trap
	- 10.3 Cake trap
	- 10.4 Pitfall trap
- 11 Manual traps
	- 11.1 Grave digging
	- 11.2 Facebreaker trap
	- 11.3 Ore tower
	- 11.4 Return home to a potion of instant damage II
- 12 Other traps
	- 12.1 Spike trap
	- 12.2 Slow monologue trap
	- 12.3 Falling minecart [verify]
	- 12.4 Magma carpet trap
	- 12.5 Anvil trap
	- 12.6 Command mine
	- 12.7 Arrow trap
	- 12.8 Murder holes [verify]
	- 12.9 Spider trap
	- 12.10 Wither rose field
	- 12.11 Fake base 1
	- 12.12 Fake base 2
	- 12.13 Big spiky fish
	- 12.14 It came from the sky
- 13 Triggers
	- 13.1 Trapped ore 1
	- 13.2 Trapped ore 2
	- 13.3 Trapped ore 3
	- 13.4 Redstone mine
	- 13.5 Furnace trap
	- 13.6 Minecart mine
	- 13.7 Wrong lever
	- 13.8 Exploding bed
	- 13.9 Invisible tripwire [verify]
	- 13.10 Chest bomb
	- 13.11 Fishing trap
	- 13.12 Proximity detector
- 14 Lures
	- 14.1 Dropped loot
	- 14.2 Signs
	- 14.3 Chests
	- 14.4 Ore blocks
	- 14.5 Fake mineshaft
	- 14.6 Iron door
- 15 Disarming traps
- 16 See also
- 17 References

## Overview
Traps are devices designed to trap or damage entities, often referred to as targets. Traps are often made up of 3 components: A lure, a trigger, and the damage source. In a simple landmine, the lure could be a base behind the landmine, the trigger a pressure plate, the damage source TNT. Not all traps have a lure, they may rely on chance or something else to lure the target. Feel free to add any ideas of traps you have here. Just follow the style guide and everyone will have new strategies to remove their enemies.

A list of components for a good trap can be seen below: 

## Trigger components
These components are a trigger that allows the rest of the trap to work.

### Pressure plates
Pressure plates are commonly used to detect whether an entity or item presses on it . There are 4 variants (viz.wooden pressure plate, stone pressure plate, light-weighted pressure plate, and heavily weighted pressure plate.)

#### Wooden
Wooden pressure plates measure all entities and give out maximum signal strength. The most commonly used pressure plate. Useful if you want to detect anything including items being thrown. Works best when paired with an observer.

#### Stone
Stone pressure plates measure only players and mobs and give out maximum signal strength. The second most commonly used pressure plate. Useful if you want to detect only a player or mob. Works best when paired with an observer.

#### Light-weighted
Light-weighted pressure plates measure all entities, and the strength increases as more entities are added. Useful if you want to detect a specific number of entities. Works better with only redstone dust if the pressure plate is for detecting entities and not players.

#### Heavy-weighted
Heavy-weighted pressure plates are similar to a light weighted pressure plate but they measure groups of 10 entities per redstone comparator output.

### Observers
Observers are most commonly used to detect whether a block state changes (ie: an ore trap). They are useful if you want to kill someone destroying a block in your base, a TNT lighting, redstone getting activated, containers being opened, furnaces turning on or off, etc.

### String
String, when connected to a pair of tripwire hooks or an observer, can detect when a player/mob steps through it or breaks it. It is also difficult to see.

#### Tripwire hook
When a player/mob/item comes in contact with a string connected to 2 tripwire hooks, it will output a redstone signal.

Pros:

- Can detect all entities
- Wide range of detection

Cons:

- Hooks can be seen easily when placed on a wall
- String connected to it can be broken withshearswithout outputting a signal

### Button
When a button is pressed, it outputs a redstone signal. Useful for redstone control rooms.

### Daylight sensor
It detects the 'time' of Minecraft day. It can be right clicked to detect sun or moon. Shadow affects this, however, so if you set it to detect sun, and it is in direct sunlight, a redstone signal will be produced, at a power level relating to the height of sun or moon. If it was in shadow, it would not produce any signal, and vice-versa for moon mode. Useful for hourly traps and such, though redstone clocks are more precise but also expensive. 

It has no effect on adjacent opaque blocks.

### Lectern
The lectern can hold books. It emits a redstone signal power depending upon the page of the displayed book. Useful when you want to tempt someone with important information, and blow them up as soon as they start reading a particular page.

## Mechanism components
These components actually affect the target.

### TNT
Of course, that's obviously coming to your mind first. TNT traps are ubiquitous and common. Most like the landmine (involving a pressure plate and some TNT) are easy to make; others like the TNT floor house are harder and more expensive. TNT traps have many triggers; from pressure plates to observers to pistons to dispensers...and more!

### Pistons
Pistons are often used, for example, to push a player into lava, push someone into a pressure plate, push someone into a block and suffocate them, and more. They are often used in some capture traps to continuously keep a player out of an area.

### Dispensers
Dispensers can be used to shoot out deadly objects like Potions, Arrows, Tipped Arrows, Fire Charges, Lava, etc.

Don't ever put diamonds in a dispenser unless you are trying to lure someone, or else they will just become rich off your trap

### Nether Portals
Nether Portals can be used to make traps upon entering The Nether. They pause chunk generation, witch means you light TNT in the Overworld over a Nether Portal, then light the portal. as long as there is no chunk generator (Machine That Uses A Minecart In A Nether Portal To Load Chunks) or players in the nether, you, upon entering the nether, will be blown up.

### Mobs
Mobs, like Zombies, Skeletons, Witches, Ravagers, Creepers, Iron Golems, Zoglins, Vindicators, Piglin Brutes and Pufferfish can deal damage to players. To prevent mobs inside of traps from despawning, one should use Name tags. Each mob has their own pros and cons:

- Zombies—Most common mob to obtain and quite flexible, but can be killed easily. Burns in sunlight.
- Skeletons—Ideal for long-range traps without hiding spots, like long hallways and corridors. Slow rate of fire and no melee damage makes them ineffective for smaller traps. Burns in sunlight.
- Witches—Splash potions are effective against weaker victims, and they have a large area of effect. Self-healing ensures longevity. The unpredictability and inconsistency with the types of potions thrown makes them ineffective at killing victims.
- Ravagers—Powerful and deals significant knockback. The large hitbox of the Ravager can make them difficult to contain.
- Creepers—Deals explosive damage. In Survival, the difficulty of transporting them and the one-time use of Creepers makes them an awful choice compared to simple and effective TNT.
- Iron Golems—Powerful. Can be repaired/healed withiron ingots. Only attacks if it is attacked first.
- Hoglins/Zoglins—Powerful. Attack almost anything and everything they see. They can be difficult to transport out of the Nether due to their fear of Nether Portals.
- Vindicators—High damage output. Attack all mobs exceptghastsandillagersif renamed to "Johnny". Has a short attack range.
- Piglin Brutes—Deal the same amount of damage as vindicators. Convert into a normalzombified piglinsupon leaving the Nether.
- Pufferfish—Moderate damage, inflicts poison. They can be picked up in buckets and placed by dispensers.

## Explosive traps
The traps here primarily use TNT to cause harm to the target. When testing explosive traps it may be a good idea to use a different block such as the redstone lamp, which like TNT, is triggered by redstone but it is less likely to accidentally blow up prematurely.

### Lectern info bait
Lecterns can hold books, therefore, you could give a hint to someone about some important info, and set it up so as soon as they reach the sixth page maybe, the doors close, and TNT blows up the place. Don't set it to explode at the first page, they would go through the first few pages cautiously, and then feel safe, only to find out while they are reading the most important page, TNT removes them from the Minecraft world.

### Trick house trap
This is a trap that can be used to catch someone while they are out adventuring. You place TNT at various points around their house, prioritizing spots which are behind an input like a button or likely to be set alight by an unsuspecting player, like behind an empty fireplace. To finish it all off, place a few pressure plates near their bed with TNT underneath. If the player dies and respawns, they would spawn on top of the pads and cause an easy kill. Keep in mind that some servers would consider this sort of behavior cheating or griefing.

### Warehouse trap
This trap takes a long time to make but the payoff is worth it. make a big warehouse, about 50x50 for best results. underneath the floor add TNT in a checkerboard pattern.

next, you add a 15 second redstone repeater delay set to a pressure plate on the enterance. when the target enters this warehouse to steal your items.

The TNT underneath them slowly ignites, exploding the warehouse and anything in it. leaving no time to escape.

### End portal trap
If you have enough TNT, a dispenser, and an input, it can't hurt to pump some TNT into the End Portal. The TNT will go to the spawn point of the world and will be loaded, as the spawn chunks are always loaded, and will explode soon after. If nobody is in the end, the first player enter the portal will make the chunks load, which will instantly kill that player.

### Bog-standard landmine
This landmine by itself is inefficient and non-lethal. It damages the landscape and deals little if any damage to players. It is easy to make by placing a pressure plate on a block and one or more TNT directly beneath. Stepping on the pressure plate will ignite the TNT To make it more efficient, there are many variations players can use:

- If you want to protect the landscape, you can place 2 water sources at the bottom of the hole. Place a slab at the bottom as sand/ gravel may quench the water source. This method will reduce the dealt damage, however.
- This is well disguised next to adoor; the player may think it is to open the door.
- By digging a pit underneath it, the player might fall into it.
- Try to camouflage the landmine by making it less noticeable, e.g. grow tall grass around it.
- Concrete powder cannot be used in this design, the concrete powder will harden into concrete upon contacting water and quench the water source.


### Instant landmine 1






































Side view
TNT, when activated normally, plays an audible hissing sound and waits for a few seconds before blowing up, which can give anyone plenty of time to escape a landmine placed on the ground. A much more dangerous landmine with instant activation can be built instead:

1. Dig a 3×3×3 hole in the ground, jump in, and stand on a corner.
2. On the center, place a block of dirt and arailon top of it.
3. On the rail, place aminecart with TNT. Be careful not to push it.
4. Destroy the block under the rail to derail the minecart. The minecart will fall one block lower, this won't really cause any damage unless you accidentally pushed the minecart.
5. Put adispenserwithflint and steelabove the minecart like shown.
6. Surround the minecart with TNT, cover it all up, and place apressure plateon top.


### Instant landmine 2






































Side view
Replace the wool with an end crystal, and put an arrow in the dispenser.
when the dispenser is activated, it will shoot an arrow and blow up the crystal, leaving no time to escape.




### Instant landmine 3: Sculk proximity jubilee





ESC










































Top view for the Sculk Proximity Instant Landmine. Design by DialgaTheTimeLord, aka LeopardBunny.
Sculk Proximity Instant Landmine construction process.
This one's a bit tricky to build. It requires both precise placement of TNT minecarts and extreme care not to set the trap off yourself. Do everything in order and make liberal use of the Sneak key and you'll be fine. Probably. Test it several times in Creative Mode just to be sure.The top row has an empty space labeled with ESC. This is your escape route.

First dig a hole 2×2 wide and 3 deep. Seal off the top with matching blocks. Surround the hole with a 2 block high wall of wool, leaving a Steve-sized gap for your escape route. Do not fill it back in yet. In the spot where you left the gap, dig out an escape route leading directly away from the mine. Return to your wool pit. Place two powered rails (keeping them unpowered) along the wall opposite of your escape route (you do NOT want the TNT carts in the way of your escape). Here's where things start to get tricky. You need to place at least two TNT carts on the same powered rail. The trap will not work otherwise. Placing the first will of course be easy. For subsequent carts, you will need to right click carefully on the side hitbox of the track that the first cart is on. The top will not work, as the first cart is in the way. You'll know it worked if the minecart's shadow gets noticeably darker, or know, if your hand empties. Once you find the right spot, feel free to place as many TNT carts as you care to sacrifice. More carts means a bigger, more powerful explosion, and significantly less chance of escaping the blast (though it's not much of a chance to begin with). Just make sure not to bump the carts. Now is where things go from tricky to deadly. One wrong move will make you the victim of your own trap. This is when you hold Shift like your life depends on it, because it absolutely does. While holding Shift and not letting go, place the sculk sensor, either adjacent to or in front of your escape hole. Now, still holding Shift, sneak your way into your escape hole. This is where you finally close the gap in the Steve-sized wool wall hole, making sure there is no hole for the Sculk Sensor to hear you through. You should be safe by this point, but if you want to be extra careful, continue sneaking as you move away from your newly planted mine.



That should be it! Just whatever you do, do NOT step over your landmine. You will almost certainly die. Save the dying for the enemy. It's also worth noting that currently in 21w06a, carpets do not muffle sound, unlike full wool blocks, which makes this an effective floor bomb, easily concealed under a rug. However, there's a decent chance that this may change in the full release of 1.17.


### Tree trap
























The tree trap
When the player chops down the tree, the TNT will be lit by the observer. The observer can be replaced by a lever and a NOT Gate if you are short on quartz.                          

How to Build an Exploding Tree Trap by Bugo03. Uses a NOT Gate for all of you who are low on quartz.

### Cake trap
























Replace the slab with cake. Replace the dirt with any block.
You eat the cake, you explode! In this trap when you eat the cake, the observer senses the update in the cake and ignites the TNT. 1) Dig down 2 blocks. 2) Place the observer at the bottom. 3) On top of the observer place a cake. 4) under the observer place the TNT.

If you place before the TNT you'll explode.


### Death temple
























Replace sand with sandstone.
Create BUD underneath the pressure plate in a desert temple. If a player should try to disarm it, KABOOM! Note that if you use the observer, players might be able to detect it, since the pressure plate won't cover it completely.


### The hidden house
























TNT field trap
This trap is the opposite of a TNT door trap: The TNT is obvious, while the house is hidden. Make a field of TNT extending about 5 blocks into the ground. Place signs all over the field saying: "Find my hidden house." It lures people in twice: the TNT danger, and the hidden house challenge. The problem is that there is no house! Beneath the field are pressure plates which ignite the TNT, leaving no time to escape, as you are in a field of TNT 5 blocks under.


### TNT floor house
Blow up a fake base and kill assassins attacking you! (this can also be used for demolition)

1. Build a base, preferably a half-hidden one, as not to arouse suspicion.
2. Make the floor withTNTand put some carpet on it to look like a normal decorated house.
3. Have an iron door as the entrance, with a pressure plate to open it. Redirect the pressure plate toward the base.
4. Below, place a block of TNT, but an extra step you can take is to have a circuit which delays the fuse using repeaters so the target won't retreat as soon as they hear thehisssof the TNT.

If any enemy, mob or player steps on the pressure plate (potential griefers included), they will be blown sky-high!


### Explosive house
Griefers love blowing and burning people's houses up. This trap turns the grief onto the griefer.

1. Make a decoy house out ofwoodand possiblywool.
2. Fill the area under it with TNT and make some "rays" of TNT extend from the house.
3. If a griefer happens to burn the house down, they will probably get a bit more of a bang than they expected!

If you use this for demolition (that is, if you have any fragile buildings to be destroyed), you can set it and wait for somebody else to do the work for you by setting it off unknowingly.


### C4 trap
The "C4 trap" is a vertical or horizontal stack of TNT with a button wired to a dispenser with a fire charge in it. The dispenser is placed one block above or below the stack (vertical) or one block next to the stack (horizontal). This usually works better for demolition than for a trap. If you want to use it as a trap, wire a pressure plate to the dispenser. This works similarly to a flaming arrow hitting a stack of TNT from above. This works better than a dispenser shooting TNT, because the "C4" stays in one place. Also, if only two TNT blocks are used, it works well as a disposable cannon, even better on obsidian blocks, but not in a tube. All evidence of the trap is usually destroyed. Note: C4 trap from below does not work well.

### Exploding furnace
Want a big unexpected boom? Have a bunch of spare furnaces? You need a Redstone comparator, TNT, a furnace and something to smelt. Place the furnace, and then put the comparator directly behind it. Then, just put the TNT behind the comparator and wait till someone smelts something!

An alternative is to put coal, iron, or food in a furnace and add a redstone comparator behind linked to a not gate. Use the not gate to trigger some tnt. Also hide observers under the furnace so people can't break it.

### Inescapable arrow trap
Like to kill your fellow players with protection IV armor? You need many harming II arrows, a bow, soul sand, and water. Use the water and soul sand to make a bubble column, then shoot arrows into the pit until you run out. It will instantly kill anyone that falls in! Just don't fall in yourself.

## Pitfall traps
These traps primarily use fall damage to harm the target. Some minor variation can make a simple pit much more deadly.

- Make checkerboard pattern ofcactiat the bottom of a pit. Cacti does destroy items, though.
- To effectively improve the size of your pit without digging a larger area, dig a shallow ring around the top layer of your pit. Fill this area withwaterso that mobs will be dragged to the center. Note that this will reduce fall damage.

### Sand trap


























































Sand trap
When the target walks on top of the trap, break the bottom block of sand. It is a good idea to disguise the trap by making a house on top of the sand. If you do this, you will probably want to put in carpet so as to not make it so obvious. Some variations:

- You may be able to get the target to break the sand themselves by making the bottom block valuable.
- You can automate the trap by attaching apistonto the bottom block of sand. If you want to retract the piston when apressure plateis pressed, use aNOT Gate. You could also use an observer and a piece of bait to lure in any players wanting a piece of that[whatever valuable block you placed].

### 
Construct a hallway. A diagonal hallway works best. Fence posts should be underneath the path and you should drop the sand or gravel for the floor on the fences. Below the fences, you can have a pit.

This works because when a gravity-affected block falls on a fence post, the block stays as an entity. As a result, a player walking between the fence posts will fall through the sand entities, causing them to plummet. Diagonal hallways make it more likely to fall through the sand without landing safely on a fence post. Keep in mind that the sand is going to look half a block higher than a normal block, but this can easily be covered up. The best part: it does not need to be reset!

### 
1. Dig a 2×2 hole until you reach a drop which would ruin any player's day.
2. Place 4 hoppers, one per block on the 2×2 hole, pointing into chests.
3. Build some kind of hall to access the chests below.

This can work in conjunction with other traps. The player drops down into the pit, and at the bottom, they die and their items are sucked into the hoppers for you to use.

### Painting trap


















A painting trap. Place painting(s) instead of vines.
This trap is easy to make. It hides a secret passage behind a painting. The target may unwittingly decide to check for a secret passage behind the painting. Big mistake.

### Fake chunk error
Dig a 16×16 hole, preferably in line with real chunks, at least 20 blocks deep. Some inexperienced players may think it is a chunk error and walk-in.


### Fake water pitfall















































Fake water, fake secret passage.
Dig a hole (2×2 works best) at least 30 blocks deep, the deeper the better. At the bottom place a block of lapis lazuli, a block of blue wool or a block of blue stained glass. Add a false corridor at the bottom to make it look like it goes somewhere. When an unsuspecting player comes across the hole, they may think that there is water at the bottom, jump down and die. Experienced players are less likely to fall for this particular trap but it generally works quite well. You can also place real water instead of blocks if you're wearing frost walker boots, just go down there, hide in the fake secret passage and sneak to hide nametag. Use F5 to see if a player is coming. If someone falls down, quickly move to freeze the water.


### Snowball trap





















Snowball trap.
Load a dispenser with snowballs (or other knockback item), and connect it to a pressure plate. When the target walks across the plate, the dispenser, if aimed correctly, shoots a snowball and knocks the target into the pit. You can also replace the dispenser with a piston.


### Piston pit






























Automatic piston pitfall
Place the piston so it pushes the block the signs are on. The player can make up to twelve rows using one piston. Make sure there is a block of empty space at the end of where the piston pushes. Connect the piston to a trigger, such a pressure plate or lever, and when the piston moves it should break the signs and cause the sand to fall along with the target. It is also possible to do this by pushing a line of blocks with torches or buttons on them, which may be slightly cheaper. Alternatively, use a sticky piston connected to a NOT gate which retracts a block with a sign on it, which allows the player to use more than 12 rows.


### Fake elevator































Fake water elevator































Real water elevator
Make what is shown in the schematic, a water elevator with water only on the top block. Make sure the hole is 30-40 blocks deep, which is enough to kill the player. It could help to place a lure sign near the 'elevator' saying something like "Do not enter!" You can also make the signs' text something like a floor countdown like "35", "34", "33", etc. so players are more likely to fall for the trap. If they want, you can place hoppers with chests so you can gather the loot from the victims, but if they really want the drops, they will need a secret passage to the bottom of the pit for collection.


### False-floor trap
A false-floor trap is a variation of a pitfall trap. It works by creating a concealed safe route through the pitfall to allow authorized players to pass, while catching unauthorized players or mobs and killing them. It generally works best when there is no way around, forcing the player to pass through the trap.

1. Dig a pit. The deeper and longer the better.
2. PlaceTNTto build a bridge across the pit. It should be at least 2 blocks wide, preferably more as someone could cheat otherwise.
3. Replace some of the TNT withtorches. Read the next step to understand which ones to replace.
4. On top of the torches, placesandorgravel. Try to get across the bridge now by only stepping on the sand. Make sure you can do it, because it will be even harder at the end as you must stay off the edges of the sand.
5. Once you have picked a satisfactory path, cover up the TNT with the same blocks as before.
6. Placepressure platesover all the sand/gravel.

If anyone steps on one of the pressure plates with TNT under it, the TNT will explode causing the whole bridge to collapse! Note: You will need to have something under the TNT, perhaps more TNT or something easily destructible to make sure the TNT doesn't fall and fail to ignite the rest of the TNT.

### False door pit
A false door pit utilises Redstone torches and pressure plated to drop an unsuspecting player

1. Make a regular doorway. The ground blocks should be some form of stone or wood to disguise the pressure plates. Make sure that the door is not on the same block as directly in front of it.
2. Dig a 2×1 hole in front of the door. If the door is placed correctly, there should be no room in front of the door.
3. To the side of the door, dig a 4×2×3 hole.
4. At the top of the pit, place a sticky piston with the ground block in front of it. The piston should not cover up the pit until activated. Repeat at the bottom of the pit.
5. In between the two pistons, place any block and place a Redstone torch facing away from the pistons.
6. Place a single piece of Redstone below the torch.
7. If possible, place a regular piston between the two pistons' arms facing toward the block with the torch on it.
8. 8. Cover up the pit with ground blocks and place the pressure plates! Some parts of the trap may still be visible, you can cover these up with walls.

## Water traps
Water traps use water to suffocate, trap, or push the target. None of these traps will work on zombies, as they will turn into drowned after drowning, instead of dying. Players who use potions of water breathing will also be unaffected.

### Fake water elevator






































Cobblestone can be swapped for obsidian
Make a water elevator using soul sand bubble column, but without an exit at the top. The column will force the unfortunate player upward, where they will be trapped against the ceiling, unable to break their way out because of the fact that blocks break much slower underwater. Cobblestone can be swapped for obsidian. This can also be used reversely, with magma blocks, taking advantage of the fact players cannot swim upward easily. In both cases, the players may not drown since they're in a bubble column, 
or you could make it more dangerous and put a sign with lava on the top but make sure to not have the blocks the lava is touching or is around is not flammable as it will burn.

### Retrieval trap
A trap made with water and dirt which can kill any mob except zombies.
Create a water current that drags the mobs down under a solid block. The current will hold the mobs under until they drown. The loot from the mobs will float, making the collection hard. If you use this trap to kill zombies, they won't die, but will turn into drowned instead. This trap will also not work on skeletons.

### Whirlpool trap
Through clever use of magma blocks, you can pull the target down into water. It should be noted that it's possible to breathe while inside a bubble column, so this trap is not useful for drowning players.


### Pufferfish pit
Dig a 1 block wide, 1 block long, 2 block deep pit with a magma block floor. Replace the 4 adjacent blocks to the air block at the bottom with trapdoors (make sure they open toward the magma so the pufferfish don't escape and die) and open them, then put a pufferfish in each one. Fill the pot with water, and (optional) add an open trapdoor in the hole, which mob AI sees as a solid block. The magma pulls it down and causes fire damage, while the pufferfish poison and damage the mob/player who fell in or was knocked in.

Note: This could be disguised as an elevator to a secret by putting the magma further down.

Resource requirements: 1 magma block, 4 buckets of pufferfish, 4 trapdoors (any), and 2 water buckets.

## Lava traps
Lava traps usually use lava to burn the target, or distract them for an easier kill. Note that most of these traps will destroy the loot.

### Lava staircase trap


























































A lava staircase trap
This trap can be handy for players who want to deal with assailants. The player should lure the target into the staircase for this trap to be most effective.

1. Dig a standard staircase down a way. The tighter the space available the better.
2. After a certain distance, place astone pressure platein the staircase. It's suggested to place it so it blends in. In the schematic, a wooden pressure plate is used for visibility.
3. Placeredstone dustin an upward trail for a certain distance. Make sure it does not look different from any other part of the staircase.
4. Connect the dust to adispenserand put alava bucketinside.

When the target steps on the pressure plate, it will be trapped by the lava running down the staircase. Even if they have Fire Resistance, it will take a long time to wade back up.

This trap can be expanded to make a handy escape mechanism. If you place the pressure plate on the upward side of the dispenser, the lava will flow down onto anyone chasing you. You could also make a hidden escape at the bottom. Just make sure you have a button to remove the lava.

With some clever piston work, the entire trap could be concealed except the pressure plate. Be wary of stepping on the trap yourself or placing the pressure plate in the wrong location.

There are many variations of this trap, so don't be scared to alter elements of it, especially concerning the direction (descending or ascending), who steps on the trap (you or assailant) and more.

### Chest lava trap




































































Chest trap
1. Build 2 rows ofsticky pistonssuch that are facing each other and the rows are 4 blocks apart.
2. Attach solid blocks to the rows of sticky pistons.
3. Link the rows of pistons toredstone torches.
4. Attach thetrapped chestto the Redstone torches.
5. Dig a hole below the sticky pistons and fill it with lava.
6. Decorate the area around the trapped chest to attract players!

### Lava pit
1. Make a 3×3 pit at least 4 blocks deep.
2. Placelavaat the top,laddersin the middle, andwaterat the bottom.
3. If you get mobs to go into the trap, they will burn in the lava and their drops should go into the water.

### Lava door
Make a house, and right inside the front door make a pit with lava. Most players will likely notice the trap and avoid it, so it works only on really careless players.

### Trapdoor lava pit
If the target should wander onto the pressure plate, good luck getting off!

An example of a trapdoor lava pit.
### Lava filler
1. Make astoneroom.
2. Place apressure platein the room.
3. Connect the plate to adispenserwithlavain it on the ceiling.






## Capture traps
These traps don't actually kill the target. Instead another trap is often used, or the player can come later to kill captured mobs.

### Curiosity trap
1. Place a pressure plate on a piece of 3 by 3 flat land.
2. Place 4 iron doors in a way that when you step on the pressure plate, the doors will close, revoking your chance to escape.
3. Place a ceiling that is either blast resistant or unbreakable. Also have an observer under the pressure plate that connects to some TNT so that when a player tries to escape, they will get blown up. This not only traps the player, but it also kills the player if they try to escape. You can also replace the observer with a block that blends in with the terrain so that they cannot see the TNT.

This might work on only inexperienced players because experienced players can use the parts that are shown to think of what might happen to them if they went in. You may also have a bit like having a dropper that throws out diamonds to lure them over to the trap.

### Piston trap
























Piston trap
This trap is best for 2-tall tunnels, perhaps inside a friend’s mine. Make sure there is a roof over it, so when the target hits the pressure plate, it cannot escape. When the pressure plate is stepped on, two pistons push up. Note that players will easily be able to break blocks and escape so you probably will want to combine this with another trap. 

| YouTube Video (view on YouTube) |
|---------------------------------|
|                                 |

### Door trap
This is a simple and rather obvious trap that is made by putting a pressure plate in the middle of 4 open iron doors so that the target is trapped inside when they enter. If using this trap against mobs such as skeletons, you don’t have to use iron doors.

### Shallow pitfall
Dig a 1-block deep pit at least 5×5 blocks. Place fences on the inside edge. Since fences count as one and one half blocks in height, mobs can walk in, but cannot jump out. Alternatively, line the outside with half-slabs. This can also be combined with a mob grinder, via water currents leading to it. Zombies and Skeletons will take damage from sunlight during the day if the pit is uncovered, making this an effective way to sort out creepers. This design does not capture spiders.

### Trapping pool
This trap is designed to trap skeletons and zombies, not to kill them!

1. Dig out a 5×5 square.
2. Dig a 3×3 square 2 layers deep in the center.
3. Place water in each of the corners and in the middle of each side on the top, where the water isn't flowing along the top.

### Slime trap
This simple trap targets slimes. 

1. Dig a 4×4 hole three blocks deep.
2. Fill the bottom layer with water, so that it is all still water on the bottom.

When a slime of any size wanders around, it may fall into the hole. Since slimes cannot jump in water, it will not be able to escape. You can come by later and kill all the slimes. If you are not interested in the drops, just leave them into lower slime population. This trap is best on superflat survival worlds where slimes spawn frequently. In that case, water can be obtained in villages.

### Quicksand
Step 1: Dig down an x/1<y/z (However wide and long you want, a minimum of 2 blocks deep) hole with soul sand on the bottom

Step 2: Fill it with water that goes up to 1 block below ground level, make sure bubble columns are made

Step 3/4: Fill in the area at ground level with cobwebs*

Step 3/4: Place sand in the bubble columns*

Step 5: Knock someone in!


Explanation: The bubble columns keep the sand on the same level as the cobwebs, so it just looks like slightly darker sand (entity and block shading are different) but sand entities don't collide with players or mobs, so you get stuck in the cobwebs and you need to use a sword or shears to break them, and you have to hit through the sand entities. You could also break a block at the edge of the hole.


NOTE: Only works on BE, in Java the sand will break after several seconds.

*You can do step 4 before 3, or vice versa, so they're 3/4

### Netherite block live-capture trap
This trap is extremely expensive to construct.

This trap is intended to work on players, and requires a secondary trap to initiate.

1. Locate a location in the overworld at bedrock level in which a 1×1×2 hole exists. If a player were to jump into said hole, they should see a block of bedrock directly in front of their face on all four sides.
2. Dig a vertical, 1×1 shaft all the way to the surface and construct a secondary trap there. The secondary trap must be able to force the target into the 1×1 shaft.
3. Approximately 10-15 blocks above bedrock, place a pair of tripwire hooks and string so that mobs that fall down the 1×1 shaft will trigger the tripwire.
4. Wire the Tripwire setup down to bedrock level by any means necessary, but ideally with as little delay as possible.
5. Place a Block of Netherite on top of one of the four bedrock blocks surrounding the hole.
6. Place a second Block of Netherite on top of another one of the four bedrock blocks surrounding the hole, but not directly across from the Block of Netherite placed in Step 5.
7. Place a piston adjacent to and facing toward the Block of Netherite placed in Step 5. The piston must face toward the hole.
8. Place a piston adjacent to and facing toward the Block of Netherite placed in Step 6. The piston must face toward the hole.
9. Place a disposable block opposite to the Block of Netherite placed in Step 5.
10. Place a piston adjacent to and facing toward the disposable block placed in Step 9. The piston must face toward the hole.
11. Remove the disposable block placed in Step 9.
12. Using redstone dust and redstone repeaters, separate the redstone line coming from the Tripwire placed in Step 3 into two repeaters. Set one to 1 tick, the other to 4 ticks.
13. Wire the redstone line from the 1-tick repeater directly into the piston placed in Step 8.
14. Wire the redstone line from the 4-tick repeater into a pulse shortener to reduce it to a 1-tick signal.
15. Construct a basic repeater clock, composed of 2 1-tick repeaters wired into each other.
16. Wire the pulse shortener to the repeater clock.
17. Wire one end of the repeater clock to the piston placed in Step 7.
18. Wire the other end of the repeater clock to the piston placed in Step 10.
19. Place a Cobweb on the bottom of the hole to prevent the target from dying to fall damage.

Should the trap be triggered, the following sequence of events will occur:

- Target springs secondary trap and is forced into 1×1 shaft.
- Target triggers tripwire while falling down shaft.
- Target hits cobweb at bottom.
- Piston placed in Step 8 triggers, pushing Block of Netherite directly above hole.
- Repeater clock triggered, causing pistons placed in Steps 7 and 10 to repeatedly shift the Blocks of Netherite back and forth, preventing them from being dug out. Blocks of Netherite are shifted at an interval of time that is shorter than the amount of time needed to break a Block of Netherite by conventional means such as by pickaxe.
- Target is contained within the trap until trap is disabled or target dies (or remains trapped indefinetly if difficulty settings forbid death by hunger and target has no other means of commiting suicide (Ender pearls, Potions etc.)).

## Piston traps
These traps use pistons to harm the target.

### Crushing trap





















A piston suffocation trap
This is ideal at the end of a water flow mob grinder as it minimizes drop losses. The design can be expanded to make a long row.


### Honeycomb trap






























A simple honeycomb trap. Replace the wool with a honeycomb block.
Connect two sticky pistons to a clock circuit so that they rapidly push a honeycomb block back and forth. If done correctly a player fallen into this trap will be unable to get out. Honeycomb block was chosen because tools do not affect the breaking speed, even with enchantments. Alternatively, a Block of Netherite could be used instead, as while Pickaxes break it faster, it still takes so long to break that even an Efficiency V Netherite Pickaxe cannot break it in time before it gets moved.

### Cake trap
1. Dig down two blocks in a flat area and put apistonat the bottom.
2. Dig down two blocks around the piston and putredstone dustat the bottom.
3. Dig down two blocks around the redstone and put pistons at the bottom.
4. Cover everything up with the block(s) of your choice.
5. Placepressure platesin a ring around the center block, above the redstone.
6. Put acakeon top of the center piston.
7. Above the outer ring of pistons, place blocks in the air so there is room to walk under if the pistons are retracted.

If the target moves too near to the cake, the pistons will trap them and destroy the cake.

### Pitfall trap
This device uses pistons to push entities into a pit.

| YouTube Video (view on YouTube) |
|---------------------------------|
|                                 |

## Manual traps
These traps require the player to manually trigger the trap, or perhaps even be the trap.

### Grave digging
Ask someone if they could dig down at a spot, perhaps because you lost diamonds there. When they get far enough, cover them with sand or gravel. You can also use lava for a more dramatic death, however, this will destroy their drops as well and won't work if they have a source of Fire Resistance. This will probably only work on inexperienced players.

### Facebreaker trap
1. Make a tower that is at least three blocks high so it will be seen from a distance. This will work best when built in a flat area such as plains or desert. The tower will act as a bait for this trap.
2. Around the tower, dig a pit at least three blocks deep. If you want this trap to be fully automatic, dig the pit at least 30 blocks deep.
3. When the target falls in the pit, dropgravelon the target. If you dug the pit at least 30 blocks deep, this isn't necessary, because most players will die from fall damage anyway.

If done correctly, the gravel blocks should fall on your target's head, thus trapping or killing them. Hence the name facebreaker. Make sure not to take too long or else the target may escape jumping off the gravel or placing blocks.

### Ore tower













































For a fully automated version, replace the top TNT with an observer.
1. Make a tall watchtower.
2. At the top out of sight, put a bunch ofTNT.
3. Make averticalredstonepath to the TNT with aleverto activate it.
4. Put alureat the top, and ask someone to go get it. When they get to the top, pull the lever.



### Return home to a potion of instant damage II
Note: This trap needs to be built on an already existing ender pearl "stasis chamber" where a player throws an ender pearl in and it teleports them back if the chamber is turned off, or a player enters it

1: Throw in a lot of splash potions of various negative effects. Make sure they don't shatter.


2: Trigger the ender pearl, teleporting the player who threw it into the splash potions, which shatter, possibly killing them

## Other traps
The traps here do not yet fit into any of the other categories.

### Spike trap
























The spike trap.
Materials: a dispenser, a pressure plate and any type of arrows.

1. Dig a 1×1×1 hole.
2. Place a dispenser facing up in the hole and fill it with arrows.
3. Place a stone pressure plate on top of the dispenser.
4. If the target steps onto the pressure plate, they will get shot by an arrow.

This trap is not lethal, except to players or mobs with low health. It could be made to be more of an annoyance if you replace the arrows with tipped arrows with potions such as Slowness, Poison, Weakness, or even fire charge to inflict fire damage.

### Slow monologue trap
























The slow monologue trap.
Use shears to collect spider webs. Then dig a 3 block deep hole placing lava at the bottom and cobwebs on the top layer. Anyone not watching their step could get caught in the web and slowly fall to their death, allowing you to get a few dramatic words in as they die. (experienced players will be able to get out of this by mining the cobweb, and quickly placing a block in the lava)

### 
There is a way to 'store' fall damage in a minecart and later have someone take that damage even though they don't actually fall a distance that would make them take damage. You can also search up for a video on how to do this.

### Magma carpet trap
This trap will probably involve a trip to the Nether. After gathering a fair amount of magma blocks, make a room. Use the magma blocks you have gathered to make the floor of the room, and cover ALL the magma blocks with carpets. When the target walks on to the carpet, they will take damage from the hidden magma blocks, often wondering and unable to figure out where the damage is coming from. If they don't figure out the trap soon enough, they will eventually die or lose a lot of health from fire damage.

One alternative is to make the entrance to the Magma Room two iron doors with pressure plates on the outside but not on the inside, potentially trapping the target inside to burn.

This trap could also be a potential mob farm. When the mob is killed by the fire damage, you can enter the room, most likely by a secret entrance, and by sneaking or wearing Frost Walker boots, claim the mob loot and go back out without taking any damage at all.

Note: This trap will not work on all types of Nether mobs, as they are immune to all kinds of fire damage.

Note: This only works pre 1.16.

### Anvil trap
1. Place twoiron doorssideways withredstone torchesunder them so they stay shut.
2. Set up twopressure platesin front of the doors. The plates shouldn't do anything yet.
3. Runredstone dustfrom underneath the plates onto the roof of your porch to trigger twopistons.
4. Put ananvilon each extended piston arm, and make sure there is a hole through the porch roof down to the entrance where the target stands.

When the target stands on the pressure plates, the doors won't open and while they are confused the anvils will fall on them. They will either be killed or if the anvils don't fall from high enough they get injured. This trap is useful to stop thieves from stealing valuable goods, and exploits the fact that people don't look up.

### Command mine































Command mine.
Sick of rebuilding land mines that don't even kill the target? Replace the TNT with a command block with the command '/kill @e[distance=..3]' and the command block will instantly kill any entity that touches the trigger! If you use a repeating command block instead of an impulse command block and set "needs redstone" to "always active", you don't need a pressure plate. This trap may be of use only in Creative mode, though. (you can also use the /summon lightning_bolt command)


### Arrow trap































A simple arrow dispenser
By connecting this to a trigger, you can rapidly fire arrows at the target. It is recommended to place this trap in a 1-wide 2 tall tunnel so there is less room to run. You can either place this in the side of the tunnel or shooting down the tunnel.
Some variations:

- Placelavain front of thedispenserto catch the target on fire.
- You can adjust therepeater, which will change the speed. You can also completely change theclockif you don't havequartz.
- You could use this to knock the target into apit.
- Attach this to aRS-Latchto keep it on until a button is pressed.
- Usetipped arrowswith negative effects to make the trap more dangerous.

### 
1. Dig a 2-wide trench down 1 block deep on one side, 3 or more on the other.
2. Placesignson the deeper side at the same height as the shallow side.

Wandering mobs will not be afraid to try and walk on the signs. If they do, they will get trapped. This will not always work, so it is advised to make the deeper part wider.

### Spider trap
1. Find acave spidermonster spawner, or enable cheats and use/giveto give yourself one. It is recommended to place atorchto keep it from spawning.
2. Dig a pit under it. It should be at least 5 blocks deep.
3. Placecobwebor something for the spiders to spawn on.
4. Break the torch and allow the pit to fill with spiders. You need to be within 15 blocks for this to work.
5. Get a player to go into the pit.

### Wither rose field
Surround your base with a field of wither roses or sweet berry bushes, and leave a block-wide path leading to your base, or make a hidden underground tunnel leading to it. Any hostile mob that walks through the field takes significant damage, but unless you make the field large enough, this trap isn't fatal. This trap works only on mobs and not on players, because players can disarm it quickly with just a water bucket. For added effect, place cobwebs on top of the plants, and if you are using wither roses, plant them on soul sand. This way, the mobs have to spend more time inside the trap, making it more fatal.

### Fake base 1
1. Build a really high staircase up into the sky. The longer you build, the higher it is, the better.
2. Make a hole into the staircase
3. You can even make yourself look like a noob, which will also give you an advantage. When someone notices and walks up, due to the player's view, they will fall through the hole you create, resulting in the target falling to the ground. This trap can even be effective with experienced players, if they don't look carefully.

### Fake base 2
1. Build a water elevator ( using soul sand and water )
2. At the top of the elevator, start building a fake base. Do not use any valuable material because unlike last trap, it will be destroyed completely (unless you want to).
3. In the fake base, connect twotripwire hookstogether with string right in the top of the elevator. Using redstone dust to lead around the base from the tripwire, then filling it with TNT.
4. If someone notice a base with a water elevator, they will sometimes attempt trying to go up. After they discovered the TNT behind those walls, they are likely to be gone.

### Big spiky fish
1. Make a somewhat small, square-ish room with a one way door and 2 block thick walls
2. Make 1×1×1 holes in the walls
3. Add trapdoors on each hole. Make sure that when closed they're on the upper half of a block, not on the bottom
4. Connect the one way door to a redstone signal inverter that is triggered when walked through
5. Then connect the signal inverter to the trapdoors, just make sure it allows for enough room for step 6*
6. Fill each hole with a pufferfish.
7. Make it look attractive to go into!
8. It's done!

When in action, the player will be trapped and the pufferfish will inflate and bounce around the room. (Fun fact: Fish out of water bounce. A lot.)

*You could probably use some hoppers attached to dispensers and fill the hoppers with buckets of pufferfish. Then, invert power to the dispenser. This makes it a renewable trap!

### It came from the sky
1. Make an observer clock (Face 2 observers at each other, which will produce a blinking redstone signal)
2. Place a redstone comparator going out of the observer clock and use it to change it to subtract mode (the redstone torch on the end is ON) (this is for your on/off switch!)
3. Add a trigger somewhere that goes into a signal inverter and into the SIDE of the comparator, make sure the signal that the comparator receives is equal to the observer's signal (signal strength of 15, like a redstone torch)
4. Now back to the trap, send the comparator's output into a repeater and then a dispenser
5. Now Cover it With Slabs. If you've done it right, your trap should be nearly flush with the ground (1.5 blocks tall from the ground) and only show the dispenser
6. Now fill up the dispenser with arrows. Eggs, snowballs, bottles of enchanting, and potions fly straight up. Arrows and fire charges are offset from the center, but fire charges don't come back down. If you want to destroy something flammable in the sky, FIRE CHARGES
	- (optional) Add a storage block with a hopper going into the dispenser. If the dispenser is empty and getting refilled while the trap is active, it won't shoot as much (Constant fire while containing arrows, shoots twice and "misses" once (It's empty, so it makes the annoying TICK sound) while being refilled)
7. Now maybe disguise it?
8. If you've done this right, it'll start raining arrows when someone activates the trigger. I recommend a flip flop before it activates, and a one time trigger, that way it starts constantly shooting arrows after being triggered.
9. As a last minute extra bit, if you can squeeze one in and a skeleton monster spawner's nearby, why not make the monster spawner an automatic farm and use an item elevator to bring arrows up to it? Just visit every now and then to refill it because of 1.16 mob despawning.

## Triggers
The traps here are most notable for their trigger and can be connected to many different mechanisms of harm.

### Trapped ore 1





















Trapped ore. Replace the cobblestone with ore.
When someone mines the ore the TNT will explode! Be sure to place the torches before the TNT and to not place any TNT next to a lit torch.

### Trapped ore 2
Use a piston to push a TNT next to a redstone torch when a block is mined. The advantage of this method is that the trapped block does not need have wires right next to it and that it can cover a wider area.

| YouTube Video (view on YouTube) |
|---------------------------------|
|                                 |

### Trapped ore 3
For a more expensive but instant explosion, place an observer behind the trapped ore and a dispenser behind the observer with an arrow inside facing away from the observer and place and end crystal where the dispenser is facing. Place the observer before the dispenser and the ore before the observer.

### Redstone mine












The redstone mine. Replace the glowstone with redstone ore.
Instead of a daylight sensor, you can also use an observer. This trap is good because it is hard to detect. If you build this above ground, it may seem somewhat out of place, so you should cover the redstone ore with carpet or build it underground. When the target walks on the redstone, it lights up, triggering the TNT. A similar trap is achieved by putting a valuable block that the player may want to mine in place of the redstone ore. When the player breaks the block, the daylight sensor activates, provided there's a light source or clear air above it.


### Furnace trap


















The furnace trap
Normally people would expect only chests to explode, so this trigger will surprise them as soon as they loot your furnace. You can replace the furnace with any other container for the same effect.

1. Fill afurnacewith coal, iron or food.
2. Put acomparatorleading away from the furnace. It should turn on.
3. Place a block in front of the comparator.
4. Place aredstone torchon the block, it should turn off.
5. Create a redstone line from the torch to TNT.

If a griefer loots the furnace the comparator deactivates and the torch turns on, blowing the victim to bits.

### Minecart mine






























A basic minecart trap
A target riding the minecart triggers the TNT and gets blown up. It might help to disguise the detector as doing something else, like switching tracks, opening a door, etc.

### Wrong lever
Place several levers on a wall and put TNT behind it. Place a sign saying something along the lines of, "Which one...," "Don't pull these!," or "Passcode entry." Eventually a player with too much curiosity may come along and pull a lever.

### Exploding bed
Connect a bed next to a Observer, the Observer to some TNT, and cover the whole thing in cobblestone. Then just wait for the player to sleep in it and get blasted sky-high.

### 




































































You will probably want to put the hooks the other way as they can be seen.
This trap relies on the fact that like end portal, string is invisible from the bottom. Make a room or hallway at least 3 blocks high, and put tripwire in a layer on the third layer up. If the victim jumps, they trigger the trap. However, if the victim sees the tripwire hooks they will probably mine the block so they don't have to jump.

### Chest bomb

















A chest bomb.
1. Place achest.
2. Place ahopperunderneath the chest.
3. Place acomparatorpointing away from the hopper.
4. Place TNT in front of the comparator.

If someone puts something inside the chest, it will go into the hopper, turn on the comparator, and activate the TNT. You could attach the comparator directly to the chest, but it would be more obvious as you can see over chests.
Trapped chests are also an option but they can be seen by experienced players.  Also, they can be seen more easily with resource packs.

### Fishing trap
It is possible to detonate TNT with a pressure plate and a fishing rod. This method is mostly undetectable; however, it is unstable and prone to premature detonation if you don't have patience.

| YouTube Video (view on YouTube) |
|---------------------------------|
|                                 |

### Proximity detector
A proximity trap is a player detector paired with an output.

| YouTube Video (view on YouTube) |
|---------------------------------|
|                                 |

## Lures
These traps' primary feature is the way they lure the target into the trap. Note that none of these lures work on mobs.

### Dropped loot
You could drop items such as gold or diamonds near your trap to increase chances that someone will walk into it. This works best if you know someone is coming by. Some tips:

- It might look too obvious with diamonds, so it could be better to use items like iron bars. You could also try to make it look like someone just died.
- If you want to get elaborate, you could setup adropperto periodically dispense an item. It would probably be possible to detect if the item was picked up, perhaps using aweighted pressure plate.

### Signs
Signs are useful for luring new, and sometimes even experienced, players into a trap. Here are some messages which can be good to lure players into traps.

- "Free Diamonds!" This could be good on a trapped chest, but would only work on newbies.
- "DO NOT ENTER!" Most players would be tempted to do exactly the opposite, even into a possible trap.
- "DO NOT PRESS!" If you see a button, you really want to press it. Especially if there is a sign saying not to.
- "FREE ADMIN!" Like the "free diamonds" example above, this probably works on newbies only.

p/s by troller10000: "DO NOT" means "yes", while "FREE" means "no".

### Chests
Chests, especially when paired with signs, can make a good lure. If you place one inconspicuously in a wooden house, what self respecting griefer would not go and investigate?

### Ore blocks
Ore blocks make an irresistible lure. After all, if you saw a diamond block just sitting there on the ground, would you just leave it there? This lure is good when paired with a BUD trigger.

### Fake mineshaft
Mineshafts are known for lots of loot. If you trap one, you can pretend to have 'accidentally given away directions' to the mineshaft.

### Iron door
An iron door looks somewhat out of place in a dark cave. If a player sees one, they may be tempted to go inside. Unfortunately for them, there may only be a pressure plate on one side of the door, or a landmine hidden under the plate.

## Disarming traps
When faced with a trap, the safest course of action is usually to leave the way you came. If the player really wants to disarm it though, here are some tips:

- Don't try to trip the trap and run away. Unless you have a really safe way of doing this, the trap is probably designed to prevent you from doing this.
- Watch out forobservers. These can be placed inside walls and underpressure platesas a fail safe.
- Don't assume it is safe to break redstone. It is usually safer to keep redstone in its current state. If it is off, it might be okay to break it. If it is on, it might be okay to place aredstone torchto keep it on. In elaborate traps the redstone may blink to check if it is broken, so watch out!
- TNTinwatergenerally doesn't do much damage. If you have awater bucket, it may be helpful to use it if you think everything is about to blow up.
- Try to always check for traps. If you see apressure platenext to aniron door, check forobserversbelow the plate, and break the door and plate, and go in. Another problem is underground traps. For ore traps, check for observers again, break them, and then mine the ore.

