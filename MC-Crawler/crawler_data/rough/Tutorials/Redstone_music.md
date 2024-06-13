# Tutorials/Redstone music
This is a tutorial on how to make songs or special sounds with note blocks and redstone. Once you know the basics of redstone music, you can make an infinite number of songs.

## Contents
- 1 Basics
	- 1.1 Tips
	- 1.2 Redstone
- 2 Translating real music
	- 2.1 Pitch
	- 2.2 Rhythm
	- 2.3 Sounds
- 3 Songs and sounds
	- 3.1 "Choo Choo" Train
	- 3.2 Twinkle Twinkle Little Star
	- 3.3 The Star Spangled Banner
- 4 External software
	- 4.1 Note Block Studio
- 5 See also

## Basics
- Use aredstonesignal to play the sound
- Right-click to change the pitch of the note block
- Remember that redstone dust activates all of theblocksaround it, not just one.
- Always remember that you need ablockof space above a note block.

### Tips
- Be careful withwateras it destroysredstoneon contact.
- If you have a lot of redstone, it might be helpful to color code or label what part does what in case it breaks.
- You can usepistonsto start/stop the song.
- You can usebuttonsto start/stop instead oflevers.
- It is possible to make a song with a certain section that keeps repeating until a signal comes through and moves to the next thing. This is achievable by making a closed circuit usingredstone,repeaters, andnote blocks, and use ahopper timerto time when to open the circuit and continue the song.

### Redstone
By placing repeaters and note blocks in lines, it is possible to play multiple times.
Another way is to put note blocks under detector rails, so as you ride along you can play the song of your choice!

## Translating real music
When making redstone music in vanilla Minecraft, it's very helpful to know how you can translate sheet music you find online into an actual note block circuit. The main two factors of music are rhythm and pitch. Rhythm is determined by how many repeaters you put before/after a note block, and how many ticks you set them to, and pitch is determined by how many times you right click a note block. Once you know how rhythm and pitches relate to ticks and note blocks, you can make an infinite number of songs.

### Pitch
Main article: Note Block § Notes
Pitch is one of the most important factors of music. Here is a table of how all notes in music that are able to be played on Minecraft can be simulated with note blocks. The table shows how many times to press the noteblock to get the desired pitch.

