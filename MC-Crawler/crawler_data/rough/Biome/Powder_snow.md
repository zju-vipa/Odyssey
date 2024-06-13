# Powder Snow
Powder snow is a block found in snowy slopes and grove biomes, or collected from snowfall using cauldrons. Players and most mobs fall through powder snow and take freezing damage within it, but leather boots can be worn to stand on and climb through it as well as gain freezing immunity. Powder snow can only be obtained using a bucket.

## Contents
- 1 Obtaining
	- 1.1 Natural generation
	- 1.2 Cauldrons
	- 1.3 Bucket
	- 1.4 Breaking
- 2 Usage
	- 2.1 Freezing
	- 2.2 Preventing fall damage
	- 2.3 Piston interactivity
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
- 5 Advancements
- 6 History
	- 6.1 Powder Snow "items"
- 7 Issues
- 8 Gallery
	- 8.1 Screenshots
- 9 References
- 10 External links

## Obtaining
### Natural generation
Powder snow naturally generates in groves and snowy slopes in strip formations. Powder snow cannot have a snow layer placed on it.

Powder snow can also naturally generate in certain rooms in trial chambers.‌[upcoming]


### Cauldrons
Main article: Tutorials/Powder snow farming
A cauldron in a snowy biome under open sky fills with powder snow when it is snowing. Powder snow can then be picked up from this cauldron with an empty bucket.

### Bucket
Using a powder snow bucket places powder snow; placed powder snow can be picked up again with an empty bucket. These actions can be automated using a dispenser. When picked up, breaking particles appear.‌[Java Edition  only][1]

### Breaking
Powder snow does not drop anything when mined, even with Silk Touch, and tools do not speed up mining.[2][3]

| Block    | Powder Snow         |
|----------|---------------------|
| Hardness | 0.25                |
|          | Breakingtime (secs) |
| Default  | 0.4                 |

Powder snow is broken by water or lava, or when shot with a Flame-enchanted bow.

## Usage
The frosty vignette when a player is within powder snow.
All entities (except rabbits, endermites, silverfish, shulkers, vexes and foxes) fall through powder snow and move much slower in it, similar to cobwebs. Powder snow does not cause suffocation damage.

Mobs, armor stands or players wearing leather boots, however, do not fall through powder snow. In this case, the snow behaves as scaffolding when the player sneaks or crouches while on the block and jumps while inside of the block. Regardless of if the entity is wearing leather boots, all fall damage is negated when falling on top of powder snow. It is impossible to climb out of powder snow without leather boots. While moving through powder snow, snowflake particles appear.

Most walking mobs (except for goats) treat powder snow as normal solid blocks while pathfinding, similar to trapdoors, allowing them to voluntarily walk into it, and fall through it if possible.[4] Goats avoid powder snow, although they are not immune to falling through it and taking freezing damage.

If an entity that is on fire touches powder snow, powder snow cools it down as the powder snow melts.

Being fully inside a block causes a thick fog effect around the point of view. Players in Spectator mode can see through powder snow without any fogging effect.

When powder snow is on top of grass blocks, mycelium or podzol, the blocks below change to a snowy texture, similar to when snow layers are on top;[5] they revert to their default textures when the powder snow is removed. This change can be detected by observers.

### Freezing
For the Minecraft Dungeons enchantment, see MCD:Freezing.

Freezing hearts when the player is in powder snow.
Freezing hearts when the player is in Hardcore.
Powder snow converting a skeleton into a stray.
When an entity is inside a powder snow block, they begin to freeze and shake, taking damage.

A player submerged in powder snow sees a frosty vignette slowly fade in at the sides of the screen and the FOV slowly decreases. When the vignette is fully shown, the player begins shivering visibly. After seven seconds (140 game ticks), the player's hearts change to a cyan frosty texture (), and the player begins taking damage at a rate of 1 every two seconds (40 game ticks). When an entity dies of freezing damage, a message appears, saying [entity] froze to death. If the player leaves the powder snow block, the vignette slowly fades away. A frozen player moves slower than usual until the vignette fully fades away. This is controlled by the "TicksFrozen" data tag, which increases by 1 every tick (to a maximum of 140) for an entity within the powder snow block. It decreases at a rate of 2 per tick after the entity leaves the powder snow block. As such, if the player reenters powder snow while they are still frozen, they resume freezing and start taking freezing damage based on the value of "TicksFrozen". This is currently not a separate effect when used with commands such as /effect give freezing, and does not have its own unique art, particles, or potion.

Players do not take freezing damage if the game rule freezeDamage is set to false.

Wearing any piece of leather armor stops the freezing effect and reverses the damage. This applies to entities that can wear armor, such as players, zombies and horses wearing leather horse armor. If the leather armor is put on while the entity already has the freezing effect, the effect fades away the same as if the entity exited the powder snow.

Snow golems, strays, polar bears, withers, and ender dragons are immune to freezing damage. Fire-related mobs like striders, magma cubes, and blazes take 5 every two seconds (40 game ticks) from freezing.

Skeletons turn into strays instead of taking freezing damage.

### Preventing fall damage
Similar to water, powdered snow resets the fall distance of players and mobs falling into it, and can be used to prevent fall damage. It is superior to water in that it can be used in the Nether. Damage is also negated when falling onto carpet placed over powdered snow.

### Piston interactivity
Despite not being a solid block, powder snow can be pushed and pulled by pistons like most solid blocks. This makes it the only block that can be placed and retrieved by dispensers, while also pushable by pistons.

## Data values
### ID
Java Edition:

| Name        | Identifier    | Form  | Block tags                            | Translation key               |
|-------------|---------------|-------|---------------------------------------|-------------------------------|
| Powder Snow | `powder_snow` | Block | `inside_step_sound_blocks`<br/>`snow` | `block.minecraft.powder_snow` |

Bedrock Edition:

| Name        | Identifier    | Numeric ID | Form                         | Item ID[i 1]   | Translation key         |
|-------------|---------------|------------|------------------------------|----------------|-------------------------|
| Powder Snow | `powder_snow` | `561`      | Block & Ungiveable Item[i 2] | Identical[i 3] | `tile.powder_snow.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Unavailable with /give command
3. ↑The block's direct item form has the same id as the block.

