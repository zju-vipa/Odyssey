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