| Pitch         | String bass | Bell | Flute | Chime | Guitar | Xylophone | Iron xylophone | Cow bell | Didgeridoo | "Bit" | Banjo | "Pling" | Harp/piano |
|---------------|-------------|------|-------|-------|--------|-----------|----------------|----------|------------|-------|-------|---------|------------|
| F♯1/G♭1       | 0           |      |       |       |        |           |                |          | 0          |       |       |         |            |
| G1            | 1           |      |       |       |        |           |                |          | 1          |       |       |         |            |
| G♯1/A♭1       | 2           |      |       |       |        |           |                |          | 2          |       |       |         |            |
| A1            | 3           |      |       |       |        |           |                |          | 3          |       |       |         |            |
| A♯1/B♭1       | 4           |      |       |       |        |           |                |          | 4          |       |       |         |            |
| B1            | 5           |      |       |       |        |           |                |          | 5          |       |       |         |            |
| C2 (low C)    | 6           |      |       |       |        |           |                |          | 6          |       |       |         |            |
| C♯2/D♭2       | 7           |      |       |       |        |           |                |          | 7          |       |       |         |            |
| D2            | 8           |      |       |       |        |           |                |          | 8          |       |       |         |            |
| D♯2/E♭2       | 9           |      |       |       |        |           |                |          | 9          |       |       |         |            |
| E2            | 10          |      |       |       |        |           |                |          | 10         |       |       |         |            |
| F2            | 11          |      |       |       |        |           |                |          | 11         |       |       |         |            |
| F♯2/G♭2       | 12          |      |       |       | 0      |           |                |          | 12         |       |       |         |            |
| G2            | 13          |      |       |       | 1      |           |                |          | 13         |       |       |         |            |
| G♯2/A♭2       | 14          |      |       |       | 2      |           |                |          | 14         |       |       |         |            |
| A2            | 15          |      |       |       | 3      |           |                |          | 15         |       |       |         |            |
| A♯2/B♭2       | 16          |      |       |       | 4      |           |                |          | 16         |       |       |         |            |
| B2            | 17          |      |       |       | 5      |           |                |          | 17         |       |       |         |            |
| C3            | 18          |      |       |       | 6      |           |                |          | 18         |       |       |         |            |
| C♯3/D♭3       | 19          |      |       |       | 7      |           |                |          | 19         |       |       |         |            |
| D3            | 20          |      |       |       | 8      |           |                |          | 20         |       |       |         |            |
| D♯3/E♭3       | 21          |      |       |       | 9      |           |                |          | 21         |       |       |         |            |
| E3            | 22          |      |       |       | 10     |           |                |          | 22         |       |       |         |            |
| F3            | 23          |      |       |       | 11     |           |                |          | 23         |       |       |         |            |
| F♯3/G♭3       | 24          |      |       |       | 12     |           | 0              |          | 24         | 0     | 0     | 0       | 0          |
| G3            |             |      |       |       | 13     |           | 1              |          |            | 1     | 1     | 1       | 1          |
| G♯3/A♭3       |             |      |       |       | 14     |           | 2              |          |            | 2     | 2     | 2       | 2          |
| A3            |             |      |       |       | 15     |           | 3              |          |            | 3     | 3     | 3       | 3          |
| A♯3/B♭3       |             |      |       |       | 16     |           | 4              |          |            | 4     | 4     | 4       | 4          |
| B3            |             |      |       |       | 17     |           | 5              |          |            | 5     | 5     | 5       | 5          |
| C4 (middle C) |             |      |       |       | 18     |           | 6              |          |            | 6     | 6     | 6       | 6          |
| C♯4/D♭4       |             |      |       |       | 19     |           | 7              |          |            | 7     | 7     | 7       | 7          |
| D4            |             |      |       |       | 20     |           | 8              |          |            | 8     | 8     | 8       | 8          |
| D♯4/E♭4       |             |      |       |       | 21     |           | 9              |          |            | 9     | 9     | 9       | 9          |
| E4            |             |      |       |       | 22     |           | 10             |          |            | 10    | 10    | 10      | 10         |
| F4            |             |      |       |       | 23     |           | 11             |          |            | 11    | 11    | 11      | 11         |
| F♯4/G♭4       |             |      | 0     |       | 24     |           | 12             | 0        |            | 12    | 12    | 12      | 12         |
| G4            |             |      | 1     |       |        |           | 13             | 1        |            | 13    | 13    | 13      | 13         |
| G♯4/A♭4       |             |      | 2     |       |        |           | 14             | 2        |            | 14    | 14    | 14      | 14         |
| A4            |             |      | 3     |       |        |           | 15             | 3        |            | 15    | 15    | 15      | 15         |
| A♯4/B♭4       |             |      | 4     |       |        |           | 16             | 4        |            | 16    | 16    | 16      | 16         |
| B4            |             |      | 5     |       |        |           | 17             | 5        |            | 17    | 17    | 17      | 17         |
| C5            |             |      | 6     |       |        |           | 18             | 6        |            | 18    | 18    | 18      | 18         |
| C♯5/D♭5       |             |      | 7     |       |        |           | 19             | 7        |            | 19    | 19    | 19      | 19         |
| D5            |             |      | 8     |       |        |           | 20             | 8        |            | 20    | 20    | 20      | 20         |
| D♯5/E♭5       |             |      | 9     |       |        |           | 21             | 9        |            | 21    | 21    | 21      | 21         |
| E5            |             |      | 10    |       |        |           | 22             | 10       |            | 22    | 22    | 22      | 22         |
| F5            |             |      | 11    |       |        |           | 23             | 11       |            | 23    | 23    | 23      | 23         |
| F♯5/G♭5       |             | 0    | 12    | 0     |        | 0         | 24             | 12       |            | 24    | 24    | 24      | 24         |
| G5            |             | 1    | 13    | 1     |        | 1         |                | 13       |            |       |       |         |            |
| G♯5/A♭5       |             | 2    | 14    | 2     |        | 2         |                | 14       |            |       |       |         |            |
| A5            |             | 3    | 15    | 3     |        | 3         |                | 15       |            |       |       |         |            |
| A♯5/B♭5       |             | 4    | 16    | 4     |        | 4         |                | 16       |            |       |       |         |            |
| B5            |             | 5    | 17    | 5     |        | 5         |                | 17       |            |       |       |         |            |
| C6 (high C)   |             | 6    | 18    | 6     |        | 6         |                | 18       |            |       |       |         |            |
| C♯6/D♭6       |             | 7    | 19    | 7     |        | 7         |                | 19       |            |       |       |         |            |
| D6            |             | 8    | 20    | 8     |        | 8         |                | 20       |            |       |       |         |            |
| D♯6/E♭6       |             | 9    | 21    | 9     |        | 9         |                | 21       |            |       |       |         |            |
| E6            |             | 10   | 22    | 10    |        | 10        |                | 22       |            |       |       |         |            |
| F6            |             | 11   | 23    | 11    |        | 11        |                | 23       |            |       |       |         |            |
| F♯6/G♭6       |             | 12   | 24    | 12    |        | 12        |                | 24       |            |       |       |         |            |
| G6            |             | 13   |       | 13    |        | 13        |                |          |            |       |       |         |            |
| G♯6/A♭6       |             | 14   |       | 14    |        | 14        |                |          |            |       |       |         |            |
| A6            |             | 15   |       | 15    |        | 15        |                |          |            |       |       |         |            |
| A♯6/B♭6       |             | 16   |       | 16    |        | 16        |                |          |            |       |       |         |            |
| B6            |             | 17   |       | 17    |        | 17        |                |          |            |       |       |         |            |
| C7            |             | 18   |       | 18    |        | 18        |                |          |            |       |       |         |            |
| C♯7/D♭7       |             | 19   |       | 19    |        | 19        |                |          |            |       |       |         |            |
| D7            |             | 20   |       | 20    |        | 20        |                |          |            |       |       |         |            |
| D♯7/E♭7       |             | 21   |       | 21    |        | 21        |                |          |            |       |       |         |            |
| E7            |             | 22   |       | 22    |        | 22        |                |          |            |       |       |         |            |
| F7            |             | 23   |       | 23    |        | 23        |                |          |            |       |       |         |            |
| F♯7/G♭7       |             | 24   |       | 24    |        | 24        |                |          |            |       |       |         |            |

