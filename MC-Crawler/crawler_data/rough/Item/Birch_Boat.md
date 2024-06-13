# Boat
A boat is a drivable vehicle entity used primarily for fast transport of players and passenger mobs over bodies of water. Bamboo rafts look different, but function almost identically to other boats.

## Contents
- 1 Obtaining
	- 1.1 Crafting
- 2 Usage
	- 2.1 Crafting
	- 2.2 Trading
	- 2.3 Fuel
	- 2.4 Transportation
		- 2.4.1 Entering
		- 2.4.2 Exiting
		- 2.4.3 Motion
- 3 Behavior
	- 3.1 Speed
	- 3.2 Floatation
	- 3.3 Destruction
	- 3.4 Passengers
	- 3.5 Damage prevention
	- 3.6 Collision
	- 3.7 Mobs
	- 3.8 Lead
- 4 Sounds
- 5 Data values
	- 5.1 ID
	- 5.2 Entity data
- 6 Achievements
- 7 Advancements
- 8 History
- 9 Issues
- 10 Trivia
- 11 Gallery
	- 11.1 Icon
	- 11.2 Renders
	- 11.3 Screenshots
	- 11.4 Development images
	- 11.5 Concept artwork
	- 11.6 In other media
- 12 See also
- 13 References
- 14 External links

## Obtaining
Boats can be crafted with any Overworld planks; crimson and warped planks cannot be used to make boats.[1]

Boats can be retrieved by repeatedly hitting them until they drop as an item. In Java Edition, Tools and weapons that deal more than 4 damage can destroy a boat in one hit.

### Crafting
| Ingredients              | Crafting recipe |
|--------------------------|-----------------|
| MatchingOverworld Planks |                 |

## Usage
Boats can be used for the transportation of players and mobs, sold for emeralds, or used as fuel.

### Crafting
| Name            | Ingredients             | Crafting recipe |
|-----------------|-------------------------|-----------------|
| Boat with Chest | Chest+<br/>MatchingBoat |                 |

### Trading
Master-level fisherman villagers always offer to buy a boat for an emerald. The type of boat depends on the biome outfit type of the villager; plains villagers offer to buy oak boats, taiga and snowy villagers offer to buy spruce boats, savanna villagers offer to buy acacia boats, desert and jungle villagers offer to buy jungle boats, and swamp villagers offer to buy dark oak boats.

### Fuel
A boat used as fuel in a furnace lasts 60 seconds, smelting up to 6 items.

### Transportation
See also: Transportation and Riding

#### Entering
A player enters a boat by using it, if the boat is not fully occupied (boats can hold two entities). Unlike beds, there is no message above the hotbar for attempting to enter a fully occupied boat.[2]

#### Exiting
A boat can be exited by sneaking or, in Bedrock Edition, pressing down the right analog stick on a controller, tapping the "Leave Boat" button when using touch controls, or jumping. When exiting a boat, the player is placed in the direction the player is facing, or, if facing directly up or down, the player is placed in front of the boat. The exiting player is placed on land if possible from the dismounting position.

#### Motion
Boats do not turn with mouse-look. 

With a keyboard or gamepad, boats are controlled using the forward, left (turns left), right (turns right), and backward keys. Using the sprint key increases the field of vision, but does not increase speed as if sprinting.

With touchscreen controls, two buttons for steering appear. The right button or key steers to the left, and the left button or key steers to the right. Pressing both buttons or keys moves the boat forward.

In Java Edition, boats can be ridden against a current, but cannot be ridden upstream to a higher elevation. A boat lift, usually made from tripwire, pistons, and optionally a slime block, can be used to move a boat up. Bubble columns created with soul sand can also be used to push boats upward. These mechanisms can also be used in Bedrock Edition but are usually unnecessary because boats can be ridden upward in descending water, as well as follow upward stair-step currents.

## Behavior
### Speed
Boats move according to the player's control or water currents, with speed affected by the surface traversed. Boats move extremely quickly on ice,[3] allowing for the construction of fast transportation systems in any dimension.

