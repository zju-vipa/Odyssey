# Fire
Fire is a non-solid block that can spread to nearby flammable blocks and destroy them.

## Contents
- 1 Obtaining
	- 1.1 Natural generation
	- 1.2 Post-generation
- 2 Usage
	- 2.1 Placement
	- 2.2 Burning entities
	- 2.3 Spread
		- 2.3.1 Flammable blocks
		- 2.3.2 Non-flammable blocks
	- 2.4 Extinguishing
	- 2.5 Eternal fire
	- 2.6 Bees
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
	- 5.1 Fire "items"
		- 5.1.1 Appearances
			- 5.1.1.1 Fire
			- 5.1.1.2 Soul Fire
		- 5.1.2 Names
			- 5.1.2.1 Fire
- 6 Issues
- 7 Trivia
	- 7.1 Bedrock Edition
- 8 Gallery
	- 8.1 Renders
	- 8.2 Screenshots
- 9 References

## Obtaining
Fire cannot be obtained as an item under any circumstances in Java Edition, though in Bedrock Edition fire may be obtained as an item via inventory editing.

### Natural generation
Fire naturally generates in fire patches across the terrain of the Nether. 

Fire also generates on top of netherrack in some treasure room bastion remnants.

In the End, fire generates on bedrock blocks on top of end spikes, at the same location as the end crystals.


### Post-generation
Lava generated next to flammable blocks can naturally cause fires.

Fire spreads quickly across flammable blocks, and can spontaneously ignite when flammable blocks are near lava, even though many blocks that should be flammable cannot catch fire from nearby lava.

Lightning strikes can also set fires, regardless of whether they are created naturally, redirected to lightning rods, summoned by a trident enchanted with Channeling, or created using the /summon command.

Placing an end crystal on bedrock or obsidian in the End causes fire to appear at the end crystal's location.

The explosion from sleeping in a bed in the Nether or the End creates fire, as does the explosion of a ghast fireball or the impact of a blaze fireball. Using a charged respawn anchor in the Overworld or the End also creates fire from the explosion.

## Usage
### Placement
Before a fire.
During the fire.
After a fire.
Fire can be placed using flint and steel or a fire charge. Fire created on soul sand or soul soil becomes soul fire.

When placed, a fire burns for a short and randomly determined amount of time. If nothing flammable is adjacent to it, the flames die out. Water that touches fire extinguishes it.

It cannot be placed suspended in midair, even with commands.[1]

### Burning entities
Players and many mobs burn when exposed to fire. Burning obstructs the player's view slightly. While inside a fire block, the fire inflicts damage at a rate of 1 per half-second unless the player or mob has Fire Resistance or a total Fire Protection of 7 or higher.‌[BE  only] When the player is on fire outside the fire block, they take damage at 1 per second. This is the same rate that the player gains health in Peaceful difficulty, so burning alone cannot kill the player in this mode. Soul fire deals damage at a rate of 2 per half-second, making it more dangerous than normal fire. After leaving a fire source, the player or mob continues burning for some time depending on how long it was exposed to the fire (stored in a Fire tag shared by all entities). Players and mobs that are burning can be extinguished by powder snow, rain, water or a cauldron.

Most dropped items that are in fire briefly catch fire and disappear. This includes the item forms of blocks that would not be flammable if placed, including obsidian. The only exceptions are these netherite-related items: netherite tools and weapons, netherite armor, blocks of netherite, netherite scrap, netherite ingots, and ancient debris.

If a mob able to drop meat dies while on fire, it drops the cooked version of it, with the exception of fish that is dropped by polar bears‌[JE  only] or guardians. This also applies to the zombie's uncommon potato drop; if a zombie dies while on fire and should drop a potato, it becomes a baked potato.‌[JE  only]

Most Nether mobs are invulnerable to fire and cannot burn. Exceptions include skeletons, endermen, piglins, piglin brutes, and hoglins. 

Zoglins, vexes, agents, NPCs, wardens, and withers are also invulnerable to fire.

Burning is not considered a status effect and therefore cannot be cured by milk.

### Spread
Safe building area around a fire
Fire spreads over flammable surfaces and can climb up walls, across floors and ceilings, and over small gaps. More precisely, a fire block can turn any air block that is adjacent to a flammable block into a fire block. This can happen at a distance of up to one block downward, one block sideways (including diagonals), and four blocks upward of the original fire block (not the block the fire is on/next to). Therefore, if the player is using fire to build a fireplace, caution is needed. Blocks in the way do not prevent fire from igniting blocks above it—so even if the player protects a wooden roof with cobblestone between it and the fire, the fire ignores that cobblestone.

Fire spreads from a still lava block similarly: any air block one above and up to one block sideways (including diagonals) or two above and two blocks sideways (including diagonals) that is adjacent to a flammable block may be turned into a fire block.

Fire that naturally spreads into a valid nether portal frame activates the portal.

