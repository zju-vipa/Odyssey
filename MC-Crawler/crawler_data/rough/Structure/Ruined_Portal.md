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

### Overworld
Note that some blocks can be replaced with others (such as crying obsidian) upon generation. A full list can be seen below.

| Structure name                 | Description                                                                   | Consists of                                                                                                                                                                                       | Images |
|--------------------------------|-------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| `ruined_portal/giant_portal_1` | A large incomplete portal.                                                    | 263 Netherrack 63 Stone Bricks 38 Stone Brick Slab 31 Obsidian 20 Stone Brick Stairs 18 Iron Bars 11 Lava 4 Chiseled Stone Bricks 2 Block of Gold 1 Chest                                         |        |
| `ruined_portal/giant_portal_2` | A large incomplete portal.                                                    | 237 Netherrack 55 Stone Bricks 30 Stone Brick Slab 29 Obsidian 22 Iron Bars 19 Lava 18 Stone Brick Stairs 6 Chiseled Stone Bricks 2 Block of Gold 1 Chest                                         |        |
| `ruined_portal/giant_portal_3` | A large incomplete portal, with the most gold blocks, separate obsidian.      | 324 Netherrack 51 Stone Bricks 40 Stone Brick Slab 33 Lava 25 Obsidian 22 Iron Bars 6 Block of Gold 6 Chiseled Stone Bricks 6 Stone Brick Stairs 1 Chest                                          |        |
| `ruined_portal/portal_1`       | A small incomplete portal, with stone slabs and no lava.                      | 55 Netherrack 11 Obsidian 10 Stone Slab 9 Stone Bricks 7 Stone 6 Stone Brick Stairs 3 Chiseled Stone Bricks 2 Block of Gold 1 Chest 1 Cracked Stone Bricks 1 Stone Brick Slab                     |        |
| `ruined_portal/portal_2`       | A hanging incomplete portal.                                                  | 115 Netherrack 26 Lava 19 Stone Bricks 14 Stone Brick Slab 11 Obsidian 10 Smooth Stone Slab 4 Stone Brick Stairs 2 Block of Gold 2 Iron Bars 1 Chest 1 Chiseled Stone Bricks 1 Mossy Stone Bricks |        |
| `ruined_portal/portal_3`       | A small incomplete portal, with no gold block.                                | 132 Netherrack 36 Stone Bricks 16 Stone Brick Slab 11 Obsidian 2 Lava 1 Chest                                                                                                                     |        |
| `ruined_portal/portal_4`       | A small incomplete portal.                                                    | 130 Netherrack 36 Stone Bricks 16 Stone Brick Slab 11 Obsidian 3 Lava 1 Block of Gold 1 Chest                                                                                                     |        |
| `ruined_portal/portal_5`       | A small portal, where the top of the portal has fallen over.                  | 145 Netherrack 22 Stone Bricks 15 Obsidian 12 Stone Brick Slab 6 Stone 5 Stone Slab 3 Block of Gold 2 Mossy Stone Bricks 1 Chest 1 Cracked Stone Bricks 1 Lava 1 Stone Brick Stairs               |        |
| `ruined_portal/portal_6`       | A 5×5 portal, where the top center block is misplaced.                        | 41 Netherrack 16 Obsidian 4 Stone Brick Slab 2 Stone Brick Stairs 1 Block of Gold 1 Chest                                                                                                         |        |
| `ruined_portal/portal_7`       | An incomplete portal submerged in lava.                                       | 92 Netherrack 21 Lava 12 Obsidian 3 Stone Brick Slab 2 Block of Gold 1 Chest 1 Stone Bricks 1 Stone Brick Stairs                                                                                  |        |
| `ruined_portal/portal_8`       | An incomplete portal at the top of a staircase. The top has fallen into lava. | 144 Netherrack 26 Lava 17 Obsidian 14 Stone Bricks 6 Stone Brick Stairs 4 Stone Brick Wall 3 Block of Gold 2 Chiseled Stone Bricks 1 Chest 1 Stone Brick Slab                                     |        |
| `ruined_portal/portal_9`       | A small incomplete portal.                                                    | 63 Netherrack 11 Obsidian 11 Stone Brick Stairs 2 Block of Gold 1 Chest 1 Magma Block 1 Stone Brick Slab                                                                                          |        |
| `ruined_portal/portal_10`      | An incomplete portal that has fallen backward into lava.                      | 123 Netherrack 19 Lava 13 Obsidian 13 Stone Bricks 3 Chiseled Stone Bricks 3 Chain 3 Stone Brick Stairs 2 Block of Gold 1 Chest                                                                   |        |

