### Stuck-Piston Based
The following designs works because pistons can't be pushed by other pistons while extended. Also, when a piston retracts, it doesn't notify any other pistons that were trying to push it. The piston with the block attached to it is sticky and acts as the sensor. This design has the advantage of a low profile, and also that the quirk it exploits is less "buggy" and less likely to be fixed in the future.

























A perpendicular "stuck piston" BUD switch. The piston with the block attached to it is sticky.
A perpendicular "stuck piston" BUD switch. The piston with the block attached to it is sticky.
An in-line "stuck piston" BUD switch. Left piston is sticky.)
The latter design above can also be extended to an array in a variety of ways, including a one-wide design.

A very compact "in-line" BUD array. Every piston is a sensor except the one next to the obsidian. None of the pistons are sticky.
A one-wide BUD array. Every piston is a sensor except the one next to the obsidian. None of the pistons are sticky.

The stuck-piston principle can also be used to hide a BUD completely underground, as shown by this video:






























Using an observer to block a sticky piston.

The design on the right uses an observer which self updates when arriving in front of the sticky piston to stick it. During retraction, when the sticky piston resets, the observer in front of it is still a block of moving piston, so the sticky piston doesn't schedule a block event; then the moving piston becomes an observer with no block update, and the sticky piston enters BUD state.






















Slime Block BUD

Sticky pistons in slime block BUDs are often stuck by a block behind a slime (or honey) block next to its head. When the design on the right retracts, the slime block updates the sticky piston after the redstone block arrives, but the diamond block is still moving so the sticky piston doesn't plan to extend; the diamond block cannot update the sticky piston on arrival. Like the compact BUD, it can reset itself unless it is updated when extending. 

### Dropper Based
Here is a video about this.[needs testing]




### Other QC components based
Here are examples based on update QC activation of a dispenser and half a door.




































Dispenser Based

The dispenser contains a water bucket, lava bucket or powder snow bucket.






























Door Based

### Redstone Torch Based

As of 14w25a (with the fix of MC-56541), a burned-out redstone torch can be used as a reliable BUD. Once burned-out, a redstone torch will reset upon an update from any adjacent block. This is the smallest and simplest BUD, only requiring a single torch and redstone dust (plus two repeaters for a solid output signal.) 
A burned torch BUD with a solid output.
A redstone torch on the side of a block and put redstone dust make the redstone signal loops with itself is also a BUD. The place around the redstone torch (include upside and downside) is the detecting place, but not the redstone dust. The redstone torch will blink for 16 ticks, and finally burn down. It has a 56 ticks cool down. It can't detect sleeping in a bed.














An example of a redstone torch based BUD.
An example of a redstone torch based BUD.
This works in the Bedrock Edition of Minecraft, as shown in the video below.




### Redirection based
A simple redirection bud
When redstone dust redirects, it does not send out block updates, so a piston can have its power removed by redirecting redstone dust away from it to remove power. When the piston receives a block update, it will update its state accordingly and the redirection bud will reset.


### Powered rail based

















































Powered Rail BUD
A powered rail or detector rail will be activated if one among the first to eighth of connected rails of the same type on the same direction should be activated, but cannot be properly updated when being activated or deactivated if part of rails before the power source are not activated or deactivated along with it. This can be used to create a BUD. Powered rails can be replaced by detector rails as a whole.


Unless integrated with minecarts and detector rails, the powered rail BUD only outputs block updates, but it causes little delay and burden on the server, and are often used to transfer block updates.

### Fluid based
Fluids calculate flow directions when receiving block updates, and can be detected by observers if flowing toward new directions.

### Components on Trapdoors based
Powered rails, detector rails,rails and activator rails attached to trapdoors break when receiving NC updates after the trapdoor opens. This type of BUD can reset itself if used for a rail duper as rails reappear after breaking.

### Tripwire Hook on Doors based












Using tripwire hooks to keep a door open.
As shown on the right, build a tripwire circuit missing one tripwire hook, trigger the tripwire, and place the missing hook on any half of a door. The tripwire hook breaks when activating the door but the door remains open. 


