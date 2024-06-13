### Fuel
Overworld wooden pressure plates can be used as a fuel in furnaces, smelting 1.5 items per pressure plate. Nether wood pressure plates (crimson and warped), cannot be used as fuel in a furnace.

### Note blocks
Wooden pressure plates can be placed under note blocks to produce "bass" sounds.

## Data values
### ID
Java Edition:

| Name                    | Identifier              | Form         | Block tags                                                                | Item tags                                | Translation key                         |
|-------------------------|-------------------------|--------------|---------------------------------------------------------------------------|------------------------------------------|-----------------------------------------|
| Oak Pressure Plate      | oak_pressure_plate      | Block & Item | pressure_plateswall_post_overridewooden_pressure_plates                   | wooden_pressure_plates                   | block.minecraft.oak_pressure_plate      |
| Spruce Pressure Plate   | spruce_pressure_plate   | Block & Item | pressure_plateswall_post_overridewooden_pressure_plates                   | wooden_pressure_plates                   | block.minecraft.spruce_pressure_plate   |
| Birch Pressure Plate    | birch_pressure_plate    | Block & Item | pressure_plateswall_post_overridewooden_pressure_plates                   | wooden_pressure_plates                   | block.minecraft.birch_pressure_plate    |
| Jungle Pressure Plate   | jungle_pressure_plate   | Block & Item | pressure_plateswall_post_overridewooden_pressure_plates                   | wooden_pressure_plates                   | block.minecraft.jungle_pressure_plate   |
| Acacia Pressure Plate   | acacia_pressure_plate   | Block & Item | pressure_plateswall_post_overridewooden_pressure_plates                   | wooden_pressure_plates                   | block.minecraft.acacia_pressure_plate   |
| Dark Oak Pressure Plate | dark_oak_pressure_plate | Block & Item | pressure_plateswall_post_overridewooden_pressure_plates                   | wooden_pressure_plates                   | block.minecraft.dark_oak_pressure_plate |
| Mangrove Pressure Plate | mangrove_pressure_plate | Block & Item | pressure_plateswall_post_overridewooden_pressure_plates                   | wooden_pressure_plates                   | block.minecraft.mangrove_pressure_plate |
| Cherry Pressure Plate   | cherry_pressure_plate   | Block & Item | pressure_plateswall_post_overridewooden_pressure_plates                   | wooden_pressure_plates                   | block.minecraft.cherry_pressure_plate   |
| Bamboo Pressure Plate   | bamboo_pressure_plate   | Block & Item | pressure_plateswall_post_overridewooden_pressure_plates                   | wooden_pressure_plates                   | block.minecraft.bamboo_pressure_plate   |
| Crimson Pressure Plate  | crimson_pressure_plate  | Block & Item | non_flammable_woodpressure_plateswall_post_overridewooden_pressure_plates | non_flammable_woodwooden_pressure_plates | block.minecraft.crimson_pressure_plate  |
| Warped Pressure Plate   | warped_pressure_plate   | Block & Item | non_flammable_woodpressure_plateswall_post_overridewooden_pressure_plates | non_flammable_woodwooden_pressure_plates | block.minecraft.warped_pressure_plate   |

Bedrock Edition:

| Name                    | Identifier              | Numeric ID | Form                       | Item ID[i 1]   | Translation key                   |
|-------------------------|-------------------------|------------|----------------------------|----------------|-----------------------------------|
| Oak Pressure Plate      | wooden_pressure_plate   | 72         | Block & Giveable Item[i 2] | Identical[i 3] | tile.wooden_pressure_plate.name   |
| Spruce Pressure Plate   | spruce_pressure_plate   | 409        | Block & Giveable Item[i 2] | Identical[i 3] | tile.spruce_pressure_plate.name   |
| Birch Pressure Plate    | birch_pressure_plate    | 406        | Block & Giveable Item[i 2] | Identical[i 3] | tile.birch_pressure_plate.name    |
| Jungle Pressure Plate   | jungle_pressure_plate   | 408        | Block & Giveable Item[i 2] | Identical[i 3] | tile.jungle_pressure_plate.name   |
| Acacia Pressure Plate   | acacia_pressure_plate   | 405        | Block & Giveable Item[i 2] | Identical[i 3] | tile.acacia_pressure_plate.name   |
| Dark Oak Pressure Plate | dark_oak_pressure_plate | 407        | Block & Giveable Item[i 2] | Identical[i 3] | tile.dark_oak_pressure_plate.name |
| Mangrove Pressure Plate | mangrove_pressure_plate | -490       | Block & Giveable Item[i 2] | Identical[i 3] | tile.mangrove_pressure_plate.name |
| Cherry Pressure Plate   | cherry_pressure_plate   | -538       | Block & Giveable Item[i 2] | Identical[i 3] | tile.cherry_pressure_plate.name   |
| Bamboo Pressure Plate   | bamboo_pressure_plate   | -514       | Block & Giveable Item[i 2] | Identical[i 3] | tile.bamboo_pressure_plate.name   |
| Crimson Pressure Plate  | crimson_pressure_plate  | 517        | Block & Giveable Item[i 2] | Identical[i 3] | tile.crimson_pressure_plate.name  |
| Warped Pressure Plate   | warped_pressure_plate   | 518        | Block & Giveable Item[i 2] | Identical[i 3] | tile.warped_pressure_plate.name   |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ a b c d e f g h i j k Available with /give command.

↑ a b c d e f g h i j k The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:

| Name    | Default value | Allowed values | Description                                           |
|---------|---------------|----------------|-------------------------------------------------------|
| powered | false         | falsetrue      | True if pressure plate is depressed, providing power. |

Bedrock Edition:

| Name            | Metadata Bits | Default value | Allowed values       | Values forMetadata Bits | Description                                      |
|-----------------|---------------|---------------|----------------------|-------------------------|--------------------------------------------------|
| redstone_signal | 0x1           | 0             | 01                   | 01                      | Specifies whether the pressure plate is pressed. |
|                 |               |               | 23456789101112131415 | Unsupported             | Unused                                           |


