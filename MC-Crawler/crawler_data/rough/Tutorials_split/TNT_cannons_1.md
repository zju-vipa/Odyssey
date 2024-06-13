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