####  Flammable blocks
Fire can spread onto and burn away any flammable block (or in the case of TNT, ignite it). On the other hand, a fire that is not adjacent to any flammable block and not on top of a forever-burning block does not spread, even to another flammable block within the normal range.

In the following table, the higher the ignite odds, the more quickly a block catches fire if the fire is available to spread there. The higher the burn odds, the more quickly a block on fire burns away. These are relative values; actual ignite odds and burn time depends not only on these values, but on difficulty, rain, the age of the fire, the direction of the block relative to the fire, and multiple random values including how long the fire waits between block ticks and further checks based on the previous factors. Fire spread is reduced if it tries to spread to a block more two blocks higher than itself. Fire spread is further reduced by 50% if the flammable blocks in a humid biome (swamp, mushroom fields and jungle, excluding sparse jungle).

| Block                                                                                                                                                                                                                                 | Ignite odds |    | Burn odds | Can catch firefrom lava |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|----|-----------|-------------------------|
| Logs<br/>Stripped Logs<br/>Wood<br/>Stripped Wood<br/>Block of Coal                                                                                                                                                                   |             | 5  | 5         | Yes                     |
| Overworld Planks<br/>Overworld Wooden Slabs<br/>Overworld Fence Gates<br/>Overworld Fences<br/>Overworld Wooden Stairs<br/>Composter<br/>Beehive<br/>Mangrove Roots<br/>Bamboo Mosaic<br/>Bamboo Mosaic Slab<br/>Bamboo Mosaic Stairs |             | 5  | 20        | Yes                     |
| Target‌[JE  only]                                                                                                                                                                                                                     |             | 15 | 20        | Yes                     |
| Cave Vines<br/>Cave Vines Plant                                                                                                                                                                                                       |             | 15 | 60        | No                      |
| TNT(ignitesinstead of vanishing)<br/>Vines<br/>Glow Lichen                                                                                                                                                                            |             | 15 | 100       | Yes                     |
| Bookshelf<br/>Lectern<br/>Bee Nest                                                                                                                                                                                                    |             | 30 | 20        | Yes                     |
| Leaves<br/>Wool<br/>Dried Kelp Block<br/>Azalea<br/>Hanging Roots                                                                                                                                                                     |             | 30 | 60        | Yes                     |
| Carpets(exceptMoss)                                                                                                                                                                                                                   | JE          | 60 | 20        | Yes                     |
|                                                                                                                                                                                                                                       | BE          | 30 | 60        |                         |
| Hay Bale                                                                                                                                                                                                                              |             | 60 | 20        | No                      |
| Bamboo<br/>Scaffolding                                                                                                                                                                                                                |             | 60 | 60        | Yes                     |
| Flowers, 1-block<br/>Sweet Berry Bush                                                                                                                                                                                                 | JE          | 60 | 100       | Yes                     |
|                                                                                                                                                                                                                                       | BE          | 30 |           |                         |
| Flowers, 2-block<br/>Grass<br/>Tall Grass<br/>Fern<br/>Large Fern<br/>Dead Bush<br/>Big Dripleaf<br/>Big Dripleaf Stem<br/>Small Dripleaf<br/>Spore Blossom<br/>Pitcher Plant                                                         |             | 60 | 100       | Yes                     |
| Bamboo Shoot‌[BE  only]                                                                                                                                                                                                               |             | ?  | ?         | Yes                     |

#### Non-flammable blocks
Non-flammable blocks can be lit but do not burn away, and such fire does not spread. Non-flammable blocks other than netherrack or magma blocks extinguish themselves quickly. In the End, bedrock also does not extinguish itself.

If a block is a part of a flammable material, it catches fire from lava. However, certain blocks do not burn away:

| Block                                                                                                                                                                                                                                                                                                                                                                                                                                      | Can catch firefrom lava |     | Can burn away |    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|-----|---------------|----|
| Bamboo Shoot                                                                                                                                                                                                                                                                                                                                                                                                                               | JE                      | No  | No            |    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            | BE                      | Yes | Yes           |    |
| Target                                                                                                                                                                                                                                                                                                                                                                                                                                     | JE                      | Yes | Yes           |    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            | BE                      | No  | No            |    |
| Banners<br/>Barrel<br/>Campfire<br/>Cartography Table<br/>Chest<br/>Crafting Table<br/>Crimson Roots<br/>Daylight Detector<br/>Fletching Table<br/>Jukebox<br/>Loom<br/>Mushroom Blocks<br/>Nether Sprouts<br/>Note Block<br/>Smithing Table<br/>Trapped Chest<br/>Warped Roots<br/>Wooden Doorsof all types<br/>Wooden Hanging Signsof all types<br/>Wooden Pressure Platesof all types<br/>Wooden Trapdoorsof all types<br/>Wooden Signs |                         | Yes |               | No |
| Wooden Buttonsof all types                                                                                                                                                                                                                                                                                                                                                                                                                 | JE                      | No  |               | No |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            | BE                      | Yes |               |    |
| Bed                                                                                                                                                                                                                                                                                                                                                                                                                                        | JE                      | Yes |               | No |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            | BE                      | No  |               |    |
| Wood-like blocks such as:<br/>Cobweb<br/>Grindstone<br/>Ladder<br/>Lever<br/>Moss Block<br/>Moss Carpet<br/>Piston<br/>Railsof all types<br/>Redstone Torch<br/>Saplings<br/>Smoker<br/>Torch<br/>Tripwire<br/>Tripwire Hook<br/>Stems<br/>Stripped Stems<br/>Hyphae<br/>Stripped Hyphae<br/>Nether Planks<br/>Nether Wood Slabs<br/>Nether Fence Gates<br/>Nether Fences<br/>Nether Wood Stairs<br/>and all other non-flammable blocks... |                         | No  |               | No |

