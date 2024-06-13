# Cave Vines (feature)
Cave vines is a feature that consists of glow berries, found in the lush caves biome.

## Contents
- 1 Generation
- 2 Data values
	- 2.1 ID
	- 2.2 Config

## Generation
Cave vines generate as a block column hanging from the ceiling of caves. Their height varies between 1 and 20 blocks.

## Data values
### ID
Java Edition:

| Feature type        | Identifier     |
|---------------------|----------------|
| [No displayed name] | `block_column` |

Java Edition:

| Configured feature  | Identifier  |
|---------------------|-------------|
| [No displayed name] | `cave_vine` |

### Config
Main article: Configured feature
Java Edition:

- config
	- directionThe direction of the column. One ofup,down,north,east,south, orwest.
	- allowed_placementA block predicate. The predicate must be passed to generate this feature.
		- 
		- Block predicate
	- prioritize_tipDetermines where to cut off blocks when space is restricted. Iftrue, starts removing layers from the start of the column.
	- layers(Required, but can be empty) The layers of this column.
		- A layer.
			- heightSpecifying the height of the layer. Must be a non-negative int.
				- 
				- Int provider
			- providerThe block to use for this layer.
				- 
				- Block state provider


An example

{
  "type": "minecraft:block_column",
  "config": {
    "direction": "down",
    "allowed_placement": {
      "type": "minecraft:matching_blocks",
      "blocks": "minecraft:air"
    },
    "prioritize_tip": true,
    "layers": [
      {
        "height": {
          "type": "minecraft:uniform",
          "value": {
            "min_inclusive": 2,
            "max_inclusive": 5
          }
        },
        "provider": {
          "type": "minecraft:simple_state_provider",
          "state": {
            "Name": "minecraft:cave_vines_plant"
          }
        }
      },
      {
        "height": 1,
        "provider": {
          "type": "minecraft:simple_state_provider",
          "state": {
            "Name": "minecraft:cave_vines"
          }
        }
      }
    ]
  }
}





| Terrain features |                                                                                                                                                                                          |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Overworld        | Terrain   Floating island Hill Mountain Noise cave   Surface   Erosion Hoodoo Strip Surface layer   Carver   Canyon Carver cave   Water bodies   Aquifer Ocean River   Others   Ore vein |
| Terrain          | Floating island<br/>Hill<br/>Mountain<br/>Noise cave<br/>                                                                                                                                |
| Surface          | Erosion<br/>Hoodoo<br/>Strip<br/>Surface layer<br/>                                                                                                                                      |
| Carver           | Canyon<br/>Carver cave<br/>                                                                                                                                                              |
| Water bodies     | Aquifer<br/>Ocean<br/>River<br/>                                                                                                                                                         |
| Others           | Ore vein<br/>                                                                                                                                                                            |
| The Nether       | Carver cave<br/>Lava sea<br/>                                                                                                                                                            |
| The End          | Central island<br/>Obsidian platform<br/>Outer islands<br/>                                                                                                                              |
| Removed          | Beach (world feature) Gravel<br/>Gravel<br/>Clay blob<br/>Far Lands<br/>Underwater cave<br/>Underwater ravine<br/>Java Edition only   Monolith                                           |
| Java Editiononly | Monolith<br/>                                                                                                                                                                            |

| Terrain      | Floating island Hill Mountain Noise cave            |
|--------------|-----------------------------------------------------|
| Surface      | Erosion<br/>Hoodoo<br/>Strip<br/>Surface layer<br/> |
| Carver       | Canyon<br/>Carver cave<br/>                         |
| Water bodies | Aquifer<br/>Ocean<br/>River<br/>                    |
| Others       | Ore vein<br/>                                       |

| Java Edition only | Monolith |
|-------------------|----------|

| Structures       |                                                                                                                                                                                                                                                                                        |  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| Overworld        | Ruined Portal<br/>Surface   Desert Pyramid Igloo Jungle Pyramid Pillager Outpost Swamp Hut Woodland Mansion Village Farm   Underwater   Ocean Monument Ocean Ruins Shipwreck   Underground   Ancient City Buried Treasure Mineshaft Stronghold Trail Ruins   Upcoming   Trial Chambers |  |
| Surface          | Desert Pyramid<br/>Igloo<br/>Jungle Pyramid<br/>Pillager Outpost<br/>Swamp Hut<br/>Woodland Mansion<br/>Village Farm<br/>Farm<br/>                                                                                                                                                     |  |
| Underwater       | Ocean Monument<br/>Ocean Ruins<br/>Shipwreck<br/>                                                                                                                                                                                                                                      |  |
| Underground      | Ancient City<br/>Buried Treasure<br/>Mineshaft<br/>Stronghold<br/>Trail Ruins<br/>Upcoming   Trial Chambers                                                                                                                                                                            |  |
| Upcoming         | Trial Chambers<br/>                                                                                                                                                                                                                                                                    |  |
| The Nether       | Bastion Remnant<br/>Nether Fortress<br/>Nether Fossil<br/>Ruined Portal<br/>                                                                                                                                                                                                           |  |
| The End          | End City<br/>                                                                                                                                                                                                                                                                          |  |
| Utility          | Jigsaw<br/>                                                                                                                                                                                                                                                                            |  |
| Joke             | 9x9.nbt<br/>Bonus barrel<br/>Bridge<br/>Colosseum<br/>command.com.nbt<br/>content.nbt<br/>desire.nbt<br/>house_of_bob.nbt<br/>library.nbt<br/>llama.nbt<br/>Lunar Base<br/>Potato Mineshaft<br/>Potato Village<br/>Ruined Portatol<br/>Shapes<br/>                                     |  |
| Removed          | Village (old)<br/>Java Edition only   Brick pyramid Glass Pillars Obsidian wall Starting house                                                                                                                                                                                         |  |
| Java Editiononly | Brick pyramid<br/>Glass Pillars<br/>Obsidian wall<br/>Starting house<br/>                                                                                                                                                                                                              |  |

