# Tutorials/TNT cannons
A TNT cannon is a mechanism that launches entities using TNT. They can be used in survival to mine, fast travel and destroy. Cannons build in survival often follow premade blueprints. In creative, on the other hand, cannons might be build to experiment with one's redstone skills or have fun in general.

Over the years communities have emerged around cannon-PVP and created constraints on the cannons to increase fun when fighting. A limit on the use of blocks, especially those with high blast resistance, is the most common constraint. In WarGear and Slime Block Robot Battles, the fighting machines are built in creative and then are copied to an arena where combat takes place in survival. The size of both is constrained. Dispensers and some entities (and for WarGear also duplication bugs) are prohibited. SBRT requires the whole fighting machine to be movable. Factions bases, on the other hand, are built in survival, though they might be designed in creative. Dispenser cannons and water shielding are allowed here. Those constraints and the absence of constraints have caused a great amount of cannon diversity, which is discussed in this article.

Topic specific speech is used for this page and the sub-pages. It is either explained on this page or under the according headlines.

## Contents
- 1 Loading types
	- 1.1 Manual cannons
	- 1.2 Automatic cannons
- 2 Damage types
- 3 Course types
	- 3.1 Mid-air maneuvering
	- 3.2 Straight trajectories
- 4 Launch types
- 5 Special purposes
	- 5.1 Other projectiles
- 6 General implementation strategies
	- 6.1 Intel
	- 6.2 Signals
		- 6.2.1 Converting signals
		- 6.2.2 Synchronization
	- 6.3 Moving TNT
	- 6.4 Increasing efficiency
	- 6.5 Lag reduction
- 7 Armor and Shielding
	- 7.1 Armor
	- 7.2 Shielding
- 8 Missiles and flying machines
	- 8.1 Missiles
	- 8.2 Flying machines

## Loading types
One game tick Tunnler Machine gun (1gt TMg).
### Manual cannons
As the name suggest, in manual cannons everything is loaded by hand. This includes TNT and might include other entities such as sand.

### Automatic cannons
An automatic cannon can shoot without player interaction (excepting activation).

## Damage types
Comparison of different damage types.
Instead of just exploding all TNT at the same position, like in a Shotgun, many different ways to damage the enemy on multiple positions were found. Tunnler cannons stood out as being the most effective in a lot of situations but there are also some other important damage types, listed here.

## Course types
### Mid-air maneuvering
A Flank Tunnler (FT).
Mid-air maneuvering  is mostly achieved using injectors that explode near the projectiles.

It may be used used to hit the enemy from unexpected angles, to shift around freely or to reduce barrel size.

### Straight trajectories
Straight trajectories describe all trajectories that are not influenced by TNT after leaving the cannon or barrel.

Techniques

The most important techniques to achieve the above are listed on this page: Techniques

## Launch types
Trace of a Nether cannon's launch point.
The place where the Boosters explode is called the launch point. There are two general variants of launch points. Either the Boosters sit on blocks, such a launch point is called a platform or they are in mid-air - such launch points are found in Ejector cannons.

## Special purposes
A Hybrid cannon piercing water armor.
Piercing

A cannon is Piercing when it can penetrate enemy shielding. If it can only penetrate certain shielding types <shielding type>-Piercing is used.

Hybrid

A Hybrid is a combination of sand- and TNT cannon, that uses sand entities wich are transferred to their block form to replace water and penetrate water armor this way.

Instant (I)

To counter Active armor, an Instant cannon penetrates the enemy defense in one shot or in a fast burst of shots so that it cannot replenish itself in time.

Anti Tech-KO (At)

An Anti Tech-KO cannon is small and placed at locations where the enemy might not be able to hit it at all.

It is mostly used when the other cannons are destroyed or to cheat the Tech-KO (that the enemy has no living cannons) win condition.

Anti cannon (!<cannon type>, Scraper)

An Anti cannon is a counter for specific cannons or strategies.

The most common type of Anti cannon is a Shotgun that scrapes the side or back of the enemy. It should be noted that most Anti cannons are just an additional mode for other cannons that can be easily modified for this purpose.

A Scraper does not counter any specific cannon but instead any cannons in (almost) exposed parts of the target. It is often found in the form of Scatter- or Multi impact cannons.

Playerkill

As with Anti cannon, cannons sometimes can easily get modified to specialize on killing players or to prevent players from just moving out of the trajectory. Those modes are named Playerkill.

Moving cannon

Some fighting machines are fully movable so a movable cannon is a no-brainer there.

Extender cannon

Extender cannons move outside the fighting machine and then stay there.

