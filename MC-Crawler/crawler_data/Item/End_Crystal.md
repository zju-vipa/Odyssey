# End Crystal
An end crystal is an entity that can be crafted or found on the End's main island, where it heals the ender dragon. It can be placed only on obsidian or bedrock and explodes instantly when attacked or damaged in most ways.

## Contents
- 1 Spawning
	- 1.1 Natural generation
- 2 Obtaining
	- 2.1 Crafting
- 3 Usage
	- 3.1 Healing the ender dragon
	- 3.2 Respawning the ender dragon
	- 3.3 Explosions
	- 3.4 Beams
	- 3.5 Properties
- 4 Sounds
- 5 Data values
	- 5.1 ID
	- 5.2 Entity data
- 6 Achievements
- 7 Advancements
- 8 History
- 9 Issues
- 10 Trivia
- 11 Gallery
	- 11.1 Screenshots
- 12 References

## Spawning
### Natural generation
An end crystal is found atop each obsidian pillar on the central island of the End, each on top of a piece of bedrock. There are 10 end crystals in total, of which two are protected in "cages" of iron bars. All end crystals respawn one after another as the respawning process of the ender dragon starts.

## Obtaining
### Crafting
| Ingredients                   | Crafting recipe |
|-------------------------------|-----------------|
| Glass+Eye of Ender+Ghast Tear |                 |

## Usage
### Healing the ender dragon
Their primary purpose is to recharge the health of the ender dragon, who gains a charge from the nearest crystal within a cuboid extending 32 blocks from the dragon in all directions. The dragon is healed 1 each half-second. If multiple ender dragons are spawned, an end crystal can affect multiple dragons at the same time. The healing beam is neither obstructed nor is its power diminished by entities or blocks.

### Respawning the ender dragon
How to arrange end crystals on the exit portal to respawn the ender dragon.
As items, end crystals may be placed on bedrock and obsidian, if the two blocks above the bedrock or obsidian block are air or replaceable blocks and no other entities intersect the area. When an end crystal is placed in the End, a fire block is created at the end crystal location. If four are placed on the end exit portal, one on each of the flat sides, the crystals respawn the original end crystals on the obsidian pillars, as well as resurrect the dragon itself, before exploding. The top of each pillar also explodes, destroying any player-placed blocks. This happens even if TNT explosions are turned off in settings.

If the exit portal is ever broken for any reason, end crystals can still be placed on obsidian blocks with the same location as the exit portal.

### Explosions
End crystals explode when attacked or damaged in most ways, even by attacks that normally do zero damage. They are not affected by exploding fireworks, and if damaged by an explosion, they disappear instead of exploding.‌[Java Edition  only][1] The end crystal's explosion has an explosion strength of 6, the same as a charged creeper. The end crystal's fire often remains after the crystal explodes. Any ender dragon charging from the crystal when it is destroyed takes 10 damage.

In Java Edition, an end crystal's explosion can be blocked by a shield.

Although an ender dragon damages most blocks and entities in its path, it cannot destroy end crystals simply by going near them.

Placing water on the end crystal neutralizes the blast effect, but not the damage or knockback.

End crystals with obsidian or bedrock below them do not damage blocks below them when they explode.

In Bedrock Edition, having the game rule mobGriefing to false prevents the end crystal from destroying any blocks, while in Java Edition the same game rule does not prevent the end crystal from destroying any blocks.

### Beams
The end crystal naturally shoots a beam at the ender dragon and heals it when the dragon is within range. This beam can be manually created using the command /data merge entity @e[type=end_crystal,limit=1] {BeamTarget:{X:0, Y:0, Z:0}}. The beam can be pointed in any direction, allowing it to mark locations or objects.

### Properties
A base-less end crystal.
End crystals are of two kinds: the ones with a base beneath them are created either by game mechanism or by the /summon command; while the base-less ones are created by players by manually placing the crystal items on top of obsidian or bedrock.

The base appears to be made of bedrock, with a crystal hovering over it. While in the End, a crystal continually generates fire at its current position, one block above the base (directly on top of the block the base is embedded in), replacing any other block at that location. This fire is capable of spreading.

The end crystal entity is not solid and can be walked through freely. End crystals can be pushed by pistons, but they explode if moved while on fire. Because fire is checked only when an entity moves, end crystals do not normally take damage from their own fire unless moved.

## Data values
### ID
Java Edition:

| Item        | Identifier  | Form | Translation key            |
|-------------|-------------|------|----------------------------|
| End Crystal | end_crystal | Item | item.minecraft.end_crystal |

| Entity      | Identifier  | Translation key              |
|-------------|-------------|------------------------------|
| End Crystal | end_crystal | entity.minecraft.end_crystal |

Bedrock Edition:

| Item        | Identifier  | Numeric ID | Form | Translation key       |
|-------------|-------------|------------|------|-----------------------|
| End Crystal | end_crystal | 637        | Item | item.end_crystal.name |

| Entity      | Identifier    | Numeric ID | Translation key           |
|-------------|---------------|------------|---------------------------|
| End Crystal | ender_crystal | 71         | entity.ender_crystal.name |

### Entity data
End crystals have entity data that define various properties of the entity.

Java Edition:

Main article: Entity format

 Entity data
Tags common to all entities
 BeamTarget: The block location its beam points to.
 X: X-coordinate.
 Y: Y-coordinate.
 Z: Z-coordinate.
 ShowBottom: 1 or 0 (true/false) – if true, the end crystal shows the bedrock slate underneath. Defaults to false when placing by hand, and true when naturally generated or using /summon.

Bedrock Edition:

See Bedrock Edition level format/Entity format.