### Extinguishing
Fire burns out after a while when on a non-flammable block other than netherrack or magma blocks; however, punching or hitting the side of a burning block extinguishes the fire on that side, making the Fire extinguished sound (see below). Hitting fire while holding a tool does not reduce the tool's durability. Placing blocks on the fire also extinguishes it. Water and lava extinguish fires that they flow into, and thrown splash and lingering water bottles extinguish fires in the block hit and the four blocks horizontally surrounding it.

Mobs on fire are extinguished when in water or in a cauldron containing it. In the latter case, one layer of water disappears.

Fire extinguishes more quickly if nothing flammable is present, and soon after it consumes a flammable block immediately beneath it.

- Fire has anageproperty that determines how it extinguishes, ranging from age 0 when the fire is set, and growing to age 15. For fire older than age 3, if nothing flammable is adjacent to the fire, or if the block below doesn't have a solid top surface, the fire is extinguished by the nextblock tick. At age 15, as long as there isn't a flammable block below the fire, a block tick has a1⁄4chance to extinguish the fire.

If a fire is exposed to rain, it extinguishes quickly.

- Rain affects fire if it falls directly onto the fire, or into the four adjacent blocks. Specifically, no matter the age, any block tick has a 20–65% chance of rain extinguishing the fire, depending on the fire's age: 20 percent plus 3 percentage points per age of the fire.

Fire burning on netherrack creates a perpetually burning fire.
### Eternal fire
When lit, netherrack and magma blocks maintain fire forever, unless extinguished by any method except rain. Bedrock in the End also burns eternally. Eternal fire cannot exist on the sides of these blocks.

The blocks that can support eternal fire are defined per-dimension, in the #infiniburn_overworld, #infiniburn_nether, and #infiniburn_end block tags.

If /gamerule doFireTick is false, fire lasts forever until it is put out by the player, and does not spread or affect flammable blocks.

### Bees
Setting fire to a beehive or bee nest causes the contained bees to be ejected from the block.

## Data values
### ID
Java Edition:

| Name | Identifier | Form  | Block tags | Translation key        |
|------|------------|-------|------------|------------------------|
| Fire | `fire`     | Block | `fire`     | `block.minecraft.fire` |

Bedrock Edition:

| Name | Identifier | Numeric ID | Form                         | Item ID[i 1]   | Translation key  |
|------|------------|------------|------------------------------|----------------|------------------|
| Fire | `fire`     | `51`       | Block & Ungiveable Item[i 2] | Identical[i 3] | `tile.fire.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Unavailable with /give command
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:
Fire:

| Name  | Default value | Allowed values                                                                                                                    | Description                                                                                                                                             |
|-------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| age   | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | $Newly placed fire has an age of 0, and has a\frac{1}{3}$chance of incrementing with eachblock tick.<br/>This factor affects how the fire extinguishes. |
| east  | `false`       | `false`<br/>`true`                                                                                                                | When true, fire texture shows on that face of the block to the east; false if there's a block below this fire.                                          |
| north | `false`       | `false`<br/>`true`                                                                                                                | When true, fire texture shows on that face of the block to the north; false if there's a block below this fire.                                         |
| south | `false`       | `false`<br/>`true`                                                                                                                | When true, fire texture shows on that face of the block to the south; false if there's a block below this fire.                                         |
| up    | `false`       | `false`<br/>`true`                                                                                                                | When true, fire texture shows on that face of the block above; false if there's a block below this fire.                                                |
| west  | `false`       | `false`<br/>`true`                                                                                                                | When true, fire texture shows on that face of the block to the west; false if there's a block below this fire.                                          |

Bedrock Edition:
Fire and Soul Fire:

| Name | Metadata Bits                       | Default value | Allowed values                                                                                                                    | Values forMetadata Bits                                                                                                           | Description                                                                           |
|------|-------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| age  | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | Newly placed fire has an age of 0.<br/>This factor affects how the fire extinguishes. |



