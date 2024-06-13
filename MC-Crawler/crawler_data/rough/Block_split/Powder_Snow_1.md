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