Most cannons are tailored to a specific area of interest. Extender cannons exploit that by moving out of this area of interest. Sometimes that can turn them into almost unbeatable AntiTKOs that don't even need to be compact. But if the enemy is prepared, moving out of the safety of the fighting machine's armor can be devastating.

### Other projectiles
Most other projectiles have different movement physics and explosion interactions.

Pearl cannons

A Pearl cannon can move players far distances but needs its destination to be loaded.

Arrow launchers

Since arrows do way more damage, when traveling faster, arrows accelerated by TNT might instantly kill any entity that is not protected by a Totem of Undying. Arrows can be scattered easily be scattered using the random motion, when dispensing them. This eliminates the need to aim arrow launchers precisely and allows to hit multiple targets in a single shot.

Sand cannons

Sand and other falling blocks have the same flight behavior as TNT (apart from TNT usually flying only for less than 4 seconds).

When multiple falling blocks are accelerated downwards together, they can form towers up to the height of their velocity (rounded up). Those towers are usually used to remove water and could be used to remotely build structures.

Some falling blocks such as anvils and dripstone might be used to damage players, though this is hard to achieve, when they are moving.

Falling blocks can be stored, while inside moving pistons.

Player cannons

A Player cannon is usually just a fun cannon build with a few propellants under the player launching them up hundreds to tens of thousands of blocks. TNT-minecarts might be used instead of TNT.

Some player cannons accelerate pigs instead of players to take advantage of lazy acceleration. They are similar in functionality to pearl cannons but don't need to have their destination loaded.

## General implementation strategies
### Intel
Having intel about the enemies actions as well as the damage to all fight machines is crucial for deciding which cannon to use and where to shoot.

Comparison between an outlook (2x 3 seconds away from the cannon) and a window.
Windows

Windows and outlooks can be a powerful way to get intel on your enemy.

This can be especially valuable, if you fight alone and thus methods to spy on the enemy are scarce. The main problem with using windows is, that they are usually associated with having less armor or only a narrow FOV. On the other side outlooks don't have those problems but it can take you valuable seconds to try reaching them.

Alarms

Contraptions detecting block destructions can notify the player if a cannon is damaged. Since holes of TNT cannons are generally rather wide often it is enough to just detect one block per 7x7 section (no multiple detections are needed towards the enemy).

Alarms are generally very limited in their use because they can get messy and thus often just provide some very specific informations. Thus they are mostly used in cannons where you wouldn't notice the damage else way - not in time at least.

Common variations on the concept of the Alarm are circuits ejecting the player automatically out of the loading position, if the cannon is exploding and counters that inform the player that they have to change modes or else would do no further damage to the enemy.

Spotting

Spotting relies on other players - often spectators - to relay information to the fighters. The "Spotters" often also have the role of coordinating the attack.

Spotting is the most common and versatile form of intel gathering. But still some drawbacks are that this method relies on other players. Spotting is still limited in the amount of information that can be passed on to other players and especially that can be coordinated since multiple players speaking at the same time can get quite messy. This information overload is especially prevalent in the first minutes of the fight.

This is why Spotting often is already practiced when one party isn't even fighting against the other. This way this team can strategize on how to best destroy their enemy beforehand and greatly increase their initial chances as well as the value of transferred information.

Tools

Tools to support intel gathering include reloading the chunks (F3+A) or the shaders since entities are rendered first. Highlighting entities (F3+B) and using the debug info screen might also help. Other tools to help spying on the enemy include "X-Ray"-texture packs as well as entity tracer / highlighter and free cam mods.

Due to most of those tools being considered cheating and heavily punished on servers they aren't used often.

### Signals
Inputs

The aim of all inputs is to reduce the minimum time a component has to wait between entering a functional state and activating.

Manual cannon activation.Left: Noteblock + Observer Right: Movement detection  Left: Autostarter Center: Book Right: Visual feedback
Manual

When thinking about manual activation of redstone circuits what comes to mind first are levers and buttons. But those aren't good options in cannoning because they are quite small and thus hard to aim at, usually increasing the time needed to click them. Buttons also need 1 to 1.5 seconds to reset. As an alternative one can use noteblocks instead of buttons and fence gates in combination with T flip-flops instead of levers.

Since moving the mouse around and clicking can take quite some time, one common method of cannon activation is player detection by string through jumping. To minimize the air-time one can place a grindstone next to the string (and optionally a trapdoor under the player) so that the player will rebound of it after just two pixels. This can happen in parallel to loading the cannon

Food practice is to switch between many modes with variable delay / signal strength. Variable delay can be achieved using repeaters. For signal strength the easiest way to do that is by using a lectern with a (15-paged) book and a comparator behind it. Sometimes it can be useful to encode modes using binary. This can be a pretty fast and compact method but one should keep in mind the risk of the convertion from our imagination into binary might take more time, than the few inputs required bring.

