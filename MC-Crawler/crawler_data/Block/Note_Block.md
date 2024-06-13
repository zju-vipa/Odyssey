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

#### Instruments
The instrument played depends on the material of the block underneath the note block. Note that these are groups of blocks defined by the code, not just the individual block.

##### Mob heads
When a mob head is placed on top of a note block, the sound made by the note block becomes that of the corresponding mob's ambient sound, with the exception of the creeper head, which instead causes the note block to play the primed sound.

| Block                                                                                                                                                                                                                             | Instrument                         | Range   | Sound event names (Java)                 | Sound event names (Bedrock) |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|---------|------------------------------------------|-----------------------------|
| Material: wood                                                                                                                                                                                                                    | Bass (String Bass)                 | F♯1–F♯3 | block.note_block.bass                    | note.bass                   |
| Material: sand, gravel, concrete powder                                                                                                                                                                                           | Snare Drum                         | —       | block.note_block.snare                   | note.snare                  |
| Material: glass, sea lantern, beacon                                                                                                                                                                                              | Clicks and Sticks (Hihat)          | —       | block.note_block.hat                     | note.hat                    |
| Material: stone, blackstone, netherrack, nylium, obsidian, quartz, sandstone, ores, bricks, corals, respawn anchor, bedrock, concrete, stonecutter, furnace, observer, terracotta, prismarine, prismarine bricks, dark prismarine | Bass Drum (Kick)                   | —       | block.note_block.basedrum                | note.bd                     |
| Block of gold                                                                                                                                                                                                                     | Bells (Glockenspiel)               | F♯5–F♯7 | block.note_block.bell                    | note.bell                   |
| Clay,honeycomb block‌[BE  only][3],infested block‌[BE  only]                                                                                                                                                                      | Flute                              | F♯4–F♯6 | block.note_block.flute                   | note.flute                  |
| Packed ice                                                                                                                                                                                                                        | Chimes                             | F♯5–F♯7 | block.note_block.chime                   | note.chime                  |
| Wool                                                                                                                                                                                                                              | Guitar                             | F♯2–F♯4 | block.note_block.guitar                  | note.guitar                 |
| Bone block                                                                                                                                                                                                                        | Xylophone                          | F♯5–F♯7 | block.note_block.xylophone               | note.xylophone              |
| Block of iron                                                                                                                                                                                                                     | Iron Xylophone (Vibraphone)        | F♯3–F♯5 | block.note_block.iron_xylophone          | note.iron_xylophone         |
| Soul sand                                                                                                                                                                                                                         | Cow Bell                           | F♯4–F♯6 | block.note_block.cow_bell                | note.cow_bell               |
| Pumpkin                                                                                                                                                                                                                           | Didgeridoo                         | F♯1–F♯3 | block.note_block.didgeridoo              | note.didgeridoo             |
| Block of emerald                                                                                                                                                                                                                  | "Bit" (Square wave)                | F♯3–F♯5 | block.note_block.bit                     | note.bit                    |
| Hay bale                                                                                                                                                                                                                          | Banjo                              | F♯3–F♯5 | block.note_block.banjo                   | note.banjo                  |
| Glowstone                                                                                                                                                                                                                         | "Pling" (Electric piano)           | F♯3–F♯5 | block.note_block.pling                   | note.pling                  |
| Skeleton skull                                                                                                                                                                                                                    | "Skeleton"                         | -       | block.note_block.imitate.skeleton        | note.skeleton               |
| Wither skeleton skull                                                                                                                                                                                                             | "Wither Skeleton"                  | -       | block.note_block.imitate.wither_skeleton | note.witherskeleton         |
| Player head                                                                                                                                                                                                                       | Sound event set innote_block_sound | -       | Dependent                                | Dependent                   |
| Zombie head                                                                                                                                                                                                                       | "Zombie"                           | -       | block.note_block.imitate.zombie          | note.zombie                 |
| Creeper head                                                                                                                                                                                                                      | "Creeper"                          | -       | block.note_block.imitate.creeper         | note.creeper                |
| Piglin head                                                                                                                                                                                                                       | "Piglin"                           | -       | block.note_block.imitate.piglin          | note.piglin                 |
| Dragon head                                                                                                                                                                                                                       | "Ender Dragon"                     | -       | block.note_block.imitate.ender_dragon    | note.enderdragon            |
| Any other blocks                                                                                                                                                                                                                  | Harp / piano                       | F♯3–F♯5 | block.note_block.harp                    | note.harp                   |

#### Activating note blocks
A pair of note blocks wired to a clock circuit to play alternately.
Note blocks can be activated in a variety of different ways following normal redstone principles.In Java Edition, after activating the note block, it sends block update immediately and play a sound after start delay. However, some ways of activating note blocks are more convenient than others or produce unexpected results. 

- When a note block is activated by abuttonon its side, it does play a note, but is often difficult to hear because the sound of the button can overlap the note block.
	- On the contrary, if theobserverorblock update detectorare used to detect the note block, the note block acts as a button with better attributes: the pulse is shorter, it's easier to click, and it can be completely silent when put a block above it.
- Because note blocks need space above them, note blocks activated by pressure plates or redstone directly above them do not make a sound.
- Note blocks areconductive blocks, they can be powered, it can activate the note blocks next to it when it is powered.

#### Interaction with allays
If an allay hears a note block play within 16 blocks of its location, it tries to path find to the note block and then spends 30 seconds around that particular note block, seeking items around it and returning them to it instead of its player. After 30 seconds, the allay returns to targeting its player. A vibration particle emanates from the note block and reaches the allay to indicate the allay has locked on to the note block. Because the allay and the note block interact via a vibration particle, placing wool between the note block and the allay can prevent this interaction.

### Fuel
Note blocks can be used as a fuel in furnaces, smelting 1.5 items per block.

## Data values
### ID
Java Edition:

| Name       | Identifier | Form         | Translation key            |
|------------|------------|--------------|----------------------------|
| Note Block | note_block | Block & Item | block.minecraft.note_block |

Bedrock Edition:

| Name       | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key     |
|------------|------------|------------|----------------------------|----------------|---------------------|
| Note Block | noteblock  | 25         | Block & Giveable Item[i 2] | Identical[i 3] | tile.noteblock.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


| Name         | Savegame ID |
|--------------|-------------|
| Block entity | Music       |

### Block states
See also: Block states

Java Edition:

| Name       | Default value | Allowed values                                                                                                                                                | Description                                    |
|------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| instrument | harp          | banjobasedrumbassbellbitchimecow_bellcreepercustom_headdidgeridoodragonfluteguitarharphatiron_xylophonepiglinplingskeletonsnarewither_skeletonxylophonezombie | The instrument of the note block.              |
| note       | 0             | 0123456789101112131415161718192021222324                                                                                                                      | The pitch of the note block                    |
| powered    | false         | falsetrue                                                                                                                                                     | True if the note block is currently activated. |



### Block data
In Bedrock Edition, a note block has a block entity associated with it that holds additional data about the block.

See Bedrock Edition level format/Block entity format.

## See also
- Tutorials/Redstone music
- Tutorials/Redstone music/Doorbell
- Jukebox
- Minecraft Note Block Studio– A music editor forMinecraft.