### Nether
| Structure name                 | Description                                                                   | Consists of                                                                                                                                                                                                                                                        | Images |
|--------------------------------|-------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| `ruined_portal/giant_portal_1` | A large incomplete portal.                                                    | 263 Netherrack 63 Polished Blackstone Bricks 38 Polished Blackstone Brick Slab 31 Obsidian 20 Polished Blackstone Brick Stairs 18 Chain 11 Lava 4 Chiseled Polished Blackstone 2 Block of Gold 1 Chest                                                             |        |
| `ruined_portal/giant_portal_2` | A large incomplete portal.                                                    | 237 Netherrack 55 Polished Blackstone Bricks 30 Polished Blackstone Brick Slab 29 Obsidian 22 Chain 19 Lava 18 Polished Blackstone Brick Stairs 6 Chiseled Polished Blackstone 2 Block of Gold 1 Chest                                                             |        |
| `ruined_portal/giant_portal_3` | A large incomplete portal, with the most gold blocks, separate obsidian.      | 324 Netherrack 51 Polished Blackstone Bricks 40 Polished Blackstone Brick Slab 33 Lava 25 Obsidian 22 Chain 6 Block of Gold 6 Chiseled Polished Blackstone 6 Polished Blackstone Bricks 1 Chest                                                                    |        |
| `ruined_portal/portal_1`       | A small incomplete portal, with blackstone slabs and no lava.                 | 55 Netherrack 11 Obsidian 10 Polished Blackstone Slab 9 Polished Blackstone Bricks 7 Polished Blackstone 6 Polished Blackstone Stairs 3 Chiseled Polished Blackstone 2 Block of Gold 1 Chest 1 Cracked Polished Blackstone Bricks 1 Polished Blackstone Brick Slab |        |
| `ruined_portal/portal_2`       | A hanging incomplete portal.                                                  | 115 Netherrack 26 Lava 20 Polished Blackstone Bricks 14 Polished Blackstone Slab 11 Obsidian 10 Polished Blackstone Slab 4 Polished Blackstone Brick Stairs 2 Block of Gold 2 Chain 1 Chest 1 Chiseled Polished Blackstone                                         |        |
| `ruined_portal/portal_3`       | A small incomplete portal, with no gold block.                                | 132 Netherrack 36 Polished Blackstone Bricks 16 Polished Blackstone Brick Slab 11 Obsidian 2 Lava 1 Chest                                                                                                                                                          |        |
| `ruined_portal/portal_4`       | A small incomplete portal.                                                    | 130 Netherrack 36 Polished Blackstone Bricks 16 Polished Blackstone Brick Slab 11 Obsidian 3 Lava 1 Block of Gold 1 Chest                                                                                                                                          |        |
| `ruined_portal/portal_5`       | A small portal, where the top of the portal has fallen over.                  | 145 Netherrack 24 Polished Blackstone Bricks 15 Obsidian 12 Polished Blackstone Brick Slab 6 Polished Blackstone 5 Polished Blackstone Slab 3 Block of Gold 1 Chest 1 Cracked Polished Blackstone Bricks 1 Lava 1 Polished Blackstone Brick Stairs                 |        |
| `ruined_portal/portal_6`       | A 5×5 portal, where the top center block is misplaced.                        | 41 Netherrack 16 Obsidian 4 Polished Blackstone Brick Slab 2 Polished Blackstone Brick Stairs 1 Block of Gold 1 Chest                                                                                                                                              |        |
| `ruined_portal/portal_7`       | An incomplete portal submerged in lava.                                       | 92 Netherrack 21 Lava 12 Obsidian 3 Polished Blackstone Brick Slab 2 Block of Gold 1 Chest 1 Polished Blackstone Bricks 1 Polished Blackstone Brick Stairs                                                                                                         |        |
| `ruined_portal/portal_8`       | An incomplete portal at the top of a staircase. The top has fallen into lava. | 144 Netherrack 26 Lava 17 Obsidian 14 Polished Blackstone Bricks 6 Polished Blackstone Brick Stairs 4 Polished Blackstone Brick Wall 3 Block of Gold 2 Chiseled Polished Blackstone 1 Chest 1 Polished Blackstone Slab                                             |        |
| `ruined_portal/portal_9`       | A small incomplete portal.                                                    | 63 Netherrack 11 Obsidian 11 Polished Blackstone Brick Stairs 2 Block of Gold 1 Chest 1 Magma Block 1 Polished Blackstone Brick Slab                                                                                                                               |        |
| `ruined_portal/portal_10`      | An incomplete portal that has fallen backward into lava.                      | 123 Netherrack 19 Lava 13 Obsidian 13 Polished Blackstone Bricks 3 Chiseled Polished Blackstone 3 Chain 3 Polished Blackstone Brick Stairs 2 Block of Gold 1 Chest                                                                                                 |        |

