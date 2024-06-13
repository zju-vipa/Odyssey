# Sound
Sounds are auditory outputs of the game intended to communicate the happening of certain events, as well as create atmosphere. Different objects such as mobs, weapons or blocks have sounds.

## Contents
- 1 Gameplay
	- 1.1 Mood
	- 1.2 Commands
- 2 Categories
	- 2.1 Entity-dependent categories
- 3 Accessibility
	- 3.1 Subtitles
- 4 Data values
- 5 History
- 6 Trivia
- 7 Gallery
- 8 References

## Gameplay
In Java Edition, up to 255 sounds can be played at once but general sounds can take only 247 slots, with mood slots taking the remaining 8 slots. In Bedrock Edition, up to 32 sounds can be played at the same time.[1]

Most sounds can be heard from up to 16 blocks away, with the exception of:

- Note Blocks, which can be heard up to 48 blocks away.
- Jukeboxes, which can be heard up to 64 blocks away.
- Global sound events, which is played for every player at the same volume, regardless of distance. These include:
	- When anend portalopens
	- When theender dragondies
	- When awitherfinishes charging up[2]
	- When aguardianattacks[3]

In Java Edition, these global sound events can be disabled by setting the game rule globalSoundEvents to false.

### Mood
Main article: Ambience
Mood is a special group of sounds that play after an internal counter reaches 100%, visible on the debug screen, activating only when the player is in light level 0.

### Commands
Sounds can be played and stopped with the /playsound and /stopsound commands.

## Categories
| Sound Name                                            | Technical Name   | Description                                                                                                                                   |
|-------------------------------------------------------|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Master Volume‌[JE  only]<br/>Main‌[BE  only]          | `master`[verify] | Controls the overall volume of the entire game.                                                                                               |
| Sound‌[BE  only]                                      | -                | Bedrock Editiononly, controls the volume of certian special sounds including GUI sounds, and sounds with an invalid category.                 |
| Music                                                 | `music`          | Controls the volume of the in-gamesoundtrack.                                                                                                 |
| Jukebox/Note Blocks                                   | `record`         | Controls the volume ofjukeboxesandnote blocks.                                                                                                |
| Weather                                               | `weather`        | Contols the volume ofrainandthunder.[note 1]                                                                                                  |
| Blocks                                                | `block`          | Controls the volume ofblock interactionandpassive block sounds.This includes redstone, fluids, player interaction with blocks and explosions. |
| Hostile Creatures                                     | `hostile`        | Controls the volume of allmonstersand bosses.                                                                                                 |
| Friendly Creatures                                    | `neutral`        | Controls the volume of all non-monsterentities; mostlyanimals.                                                                                |
| Players                                               | `player`         | Controls the volume of player movement, throwing/shooting projectiles and interaction withentities.                                           |
| Ambient/Enviroment                                    | `ambient`        | Controls the volume ofambienceand firework rockets going off.                                                                                 |
| Voice/Speech‌[JE  only]<br/>Text to Speech‌[BE  only] | `voice`[verify]  | Controls the volume of thenarrator.                                                                                                           |

1. ↑A custom snow sound is also affected, but normally not noticeable because snow is silent by default.

### Entity-dependent categories

  

This feature is exclusive to  Java Edition. 


Some sounds choose their category based on the entity that performs the action. For example, if a vindicator steps on a block, the step sound is in the Hostile Creatures category, but if a player steps on a block, the step is in the Players category.

## Accessibility
See also: Narrator

### Subtitles

  

This feature is exclusive to  Java Edition. 


Main article: Subtitles
Subtitles display text for in-game sounds in the bottom-right corner of the screen. They also add arrows next to the sounds that show the general direction that the sound came from. They allow deaf people to not be at an extreme disadvantage, as well as to aid other players in knowing where sounds came from. Subtitles can be toggled in the Music & Sounds and Accessibility Settings option menus.

## Data values
Main article: Sound events
All sound events have names, such as block.stone.hit ‌[Java Edition  only] or step.stone ‌[Bedrock Edition  only].