| Substance                  | Speed         |
|----------------------------|---------------|
| Water                      | 8.0 blocks/s  |
| Ice,frosted ice,packed ice | 40 blocks/s   |
| Blue ice                   | 72.7 blocks/s |
| Land                       | 2.0 blocks/s  |

### Floatation
The animation of an oak boat when atop a bubble column.
A boat floats atop still or flowing water. In Java Edition, a boat sinks if it enters a waterfall.[4] In Bedrock Edition, a boat does not sink when submerged but floats up. This feature lets a player contrive stepped uphill water flows to propel a boat uphill using only flowing water.

When a boat moves over a bubble column, it begins to shake. If the bubbles are caused by a magma block, all passengers are expelled and the boat sinks.

In Java Edition, a sunken boat cannot be re-floated until a bubble column pushes it up or it is broken by the player. In Bedrock Edition, a boat resumes floating when it emerges from the currents keeping it down, or when the bubble column is blocked or removed.

Dolphins chase players riding a boat in motion, occasionally bumping the boat, causing it to shake briefly.

### Destruction
As boats are entities, they have health. Boats effectively have just over 4 (exactly 4 damage is not enough to destroy a boat), and regenerate 1⁄10 per game tick. Critical hits are not applied to boats although the particles suggest otherwise.

Boats can be destroyed by explosions, fire and lava (but not magma blocks), cactus, and by being punched/shot by mobs, such as drowned. Boats made invulnerable with commands cannot be broken by any of these, but they still cannot be used to travel on lava because they sink.

When a boat is destroyed under normal conditions, it drops itself in item form. In certain conditions, such as when falling for exactly 12, 13, 49, 51, 111, 114, 198, 202, 310, or 315 blocks,[5] it drops two sticks and three planks upon being destroyed.

### Passengers
Multiple mobs in 2 types of boats.
Boats can support two riders, including mobs. Except for endermen in Bedrock Edition, a mob cannot exit a boat and is trapped until the boat gets destroyed, or until the player uses a fishing rod or lead to remove the mob. This can be used to transport mobs, although hostile mobs still attack while in boats. Mobs riding a boat don't despawn‌[Java Edition  only] and don't count toward the mob cap.[6]

A player cannot both move (row) and use items at the same time. It is still possible to initialize item use (e.g. start eating) and row the boat while the item is still in the middle of the use animation. Although the rowing animation overrides the item use animation, the item can still be successfully consumed. This does not work with items that are triggered by the release of the use button (such as bows and tridents).‌[Java Edition  only]

Being in a boat limits the player's mouse-look to the forward 210° arc in Java Edition and 180° in Bedrock Edition.

Underwater boats cannot be ridden. When the boat is underwater, all passengers in it are expelled.

### Damage prevention
Riding a boat does not deplete hunger, making it an efficient way to travel.

Boats can completely nullify fall damage for themselves and any players/mobs inside, making them useful for travel through mountains or through the Nether.[7][8] However in Java Edition, due to a bug, boats can break when falling from certain heights, and the riders take fall damage.[5]

### Collision
A boat has a solid collision box, which means players and other entities can't go through it even with high speed. Falling blocks are also blocked by boats.

In Java Edition, a boat falling on top of an entity stops on top of the entity. In Bedrock Edition, a falling boat can go through other entities.

Riding a boat over a lily pad causes the lily pad to drop, although the boat's speed stutters a bit.

### Mobs
Most mobs can ride boats. Mobs cannot exit the boat unless the boat is destroyed, sinks, or moves over a bubble column. However, in Bedrock Edition, endermen can teleport out of boats.

Mobs can be picked up into the boat when they collide with the side of the boat. A mob cannot control the boat. In Java Edition, a boat being ridden by a player cannot pick up a mob. In Bedrock Edition, mobs can be picked up by a boat being ridden by a player. In Minecraft Education, even tripod cameras can ride boats.

A mob can ride a boat if it is narrower than a boat, and is neither an aquatic[9] nor ambient animal. The following mobs are unable to ride in a boat:

- Agent
- Bat
- Cod
- Dolphin
- Elder guardian
- Ender dragon
- Ghast
- Giant
- Glow squid
- Iron golem
- NPC
- Pufferfish
- Ravager
- Salmon
- Spider
- Squid
- Tadpole
- Tropical fish
- Warden[10]
- Wither[10]

