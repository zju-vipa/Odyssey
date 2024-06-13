### Redstone component
See also: Redstone circuit

Activator rails can be used to affect minecarts that travel over them.

Activation
An activator rail is a redstone mechanism and can be activated by:
an adjacent active power component (for example, a redstone torch, a block of redstone, a daylight sensor, etc.)
an adjacent powered block (strongly-powered or weakly-powered)
a powered redstone comparator or redstone repeater facing the activator rail
powered redstone dust configured to point at the activator rail, or configured as a plus sign. An activator rail is not activated by adjacent powered redstone dust that is configured to point in another direction.
An activated activator rail also activates any adjacent activator rails it is connected to, up to eight away from the original activation source. Thus a single activation source can activate up to 17 rails (one original in the middle and eight on either side). An activated activator rail does not activate adjacent rails not connected to it.
Activation and deactivation are instant and occur in the same gametick the power source turns on or off (any eventual delay depends on the power source).
Behavior
An activator rail affects minecarts above it with varying effects that occur as soon as any part of the minecart is on the activator rail.

An active activator rail:

- starts shaking, and ejects mobs (including players) from minecarts — the destination location is picked the same way as whendismountinga minecart
- repeatedly activatesminecarts with command blocks— a command block minecart executes its command every four game ticks until the command block minecart is no longer on the activator rail
- disablesminecarts with hoppers— a disabled hopper minecart cannot pick up items it travels through until it is enabled by an inactive activator rail (or until it is broken and re-placed)
- primesminecarts with TNT— primed TNT minecarts explode after four seconds with an explosive power proportional to their speed over the activator rail.

An inactive activator rail enables minecarts with hoppers — an enabled hopper minecart picks up items it travels through until it is disabled by an active activator rail.

A hopper minecart stops picking up items in the same tick it touches an active activator rail or in the same tick the inactive rail it is standing on is powered (it does not collect the item it could have taken from a container above in the same tick the activator rail turns on and takes the first item in the same tick the rail turns off again).

### Mob interaction
Like other types of rails, spiders, cave spiders, and wardens are the only land mobs that can walk onto activator rails.

## Data values
### ID
Java Edition:

| Name           | Identifier     | Form         | Block tags                       | Item tags | Translation key                |
|----------------|----------------|--------------|----------------------------------|-----------|--------------------------------|
| Activator Rail | activator_rail | Block & Item | prevent_mob_spawning_insiderails | rails     | block.minecraft.activator_rail |

Bedrock Edition:

| Name           | Identifier     | Numeric ID | Form                       | Item ID[i 1]   | Translation key          |
|----------------|----------------|------------|----------------------------|----------------|--------------------------|
| Activator Rail | activator_rail | 126        | Block & Giveable Item[i 2] | Identical[i 3] | tile.activator_rail.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values                                             | Description                                                                                                                                     |
|-------------|---------------|------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| powered     | false         | falsetrue                                                  | True if rail is activated.                                                                                                                      |
| shape       | north_south   | east_westnorth_south                                       | Specifies the rail's orientation.                                                                                                               |
|             |               | ascending_eastascending_northascending_southascending_west | A rail that ascendstowardthe direction noted.For example, anascending_westrail is a straight rail that goes upward from the easttowardthe west. |
| waterlogged | false         | falsetrue                                                  | Whether or not there's water in the same place as this rail.                                                                                    |

Bedrock Edition:

| Name           | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                         |
|----------------|---------------|---------------|----------------|-------------------------|-------------------------------------|
| rail_data_bit  | 0x8           | false         | falsetrue      | 01                      | True if rail is activated.          |
| rail_direction | 0x10x20x4     | 0             | 0              | 0                       | flat track going north-south        |
|                |               |               | 1              | 1                       | flat track going east-west          |
|                |               |               | 2              | 2                       | sloped track ascending to the east  |
|                |               |               | 3              | 3                       | sloped track ascending to the west  |
|                |               |               | 4              | 4                       | sloped track ascending to the north |
|                |               |               | 5              | 5                       | sloped track ascending to the south |
|                |               |               | 6789           | Unsupported             | Unused                              |

## See also
- Rail
- Powered rail
- Detector rail


