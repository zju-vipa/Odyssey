# TNT
TNT is a block that can be primed by a redstone signal, flint and steel, stray fire, flaming projectile or explosion.

Primed TNT is a gravity-affected entity that produces a damaging, block-destroying explosion after a few seconds.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Container loot
	- 1.4 Crafting
- 2 Usage
	- 2.1 Behavior
	- 2.2 Redstone component
	- 2.3 Crafting ingredient
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Entity data
- 5 History
- 6 Issues
- 7 Trivia
- 8 Gallery
	- 8.1 Screenshots
- 9 See also
- 10 References
- 11 External links

## Obtaining
### Breaking
TNT can be broken instantly with any tool, or without a tool. Primed TNT cannot be broken as it is an entity, but it can be removed with the /kill command. 

### Natural generation
Nine TNT blocks occur naturally in each desert pyramid.

Two TNT blocks flank a trapped chest in one secret woodland mansion room.

### Container loot
| Item | Structure       | Container       | Quantity | Chance          |
|------|-----------------|-----------------|----------|-----------------|
|      |                 |                 |          | Java Edition    |
| TNT  | Buried Treasure | Chest           | 1–2      | 62.7%           |
|      | Desert Pyramid  | Suspicious sand | 1        | 12.5%           |
|      | Shipwreck       | Supply chest    | 1–2      | 7.5%            |
|      |                 |                 |          | Bedrock Edition |
| TNT  | Buried Treasure | Chest           | 1–2      | 34.3%           |
|      | Desert Pyramid  | Suspicious sand | 1        | 12.5%           |
|      | Shipwreck       | Supply chest    | 1–2      | 7.5%            |

### Crafting
| Ingredients                        | Crafting recipe | Description                                                 |
|------------------------------------|-----------------|-------------------------------------------------------------|
| Gunpowder+<br/>Sandor<br/>Red Sand |                 | It is possible to use any combination of sand and red sand. |

## Usage
A TNT explosion.
TNT blocks can be primed by:

- usingaflint and steelor afire charge
- using any itemenchantedwithFire Aspect
- a poweredredstonesignal
- being shot by a flaming or explosive projectile
	- being hit an arrow from abowwithFlameenchantment
	- being hit by an arrow that has traveled throughlavaorfire
	- being hit by a ghast, blaze fireball or a fire charge fired from adispenser
	- being hit by an explosive skull from aWither
- coming into contact with spreadingfireorlava
- being in the blast radius of a nearbyexplosion, including that of another TNT block, acreeper, abed, arespawn anchor, or anend crystal
- being placed by adispenser
- being lit by a flint and steel used by a dispenser
- being hit by alightningbolt
- being duplicated by aTNT duplicator

### Behavior


| Hitbox size | Height: 0.98 blocksWidth: 0.98 blocks |
|-------------|---------------------------------------|

{
    "title": "Primed TNT",
    "rows": [
        {
            "field": "Height: 0.98 blocks<br>Width: 0.98 blocks<br>",
            "label": "(link to Hitbox article, displayed as Hitbox size)"
        }
    ],
    "invimages": [],
    "images": [
        "TNT.png"
    ]
}
Once primed, TNT turns into an entity, meaning it is subject to normal entity physics, such as being affected by gravity. The primed TNT entity begins a countdown timer that lasts 40 redstone ticks (4 seconds/80 game ticks) if activated by redstone or fire, or a random number between 10 and 30 game ticks (0.5 to 1.5 seconds) if it is detonated by another explosion.

Once the fuse of the primed TNT runs out, the TNT explodes, destroying blocks and damaging entities nearby. The TNT creates an explosion with a power of 4, meaning it can destroy blocks with a blast resistance of up to 9. When primed TNT detonates while in water or lava, it does not break any blocks; In Java Edition, it still damages nearby entities.[1] Primed TNT that detonates outside water can still damage submerged blocks. In Java Edition, destroyed blocks have an 100% rate of dropping as items, unlike other explosions; in Bedrock Edition, blocks have a chance of being destroyed as usual.‌[until BE 1.21.0]

The primed TNT entity is spawned at the center (+0.5,+0.5,+0.5) of where the ignited TNT block was. Once spawned, primed TNT is given a vertical velocity of 0.2 blocks per tick, and a horizontal velocity of 0.02 blocks per tick in a random direction. Given these velocities, the TNT travels 0.166 blocks (or 6 block pixels) horizontally before it stops, given there is no block in the way. When the countdown timer expires, the TNT explodes. If in the air, TNT falls roughly 77 blocks before exploding once it is ignited.