| Surface     | Desert Pyramid Igloo Jungle Pyramid Pillager Outpost Swamp Hut Woodland Mansion Village Farm                |
|-------------|-------------------------------------------------------------------------------------------------------------|
| Underwater  | Ocean Monument<br/>Ocean Ruins<br/>Shipwreck<br/>                                                           |
| Underground | Ancient City<br/>Buried Treasure<br/>Mineshaft<br/>Stronghold<br/>Trail Ruins<br/>Upcoming   Trial Chambers |
| Upcoming    | Trial Chambers<br/>                                                                                         |

| Upcoming | Trial Chambers |
|----------|----------------|

| Java Edition only | Brick pyramid Glass Pillars Obsidian wall Starting house |
|-------------------|----------------------------------------------------------|

| Features                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Overworld                      | Lava lake<br/>Spring<br/>Surface   Bonus Chest Desert well Disk Iceberg Blue Ice Ice Patch Ice spike Freeze top layer Forest rock Pile   Underground   Amethyst geode Pointed Dripstone Dripstone cluster Large dripstone Monster room Fossil Ore Underwater magma   Vegetation   Patched vegetations Bamboo Coral reef Kelp Sea Pickle Seagrass Glow Lichen Sculk Vein Sculk patch Huge mushroom Root system Tree Oak Spruce Birch Jungle Jungle Bush Acacia Dark oak Azalea tree Mangrove Cherry Vines Cave Vines Vegetation patch   Java EditionSuperflat only   Void start platform Fill layer |
| Surface                        | Bonus Chest<br/>Desert well<br/>Disk<br/>Iceberg<br/>Blue Ice<br/>Ice Patch<br/>Ice spike<br/>Freeze top layer<br/>Forest rock<br/>Pile<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Underground                    | Amethyst geode<br/>Pointed Dripstone Dripstone cluster Large dripstone<br/>Dripstone cluster<br/>Large dripstone<br/>Monster room<br/>Fossil<br/>Ore<br/>Underwater magma<br/>                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Vegetation                     | Patched vegetations<br/>Bamboo<br/>Coral reef<br/>Kelp<br/>Sea Pickle<br/>Seagrass<br/>Glow Lichen<br/>Sculk Vein<br/>Sculk patch<br/>Huge mushroom<br/>Root system<br/>Tree Oak Spruce Birch Jungle Jungle Bush Acacia Dark oak Azalea tree Mangrove Cherry<br/>Oak<br/>Spruce<br/>Birch<br/>Jungle<br/>Jungle Bush<br/>Acacia<br/>Dark oak<br/>Azalea tree<br/>Mangrove<br/>Cherry<br/>Vines<br/>Cave Vines<br/>Vegetation patch<br/>                                                                                                                                                            |
| Java Edition<br/>Superflatonly | Void start platform<br/>Fill layer<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| The Nether                     | Basalt columns<br/>Basalt pillar<br/>Blob<br/>Delta<br/>Glowstone blob<br/>Lava spring<br/>Fire patch<br/>Vegetation   Nether forest vegetation Twisting Vines Weeping Vines Huge fungus                                                                                                                                                                                                                                                                                                                                                                                                           |
| Vegetation                     | Nether forest vegetation<br/>Twisting Vines<br/>Weeping Vines<br/>Huge fungus<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| The End                        | Chorus plant<br/>Exit portal<br/>End gateway<br/>End spike<br/>Small island<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Utility                        | no_op<br/>Random boolean selector<br/>Random selector<br/>Replace single block<br/>Simple block<br/>Simple random selector<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Joke                           | Hash Well<br/>Potato Geode<br/>Potato Tree<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Removed                        | Water lake<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

| Surface                        | Bonus Chest Desert well Disk Iceberg Blue Ice Ice Patch Ice spike Freeze top layer Forest rock Pile                                                                                                                                                                                                                                                                                                                                     |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Underground                    | Amethyst geode<br/>Pointed Dripstone Dripstone cluster Large dripstone<br/>Dripstone cluster<br/>Large dripstone<br/>Monster room<br/>Fossil<br/>Ore<br/>Underwater magma<br/>                                                                                                                                                                                                                                                          |
| Vegetation                     | Patched vegetations<br/>Bamboo<br/>Coral reef<br/>Kelp<br/>Sea Pickle<br/>Seagrass<br/>Glow Lichen<br/>Sculk Vein<br/>Sculk patch<br/>Huge mushroom<br/>Root system<br/>Tree Oak Spruce Birch Jungle Jungle Bush Acacia Dark oak Azalea tree Mangrove Cherry<br/>Oak<br/>Spruce<br/>Birch<br/>Jungle<br/>Jungle Bush<br/>Acacia<br/>Dark oak<br/>Azalea tree<br/>Mangrove<br/>Cherry<br/>Vines<br/>Cave Vines<br/>Vegetation patch<br/> |
| Java Edition<br/>Superflatonly | Void start platform<br/>Fill layer<br/>                                                                                                                                                                                                                                                                                                                                                                                                 |

| Vegetation | Nether forest vegetation Twisting Vines Weeping Vines Huge fungus |
|------------|-------------------------------------------------------------------|