### Blocks
| All ruined portals                                                                                    | Overworld                                                                                                                                                                                                                                                                                                    | Nether                                                                                                                                                                                                                                                                                                           |
|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Block of Gold<br/>Chest<br/>Crying Obsidian<br/>Lava<br/>Magma Block<br/>Netherrack<br/>Obsidian<br/> | Iron Bars<br/>Stone<br/>Stone Slab<br/>Smooth Stone Slab<br/>Stone Bricks<br/>Stone Brick Slab<br/>Stone Brick Stairs<br/>Stone Brick Wall<br/>Chiseled Stone Bricks<br/>Cracked Stone Bricks<br/>Mossy Stone Bricks<br/>Mossy Stone Brick Slab<br/>Mossy Stone Brick Stairs<br/>Mossy Stone Brick Wall<br/> | Chain<br/>Polished Blackstone<br/>Polished Blackstone Slab<br/>Polished Blackstone Stairs<br/>Polished Blackstone Bricks<br/>Polished Blackstone Brick Slab<br/>Polished Blackstone Brick Stairs<br/>Polished Blackstone Brick Wall<br/>Cracked Polished Blackstone Bricks<br/>Chiseled Polished Blackstone<br/> |

## Loot
In Java Edition, each ruined portal chest contains 4–8 item stacks,  with the following distribution: 