### Rhythm
Rhythm is another important factor of music, which is basically how long a note is held for. The next table shows how many redstone ticks, using repeaters, must go after a note block, depending on the tempo of the music, and what kind of rhythm the note is. Remember; the maximum number of ticks for one repeater is 4, so if you need more than 4 ticks, you need more than one repeater. Also, the numbers you see on top is the tempo of the music, which is how many beats there are in a minute. Finally, numbers with a .5 are unobtainable with repeaters alone. The easiest way to get them is to use a sticky piston with a redstone block attached, which has a delay of 1.5 ticks. Any other fraction has no exact match.

|                       | x           | 50       | 60               | 75               | 100       | 150              |
|-----------------------|-------------|----------|------------------|------------------|-----------|------------------|
| Sixteenth note/rest   | 150/xticks  | 3 ticks  | (No exact match) | 2 ticks          | 1.5 ticks | 1 tick           |
| Triplet note/rest     | 200/xticks  | 4 ticks  | (No exact match) | (No exact match) | 2 ticks   | (No exact match) |
| Eighth note/rest      | 300/xticks  | 6 ticks  | 5 ticks          | 4 ticks          | 3 ticks   | 2 ticks          |
| Quarter note/rest     | 600/xticks  | 12 ticks | 10 ticks         | 8 ticks          | 6 ticks   | 4 ticks          |
| Half note/rest        | 1200/xticks | 24 ticks | 20 ticks         | 16 ticks         | 12 ticks  | 8 ticks          |
| Dotted half note/rest | 1800/xticks | 36 ticks | 30 ticks         | 24 ticks         | 18 ticks  | 12 ticks         |
| Whole note/rest       | 2400/xticks | 48 ticks | 40 ticks         | 32 ticks         | 24 ticks  | 16 ticks         |