Primed TNT's texture blinks, alternating every 0.5 seconds between the TNT block's texture, and a copy of it that has been brightened to near-white. The effect is dynamic and the brightened texture can't be found in the assets.

Primed TNT cannot be pushed by players or other mobs, but it moves when in flowing water or lava. Primed TNT cannot mount minecarts or boats.

To make TNT destroy blocks in the water, e.g. to enter an ocean monument from the top, one can place sand or gravel on the TNT before it is primed. Priming the TNT causes the sand or gravel to fall one block, engulfing the TNT. Because the TNT is no longer immersed in water, it can destroy the surrounding blocks.

In Java Edition, primed TNT is not teleported when entering a nether portal; instead, it passes through portal blocks. In Bedrock Edition, however, primed TNT is teleported to the Nether. In both editions, primed TNT teleports as expected when entering an end portal, maintaining its direction and speed. The fuse timer keeps counting down (unless the spawn chunks are unloaded, then it pauses until a player loads the chunks).

If the TNT is primed atop any sort of fence post that is two blocks high or larger, it falls through the fence block on which it was activated and stops on the next lower one. Its detonation damages only the fence block it was "stuck" in.

In Java Edition, primed TNT summoned by a command explodes immediately because the fuse time defaults to zero if not specified.

### Redstone component
For redstone to activate TNT, it must either lead directly to the TNT, or power an adjacent block.

### Crafting ingredient
| Name              | Ingredients       | Crafting recipe | Description                                      |
|-------------------|-------------------|-----------------|--------------------------------------------------|
| Minecart with TNT | TNT+<br/>Minecart |                 |                                                  |
| Underwater TNT    | Sodium+<br/>TNT   |                 | ‌[Bedrock Edition and Minecraft Education  only] |

## Data values
### ID
Java Edition:

| Name | Identifier | Form         | Block tags          | Translation key       |
|------|------------|--------------|---------------------|-----------------------|
| TNT  | `tnt`      | Block & Item | `enderman_holdable` | `block.minecraft.tnt` |

| Name       | Identifier | Translation key        |
|------------|------------|------------------------|
| Primed TNT | `tnt`      | `entity.minecraft.tnt` |

Bedrock Edition:

| Name | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key                                |
|------|------------|------------|----------------------------|----------------|------------------------------------------------|
| TNT  | `tnt`      | `46`       | Block & Giveable Item[i 2] | Identical[i 3] | `tile.tnt.name`<br/>`tile.underwater_tnt.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

| Name       | Identifier | Numeric ID | Translation key   |
|------------|------------|------------|-------------------|
| Primed TNT | `tnt`      | `65`       | `entity.tnt.name` |

### Block states
Java Edition:

| Name     | Default value | Allowed values | Description                                                                   |
|----------|---------------|----------------|-------------------------------------------------------------------------------|
| unstable | `false`       | `false`        | Hittingthe TNT block breaks it, dropping it as an item that can be picked up. |
|          |               | `true`         | Hittingthe TNT block causes it to ignite and then explode.                    |

Bedrock Edition:

| Name                 | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                                                   |
|----------------------|---------------|---------------|----------------|-------------------------|-------------------------------------------------------------------------------|
| allow_underwater_bit | `0x2`         | `false`       | `false`        | `0`                     | This is normal TNT.                                                           |
|                      |               |               | `true`         | `1`                     | This is Underwater TNT.                                                       |
| explode_bit          | `0x1`         | `false`       | `false`        | `0`                     | Hittingthe TNT block breaks it, dropping it as an item that can be picked up. |
|                      |               |               | `true`         | `1`                     | Hittingthe TNT block causes it to ignite and then explode.                    |



### Entity data
TNT has entity data associated with them that contain various properties of the entity.

Java Edition:

Main article: Entity format
- Dynamic block entity data
	- 
	- Tags common to all entities
	- Fusefuse: Ticks until explosion. Default is 0. If activated from a TNT block, the fuse duration is 80 ticks (4 seconds).
	- block_state: The block model to use.
		- Name: Theresource locationof the block.
		- Properties: Optional. Theblock statesof the block.
			- Name: The block state name and its value.

Bedrock Edition:

SeeBedrock Edition level format/Entity format.