| Item                           | Stack Size  [A] | Weight   [B]     | Chance   [C] | Avg.per chest   [D] | Avg. # cheststo search   [E] |
|--------------------------------|-----------------|------------------|--------------|---------------------|------------------------------|
| Iron Nugget                    | 9–18            | $\frac{40}{398}$ | 46.4%        | 8.141               | 2.2                          |
| Flint                          | 1–4             | $\frac{40}{398}$ | 46.4%        | 1.508               | 2.2                          |
| Obsidian                       | 1–2             | $\frac{40}{398}$ | 46.4%        | 0.905               | 2.2                          |
| Fire Charge                    | 1               | $\frac{40}{398}$ | 46.4%        | 0.603               | 2.2                          |
| Flint and Steel                | 1               | $\frac{40}{398}$ | 46.4%        | 0.603               | 2.2                          |
| Gold Nugget                    | 4–24            | $\frac{15}{398}$ | 20.5%        | 3.166               | 4.9                          |
| Golden Apple                   | 1               | $\frac{15}{398}$ | 20.5%        | 0.226               | 4.9                          |
| Enchanted Golden Axe[F]        | 1               | $\frac{15}{398}$ | 20.5%        | 0.226               | 4.9                          |
| Enchanted Golden Hoe[F]        | 1               | $\frac{15}{398}$ | 20.5%        | 0.226               | 4.9                          |
| Enchanted Golden Pickaxe[F]    | 1               | $\frac{15}{398}$ | 20.5%        | 0.226               | 4.9                          |
| Enchanted Golden Shovel[F]     | 1               | $\frac{15}{398}$ | 20.5%        | 0.226               | 4.9                          |
| Enchanted Golden Sword[F]      | 1               | $\frac{15}{398}$ | 20.5%        | 0.226               | 4.9                          |
| Enchanted Golden Helmet[F]     | 1               | $\frac{15}{398}$ | 20.5%        | 0.226               | 4.9                          |
| Enchanted Golden Chestplate[F] | 1               | $\frac{15}{398}$ | 20.5%        | 0.226               | 4.9                          |
| Enchanted Golden Leggings[F]   | 1               | $\frac{15}{398}$ | 20.5%        | 0.226               | 4.9                          |
| Enchanted Golden Boots[F]      | 1               | $\frac{15}{398}$ | 20.5%        | 0.226               | 4.9                          |
| Glistering Melon Slice         | 4–12            | $\frac{5}{398}$  | 7.3%         | 0.603               | 13.7                         |
| Golden Carrot                  | 4–12            | $\frac{5}{398}$  | 7.3%         | 0.603               | 13.7                         |
| Gold Ingot                     | 2–8             | $\frac{5}{398}$  | 7.3%         | 0.377               | 13.7                         |
| Clock                          | 1               | $\frac{5}{398}$  | 7.3%         | 0.075               | 13.7                         |
| Light Weighted Pressure Plate  | 1               | $\frac{5}{398}$  | 7.3%         | 0.075               | 13.7                         |
| Golden Horse Armor             | 1               | $\frac{5}{398}$  | 7.3%         | 0.075               | 13.7                         |
| Block of Gold                  | 1–2             | $\frac{1}{398}$  | 1.5%         | 0.023               | 66.8                         |
| Bell                           | 1               | $\frac{1}{398}$  | 1.5%         | 0.015               | 66.8                         |
| Enchanted Golden Apple         | 1               | $\frac{1}{398}$  | 1.5%         | 0.015               | 66.8                         |

In Bedrock Edition, each ruined portal chest contains 4–8 item stacks,  with the following distribution: 

| Item                           | Stack Size  [A] | Weight   [B]     | Chance   [C] | Avg.per chest   [D] | Avg. # cheststo search   [E] |
|--------------------------------|-----------------|------------------|--------------|---------------------|------------------------------|
| Iron Nugget                    | 9–18            | $\frac{40}{398}$ | 46.4%        | 8.141               | 2.2                          |
| Flint                          | 1–4             | $\frac{40}{398}$ | 46.4%        | 1.508               | 2.2                          |
| Obsidian                       | 1–2             | $\frac{40}{398}$ | 46.4%        | 0.905               | 2.2                          |
| Fire Charge                    | 1               | $\frac{40}{398}$ | 46.4%        | 0.603               | 2.2                          |
| Flint and Steel                | 1               | $\frac{40}{398}$ | 46.4%        | 0.603               | 2.2                          |
| Gold Nugget                    | 4–24            | $\frac{15}{398}$ | 20.5%        | 3.166               | 4.9                          |
| Golden Apple                   | 1               | $\frac{15}{398}$ | 20.5%        | 0.226               | 4.9                          |
| Enchanted Golden Axe[F]        | 1               | $\frac{15}{398}$ | 20.5%        | 0.226               | 4.9                          |
| Enchanted Golden Hoe[F]        | 1               | $\frac{15}{398}$ | 20.5%        | 0.226               | 4.9                          |
| Enchanted Golden Pickaxe[F]    | 1               | $\frac{15}{398}$ | 20.5%        | 0.226               | 4.9                          |
| Enchanted Golden Shovel[F]     | 1               | $\frac{15}{398}$ | 20.5%        | 0.226               | 4.9                          |
| Enchanted Golden Sword[F]      | 1               | $\frac{15}{398}$ | 20.5%        | 0.226               | 4.9                          |
| Enchanted Golden Helmet[F]     | 1               | $\frac{15}{398}$ | 20.5%        | 0.226               | 4.9                          |
| Enchanted Golden Chestplate[F] | 1               | $\frac{15}{398}$ | 20.5%        | 0.226               | 4.9                          |
| Enchanted Golden Leggings[F]   | 1               | $\frac{15}{398}$ | 20.5%        | 0.226               | 4.9                          |
| Enchanted Golden Boots[F]      | 1               | $\frac{15}{398}$ | 20.5%        | 0.226               | 4.9                          |
| Glistering Melon Slice         | 4–12            | $\frac{5}{398}$  | 7.3%         | 0.603               | 13.7                         |
| Golden Carrot                  | 4–12            | $\frac{5}{398}$  | 7.3%         | 0.603               | 13.7                         |
| Gold Ingot                     | 2–8             | $\frac{5}{398}$  | 7.3%         | 0.377               | 13.7                         |
| Clock                          | 1               | $\frac{5}{398}$  | 7.3%         | 0.075               | 13.7                         |
| Light Weighted Pressure Plate  | 1               | $\frac{5}{398}$  | 7.3%         | 0.075               | 13.7                         |
| Golden Horse Armor             | 1               | $\frac{5}{398}$  | 7.3%         | 0.075               | 13.7                         |
| Block of Gold                  | 1–2             | $\frac{1}{398}$  | 1.5%         | 0.023               | 66.8                         |
| Bell                           | 1               | $\frac{1}{398}$  | 1.5%         | 0.015               | 66.8                         |
| Enchanted Golden Apple         | 1               | $\frac{1}{398}$  | 1.5%         | 0.015               | 66.8                         |



