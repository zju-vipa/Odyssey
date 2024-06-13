# Ruined Portal
A ruined portal is a structure resembling a damaged nether portal, which generates in both the Nether and the Overworld. It contains some decoration and a loot chest around it.

## Contents
- 1 Generation
- 2 Structure
	- 2.1 Overworld
	- 2.2 Nether
	- 2.3 Blocks
- 3 Loot
- 4 Data values
	- 4.1 ID
	- 4.2 Config
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Screenshots
- 8 References

## Generation
Underside of a ruined portal
Ruined portals are the only structures that generate in more than one dimension; they generate in all biomes in both the Nether and the Overworld, except the Deep Dark. They can spawn underground, underwater, or exposed to the air. If they generate underground, they have air pockets around them. Natural terrain around ruined portals generates as netherrack. They also generate a mass of netherrack underneath them (including "stalactite"-like shapes, and this may contain blackstone deposits in the Nether). Giant ruined portals have 3 distinct designs, and normal ruined portals have 10 designs. When a ruined portal generates, it has a 5% chance to be a giant ruined portal, for about a 1.67% chance per giant portal design. This gives normal ruined portals a 95% chance, for a 9.5% chance per normal ruined portal design.[more information needed]

|                        | Biome                 |                   |               |         |             |                              |                   |             |        |
|------------------------|-----------------------|-------------------|---------------|---------|-------------|------------------------------|-------------------|-------------|--------|
|                        |                       | Standard          | Desert        | Jungle  | Swamp       |                              | Windswept hills   | Ocean       | Nether |
| Vertical<br/>placement | Underground<br/>(50%) | Surface<br/>(50%) | Partly buried | Surface | Ocean floor | In windswept hills<br/>(50%) | Surface<br/>(50%) | Ocean floor | Nether |
| Mossiness              |                       | 0.2               | 0             | 0.8     | 0.5         |                              | 0.2               | 0.8         | 0      |
| Air Pocket             | Yes                   | 50%               | No            | 50%     | No          | Yes                          | 50%               | No          | 50%    |
| Overgrown              |                       | No                | No            | Yes     | No          |                              | No                | No          | No     |
| Vines                  |                       | No                | No            | Yes     | Yes         |                              | No                | No          | No     |
| Blackstone             |                       | No                | No            | No      | No          |                              | No                | No          | Yes    |

Ruined portals that generate underground do so at Y-level from 15 to n−n2, where n is the highest block at the point of generation and n2 is the height of the ruined portal structure. This means the terrain is always higher than or level with the top of the structure. Some ruined portal variants are short enough to generate completely on the surface.

Ruined portals that generate in windswept hills generate at y-level from 70 to n−n2.

Ruined portals that generate partially buried do so at y-level n−n2, plus a random integer from 2 to 8. This means that the structure has 2 to 8 layers raised above the surface.

In the Nether, ruined portals with air pockets generate from Y-level 32 to 100. Ruined portals without air pockets have a 50% chance to spawn from Y-level 27 to 29, and a 50% chance to spawn from Y-level 29 to 100.

Many blocks in ruined portals are replaced upon generation. A ruined portal is in a snowy biome if the temperature is less than 0.15.

| Original Block                           | Replacing Block                                 | Chance per Block                                              |
|------------------------------------------|-------------------------------------------------|---------------------------------------------------------------|
| Block of Gold                            | Air                                             | 30%                                                           |
| Lava                                     | Magma Block                                     | On ocean floor: 100%<br/>Not on ocean floor: 20%<br/>Cold: 0% |
|                                          | Netherrack                                      | Cold: 100%<br/>Not cold: 0%                                   |
| Netherrack[n 1]                          | Magma Block                                     | Not cold: 7%<br/>Cold: 0%                                     |
| Obsidian                                 | Crying Obsidian                                 | 15% ‌[JE  only]<br/>20% ‌[BE  only]                           |
| Stone Stone Bricks Chiseled Stone Bricks | Cracked Stone Bricks Stone Brick Stairs         | 50%×(1-Mossiness)                                             |
|                                          | Mossy Stone Bricks Mossy Stone Brick Stairs     | 50%×Mossiness                                                 |
| Anyslabs                                 | Mossy Stone Brick Slab                          | Mossiness                                                     |
| Anystairs                                | Stone Slab Stone Brick Slab                     | 50%×(1-Mossiness)                                             |
|                                          | Mossy Stone Brick Stairs Mossy Stone Brick Slab | 50%×Mossiness                                                 |
| Anywalls                                 | Mossy Stone Brick Wall                          | Mossiness                                                     |

1. ↑This includes netherrack generated as part of the netherrack "spread" through nearby terrain.

## Structure
Main article: /Structure
Ruined portals generate incomplete portal frames composed of obsidian and, sometimes along with crying obsidian, although nether portals cannot be activated with crying obsidian in the frame.[1] Some frames generate flat on the ground, as if they toppled over.  Others are free-standing separately, as if still being assembled/attached.

All ruined portals generate with a chest on Bedrock Edition, but on Java Edition the chest may be replaced if terrain overrides it. Each chest contains various golden items and items used to build portals such as obsidian and flint and steel.

Any ruined portal generated in the Overworld is surrounded with structures made of stone, stone bricks, and iron bars; in the Nether it is surrounded by blackstone variants and chains.

Currently there are 13 variants: 10 normal size portals and 3 giant portals in varying states of decay.

In Java Edition, ruined portals can be generated by the player by loading ruined_portal/portal_<1 to 10> or ruined_portal/giant_portal_<1 to 3> with a structure block. These ruined portals generate as they are stored, meaning they are not modified as detailed in the Generation section above. All portals generated this way create air pockets if generated in other blocks.

