### Changing profession
If a village has a brewing stand that has not been claimed by a villager, any villager who hasn't already picked a job site block in the village has a chance to change their profession into cleric.

### Light source
Brewing stands emit a light level of 1.‌[Java Edition  only]

## Data values
### ID
Java Edition:

| Name          | Identifier    | Form         | Translation key                                           |
|---------------|---------------|--------------|-----------------------------------------------------------|
| Brewing Stand | brewing_stand | Block & Item | block.minecraft.brewing_standitem.minecraft.brewing_stand |

| Name         | Identifier    |
|--------------|---------------|
| Block entity | brewing_stand |

Bedrock Edition:

| Brewing Stand | Identifier    | Numeric ID | Form                         | Item ID[i 1]       | Translation key         |
|---------------|---------------|------------|------------------------------|--------------------|-------------------------|
| Block         | brewing_stand | 117        | Block & Ungiveable Item[i 2] | item.brewing_stand | —                       |
| Item          | brewing_stand | 431        | Item                         | —                  | item.brewing_stand.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Unavailable with /give command


| Name         | Savegame ID  |
|--------------|--------------|
| Block entity | BrewingStand |

### Block states
See also: Block states

Java Edition:

| Name         | Default value | Allowed values | Description                      |
|--------------|---------------|----------------|----------------------------------|
| has_bottle_0 | false         | falsetrue      | True when a bottle is in slot 1. |
| has_bottle_1 | false         | falsetrue      | True when a bottle is in slot 2. |
| has_bottle_2 | false         | falsetrue      | True when a bottle is in slot 3. |

Bedrock Edition:

| Name                     | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                      |
|--------------------------|---------------|---------------|----------------|-------------------------|----------------------------------|
| brewing_stand_slot_a_bit | 0x1           | false         | falsetrue      | 01                      | True when a bottle is in slot 1. |
| brewing_stand_slot_b_bit | 0x2           | false         | falsetrue      | 01                      | True when a bottle is in slot 2. |
| brewing_stand_slot_c_bit | 0x4           | false         | falsetrue      | 01                      | True when a bottle is in slot 3. |



### Block data
A brewing stand has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format


 Block entity data
Tags common to all block entities
 BrewTime: The number of ticks the potions have to brew.

 CustomName: Optional. The name of this container in JSON text component, which appears in its GUI where the default name ordinarily appears.
 Fuel: Remaining fuel for the brewing stand. 20 when full, and counts down by 1 each time a potion is brewed.
 Items: List of items in this container.
: An item in the brewing stand, including the slot tag:Slot 0: Left potion slot.Slot 1: Middle potion slot.Slot 2: Right potion slot.Slot 3: Where the potion ingredient goes. Slot 4: Fuel (Blaze Powder).
Tags common to all items

 Lock: Optional. When not blank, prevents the container from being opened unless the opener is holding an item whose name matches this string.

Bedrock Edition:

See Bedrock Edition level format/Block entity format.
## See also
- Glass Bottle
- Splash Potion


