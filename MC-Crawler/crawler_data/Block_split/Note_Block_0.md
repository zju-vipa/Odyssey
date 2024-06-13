# Note Block
A note block is a block that emits sounds when attacked, used or activated with redstone. The sound produced can be altered in various ways by using it or putting certain blocks directly above or below it. A note block's sound played repeatedly can be used to direct allays to stay nearby and drop collected items near it.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Playing music
		- 2.1.1 Notes
		- 2.1.2 Instruments
			- 2.1.2.1 Mob heads
		- 2.1.3 Activating note blocks
		- 2.1.4 Interaction with allays
	- 2.2 Fuel
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Block data
- 5 Achievements
- 6 Advancements
- 7 History
	- 7.1 Data history
- 8 Issues
- 9 Trivia
- 10 Gallery
	- 10.1 Screenshots
	- 10.2 Concept artwork
	- 10.3 In other media
- 11 See also
- 12 References
- 13 External links

## Obtaining
### Breaking
Note blocks are most quickly broken with an axe.

| Block     | Note Block            |
|-----------|-----------------------|
| Hardness  | 0.8                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 1.2                   |
| Wooden    | 0.6                   |
| Stone     | 0.3                   |
| Iron      | 0.2                   |
| Diamond   | 0.15                  |
| Netherite | 0.15                  |
| Golden    | 0.1                   |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Natural generation
Note blocks generate in ancient cities.

### Crafting
| Ingredients             | Crafting recipe |
|-------------------------|-----------------|
| AnyPlanks+Redstone Dust |                 |

## Usage
### Playing music
#### Notes
A note block being triggered and playing a note.
Note blocks play a musical note when hit (pressing the attack button) or activated by redstone. A note block must have air in the space directly above it to play a sound. Unlike most other sound-emitting blocks, note blocks can be heard up to 48 blocks away. The volume of a note block decreases as the player gets further away from it. The sound of note blocks (as well as jukeboxes) can be independently controlled by the Jukebox/Note Blocks slider in the audio settings.

Note blocks play when on or next to a powered block. Each time a note block plays a note, a note particle may fly out of the top (if pressed too fast, notes may not appear), with the color depending on the pitch (but not the instrument).

There are 16 different instruments and 25 different pitches per instrument. Pressing the use button on the block increases the note pitch up a semitone, with a total of two full octaves (24 semitones in total) being available for each instrument. The standard range (for harp and pling instruments) of notes span from F♯3 to F♯5. After reaching the highest note (24th pressing of use button), pressing use again (25th pressing of use button) resets the pitch back to F♯3, as does breaking the block and picking it back up.

The string bass and didgeridoo are two octaves (24 semitones) lower than the standard range, the guitar is one octave (12 semitones) lower than the standard range, the flute is one octave above the standard range, and the bells, chimes, and xylophone are 2 octaves above the standard range. This gives the player six octaves (72 semitones) of effective range to combine instruments for greater pitch coverage.

The exact pitch can be found from its use-count by using the following formula: 2 ^ ((use count - 12) / 12).

The exact pitch to use-count assignment is shown below,[1][2] along with the note's color, which is rendered with shading using the particle's texture.

| Pitch (Octave 1) | Use count | Pitch (/playsound)    | Color (hex) |
|------------------|-----------|-----------------------|-------------|
| F♯/G♭- Fi/Se     | 0         | 0.5                   | #77D700     |
| G - Sol          | 1         | 2^(-11/12) ≈ 0.529732 | #95C000     |
| G♯/A♭- Si/Le     | 2         | 2^(-10/12) ≈ 0.561231 | #B2A500     |
| A - La           | 3         | 2^(-9/12) ≈ 0.594604  | #CC8600     |
| A♯/B♭- Li/Te     | 4         | 2^(-8/12) ≈ 0.629961  | #E26500     |
| B - Ti           | 5         | 2^(-7/12) ≈ 0.667420  | #F34100     |
| C - Do           | 6         | 2^(-6/12) ≈ 0.707107  | #FC1E00     |
| C♯/D♭- Di/Ra     | 7         | 2^(-5/12) ≈ 0.749154  | #FE000F     |
| D - Re           | 8         | 2^(-4/12) ≈ 0.793701  | #F70033     |
| D♯/E♭- Ri/Me     | 9         | 2^(-3/12) ≈ 0.840896  | #E8005A     |
| E - Mi           | 10        | 2^(-2/12) ≈ 0.890899  | #CF0083     |
| F - Fa           | 11        | 2^(-1/12) ≈ 0.943874  | #AE00A9     |
| F♯/G♭- Fi/Se     | 12        | 1.0                   | #8600CC     |

| Pitch (Octave 2) | Use count | Pitch (/playsound)   | Color (hex) |
|------------------|-----------|----------------------|-------------|
| F♯/G♭- Fi/Se     | 12        | 1.0                  | #8600CC     |
| G - Sol          | 13        | 2^(1/12) ≈ 1.059463  | #5B00E7     |
| G♯/A♭- Si/Le     | 14        | 2^(2/12) ≈ 1.122462  | #2D00F9     |
| A - La           | 15        | 2^(3/12) ≈ 1.189207  | #020AFE     |
| A♯/B♭- Li/Te     | 16        | 2^(4/12) ≈ 1.259921  | #0037F6     |
| B - Ti           | 17        | 2^(5/12) ≈ 1.334840  | #0068E0     |
| C - Do           | 18        | 2^(6/12) ≈ 1.414214  | #009ABC     |
| C♯/D♭- Di/Ra     | 19        | 2^(7/12) ≈ 1.498307  | #00C68D     |
| D - Re           | 20        | 2^(8/12) ≈ 1.587401  | #00E958     |
| D♯/E♭- Ri/Me     | 21        | 2^(9/12) ≈ 1.681793  | #00FC21     |
| E - Mi           | 22        | 2^(10/12) ≈ 1.781797 | #1FFC00     |
| F - Fa           | 23        | 2^(11/12) ≈ 1.887749 | #59E800     |
| F♯/G♭- Fi/Se     | 24        | 2.0                  | #94C100     |

Alternatively, there is a graphical version available:


Players can roughly check the tuning of a block by looking at the note icon.


In Java Edition, the tuning can also be checked by looking at the right side of the debug screen (accessed by pressing F3). It is denoted as "note:" followed by a number from 0 to 24.