In some game modes the kits get distributed to start the fight. Using a block that can only be interacted with by placing an item inside (like placing music discs into jukeboxes or flowers into flower pots) one can spam the slot where said item will appear and thus eliminate reaction time. This is most commonly used to activate flying machines, automatic cannons and missiles.

Sometimes modes can only be changed by destroying and replacing the mounting blocks. This is quite compact and for some modes necessary but only viable in late-game applications because it is too slow for any early game interactions.

Automatic cannon activation. Top-left: counting circuit Top-right: BUDBottom-left: clock Bottom-right: Wall + observer
Automatic

Automation is a key part of freeing up player time for other purposes. Automation circuits might become quite big. To counter this they are often seperated from the rest of the cannon so that the cannon won't cease functioning when the automation circuits get damaged.

The most common way to activate cannons automatically is by using block update detectors (including observers). They detect if TNT is at its position to activate a circuit. If this circuit is moving said TNT, common practice is to use a wall + observer combo (fences, iron bars and glass panes can be used as well) since walls only detect full blocks appearing/disappearing next to them and do not detect the piston head movement. This can prevent unwanted double activations.

Clocks might be used instead of BUDs. They are smaller and might be faster. On the flipside they (often) require consistent conditions, limiting their use in manual cannons.

Parts of a cannon can be triggered with redstone logic. For example: If the blockstream has triggered four times, the cannon will activate. This can have various advantages discussed below.

Auto delay

To maintain maximum efficiency over multiple shots into one hole, usually the delay needs to be adjusted each shot. Delay can also be a way to change the current mode. This is usually achieved by wiring the delays in parallel and blocking those that would trigger before the current one.

Auto modes

Modes often can be designed to be full-automatically adjustable too. Having automatic modes might increase the risk of shooting into holes without targets of interest but them being faster often makes up for that.

Automation matrix

If the enemies are likely to change their targets of interest, it might be beneficial to adopt dynamic automation. Automation matrices allow for planning many shots before the fight begins and tailoring them to the enemies Formation and tactic.

The future

As slightly touched on above, cannoning often is a game of predictions. The only ways to predict Formations, tactics and player movement in advance are to learn by asking other players and playing yourself. But some consistencies exist that will be discussed here:

Usually the projectiles and injectors are ignited after the propellants. Thus in many cannons it will save time to prime the propellants before the projectiles are ready, anticipating that they will likely be ready after the delay between propellants and projectiles.

Since not all players are equally fast it might be beneficial to test which players are faster and sort them so that the parts of the fighting machine that need faster actions are supplied as best as possible or fewer potential is wasted on cannons that require slower actions.

#### Converting signals
Sometimes signals can have unwanted side effects. This section is explaining, which signal type fits which purpose.

Double- & long activation

Double- and long activation often interfere with future events such as placing new TNT. They might also mess up T flip-flops and counting circuits.

To prevent this try to reduce all kinds of long activations (>four game ticks).
Common sources are: (observers detecting...) Buttons, pressure plates, repeaters, redstone lamps, pistons, string, TNT placement and ignition.
If there is no way around long or double activations, they can be reduced back to short pulses using rising edge monostable circuits.

Piston spitting

Piston spitting is sticky pistons pushing blocks but not pulling them back.

If this is unwanted it can be fixed by using signal lengths of more than two game ticks.

Update order

As a rule of thumb: The earlier a signal was created, the earlier it's update priority is. A 4 redstone tick repeater is processed before a comparator that activates that same tick, because it's signal was created 8 game ticks before that of the comparator (comparators create their signals in the same game tick as they get powered due to comparator priming). And the same can be said about the TNT that will be ignited by those components. The difference in update order is called event delay or ED.

Zero ticks

When a redstone pulse is terminated in the same tick, it is called a zero tick. It is equivalent to a one game tick pulse for some blocks and entities but is not processed by others at all. Some blocks such as sticky pistons and trapdoors get activated and deactivated with the pulse. This results in loads of useful properties. Some are:
Trapdoors that are activated with a zero tick pulse might let TNT pass but not players. Propellants might move only for a zero tick, after accelerated to destroy nearby blocks or phase through unloaded chunks.

#### Synchronization
The synchronization of cannons is explained above.

