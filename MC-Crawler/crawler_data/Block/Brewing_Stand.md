# Brewing Stand
A brewing stand is a block used for brewing potions using water bottles and suitable ingredients. It also serves as a cleric's job site block.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Brewing
	- 2.2 Changing profession
	- 2.3 Light source
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Block data
- 5 Achievements
- 6 Advancements
- 7 History
	- 7.1 Brewing stand "item"
		- 7.1.1 Appearances
		- 7.1.2 Names
- 8 Issues
- 9 Trivia
- 10 Gallery
	- 10.1 Screenshots
- 11 See also
- 12 References
- 13 External links

## Obtaining
### Breaking
A brewing stand can be obtained using any pickaxe. If mined without a pickaxe, it drops nothing in Java Edition, while it drops itself in Bedrock Edition. However, destroying a brewing stand that is completely full with blaze powder drops the powder with it.

| Block     | Brewing Stand         |
|-----------|-----------------------|
| Hardness  | 0.5                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 2.5                   |
| Wooden    | 0.4                   |
| Stone     | 0.2                   |
| Iron      | 0.15                  |
| Diamond   | 0.1                   |
| Netherite | 0.1                   |
| Golden    | 0.1                   |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Natural generation
Brewing stands generate in end ships. They have two Instant Health II potions in their holders. 

A brewing stand also generates in the basement of igloos with a splash potion of Weakness in it.

Brewing stands can generate without potions in village churches.

### Crafting
| Ingredients                   | Crafting recipe | Description                                                 |
|-------------------------------|-----------------|-------------------------------------------------------------|
| Blaze Rod+Anystone-tier block |                 | Can use cobblestone and its other variants interchangeably. |

## Usage
Brewing stand GUI in Java Edition
By default, the interface of a brewing stand is labeled "Brewing Stand", but this name can be customized by naming it in an anvil before placing it.

Brewing stands cannot be pushed by pistons in Java Edition.

### Brewing
Main article: Brewing
The main purpose of brewing stands is to allow for the brewing of potions. Its interface can be opened by pressing use on them.

Brewing stands need blaze powder as fuel. Each piece brews 20 batches of potions, with each stage of brewing counting separately. Unlike furnaces, there is no time limit; fuel is consumed only when there are water bottles and an ingredient to brew into it.

Brewing stands interact with hoppers as follows:

- They accept brewing ingredients from hoppers pointing down into the top.
- Any valid brewing ingredient will be pushed into the ingredient slot, regardless of whether or not it would actually start the brewing process.
- Any valid potion recipe can be preloaded for "hands-free" brewing of a complex recipe, with thenether wartfalling through into the stand for the first step.
- Bottles (including empty bottles) and fuel are accepted from hoppers pointing into the side.
- Finished products can be pulled out by hoppers below, but each stage of brewing counts as a batch of "finished" potions.

In Minecraft Education, elements can be combined in the brewing stand to make the medicine potions: antidote, elixir, eye drops, and tonic.

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

