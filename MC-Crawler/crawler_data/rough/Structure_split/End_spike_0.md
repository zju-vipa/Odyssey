# End spike
End spikes, also known as obsidian spikes, obsidian pillars, obsidian towers, and end pillars are a feature in the End biome that are made of obsidian.

## Contents
- 1 Generation
- 2 Construction
- 3 Data values
	- 3.1 ID
	- 3.2 Config
- 4 History
- 5 Issues
- 6 Gallery
	- 6.1 Screenshots
- 7 See also

## Generation
End spikes generate naturally the first time the player enters the End, and regenerate when the ender dragon is respawned.

When the ender dragon respawns, any blocks the player had placed within 10 blocks in all directions of the bedrock block at the top of the end spikes are deleted, as well as blocks inside the square containing the edge of the pillar down to Y=66.

## Construction
Main article: /Structure
End spikes are composed of obsidian, with a single bedrock block, fire block and an end crystal on top of each pillar. They have cylindrical forms.

The following 10 pillars generate in a 43-block radius circle around the exit portal in a random order (total of 40499 obsidian):

- A 3-block radius pillar ending at Y=76 (total of 1596 blocks of obsidian);
- A 3-block radius pillar with iron bars ending at Y=79 (total of 1659 blocks of obsidian);
- A 3-block radius pillar with iron bars ending at Y=82 (total of 1722 blocks of obsidian);
- A 4-block radius pillar ending at Y=85 (total of 3145 blocks of obsidian);
- A 4-block radius pillar ending at Y=88 (total of 3256 blocks of obsidian);
- A 4-block radius pillar ending at Y=91 (total of 3367 blocks of obsidian);
- A 5-block radius pillar ending at Y=94 (total of 5358 blocks of obsidian);
- A 5-block radius pillar ending at Y=97 (total of 5529 blocks of obsidian);
- A 5-block radius pillar ending at Y=100 (total of 5700 blocks of obsidian);
- A 6-block radius pillar ending at Y=103 (total of 9167 blocks of obsidian).

The bottom of all pillars are at Y level 0, which means that pillars are generated through the island. If the End biome is used in the Overworld, end spikes generate all the way down to Y=-64, replacing all other blocks, including bedrock.

The second and third shortest pillars include a cage comprised of 73 iron bars surrounding the end crystal, to protect it from projectiles.

## Data values
### ID
Java Edition:

| Feature type        | Identifier  |
|---------------------|-------------|
| [No displayed name] | `end_spike` |

| Configured feature  | Identifier  |
|---------------------|-------------|
| [No displayed name] | `end_spike` |

Bedrock Edition:

| Feature             | Identifier |
|---------------------|------------|
| [No displayed name] | `[No ID]`  |

### Config
Main article: Configured feature
Java Edition:

- config
	- crystal_invulnerable(optional, defaults to false) Whether the end crystals on it are invulnerable.
	- crystal_beam_target(optional) Block position of the beam target.
		- The X coordinate.
		- The Y coordinate.
		- The Z coordinate.
	- spikes(Required, but can be empty. If empty, uses the default random spikes) Configurations of each spike.
		- A spike.
			- centerX(optional, defaults to 0) The X coordinate.
			- centerZ(optional, defaults to 0)  The Z coordinate.
			- radius(optional, defaults to 0)  The radius of the spike.
			- height(optional, defaults to 0)  The height of the spike.
			- guarded(optional, defaults to false)  Whether to generate an iron bar cage around the crystal.




An example

{
  "type": "minecraft:end_spike",
  "config": {
    "crystal_invulnerable": false,
    "spikes": []
  }
}