Since this is a brought topic, only some rules how to make the synchronization less complicated can be named:
It is best to let signals stay combined whenever possible. For example if you have an injector- and a projectile delay, let the projectile delay branch of off the injector delay. Now they can be adjusted simultaneously without changing the relative delay between projectile and injector. Or if two parts of the cannon undergo similar changes, it might be possible to perform those changes using the same component.
Parts acting in parallel can hide dangers. A common problem is, that one part is BUDed by the other. Those problems are usually easy to fix but hard to find, so it is important to know, what to look for.

### Moving TNT
Moving blocks

Moving TNT blocks comes with some unique problems. Many of them are caused by it being impossible to power the TNT / direct redstone signals through. But other, way more problematic problems come from the TNT often needing to move, while the player is using the cannon.

To prevent slow down of the loading in block streams, the pusher might use 0 ticks. Those allow continuous loading but come with some problems. If the TNT is pushed using a clock it will be unordered. 0 tick placement detectors on the other hand can get big and might not reset fast enough, especially during lag spikes.
Another way to reduce this slow down is by moving the player. Trapped between two flowerpots the player can quickly move left and right, placing TNT into two different pushers. This requires a lot of loading skill and is not applicable in most conventional cannon layouts though.
A similar effect is achieved by moving the TNT furthest away from the player first, so that it can already be loaded again - looking through the transparent parts of the piston head - while the TNT closer to the player are still pushed.

To prevent TNT blocks from being pushed into the TNT of previous shots (no matter if the latter is in block or entity, form this might cause problems) either those TNT have to be primed faster or they need to be moved somewhere else. Moving it somewhere else can increase cannon volume dramatically though if it is solved via multiple chambers so instead a better and more complicated solution is to store all the TNT and ignite them in one chamber.

Compression

Top: Trapdoors, that let TNT but not players passMiddle: CompressorBottom: Compressor and separator
Compression is the process of moving TNT to their launching position.

Gravity and pistons and / or flowing water are usually used to achieve the compression. To prevent the inaccuracies that come with the prime motion of TNT, it has to be pushed into a wall, so that the motion gets cancelled.

Separation

As the name suggests, separation refers to the process of separating TNT and keeping it separated.

TNT can be separated by it's position in the update order using pressure plates. If the TNT is moved onto the pressure plate it activates a trapdoor, that prevents other TNT from being moved there. To separate multiple TNT at once, the process might be repeated setups involving iron- or golden pressure plates can be used.

Usually the TNT are initially separated though. To keep the TNT less complicated and more compact methods can be used. Those include flaps (trapdoors or piston setups, that open for a moment to let a bunch of TNT pass, while the next batch lands on them) - which are most commonly used to separate multiple shots from each other - and setups, that push the TNT into multiple horizontally differing positions - often used to separate propellants and projectiles or in very fast Machine guns.

### Increasing efficiency
Increasing accuracy

Very high accuracy can be achieved by rebounding the TNT or shooting straight forward, because this reduces the alignment complexity by one axis. On the other hand direction changes in mid-air usually decrease accuracy.

Pixel precision:


Pushing TNT into Blocks with different width/ letting it fall onto blocks with different height aligns the TNT against those Blocks. This technique results in a precision of 1 pixel which is equivalent 1⁄16th of a block (or half a pixel/1⁄32th of a block for chains and lily pads). If TNT are pushed into the same hit box from the same direction they will usually have the same position in that axis.

Subpixel precision:

TNT with alignment differing in the subpixel precision.
Since TNT is only 0.98 blocks wide it makes a difference, from which direction it is pushed into a block. This can be used to achieve 0.02 block differences in alignment. If the TNT is not pushed against a block it is placed into the middle of the pixel which allows for 0.01 block differences in alignment.

Using errors in Java's floating point calculations alignments (for example pushing TNT from different directions) with approximately e-9 differences in alignment are possible.

TNT can be pushed into boats, which can be aligned anywhere to a precision of about e-11 using minecarts. This method is more complicated and less compact, than the other methods (since boats can be damaged multiple times in one tick, which forces them to be at least 8 blocks away from the propellants in reusable cannons). But it allows almost unmatched precision anywhere.

Motion alignment:

Using the motion of TNT any alignment can be achieved. Precise alignments can be hard to figure out properly though since most motion types are either too slow for TNT or to inconsistent and need to be canceled. Some motion types with notable consistency include water streams, bubble columns and TNT falling through powdered snow. They are especially useful since changing the delay for which TNT is exposed to them results in consistent position changes.

Propulsion and velocity

Some cannons use other methods than TNT (ie. slime blocks, water...) to accelerate TNT but this section is about propulsion from TNT explosions.

In general the following rules apply:

Propulsion is increased by adding propellants and reducing the distance between the propellant's explosion centre and the TNT's position (for many other entities the eyes are used instead of the position). Disregarding some exploits that involve the world's origin the maximum acceleration per propellant is one block per tick.

