# Jukebox
A jukebox is a block used to play music discs.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
- 2 Usage
	- 2.1 Playback
		- 2.1.1 Allay duplication
	- 2.2 Redstone component
		- 2.2.1 Looping
	- 2.3 Fuel
	- 2.4 Note blocks
	- 2.5 Piston interactivity
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Metadata
	- 4.3 Block states
	- 4.4 Block data
- 5 Achievements
- 6 Advancements
- 7 History
- 8 Gallery
	- 8.1 Screenshots
- 9 Issues
- 10 Trivia
- 11 See also
- 12 References
- 13 External links

## Obtaining
### Breaking
A jukebox can be broken using any tool, but an axe is the fastest. Jukeboxes also drop all of their contents.

| Block     | Jukebox               |
|-----------|-----------------------|
| Hardness  | 2                     |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 3                     |
| Wooden    | 1.5                   |
| Stone     | 0.75                  |
| Iron      | 0.5                   |
| Diamond   | 0.4                   |
| Netherite | 0.35                  |
| Golden    | 0.25                  |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Crafting
| Ingredients            | Crafting recipe |
|------------------------|-----------------|
| AnyPlanks+<br/>Diamond |                 |

## Usage
### Playback
Using a music disc on a jukebox inserts the disc and plays music corresponding to the type of music disc used. Pressing use on the jukebox again ejects the disc and stops any music playing. Music discs play only once before they must be ejected and reinserted. Note particles emit out the top when sound is playing. Unlike most other blocks, the sound from the jukebox can be heard from up to 64 blocks away.

Hoppers and droppers can be used to insert a disc into a jukebox.

Tamed parrots and allays dance when in a 3 block radius from a jukebox that's playing a disc. 

#### Allay duplication
If an amethyst shard is used on an allay dancing next to a playing jukebox, the allay consumes the amethyst shard, emits heart particles, and duplicates into two allays. Both allays have a 5-minute cooldown before they can be duplicated again.

### Redstone component
See also: Redstone circuit

Active jukeboxes emit a redstone signal when a redstone comparator is placed directly behind it or through an adjoining block; its strength depends on the ID of the inserted disc. The following table shows the redstone strength output for each disc.

| Power level | Disc                    |
|-------------|-------------------------|
| 0           | No disc inserted        |
| 1           | "13"                    |
| 2           | "cat"                   |
| 3           | "blocks"                |
| 4           | "chirp"                 |
| 5           | "far"                   |
| 6           | "mall"                  |
| 7           | "mellohi"               |
| 8           | "stal"                  |
| 9           | "strad"                 |
| 10          | "ward"                  |
| 11          | "11"                    |
| 12          | "wait"                  |
| 13          | "Pigstep"               |
| 14          | "otherside"<br/>"Relic" |
| 15          | "5"                     |

They also emit a redstone signal when any music disc is played inside.

#### Looping
Jukeboxes disable adjacent hoppers when a music disc is playing inside them, due to them emitting a redstone signal even without using a comparator. When the song ends, the hopper placed below the jukebox is re-enabled, so the disc is automatically ejected and stored in the hopper. A system of hoppers and droppers can then be used to automatically re-insert the disc, causing it to loop.

If the hopper under the jukebox is powered by anything else, it does not eject the disc, breaking the loop.

### Fuel
Jukeboxes can be used as a fuel in furnaces, smelting 1.5 items per block.

### Note blocks
Jukeboxes can be placed under note blocks to produce "bass" sounds.

### Piston interactivity
Jukeboxes cannot be pushed by pistons. They also cannot be pushed or pulled by sticky pistons.

## Data values
### ID
Java Edition:

| Name    | Identifier | Form         | Translation key           |
|---------|------------|--------------|---------------------------|
| Jukebox | `jukebox`  | Block & Item | `block.minecraft.jukebox` |

| Name         | Identifier |
|--------------|------------|
| Block entity | `jukebox`  |

Bedrock Edition:

| Name    | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key     |
|---------|------------|------------|----------------------------|----------------|---------------------|
| Jukebox | `jukebox`  | `84`       | Block & Giveable Item[i 2] | Identical[i 3] | `tile.jukebox.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

| Name         | Savegame ID |
|--------------|-------------|
| Block entity | `Jukebox`   |

### Metadata
See also: Data values

|  | DV | Description      |
|--|----|------------------|
|  | 0  | No disc inserted |
|  | 1  | Contains a disc  |

The associated block entity is used to identify which record has been inserted.

### Block states
See also: Block states

Java Edition:

| Name       | Default value | Allowed values     | Description                                 |
|------------|---------------|--------------------|---------------------------------------------|
| has_record | `false`       | `false`<br/>`true` | True when the jukebox contains amusic disc. |



### Block data
A jukebox has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format

- Block entity data
	- 
	- Tags common to all block entities
	- IsPlaying: Whether the record is currently playing.
	- RecordItem: The item, without the Slot tag.
		- 
		- Tags common to all items
	- RecordStartTick: Value of TickCount when the record started playing.
	- TickCount: Count of the number of record-playing ticks this jukebox has processed. Increments only while a record is loaded, whether playing or not.

Bedrock Edition:

SeeBedrock Edition level format/Block entity format.