↑ a b The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ a b The weight of this item relative to other items in the pool.

↑ a b The odds of finding any of this item in a single chest.

↑ a b The number of items expected per chest, averaged over a large number of chests.

↑ a b The average number of chests the player should expect to search to find any of this item.

↑ a b c d e f g h i j k l m n o p q r All enchantments are equally probable, including treasure enchantments (except Soul Speed, and Swift Sneak), and any level of the enchantment is equally probable.



Most ruined portal structures contain enough obsidian to make a complete portal, although in the smaller portals, there may not enough because each obsidian has a 15%‌[JE  only] or 20%‌[BE  only] chance to be replaced by crying obsidian.

## Data values
### ID
Java Edition:

| Structure type | Identifier      |
|----------------|-----------------|
| Ruined Portal  | `ruined_portal` |

| Structure              | Identifier               |
|------------------------|--------------------------|
| Ruined Portal          | `ruined_portal`          |
| Desert Ruined Portal   | `ruined_portal_desert`   |
| Jungle Ruined Portal   | `ruined_portal_jungle`   |
| Mountain Ruined Portal | `ruined_portal_mountain` |
| Nether Ruined Portal   | `ruined_portal_nether`   |
| Ocean Ruined Portal    | `ruined_portal_ocean`    |
| Swamp Ruined Portal    | `ruined_portal_swamp`    |

Bedrock Edition:

| Structure     | Identifier      | Alias ID       | Translation key         |
|---------------|-----------------|----------------|-------------------------|
| Ruined Portal | `ruined_portal` | `ruinedportal` | `feature.ruined_portal` |

### Config
Java Edition:

- Structure configuration
	- type:minecraft:ruined_portal
	- 
	- Fields common to all structures
	- setups: (Cannot be empty) A list of ruined portal setups to randomly choose one from it.
		- weight: The weight this ruined portal setup is chosen.
		- placement: Eitheron_land_surface,partly_buried,on_ocean_floor,in_mountain,underground,in_nether. Determines how the ruined portal is placed.
		- air_pocket_probability: The probability that the ruined portal generates an air pocket around it. Value between 0.0 and 1.0 (inclusive).
		- mossiness: Determines how mossy the ruined portal is, as an argument forminecraft:block_ageprocessor. Value between 0.0 and 1.0 (inclusive).
		- overgrown: Determines whether or not jungle leaves generate.
		- vines: Determines whether or not vines generate on the ruined portal.
		- can_be_cold: Determines whether or not lava and magma can be replaced with netherrack.
		- replace_with_blackstone: Determines whether or not stone bricks in the ruined portal are replaced with their blackstone equivalents.