Propulsion is decreased, if the projectiles rebound, when different propellants cancel each other's motion, when exposure sample rays are obstructed, or when propellants slide on the ground.

Using every projectile

It is worth looking out for which projectiles can be removed and where other projectiles can be added. More projectiles often lead to a worse cannon. Scatter cannons and statics are known to be quite inefficient.

### Lag reduction
Lag reduction can be important in some cannons. For that it is advisable to shoot as straight as possible or use modifications, that improve entity motion performance. Apart from that all the rules that apply for other redstone contraptions also apply here.

Lazy acceleration

Lazy chunks only tick blocks and not entities. If the projectiles lay inside lazy chunks, they can accumulate acceleration given by propellants that explode outside lazy chunks. This allows for cannons to be charged way longer than four seconds, so that only a few hundred TNT are loaded at any time (except for the few ticks, where the cannon is shooting). Thus lag is reduced and cannons are also more compact. Chunk loading will break lazy cannons, if no safety mechanisms are implemented.

## Armor and Shielding
### Armor
It is generally best to use the highest blast resistance allowed. It is preferable to use blocks that have no hit box but some blast resistance (such as fence gates) over air.

Anti Mortar armor (without causing armor gaps).
Anti Mortar

By alternating slabs and walls vertically mortars with a prime phase intervals of one game tick can be stopped without it taking any armor away (compared to other blocks with the same blast resistance). Slabs and other blocks that are less than a block high can also help against shots that aren't fully compressed. Blocks that slow entities such as cobweb can be used to further increase the time it takes the Mortar to settle down, costing it even more delay.

Invisible

Some blocks can be invisible such as some block entities and walls (for invisible walls use the debug stick to remove all sides and set the Up-State to false).

Those blocks will still serve as armor (though TNT can pass through some of them) but they might be unexpected and can even hurt cannons.

Unmovable armor

It is generally slightly preferable to use unmovable armor so that flying machines cannot push it around.

Alternatives
Honey, powdered snow and cobweb can slow the TNT down. This can be useful at times but those blocks often get destroyed before they can be effective.

TNT resistant


Cannon resistant

