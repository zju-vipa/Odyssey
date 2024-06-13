# Eye of Ender
An eye of ender is a craftable item used to locate strongholds and activate the end portals within them. It is also used to craft an end crystal or an ender chest.

## Contents
- 1 Obtaining
	- 1.1 Crafting
- 2 Usage
	- 2.1 Locating strongholds
	- 2.2 Activating end portals
	- 2.3 Crafting ingredient
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Entity data
- 5 Advancements
- 6 Video
- 7 History
	- 7.1 Historical images
- 8 Issues
- 9 Trivia
- 10 Gallery
	- 10.1 Screenshots
	- 10.2 In other media
- 11 External links
- 12 References

## Obtaining
### Crafting
| Ingredients              | Crafting recipe |
|--------------------------|-----------------|
| Blaze Powder+Ender Pearl |                 |

## Usage
### Locating strongholds
An animation of an eye of ender shattering.
To locate strongholds (and the end portals they house):

- Pressingusewhile holding an eye of ender causes it to fly approximately 12 blocks in the direction of the nearest stronghold, traveling through any blocks necessary, and leave a trail of purple particles, the same particle effect used forendermenandender chests.
	- The eye leads to thechunkwhere a spiral staircase, the first room generated in the stronghold, is located.
	- The center of this entrance staircase is always exactly at the chunk coordinates 4, ~, 4, although the eye of ender leads to chunk coordinates 0, ~, 0 (the northwest corner of the chunk).
- While over 12 blocks away from the northwest corner of the staircase chunk, the eye travels upward to offer an easily-visible indication of the horizontal direction the player must travel.
- When closer than 12 blocks to the northwest corner of the staircase chunk, the eye travels downward, to indicate the player is above a stronghold and must mine downward.
- After two or three seconds of travel, the eye floats in the air briefly, then either falls (becoming collectable again) or shatters in mid-air. The eye has a 20% chance of shattering (80% chance of surviving) per throw, therefore throwing it three times has approximately 50% overall chance to shatter the eye (0.83=51.2%).
- The eye of ender's flying function works only in theOverworld. It does nothing inthe Nether,the End,custom dimensions[verify], or in worlds with no strongholds.

Note that the eyes may point to an incorrect location if the target chunks were generated with a different biomes map in an older version or through different generation settings.[1]

### Activating end portals
An end portal activated with eyes of ender.
Once an end portal is found, the eyes of ender are required to activate it. End portals require a total of 12 eyes of ender in order to activate, though each individual frame-block has a 10% chance of containing an eye of ender when generated. Eyes can be placed in empty end portal frames by pressing use on them until the entire ring of 12 is filled, thereby activating the portal. Due to the fact that there is a 10% chance of each individual end portal frame having an eye in it, there is a one out of one trillion chance of every frame having an eye in it thereby activating the portal even if the player doesn't have any eyes of ender.

| Eyes    | 0    | 1   | 2   | 3   | 4  | 5-12 |
|---------|------|-----|-----|-----|----|------|
| Exactly | 28%  | 38% | 23% | 9%  | 2% | <1%  |
| Or more | 100% | 72% | 34% | 11% | 3% | <1%  |

### Crafting ingredient
| Name        | Ingredients                   | Crafting recipe |
|-------------|-------------------------------|-----------------|
| End Crystal | Glass+Eye of Ender+Ghast Tear |                 |
| Ender Chest | Obsidian+Eye of Ender         |                 |

## Data values
### ID
Java Edition:

| Item         | Identifier | Form | Translation key          |
|--------------|------------|------|--------------------------|
| Eye of Ender | ender_eye  | Item | item.minecraft.ender_eye |

| Entity       | Identifier   | Translation key               |
|--------------|--------------|-------------------------------|
| Eye of Ender | eye_of_ender | entity.minecraft.eye_of_ender |

Bedrock Edition:

| Item         | Identifier | Numeric ID | Form | Translation key     |
|--------------|------------|------------|------|---------------------|
| Eye of Ender | ender_eye  | 433        | Item | item.ender_eye.name |

| Entity       | Identifier          | Numeric ID | Translation key                 |
|--------------|---------------------|------------|---------------------------------|
| Eye of Ender | eye_of_ender_signal | 70         | entity.eye_of_ender_signal.name |

### Entity data
The purple particles left by eyes of ender have entity data that define various properties of the entity.

Java Edition:

Main article: Entity format

 Entity data
Tags common to all entities
 Item: The item to render as, may be absent.
Tags common to all items

Bedrock Edition:

See Bedrock Edition level format/Entity format.
