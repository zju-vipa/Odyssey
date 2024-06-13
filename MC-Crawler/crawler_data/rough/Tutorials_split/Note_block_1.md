#### Instruments
The instrument played depends on the material of the block underneath the note block. Note that these are groups of blocks defined by the code, not just the individual block.

##### Mob heads
When a mob head is placed on top of a note block, the sound made by the note block becomes that of the corresponding mob's ambient sound, with the exception of the creeper head, which instead causes the note block to play the primed sound.

| Block                                                                                                                                                                                                                             | Instrument                         | Range   | Sound event names (Java)                   | Sound event names (Bedrock) |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|---------|--------------------------------------------|-----------------------------|
| Material: wood                                                                                                                                                                                                                    | Bass (String Bass)                 | F♯1–F♯3 | `block.note_block.bass`                    | `note.bass`                 |
| Material: sand, gravel, concrete powder                                                                                                                                                                                           | Snare Drum                         | —       | `block.note_block.snare`                   | `note.snare`                |
| Material: glass, sea lantern, beacon                                                                                                                                                                                              | Clicks and Sticks (Hihat)          | —       | `block.note_block.hat`                     | `note.hat`                  |
| Material: stone, blackstone, netherrack, nylium, obsidian, quartz, sandstone, ores, bricks, corals, respawn anchor, bedrock, concrete, stonecutter, furnace, observer, terracotta, prismarine, prismarine bricks, dark prismarine | Bass Drum (Kick)                   | —       | `block.note_block.basedrum`                | `note.bd`                   |
| Block of gold                                                                                                                                                                                                                     | Bells (Glockenspiel)               | F♯5–F♯7 | `block.note_block.bell`                    | `note.bell`                 |
| Clay,honeycomb block‌[BE  only][3],infested block‌[BE  only]                                                                                                                                                                      | Flute                              | F♯4–F♯6 | `block.note_block.flute`                   | `note.flute`                |
| Packed ice                                                                                                                                                                                                                        | Chimes                             | F♯5–F♯7 | `block.note_block.chime`                   | `note.chime`                |
| Wool                                                                                                                                                                                                                              | Guitar                             | F♯2–F♯4 | `block.note_block.guitar`                  | `note.guitar`               |
| Bone block                                                                                                                                                                                                                        | Xylophone                          | F♯5–F♯7 | `block.note_block.xylophone`               | `note.xylophone`            |
| Block of iron                                                                                                                                                                                                                     | Iron Xylophone (Vibraphone)        | F♯3–F♯5 | `block.note_block.iron_xylophone`          | `note.iron_xylophone`       |
| Soul sand                                                                                                                                                                                                                         | Cow Bell                           | F♯4–F♯6 | `block.note_block.cow_bell`                | `note.cow_bell`             |
| Pumpkin                                                                                                                                                                                                                           | Didgeridoo                         | F♯1–F♯3 | `block.note_block.didgeridoo`              | `note.didgeridoo`           |
| Block of emerald                                                                                                                                                                                                                  | "Bit" (Square wave)                | F♯3–F♯5 | `block.note_block.bit`                     | `note.bit`                  |
| Hay bale                                                                                                                                                                                                                          | Banjo                              | F♯3–F♯5 | `block.note_block.banjo`                   | `note.banjo`                |
| Glowstone                                                                                                                                                                                                                         | "Pling" (Electric piano)           | F♯3–F♯5 | `block.note_block.pling`                   | `note.pling`                |
| Skeleton skull                                                                                                                                                                                                                    | "Skeleton"                         | -       | `block.note_block.imitate.skeleton`        | `note.skeleton`             |
| Wither skeleton skull                                                                                                                                                                                                             | "Wither Skeleton"                  | -       | `block.note_block.imitate.wither_skeleton` | `note.witherskeleton`       |
| Player head                                                                                                                                                                                                                       | Sound event set innote_block_sound | -       | Dependent                                  | Dependent                   |
| Zombie head                                                                                                                                                                                                                       | "Zombie"                           | -       | `block.note_block.imitate.zombie`          | `note.zombie`               |
| Creeper head                                                                                                                                                                                                                      | "Creeper"                          | -       | `block.note_block.imitate.creeper`         | `note.creeper`              |
| Piglin head                                                                                                                                                                                                                       | "Piglin"                           | -       | `block.note_block.imitate.piglin`          | `note.piglin`               |
| Dragon head                                                                                                                                                                                                                       | "Ender Dragon"                     | -       | `block.note_block.imitate.ender_dragon`    | `note.enderdragon`          |
| Any other blocks                                                                                                                                                                                                                  | Harp / piano                       | F♯3–F♯5 | `block.note_block.harp`                    | `note.harp`                 |

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

| Name       | Identifier   | Form         | Translation key              |
|------------|--------------|--------------|------------------------------|
| Note Block | `note_block` | Block & Item | `block.minecraft.note_block` |

Bedrock Edition:

| Name       | Identifier  | Numeric ID | Form                       | Item ID[i 1]   | Translation key       |
|------------|-------------|------------|----------------------------|----------------|-----------------------|
| Note Block | `noteblock` | `25`       | Block & Giveable Item[i 2] | Identical[i 3] | `tile.noteblock.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

| Name         | Savegame ID |
|--------------|-------------|
| Block entity | `Music`     |

### Block states
See also: Block states

Java Edition:

| Name       | Default value | Allowed values                                                                                                                                                                                                                                                                                                            | Description                                    |
|------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| instrument | `harp`        | `banjo`<br/>`basedrum`<br/>`bass`<br/>`bell`<br/>`bit`<br/>`chime`<br/>`cow_bell`<br/>`creeper`<br/>`custom_head`<br/>`didgeridoo`<br/>`dragon`<br/>`flute`<br/>`guitar`<br/>`harp`<br/>`hat`<br/>`iron_xylophone`<br/>`piglin`<br/>`pling`<br/>`skeleton`<br/>`snare`<br/>`wither_skeleton`<br/>`xylophone`<br/>`zombie` | The instrument of the note block.              |
| note       | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15`<br/>`16`<br/>`17`<br/>`18`<br/>`19`<br/>`20`<br/>`21`<br/>`22`<br/>`23`<br/>`24`                                                                                                        | The pitch of the note block                    |
| powered    | `false`       | `false`<br/>`true`                                                                                                                                                                                                                                                                                                        | True if the note block is currently activated. |



### Block data
In Bedrock Edition, a note block has a block entity associated with it that holds additional data about the block.

See Bedrock Edition level format/Block entity format.