Some blocks cannot be destroyed or bypassed by cannons (when they don't use exploits). Those include all blocks that cannot be replaced or moved and have a blast resistance above 9. Those blocks are usually not permitted or nerfed in fights because it is boring to shoot at something without progress.

Water

Even though water can't be destroyed by TNT it can be replaced with sand and sand can be destroyed with TNT so sometimes it is still allowed as armor. Water also is often allowed for sole use at launch points.

Cobblestone generators

Cobblestone generators might be considered a form of active shielding. Apart from that not much is to say about them except that they are a better version of water shielding.

Netherite

Netherite and its derivatives are indestructible for cannons. Though if it is moved, it is replaced with Block 36 (which is destructible by TNT) for a brief amount of time. 

### Shielding
Top-left: Upwards (Relocational) Heavy ATOX extensionTop-middle: (Spike) ATOX extensionTop-right: Pergola tipCenter: Horizontal Heavy ATOX extensionBottom: Horizontal Relocational Heavy ATOX extension
The idea of shielding is to counter cannons specialized on hitting a target by blocking the trajectory. If the cannon is not prepared against it this will not only serve as more armor but it will also be way more efficient armor. Even with little shielding the efficiency of the enemy's cannons can be greatly damaged for it being impossible to specialize on every type of shielding or no shielding so that inefficiencies have to occur at some point in exchange for more general usability of the cannon.

The most basic form of shielding is just to push blocks out of the fighting machine. This only works well against Artis.

ATOX

An ATOX is a shield that pushes forward a flat surface composed of many flying machine extensions.

ATOX are a prerequisite for many other shields. Their most basic form can often be found all over the fighting machine.

Pergola (Perg)

A Pergola shoves a thin layer of blocks above the fighting machine.

It allows it to be pretty efficient while often also not using blocks that would have served as armor.

Spikes

Spikes only cover every second block.

Spikes are best used for thin shielding. There is few gain for the buck when making this principle more heavy.

Heavy

Heavy shielding describes a wide wall of blocks being pushed into position.

Because a full Heavy shield is so expensive and uncommon it is quite possible that the enemy's cannons fail on it. But one can't just put Heavy shielding everywhere since there are only so many blocks to use.

Layered

Shielding can be layered to either create an emergent Heavy shield or each layer can be spaced apart so that only Tunnlers and Mortars prepared for it can destroy multiple layers at once.

If the same shield type is layered, it is referred to as a Double-, Tripple-, Quadruple shield.

Spaced or irregular layering can have a similar effect to heavy shields while using less blocks.

Relocational (2-Axis / 3-Axis)

Relocational shielding pushes the blocks out of the fighting machine and then parallel to the fighting machine.

This way armor can be moved from somewhere where it is not needed to somewhere it is needed. This is a dream for everyone building shields though sadly usually one doesn't have much blocks to spare at the outside.

3D Printer

A 3D Printer moves blocks out of a storage per block stream and prints them out somewhere else as shields. A single block storage can supply multiple shields or the other way around. The shield that is supplied can also sometimes change every fight.

It is pretty much Relocational shielding on steroids. That said in situations where they are not needed to perform armor relocation they might not be used because they can be bigger than the other shield types and they often are a lot slower.

Mining

Blocks used for shielding don't have to originate in the fighting machine. A Mining shield uses the environment for blocks to supply iself.

The blocks scraped are often of lower blast resistance than the ones originating in the fighting machine. If that is the case they might be used in the outer layer or in alternation with end stone. They can also be used to defend less valuable spots.

Active

Shielding doesn't need to happen outside the fighting machine. Active shielding seeks to close a hole before another shot enters. The most basic form is just falling blocks falling down, but this does not work against Downward- and Upward cannons and is very slow. Often a better option is pistons pushing the blocks. Ways it can be activated include using redstone clocks, block update detectors or inverted redstone signals. It can also happen outside of the fighting machine.

## Missiles and flying machines
### Missiles
A simple two way missile magazine without the activation circuit.
A Missile is a flying machine that transports TNT to the enemy and explodes it there.

After a couple of TNT, there are quick diminishing returns in TNT usage vs damage output if no cannon is mounted on top of the missile. A Missile is more TNT efficient than a cannon. On the other hand it is way slower, might use up other blocks instead, needs more loaded chunks and is easier to defend.

Making a missile able to move in both directions can be critical in maintaining efficiency when enemies can attack from both sides.

Bomber

A Bomber is a missile that drops the TNT at the enemy from above.

The main advantage of a Bomber is that it has better returns when using more TNT than most other missiles.

Torpedo

A Torpedo is a missile, that can damage structures under water. They do it in a fashion similar to Hybrid cannons by replacing the water first.

Magazines

Missiles can be stacked behind each other to penetrate deeper while maintaining TNT-efficiency. Sometimes the last missile is a big one to damage the enemy from inside. Missiles in close proximity to each other are prone to chain reacting though.

Return

A reusable missile. That makes it similar to a slower but more compact Blockstream cannon in practice.

Netherite buster

It is possible to build a missile such that it's payload explodes the moment the enemy's netherite is moved by the missile, destroying the netherite.

Tunnel bores

A Tunnel bore is the best possible missile. But because it is so overpowered the duplication bugs and withers required for it are often forbidden.

Instant win

A common win condition is to count how many blocks were destroyed by each team. Some missiles aim to exploit that by pushing huge amounts of low blast resistance blocks such as snow or end_rods to the enemy and exploding them there. Those missiles often get forbidden in such systems.

### Flying machines
Moses with instant extensions-
Moses

A Moses is a big ATOX-like flying machine sweeping towards the enemy.

Its initial use was to remove water but Moses also proved useful to block enemy barrels and crush their redstone.

A Moses can also be bigger similar to heavy ATOX.

Blanket

A Blanket is basically a Pergola, that extends around the enemy. Its purpose is to block the enemy's shots.

Anti Moses

An Anti Moses is a little flying machine, that has the only purpose of stopping Moses by exceeding their piston push limit.

Cruncher

A Cruncher is a flying machine, that flies over the enemy's side/top/bottom and constantly pushes pistons against the outermost blocks in hopes of crushing some redstone components or filling Chambers and barrels.

Player transport

A flying machine that is just used to transport players towards the enemy so that they can enter the opposing fighting machine.

| Introductory      |                                                                                                                                                                           |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Basics            | Menu screen<br/>Game terms<br/>                                                                                                                                           |
| Newcomer survival | The first day/beginner's guide<br/>The second day<br/>The third day<br/>Hunger management<br/>Things not to do<br/>Simple tips and tricks<br/>Your first ten minutes<br/> |
| Shelters          | Best biomes for homes<br/>Best building materials<br/>Building and construction<br/>Navigation<br/>Shelters<br/>Shelter types<br/>                                        |

| General                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| General                    | Achievement guide<br/>Advancement guide<br/>Best enchantments guide<br/>Breaking a fall<br/>Breaking bedrock<br/>Combat<br/>Complete main adventure<br/>Creating a village<br/>Downgrading<br/>Dual wielding<br/>End survival<br/>Exploring caverns<br/>Gathering resources on peaceful difficulty<br/>Getting food quickly<br/>Headless pistons<br/>Hitboxes<br/>Horses<br/>Indestructible end crystals<br/>Mapping<br/>Measuring distance<br/>Minecraft in education<br/>Mining Diamonds Fossils Ancient Debris<br/>Diamonds<br/>Fossils<br/>Ancient Debris<br/>Nether hub<br/>Nether portals<br/>Nether survival<br/>Organization<br/>Pillar jumping<br/>Playing with a controller<br/>PvP PvP bases<br/>PvP bases<br/>Spawn-proofing<br/>Summoning jockeys<br/>The Void<br/>Time-saving tips<br/>Thunderstorm survival<br/>Units of measure<br/>Village mechanics Trading<br/>Trading<br/>X-ray glitches<br/> |
| Enchanting<br/>andsmelting | Enchanting mechanics<br/>Anvil mechanics<br/>Automatic smelting<br/>Manual smelting<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

| Challenges                |                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| General                   | Acquiring a conduit<br/>Curing a zombie villager<br/>Defeating temples<br/>Defeating a village raid<br/>Defeating a Nether fortress<br/>Defeating a bastion remnant<br/>Defeating a monster room<br/>Defeating a pillager outpost<br/>Defeating a woodland mansion<br/>Defeating a monument<br/>Defeating an End city<br/>Defeating the Ender dragon<br/>Defeating the Wither<br/>Exploring an ancient city<br/>Obtaining every music disc<br/> |
| Non-standard<br/>survival | Adventure survival<br/>Half hearted hardcore<br/>Hardcore mode<br/>Surviving in a single area indefinitely<br/>Infinite desert survival<br/>Island survival<br/>Manhunt<br/>Mob switch<br/>Nomadic experience<br/>Skywars survival<br/>Superflat survival<br/>Flat survival<br/>Ultra hardcore survival<br/>                                                                                                                                    |
| Challenge maps            | Beating a challenge map<br/>Creating a challenge map<br/>                                                                                                                                                                                                                                                                                                                                                                                       |

| Constructions |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Constructions | Adding beauty to constructions<br/>Airlock<br/>Architectural terms<br/>Building a cruise ship<br/>Building a metropolis<br/>Building a rollercoaster<br/>Building safe homes<br/>Building water features<br/>Color palette<br/>Creating shapes<br/>Defense<br/>Desert shelter<br/>Elevators<br/>Endless circling pool<br/>Furniture<br/>Glazed terracotta patterns<br/>Making nice floors<br/>Pixel art<br/>Ranches<br/>Roof types Curved roofs Roof construction guidelines Roof decorations<br/>Curved roofs<br/>Roof construction guidelines<br/>Roof decorations<br/>Secret door<br/>Settlement guide<br/>Underwater home<br/>Walls and buttresses<br/>Water gate<br/>Water-powered boat transportation<br/> |
| Blockbreaking | Blast chamber<br/>Igniting TNT underwater<br/>Wither cage<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

| Farming        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Blocksanditems | Amethyst<br/>Armor<br/>Azalea<br/>Bamboo<br/>Basalt<br/>Bedrock<br/>Blaze rod<br/>Bone meal<br/>Cactus<br/>Chorus fruit<br/>Clay and mud<br/>Cobblestone<br/>Cocoa bean<br/>Copper<br/>Crops (Beetroot, Carrot, Potato, Wheat)<br/>Dirt<br/>Dragon's Breath<br/>Dripstone<br/>Egg<br/>Fern<br/>Fish<br/>Flower<br/>Froglight<br/>Glow berries<br/>Glow ink sac<br/>Glow lichen<br/>Goat horn<br/>Gold<br/>Hanging roots<br/>Honey<br/>Ice<br/>Iron<br/>Kelp<br/>Lava<br/>Meat<br/>Moss block<br/>Mushroom<br/>Music disc<br/>Nautilus shell<br/>Nether growth<br/>Nether vine<br/>Nether wart<br/>Obsidian<br/>Powder snow<br/>Pumpkin, Melon<br/>Rooted dirt<br/>Sculk growths<br/>Scute<br/>Seagrass<br/>Sea pickle<br/>Snow<br/>Soul soil<br/>Sugar cane<br/>Sweet berries<br/>Tree<br/>Trident<br/>Vine<br/>Villager trading hall<br/>Wither rose<br/>Wool<br/>Duplication<br/> |
| Mobs           | Mob farming<br/>Mob grinding<br/>Monster spawner traps<br/>Allay<br/>Animals<br/>Axolotl<br/>Blaze<br/>Cat<br/>Cave spider<br/>Creeper<br/>Drowned<br/>Ender dragon<br/>Enderman<br/>Frog<br/>Goat<br/>Guardian<br/>Hoglin<br/>Iron golem<br/>Magma cube<br/>Phantom<br/>Piglin bartering farm<br/>Raid<br/>Shulker<br/>Slime<br/>Squid<br/>Turtle<br/>Villager<br/>Wandering trader<br/>Warden<br/>Witch<br/>Wither<br/>Wither skeleton<br/>Zombie<br/>Zombie villager<br/>Zombified piglin<br/>                                                                                                                                                                                                                                                                                                                                                                                   |

| Mechanisms            |                                                                                                                                                                                                                                                                                                                                                                  |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Basicredstone         | Automatic respawn anchor recharger<br/>Basic logic gates<br/>Combination locks<br/>Command block<br/>Flying machines<br/>Hopper<br/>Item sorting<br/>Item transportation<br/>Mechanisms<br/>Observer stabilizer<br/>Randomizers<br/>Redstone music<br/>Redstone tips<br/>Rube Goldberg machine<br/>Shulker box storage<br/>Villager trading hall*Water tram<br/> |
| Detectors             | Block update detector<br/>Comparator update detector<br/>Daylight detector<br/>                                                                                                                                                                                                                                                                                  |
| Minecarts             | Train station<br/>Minecarts Storage Storage system<br/>Storage<br/>Storage system<br/>                                                                                                                                                                                                                                                                           |
| Traps                 | Snow golems<br/>TNT cannons<br/>Trapdoor uses<br/>Trap design<br/>Traps<br/>                                                                                                                                                                                                                                                                                     |
| Pistons               | Piston uses<br/>Piston circuits<br/>Quasi-connectivity<br/>Zero-ticking<br/>Instant repeaters<br/>                                                                                                                                                                                                                                                               |
| Advanced<br/>redstone | Advanced redstone circuits<br/>Arithmetic logic<br/>Calculator<br/>Command stats<br/>Hourly clock<br/>Morse code<br/>Printer<br/>Redstone computers<br/>Redstone telegraph<br/>                                                                                                                                                                                  |

| Servers      |                                                                                                                                                                                                                                                                      |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| General      | Playing on servers<br/>Multiplayer Survival<br/>Spawn jail<br/>Griefing prevention<br/>Joining a LAN world with alternate accounts<br/>                                                                                                                              |
| Server setup | Setting up a server<br/>Server startup script<br/>FreeBSD startup script<br/>OpenBSD startup script<br/>Ubuntu startup script<br/>Setting up a Hamachi server<br/>Setting up a Minecraft Forge server<br/>Setting up a Spigot server<br/>Ramdisk enabled server<br/> |

| Technical                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Technical                   | Improving frame rate<br/>Minecraft help FAQ (IRC channel)<br/>Running the data generator<br/>Update Java<br/>                                                                                                                                                                                                                                                                                                                                            |
| Maps                        | Custom maps<br/>Map downloads<br/>Command NBT tags<br/>Falling blocks<br/>Updating old terrain using MCEdit<br/>                                                                                                                                                                                                                                                                                                                                         |
| Resource packs              | Creating a resource pack<br/>Loading a resource pack<br/>Sound directory<br/>                                                                                                                                                                                                                                                                                                                                                                            |
| Data packs                  | Creating a data pack<br/>Installing a data pack<br/>Custom world generation<br/>                                                                                                                                                                                                                                                                                                                                                                         |
| Creating<br/>Minecraftmedia | Creating videos<br/>Livestreaming<br/>                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Game installation           | Installing snapshots<br/>Installing Minecraft Preview and beta versions<br/>How to get a crash report<br/>Installing Forge mods<br/>Custom Minecraft directory<br/>Playing and saving Minecraft on a thumb drive<br/>Playing and saving Minecraft on a thumb drive with the old launcher<br/>Recover corrupted saved world data<br/>Run Minecraft through Google Drive<br/>Save game data to Dropbox (world data only)<br/>Saved data Dropbox guide<br/> |

| Outdated |                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Outdated | Building micro shelters<br/>Custom texture packs<br/>Door-based iron golem farming<br/>End of light mob farms<br/>Far Lands<br/>How to get a crash report<br/>Installing mods<br/>Man-made lake<br/>Managing slimes in superflat mode<br/>Minecart booster<br/>Potion farming<br/>Repeater reboot system<br/>Survival with no enabled data packs<br/>Update LWJGL<br/>Update Minecraft<br/>Village chaining<br/>Water ladder<br/> |

