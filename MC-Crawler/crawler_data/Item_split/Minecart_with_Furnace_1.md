## Properties
The coal is not stored as an item in the entity, but in the object data in the fuel property as a time in ticks. Fuel is a short value, i.e. a maximum of 32767 ticks, which is about 27 minutes. However, /summon furnace_minecart ~ ~ ~ {Fuel:32000} alone doesn't make it go since it doesn't have a direction. It can be right-clicked on a track to give it a direction, or it can be summoned with the properties PushX and PushZ set, which are responsible for the direction. The Motion property of every entity allows for movement of the minecart, but it does not direct the minecart to move on its own.

## Data values
### ID
| Item                  | Identifier       | Form | Translation key                 |
|-----------------------|------------------|------|---------------------------------|
| Minecart with Furnace | furnace_minecart | Item | item.minecraft.furnace_minecart |

| Entity                | Identifier       | Translation key                   |
|-----------------------|------------------|-----------------------------------|
| Minecart with Furnace | furnace_minecart | entity.minecraft.furnace_minecart |

### Entity data
Minecarts with furnace have entity data associated with them that contain various properties of the entity.

Java Edition:

Main article: Entity format

 Entity data
Tags common to all entities
Tags common to all minecarts
 Fuel: The number of ticks until the minecart runs out of fuel.
 PushX: Force along X axis, used for smooth acceleration/deceleration.
 PushZ: Force along Z axis, used for smooth acceleration/deceleration.

Bedrock Edition:

See Bedrock Edition level format/Entity format.

