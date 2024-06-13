# Spawn Block
Spawn Block was a block that could be used by players in MinecraftEdu to set the world spawn point.

## Contents
- 1 Usage
- 2 Behavior
- 3 Availability
- 4 Data values
- 5 Video
- 6 History

## Usage
Placing a spawn block would update the world spawn point to that location. If a spawn block already existed in the world, the spawn point would always be overwritten in favor of the newest block. Breaking the active spawn block would reset the spawn point to the world origin, ignoring any other spawn blocks placed previously.

A spawn point set by a spawn block behaved identically to a world spawn point set by using commands. Student players also had the ability to teleport themselves to the current spawn block from their student menu. 

A spawn point defines the starting point where all new users enter the world. For detailed usage instructions refer to this article. (From MinecraftEdu wiki) 

## Behavior
- Placing the block immediately resets the spawn point and a visual note is displayed with the new coordinates.
- Destroying the spawn block does not alter the current spawn point.
- Placing multiple spawn blocks simply resets the spawn point to last location placed.
- Students cannot destroy a spawn block, even when student building is enabled.
- Teachers can break a spawn block at any time.

## Availability
- Block can be found in creative inventory. Only teachers can see this block in their inventory.
- Can also be given inTeacher menu"give" section.
- Can be distributed by console command or with acommand block.

## Data values

ID of this block is 3725.
| Name        | Identifier     | Translation key                |
|-------------|----------------|--------------------------------|
| Spawn Block | `blockSpawnMP` | `block.minecraft.blockSpawnMP` |