If you must have your song in a tempo where triplets have no exact match, you can substitute for 2 sixteenth notes followed by an eighth note, which sound similar to triplets at faster tempos.

### Sounds
Main article: Note Block § Instruments
Different sounds can be made on note blocks by putting different types of blocks under note blocks. Here is a list of what block(s) you need to put under a note block to make it have a specific sound.

- Bass =Wood(any type),mushroom(block),daylight sensor,banner,sign,note block
- Bass drum =Stone(any type),bricks,netherrack,magma block,purpur block,concrete,nether quartz
- Bell =Block of gold
- Chime =Packed ice
- Clicks and sticks =Glass(any type),sea lantern
- Flute =Clay block
- Guitar =Wool
- Snare drum =Sand,gravel,concrete powder
- Xylophone =Bone block
- Piano (harp) = Any other block (e.g.dirt,piston,rail, leaves)
- Iron Xylophone =Block of Iron
- Cowbell =Soul Sand
- Didgeridoo =Pumpkin
- Bit =Block of Emerald
- Banjo =Hay Bale
- Pling =Glowstone

## Songs and sounds
Note blocks can be used to make sounds that may benefit playing, or to make your favorite songs.

Note: All of the songs listed here that can be made into note blocks are in the public domain, meaning their copyright has expired.

### 
Follow these steps so that you can make a sound similar to a train whistle:

1. Place a button on the ground. Place redstone behind the button. Then, place a redstone piece on either side of the first redstone; one on the left, and one on the right.
2. Place 3 repeaters, set to no delay, behind the redstone, facing away from you, so that if the redstone were to be powered, the repeaters would pick up the signal.
3. Dig out the 3 blocks behind the repeaters and replace them with clay, so that when the note block is on top of the block, it emits a flute sound.
4. Place note blocks on top of the clay. Right-click one 8 times, another 12 times, and the final one 16 times.
5. Place 3 repeaters, side by side behind the note blocks, and set them to full delay, or 4 ticks. Place another row of repeaters behind them, and right-click them once, setting them to 2 ticks.
6. Repeat steps 3 and 4 for the three blocks behind the repeaters. When you press the button, now you have a train whistle sound.This is an example of how to make a train whistle in Minecraft. For the best sounding results, put clay blocks under each of the note blocks.
7. If you want, you can turn this into a railroad crossing sound. When aminecartruns over a detector rail near the crossing, have redstone wiring connected to the note block circuit.

### Twinkle Twinkle Little Star
If you follow these steps, you can produce the basic melody for the song: "Twinkle Twinkle Little Star."

