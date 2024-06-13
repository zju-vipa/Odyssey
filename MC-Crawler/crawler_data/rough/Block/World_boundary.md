# World boundary
The world boundary is the area defining the intended spatial edges of a Minecraft dimension. It is distinct from hard limits, which are defined by limitations of the programming language itself.

## Contents
- 1 General Information
	- 1.1 Java Edition
		- 1.1.1 Horizontal limits
		- 1.1.2 Vertical limits
	- 1.2 Bedrock Edition
		- 1.2.1 Horizontal limits
		- 1.2.2 Vertical limits
	- 1.3 Walking to the Boundary
- 2 Effects
	- 2.1 Java Edition
- 3 History
	- 3.1 Horizontal boundaries
	- 3.2 Vertical boundaries
	- 3.3 Older version effects
		- 3.3.1 Infdev
		- 3.3.2 Fake chunks
		- 3.3.3 Console info
- 4 Issues
- 5 Trivia
- 6 References

## General Information
### Java Edition
#### Horizontal limits
The world border is located at X/Z ±29,999,984. Chunks still generate past this point, but the player cannot go past ±30 million blocks out.
There are several different intended horizontal boundaries in the game.

Firstly is the maximum distance nether portals can generate at in the Overworld, at X/Z ±29,999,872 blocks (128 blocks, from the 16 blocks per chunk multiplied by the 8 block multiplier). This limit prevents any surpassing of the next borders using the Nether to multiply distance by 8.

The next layer is the world border, which lies at X/Z ±29,999,984 by default, and establishes an arbitrary (but capped at this default value) blockade to prevent the player from advancing. There are several methods of bypassing this border.

The third layer lies exactly one chunk further, at X/Z: ±30,000,000. At this point, there is an invisible "wall" preventing the player from advancing by setting any players' positions beyond it to it, even in spectator mode. Using commands like /teleport does not work, since the game does not accept any value beyond X/Z: ±29,999,999. This value is hard-coded into the game's source code. Other block interactions, such as TNT exploding or water flowing, affects blocks outside this limit. By using a minecart (in a superflat preset with the top layer as rails), the player can go even further, up to X/Z: ±30,000,208. At that point, the player is frozen in place until the minecart is destroyed, then they are teleported back to X/Z: ±29,999,999. The fourth layer lies at X/Z: ±30,000,208 in recent versions. At this point, the player is frozen in place until the minecart is destroyed, then they are teleported back to X/Z: ±29,999,999. By using a boat (in a superflat world), the player can still go even further, up to X/Z: ±30,000,544. At that point, the player is frozen in place with the camera shaking uncontrollably, until the boat is destroyed, then they are teleported back to X/Z: ±29,999,999.
As the server thinks the player is still at X/Z: ±30,000,000, no more chunks generate past X/Z: ±30,000,544. This is considered to be the absolute edge of the Minecraft world.

By editing the source code for the game, it is possible to extend the terrain generation and world border past X/Z: ±30,000,256 (up to X/Z: ±2,147,483,647) and experience the game quite normally (no ghost chunks; mobs can spawn alright; commands accept higher values). The game performs normally even at distances of X/Z: ±2,000,000,000, as in modern versions most distance effects have been patched out of the game. It is advisable to take note of what distance effects do exist, as well as the hard limits present - notably the ±33,554,432 lighting stop and hard limit of ±2,147,483,647.

#### Vertical limits
Each dimension has what is called a build limit. This is the maximum and minimum heights where a player can place and break blocks. These numbers are controlled by files in a data pack's data/<namespace>/dimension_type folder. The minimum build height is controlled by the JSON value  min_y, which must be between -2032 and 2031 and be a multiple of 16. The minimum build heights in the vanilla data pack are Y=-64 in the Overworld and Y=0 in the Nether and End. The maximum build height is controlled by  height, which dictates the total height within which a player may break or place blocks. It must be between 16 and 4064 and be a multiple of 16. The maximum build heights (not the  height values) in the vanilla data pack are Y=320 in the Overworld and Y=256 in the Nether and the End. Regardless of what  min_y and  height are set to, the minimum build height cannot be below Y=-2032 and the maximum build height cannot exceed Y=2031.

These limits do not apply to entities, which are allowed to travel to and exist above the maximum and below the minimum build heights.

The space beyond the build limit is often referred to as the void. Any mob (besides the ender dragon) that is 64 blocks or further below the minimum build height takes damage at a rate of 4 every 10 game ticks (0.5 seconds).

### Bedrock Edition

  

It has been suggested that  this section be split into its own page  at Stripe Lands. [discuss]
If this split may potentially be controversial, do not split until a consensus has been reached. Reason: Bedrock Edition does not have a world boundary, and this page says that. (UTC 18:41, 4 March 2024)


#### Horizontal limits
Bedrock Edition technically has no hard boundary, and the world at far distances is far too ravaged by several distance effects to provide any semblance of reasonable gameplay. Nonetheless, there do exist intentional defined limits for some game functionality:

- It is impossible to teleport beyond X/Z ±30,000,000 using commands in the vanilla game. Any attempts to teleport further puts the player back to this coordinate. Attempting to use any block placement command results in an error message. Despite this, it is still possible to usestructure blocksand the/locatecommand.
- X/Z ±31,999,872 are the maximum coordinates reachable in the Overworld viaNether portal. The only way to teleport beyond these coordinates is to use external tools (such as a world editor).

#### Vertical limits
The player is able to go to Y ±30,000,000 but it is impossible to teleport beyond these coordinates without the use of external tools.

### Walking to the Boundary
Legitimate terrestrial journeys to the various World Boundaries has been done across different versions of Minecraft. The 30M Java Border has been reached by Figonometry in 1.17. The Java Boundary on b1.7.3 has been reached by MysticalMidget, who reached the Far Lands before continuing the journey to 32M. One other player, DumbName, has attempted to reach the Bedrock Boundary but ceased at 2.1M due to "Lots Of Storage Problems Plus The Jitter Point At 2,097,152 Blocks"[1]

For players who reached the 12.5M Far Lands, see the Far Lands page. 

Time-wise, the walking (not sprinting) speed is 4.3 blocks per second. Walking for 6 hours per day is equal to 21,600 seconds, giving a travelled distance of 92,880 blocks every day. Walking to the 12.5M Far Lands would take just under 136 days at this pace. The Boundary is almost 3x further out.

## Effects
### Java Edition
Main article: Java Edition distance effects
Generally, long server response times caused by massive distances produce unintended results, but most blocks and entities behave normally, with a few exceptions:

- Pistons may sometimes not extend or retract until they receive another block update.
- Beyond the X/Z ±30,000,000 mark:
	- Mobsdo not spawn at all.
	- Lightingdoes not update (with exception to sunlight and moonlight).
	- Itemsmay jitter slightly.

Beyond this, most of the unintended behavior of blocks and entities is caused by either the world border (as detailed here) or being sufficiently far from the world origin (see this page). Some odd effects that are attributed to the boundary itself are as follows:

- Attempting to walk into the boundary still displays a walking animation, walking sounds, and cause view bobbing, effects that are not present for walking into the world border or solid walls.[2]
- Usingelytrato fly into the border causes the flying sound to continue to play at full volume rather than quietly or not at all.[3]
- Rainparticles always hit the ground at exactly sea level regardless of the actual shape of terrain beyond 30 million blocks.[4]

