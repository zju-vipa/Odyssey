# Dragon Egg
The dragon egg is a decorative block or a "trophy item", and is the rarest item obtainable in the game, as it generates only once (or twice in Bedrock Edition[1]) per world.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Post-generation
- 2 Usage
	- 2.1 Light source
	- 2.2 Teleporting
	- 2.3 The void
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Falling block entity
- 5 Advancements
- 6 History
- 7 Issues
- 8 Trivia
- 9 Gallery
	- 9.1 Screenshots
	- 9.2 In other media
- 10 See also
- 11 References

## Obtaining
Across both Java and Bedrock editions, the dragon egg is available in the Creative inventory. It can be obtained with pick block or the /give command, or placed in the world with commands such as /setblock and /fill.

### Breaking
The dragon egg usually cannot be mined directly, as trying to do so causes it to teleport within a 31×15×31 volume centered on the egg, with locations toward the center more likely. If all air blocks in that area are filled so there is nowhere for the egg to teleport to, or if it fails to find an air block after 1,000 attempts at teleporting, it can be mined. The dragon egg is a gravity-affected block, and drops as an item when pushed by a piston or when it falls onto a block less than a full block tall, such as a torch or a bottom slab.

When destroyed by an explosion, the block always drops as an item.

The dragon egg is not immune to destruction by the ender dragon, despite being produced by it.[2]

| Block    | Dragon Egg          |
|----------|---------------------|
| Hardness | 3                   |
|          | Breakingtime (secs) |
| Default  | 4.5                 |

### Post-generation
In Java Edition, a single dragon egg is generated on top of the exit portal when the first ender dragon is defeated. In Bedrock Edition, two dragon eggs generate on top of the exit portal; one generates when the first ender dragon is defeated, while the other generates when the second ender dragon is defeated.[1]

## Usage
See also: Falling Block § Behavior

Heatmap of where a dragon egg lands after trying to mine it.
Particles of a dragon egg.
The dragon egg, if there is no block below it, falls until it lands on the next available block. When it is being affected by gravity and falling, it exhibits a smooth falling animation.

It does not suffocate mobs or players when it falls and covers them, nor does it crush mobs or players like anvils and stalactites do.

The dragon egg can be placed on a non-solid block without falling.

Like other falling blocks, when the dragon egg is floating, it has black particles falling from it.

### Light source
The dragon egg emits a light level of 1.

### Teleporting
To cause the egg to teleport, press attack while in Survival or Adventure mode (press use in Creative). It teleports to an air block nearby (up to seven blocks vertically and fifteen blocks horizontally), creating the same particles as an enderman. It may teleport into the air and subsequently fall to the ground since it forcefully obeys gravity.

If all available air blocks are filled, it is possible to break the block.

Dragon egg teleportation lacks teleportation sounds.[3]

### The void
In the case that egg teleportation finds an invalid location (such as below the world), it makes an additional attempt to find a valid location, centered on the invalid location rather than the original position.

## Data values
### ID
Java Edition:

| Name       | Identifier   | Form         | Translation key              |
|------------|--------------|--------------|------------------------------|
| Dragon Egg | `dragon_egg` | Block & Item | `block.minecraft.dragon_egg` |

Bedrock Edition:

| Name       | Identifier   | Numeric ID | Form                       | Item ID[i 1]   | Translation key        |
|------------|--------------|------------|----------------------------|----------------|------------------------|
| Dragon Egg | `dragon_egg` | `122`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.dragon_egg.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Falling block entity
| Hitbox size | Height: 0.98 BlocksWidth: 0.98 Blocks |
|-------------|---------------------------------------|

{
    "title": "Falling Dragon Egg",
    "rows": [
        {
            "field": "Height: 0.98 Blocks<br>Width: 0.98 Blocks",
            "label": "(link to Hitbox article, displayed as Hitbox size)"
        }
    ],
    "invimages": [],
    "images": [
        "Dragon Egg.png",
        "Dragon Egg BE.png"
    ]
}
Main article: Falling Block
- Dynamic block entity data
	- 
		- 
		- Tags common to all entities
	- BlockState: The falling block represented by this entity.
		- Name: Theresource locationof the block.
		- Properties: Optional. Theblock statesof the block.
			- Name: The block state name and its value.
	- CancelDrop: 1 or 0 (true/false) - true if the block should be destroyed instead of placed after landing on a solid block. When true, the block is not dropped as an item, even if theDropItemtag is set to true. However, if the entity is deleted due to itsTimevalue being too high, this tag is ignored and an item is dropped depending on theDropItemtag.CancelDropdefaults to 1 for fallingsuspicious sandandsuspicious gravel, and 0 for the other vanilla falling blocks and any summoned falling block.
	- DropItem: 1 or 0 (true/false) – true if the block should drop as an item when it breaks. Any block that does not have an item formwith the same ID as the blockdoes not drop even if this is set.
	- FallHurtAmount: Multiplied by theFallDistanceto calculate the amount of damage to inflict. By default this value is 2for anvils, and 6for pointed dripstone.
	- FallHurtMax: The maximum hit points of damage to inflict on entities that intersect this falling block. For vanilla falling blocks, always 40× 20.
	- HurtEntities: 1 or 0 (true/false) – true if the block should hurt entities it falls on. Defaults to 1 foranvilsandpointed dripstoneand to 0 for the other vanilla falling blocks and any summoned falling block.
	- TileEntityData: Optional. The tags of the block entity for this block.
	- Time: The number of ticks the entity has existed. WhenTimegoes above 600, or above 100 while the block is at Y=-64 or is outside building height, the entity is deleted.

