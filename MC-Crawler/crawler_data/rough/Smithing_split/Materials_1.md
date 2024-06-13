## Blocks
| Material                    | Blocks                            |
|-----------------------------|-----------------------------------|
| Air                         | Air,cave air,void air,light block |
| Amethyst                    |                                   |
| Bamboo                      |                                   |
| Bamboo shoot                | Bamboo shoot                      |
| Barrier                     |                                   |
| Bubble column               |                                   |
| Buildable glass             |                                   |
| Cactus                      |                                   |
| Cake                        |                                   |
| Clay                        |                                   |
| Cloth decoration            |                                   |
| Decoration                  |                                   |
| Dirt                        |                                   |
| Egg                         |                                   |
| Explosive                   |                                   |
| Fire                        |                                   |
| Froglight                   |                                   |
| Frogspawn                   |                                   |
| Glass                       |                                   |
| Grass                       |                                   |
| Heavy metal                 |                                   |
| Ice                         |                                   |
| Ice solid                   |                                   |
| Lava                        |                                   |
| Leaves                      |                                   |
| Metal                       |                                   |
| Moss                        |                                   |
| Nether wood                 |                                   |
| Piston                      |                                   |
| Powder Snow                 |                                   |
| Plant                       |                                   |
| Portal                      |                                   |
| Replaceable plant           |                                   |
| Replaceable fireproof plant |                                   |
| Replacable water plant      |                                   |
| Sand                        |                                   |
| Sculk                       |                                   |
| Shulker shell               |                                   |
| Snow                        |                                   |
| Sponge                      |                                   |
| Stone                       |                                   |
| Structural air              |                                   |
| Top snow                    |                                   |
| Vegetable                   |                                   |
| Water                       |                                   |
| Water plant                 |                                   |
| Web                         |                                   |
| Wood                        |                                   |
| Wool                        |                                   |



## Effects
Material properties are often used in place of specific block property checks, which can sometimes lead to unexpected behavior. Other times, material properties may simply serve as a default, but individual blocks can override this default value.

- Endermenteleport depending on materials that block movement, not whether the block itself issolid. They choose a random destination and then seek downward until they find a block with a movement-blocking material.
- Various things that spawn on the "surface" similarly check material movement-blocking to find the surface.
- Paintings,Item frames,Banners,Signs, andCakesare supported by any block with a solid material. This is why signs can be placed on each other without any visible connection. In addition, paintings and item frames can also be placed on the sides of the redstone comparator and repeater.
- Player spawning checks for obstruction based on whether the material is solid or fluid, apart from banners, pressure plates, and signs.
- Cactusbreak depending on the solidity of an adjacent block's material and whether the adjacent block is lava or whether the material of the upper block is liquid.
- Farmlandanddirt pathturns to dirt if a solid-material block is placed on top, except fence gates. But moving pistons can be placed on farmland.
- Water and lava spread and currents generally depend on whether the block's materials blocks movement, while placement from a bucket depends on whether the material is solid or replaceable, except end portal and end gateway.
- When above a block with a replaceable material, the gravity-affected blocks can fall.
- Only blocks with a solid-blocking material can be redstone conductors.
- Iron golems can be spawned in air or liquid materials above a solid-blocking-material block whose collision box has a square upper surface by villagers.
- When broken,icebecomes water if above a block with a liquid or movement-blocking material.
- Lava checks for a flammable material nearby when attempting to start fires. The fire itself uses its own list of flammable materials, which is why fire can start next to a wood block without consuming the block.
- Block with a movement-blocking material and a full cube collision causes suffocation.
- Various tools check for materials to get breaking speeds.
- Rainandsnowfallfall through blocks that have a non-liquid material that does not block movement.
- Dungeon,lake, andnether portalgeneration checks for solid materials, rather than solid blocks.
- Note blockscheck blocks or materials to determine some instruments. They check for a material of stone, sand, glass, and wood, with the resulting instrument being the base drum, snare, glass, and bass, respectively.
- Doors and trapdoors often use wood and metal materials to differentiate between wood and iron doors and trapdoors.