1. Choose which note block sound you would like to use. Piano/harp is probably the easiest sound to use, because the Overworld is naturally made up of grass and dirt.
2. Place a note block, and right-click it 6 times. Attach a button to the front of the note block. Behind the note block, place a repeater set on full 4-tick delay, and another one behind that set on 2-tick delay. Repeat again, behind the structure you have made so far.
3. Repeat step 2, including the part where you repeat the same pattern again, except this time, right-click the note blocks 13 times. Repeat this same thing yet again, this time right-clicking the note blocks 15 times. So far, you should have 6 note blocks. Try pressing the button. If it does not sound, make sure the repeaters are facing the right way. If it is out of tune, make sure you have tuned the note blocks correctly.
4. Place a note block behind the last repeater, and right-click it 13 times. To conserve more space, the next 3 repeaters actually go to the right of the note block. Place a repeater to the right of the note block, and then 2 more to the right of that repeater. All of the repeaters should be set to full 4-tick delay.
5. Place a note block to the right of the repeater furthest to the right, and right-click it 11 times. Then, place a repeater in front of the note block, on full 4-tick delay, and another one in front of that one, on 2-tick delay, both repeaters facing toward you. Repeat, with the repeaters, like before, facing toward you.
6. Repeat all of step 5, including the part where you repeat the same pattern again, except this time, right-click the note blocks 10 times. Then, repeat again, but this time, right-click the note blocks 8 times. Finally, place one final note block in front of the repeater closest toward you, and right-click it 6 times.
7. Press the button, and it should sound like "Twinkle Twinkle Little Star." This is only the first part of the song, so if you want the rest of it, look up sheet music (which is easy to find). Here is the pitch/rhythm guide to Twinkle Twinkle Little Star:
	- C: Right-click note block 6 times
	- D: Right-click note block 8 times
	- E: Right-click note block 10 times
	- F: Right-click note block 11 times
	- G: Right-click note block 13 times
	- A: Right-click note block 15 times.
	- Quarter note(exclusively "Twinkle Twinkle Little Star"): 4 tick repeater + 2 tick repeater (6 redstone ticks)
	- Half note(exclusively "Twinkle Twinkle Little Star"): 4 tick repeater + 4 tick repeater + 4 tick repeater (12 redstone ticks)

### The Star Spangled Banner
The following song is the first part of The United States National Anthem. Exact instructions are not included this time, so use your knowledge from the previous two songs, and look up notes/rhythms on the chart in the section titled "Translating Real Music to Minecraft Note Blocks," so that you can figure out how to tune the note blocks, how many repeaters go in between the note blocks, and what delay they are set to.

Tip: The tempo is 75, meaning that a quarter note is equal to 8 ticks, or 2 repeaters, both set to full delay.

The only instrument that has the full range of the song is harp/piano. This means that the block under each note block must be something other than wood, sand, gravel, soul sand, concrete, glass, stone, brick, gold, clay, packed ice, wool, or a bone block.

Follow the steps, in order, and use the chart in the section titled "Translating Real Music to Minecraft Note Blocks" to translate the pitches and rhythms into redstone music.

- F4, Eighth note
- D4, Eighth note
- B♭3, Quarter note
- D4, Quarter note
- F4, Quarter note
- B♭4, Half note
- D5, Eighth note
- C5, Eighth note
- B♭4, Quarter note
- D4, Quarter note
- E4, Quarter note
- F4, Half note
- F4, Eighth note
- F4, Eighth note
- D5, Quarter note
- C5, Quarter note
- B♭4, Quarter note
- A4, Half note
- G4, Eighth note
- A4, Eighth note
- B♭4, Quarter note
- B♭4, Quarter note
- F4, Quarter note
- D4, Quarter note
- B♭3, Quarter note

## External software

  


The contents of this section are not supported by Mojang Studios or the Minecraft Wiki.


One of the many ways to create note block songs is to use external software.

### Note Block Studio
See also: Programs and editors/Minecraft Note Block Studio

You can convert any song you want into a set of note blocks using an external application called Note Block Studio created by Davve.
This method also requires MCEdit to import the result into your world.

1. First of all you need a midi version of your song. A specifically-made midi version is preferred; if there are no available midi versions, you can try certain converters to convert your mp3 files to midi, but the result is often not satisfactory.
2. Second, you should open your song in Note Block Studio, which can be done by pressing 'Load' then find your.midifile and import it.
3. Then play it to see how it sounds. If, in the top right, it mentions that the input is 'Not compatible', you can fix this by clicking the button and then pressing 'Fix'.
4. Now go to File → Export as Schematic, and choose your own options there.
5. Open your world in MCEdit and Import the Schematic you just exported and place it wherever you want in your world. Wait for it to load.
6. PressCtrl+Sto save your world. Close MCEdit, and open up your Minecraft world.

