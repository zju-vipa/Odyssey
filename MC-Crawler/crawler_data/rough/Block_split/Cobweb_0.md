# Cobweb
A cobweb is a block that slows down entity movements.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Post-generation
- 2 Usage
	- 2.1 Redstone circuits
	- 2.2 Effects
	- 2.3 Brewing ingredient
- 3 Sounds
- 4 Data values
	- 4.1 ID
- 5 History
	- 5.1 Data history
- 6 Issues
- 7 Gallery
	- 7.1 Renders
	- 7.2 Screenshots
- 8 Notes
- 9 External links

## Obtaining
### Breaking
Cobwebs can be obtained as an item using shears. Cobwebs can also be obtained with a sword enchanted with Silk Touch, which is only possible through commands or while in Creative mode‌[JE  only]. A cobweb drops one piece of string if broken with a non-Silk Touch sword, or if water touches or flows over it, or a piston pushes it. It drops nothing when broken using anything else, or if lava flows over it.

| Block    | Cobweb              |
|----------|---------------------|
| Hardness | 4                   |
|          | Breakingtime (secs) |
| Default  | 20                  |
| Shears   | 0.4                 |
| Sword    | 0.4                 |

### Natural generation
Cobwebs generate naturally in mineshafts, stronghold libraries, igloo basements, abandoned villages, woodland mansion spider spawner rooms, and trial chambers around specific trial spawners.‌[upcoming: JE 1.21 & BE 1.21.0]

### Post-generation
When an entity with the effect of Weaving‌[upcoming: JE 1.21 & BE 1.21.0] is killed, the game attempts to place cobwebs nearby.

## Usage
Mobs can spawn inside of cobwebs, in which case they do not catch fire if they are caught in a cobweb. Cobwebs also diffuse sky light.

Blocks can be placed on cobwebs. Paintings‌[Java Edition  only] and signs can be placed on their sides, or on top in the case of signs.

Despite being slowed down by them, mobs do not try to pathfind around cobwebs, which can be exploited to construct clever mob traps.

They can be useful in PvP servers, where a player can quickly erect a barrier of cobwebs that can trap players, or force them to destroy the cobwebs. They are also useful in traps that are deliberately intended to troll players, such as a long pitfall with cobwebs and lava at the bottom.

### Redstone circuits
2 cobwebs delay for around a minute
Cobwebs can be used as a delaying mechanism in a redstone circuit, for example, to delay an item falling on a pressure plate or into a hopper. They can also be used to cancel random momentum of an item thrown from a dispenser or dropper by placing them directly on their face.

### Effects
All mobs except for spiders and cave spiders experience slow movement through a cobweb. A mob falling through a cobweb takes 13 seconds to move down 1 block. A cobweb can partially stop blast damage if a player and the entity causing the explosion are both caught in the cobweb.

A cobweb affects the player's movement abilities, as well. While in contact with it, the player can move at a speed of about 25% of the normal walking speed. Additionally, in Java Edition, jumping vibrates the player akin to jumping in a 2-block-high space. A cobweb also limits the rate at which a player can break blocks. Like water, falling into a cobweb prevents a player from taking fall damage, meaning a fatal fall can be mitigated with cobwebs. Attacking while falling through cobwebs counts as a critical hit, the same as when falling after a jump.

‌In Java Edition 1.21 and Bedrock Edition 1.21.0‌[upcoming], players and mobs affected by the Weaving effect move through cobwebs at 50% of their normal speed instead of 25%.

The slowing effect of the cobweb increases if it is placed on ice. The slowest a player can move in vanilla Minecraft without commands or other third-party tools is by placing cobwebs on blue ice, sneaking, drinking a level IV Turtle Master potion, and blocking, which causes the player come to a near-total standstill, moving only a single block every few minutes.

Items thrown into a cobweb are slowed and fall through it after a maximum of about 24 seconds depending on where it enters. They do not merge with other items of the same type thrown on the ground.

Cobwebs have different effects on other moving entities. An arrow shot at a cobweb passes through without being slowed. In Java Edition, a falling block that enters a cobweb slows down, then drops as an item after existing for 30 seconds.

A minecart with no players in it takes about 9 seconds to fall through a cobweb if a rail is placed directly under the cobweb, however, if there is air between the cobweb and the rail, the minecart takes about 34 seconds to fall. Every extra cobweb added gives an additional 25 seconds of falling time. Players are unaffected by cobwebs when in a minecart unless they come into direct contact.

### Brewing ingredient
| Name              | Ingredients                | Brewing recipe | Description                      |
|-------------------|----------------------------|----------------|----------------------------------|
| Potion of Weaving | Cobweb+<br/>Awkward Potion |                | ‌[upcoming: JE 1.21 & BE 1.21.0] |

## Data values
### ID
Java Edition:

| Name   | Identifier | Form         | Translation key          |
|--------|------------|--------------|--------------------------|
| Cobweb | `cobweb`   | Block & Item | `block.minecraft.cobweb` |

Bedrock Edition:

| Name   | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key |
|--------|------------|------------|----------------------------|----------------|-----------------|
| Cobweb | `web`      | `30`       | Block & Giveable Item[i 2] | Identical[i 3] | `tile.web.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

## Notes