The baby counterparts of these mobs are able to ride in boats, but not the adult versions:

- Camel
- Donkey
- Hoglin
- Horse
- Mule
- Polar bear
- Skeleton horse
- Sniffer
- Zoglin
- Zombie horse

Additionally, few types of mobs can have various Size values, which can prevent them from riding boats:

- Slimeabove size 1
- Magma cubeabove size 1
- Phantomabove size 3

### Lead
In Java Edition, leads cannot be attached to boats. In Bedrock Edition, leads can be attached to boats, though the lead can break when stretched too far due to boats moving much slower on land.

## Data values
### ID
Java Edition:

| Name          | Identifier      | Form | Item tags | Translation key                |
|---------------|-----------------|------|-----------|--------------------------------|
| Oak Boat      | `oak_boat`      | Item | `boats`   | `item.minecraft.oak_boat`      |
| Spruce Boat   | `spruce_boat`   | Item | `boats`   | `item.minecraft.spruce_boat`   |
| Birch Boat    | `birch_boat`    | Item | `boats`   | `item.minecraft.birch_boat`    |
| Jungle Boat   | `jungle_boat`   | Item | `boats`   | `item.minecraft.jungle_boat`   |
| Acacia Boat   | `acacia_boat`   | Item | `boats`   | `item.minecraft.acacia_boat`   |
| Dark Oak Boat | `dark_oak_boat` | Item | `boats`   | `item.minecraft.dark_oak_boat` |
| Mangrove Boat | `mangrove_boat` | Item | `boats`   | `item.minecraft.mangrove_boat` |
| Cherry Boat   | `cherry_boat`   | Item | `boats`   | `item.minecraft.cherry_boat`   |
| Bamboo Raft   | `bamboo_raft`   | Item | `boats`   | `item.minecraft.bamboo_raft`   |

| Entity | Identifier | Translation key         |
|--------|------------|-------------------------|
| Boat   | `boat`     | `entity.minecraft.boat` |

Bedrock Edition:

| Name          | Identifier      | Alias ID   | Numeric ID | Form | Item tags         | Translation key           |
|---------------|-----------------|------------|------------|------|-------------------|---------------------------|
| Oak Boat      | `oak_boat`      | `boat / 0` | `375`      | Item | `minecraft:boats` | `item.boat.oak.name`      |
| Spruce Boat   | `spruce_boat`   | `boat / 1` | `378`      | Item | `minecraft:boats` | `item.boat.spruce.name`   |
| Birch Boat    | `birch_boat`    | `boat / 2` | `376`      | Item | `minecraft:boats` | `item.boat.birch.name`    |
| Jungle Boat   | `jungle_boat`   | `boat / 3` | `377`      | Item | `minecraft:boats` | `item.boat.jungle.name`   |
| Acacia Boat   | `acacia_boat`   | `boat / 4` | `379`      | Item | `minecraft:boats` | `item.boat.acacia.name`   |
| Dark Oak Boat | `dark_oak_boat` | `boat / 5` | `380`      | Item | `minecraft:boats` | `item.boat.big_oak.name`  |
| Mangrove Boat | `mangrove_boat` | `boat / 6` | `643`      | Item | `minecraft:boats` | `item.boat.mangrove.name` |
| Cherry Boat   | `cherry_boat`   | `boat / 8` | `657`      | Item | `minecraft:boats` | `item.boat.cherry.name`   |
| Bamboo Raft   | `bamboo_raft`   | `boat / 7` | `661`      | Item | `minecraft:boats` | `item.boat.bamboo.name`   |

| Entity | Identifier | Numeric ID | Translation key    |
|--------|------------|------------|--------------------|
| Boat   | `boat`     | `90`       | `entity.boat.name` |

### Entity data
Boats have entity data associated with them that contain various properties of the entity.

Java Edition:

Main article: Entity format
- Entity data
	- 
	- Tags common to all boats
	- 
	- Tags common to all entities


Boat Type
Main article: Boat/DV[edit]

Bedrock Edition: 

SeeBedrock Edition level format/Entity format.
