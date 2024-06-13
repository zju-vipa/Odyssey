# Tutorials/Measuring distance
Measuring distances in Minecraft can be quite tedious, but a few simple guidelines can prevent you from making mistakes.

See this page for more conversion details: Tutorials/Units of measure

## Contents
- 1 Marking distance
- 2 Viewing exact coordinates in-game
	- 2.1 Bedrock Edition
	- 2.2 Java Edition
		- 2.2.1 Relative to crosshair line
- 3 Calculating coordinates of distant locations
- 4 Conserving markers
- 5 Volume and surface area
- 6 Using the Euclidean distance formula
	- 6.1 Example
	- 6.2 Euclidean distance in 3 dimensions (including elevation)

## Marking distance
Distances in Minecraft are quite easy to measure. Officially,[1] Minecraft uses the metric system, and each block is considered to be 1 cubic meter. When you measure long distances, it's easier to count if you mark the terrain with a space of 4 blocks between each marked block. The first marker represents a zero.  Every second marker (ignoring the zero-mark)  is then a 10-meter mark. Make a distinguished mark at the 21st marker to represent a hundred (100), because the first marker block represents zero (0). Use a sign to mark larger numbers to save time and resources.

(ZERO) 1 2 3 4 (MARK) 1 2 3 4 (10 METERS) 1 2 3 4 (MARK) 1 2 3 4 (20 METERS) ...

If you wish to know distance in miles, you can arbitrarily decide that each block is 1 cubic yard. Then 1 mile is exactly 1760 yards. Otherwise, keeping the "official" metric units, because one mile converts to 1609.3 meters, it is practical to consider a mile to be 1610 blocks long. Use the metric method (4 block spacing between). Make 161×10th meter marks. Use a sign to mark larger numbers to save time and resources.

## Viewing exact coordinates in-game
### Bedrock Edition
In Bedrock Edition you can turn on the "View coordinates" switch in your game settings. This isn't a cheat, so doing this doesn't affect your ability to earn achievements, and it makes distance measuring quite easy. It is also a great aid to keep from getting lost if you don't have a compass.

### Java Edition
In Java Edition, if you press F3, the debug screen shows your present location in X, Y and Z coordinates. Measuring distances between two locations or waypoints is as easy as subtraction, if you walk in a cardinal direction. Otherwise you must make use of the Pythagorean theorem to compute the distance. This is not strictly in-game, but it makes a drastic difference in gameplay, avoiding a lot of frustrated wandering. Note that the X and Z coordinates are horizontal and can be positive or negative (the spawn point is fairly close to 0, 0), but the Y coordinate represents your altitude, and Y=-64 is the bedrock floor of the game world.

#### Relative to crosshair line
Measuring in the debug screen(magnified). The human hitbox is as high as the green line, meaning he stands about 62 blocks away from the player.
This method is much faster and requires no building, though may not be 100% accurate. After going into the debug screen, the crosshairs are replaced with 3 colored lines. Take the length of a line running parallel to a block edge or face (e.g., the green line when looking at the side of a block). If one normal sized block is the same height as the line, the player is standing about 35 blocks away from it. If it's 1.5 blocks long, the block is 52-53 blocks away, 2 blocks long, 70 blocks away, etc.
Humans and mobs can also be used for measurement. Pressing F3 + B shows hitboxes. If the green line is as high as a player hitbox, he is about 62 blocks away.

With this, observable distances can be measured very quickly. This method still works if the player is viewing the block at an angle, but keep in mind that it's harder to count the exact number of blocks covered by a crosshair line when the line is visibly shorter. Because there are fewer pixels in the lines and blocks, it may not be as accurate.

Note that the lines change size relative to the GUI, and was a different size entirely in 1.8. These numbers assume a normal sized GUI.[more information needed]

## Calculating coordinates of distant locations
Finding the X and Z coordinates of a distant Amethyst Geode, noting the player's position of  "XYZ: -743.349 / 137.0000 / 540.144" and and the target's direction and tilt angle (-136.2 / 21.9)
Calculate a distant object's X and Z coordinates using the tilt angle in the debug screen by estimating the target's elevation from a vantage point significantly higher or lower in elevation. Typically you would pillar up about 50 to 60 blocks, or climb a tall mountain, and use the direction and downward tilt angle of the target with your coordinates to calculate first the horizontal distance to the target, then the X and Z coordinates of the target based on that distance and direction.

Pointing at the target, using FOV 30 or a spyglass for greatest accuracy, and the debug screen on, divide the difference in elevation by the tangent of the tilt angle. If you are on a high mountaintop at Y=137 and you see an amethyst geode in a swamp, you can estimate it is at sea level, or Y=63. The debug screen says you are at "XYZ: -743.349 / 137.0000 / 540.144" and two lines below that, you are looking at a target "Facing: north (toward negative Z) (-136.2 / 21.9)". Your tilt angle is 21.9° and your rotation is 360 - 136.2 = 223.8°, converting from Minecraft's -180°/+180° notation to conventional 0° to 360° notation. The elevation difference, ∆Y, is 137 - 63 = 74. Find the distance by dividing ∆Y by the tangent of the tilt angle: 74 ÷ tan (21.9) = 74 ÷ 0.402 = 184.08 blocks. 

Your vector to the geode is 184 blocks facing the direction -136.2, or 223.8°. To find the coordinate components of this vector, multiply the distance times the sine of the direction for the ∆X, adding that to your X position, and multiply the distance times the cosine of the direction for the ∆Z, adding that to your Z position. The geode's ∆X is 184.08 ∙ sin (223.8) = 184.08 ∙ -0.692 = -127.41. Subtract this from your X, so -743.349 - (-127.41) = 615.93. The ∆Z is 184.08 ∙ cos (223.8) = 184.08 ∙ -0.723 = -132.86. Add this to your Z, 540.144 + (-132.86) = 540.144 - 132.86 = 407.28.

Standing on the geode, the target's real coordinates were -618 67 408. The elevation is four blocks higher than sea level, and with this correction, the calculation comes a couple blocks closer.
If you're confused whether to add or subtract for your X and Z values, use the debug screen for a sanity check, and note again "Facing: north (toward negative Z)". The target's Z is somewhat less than your Z value of 540, hinting that you want to subtract 132 from 540 to get 407. If you turn a little to the right, you can verify the target is east of you, "toward positive X", so you're looking for a number greater than (i.e. less negative than) your X position of -743, so you want to subtract negative 127 from -723, which is -734 + 127 = -615.

Keep in mind that small errors can be magnified at great distances. Each one block error in your estimate of the target block's elevation can cause errors of several blocks in the X and Y coordinates, though generally for things you can see within 20 to 30 chunks, it's close enough that you can see the target when you get there.

