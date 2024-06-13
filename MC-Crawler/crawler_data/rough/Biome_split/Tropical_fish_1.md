### Bedrock Edition
Tropical fish do not have common varieties in Bedrock Edition. Instead, naturally spawned tropical fish have 2 spawn attempts, the first chooses one of the 22 preset variants, and the other use randomly chosen patterns, sizes, shapes, and colors (except black).
Tropical fish spawned from a spawn egg use randomly chosen patterns, sizes, shapes, and colors (except black).
By using commands, tropical fish may be spawned as one of the 22 preset variants (due to MCPE-117477, Yellowtail Parrot Fish do not spawn, therefore only 21 preset variants exist on Bedrock Edition).

### Names
Tropical fish variants in buckets have names that are assigned based on their colors and type. In Bedrock Edition, the names are in the name of the bucket, giving names like "Bucket of Dottyback", "Bucket of Sky-Orange Snooper", or "Bucket of Orange-Lime Dasher". In Java Edition, the type, and colors are displayed as item tooltips. 

In Bedrock Edition, the following colors are renamed from their defaults when they refer to tropical fish. Parentheses indicate default name and color id - see § Entity data.

- Sky(Light Blue; 3)
- Rose(Pink; 6)
- Silver(Light Gray; 8)
- Teal(Cyan; 9)
- Plum(Purple; 10)

The base color is first, and the pattern color is next if it is different.

The fish type is determined according to the shape and pattern of the fish:

| Flopper |  |  |  | Glitter |  |  |  | Betty     |  |  |  |          |
|---------|--|--|--|---------|--|--|--|-----------|--|--|--|----------|
|         |  |  |  | Stripey |  |  |  | Blockfish |  |  |  | Clayfish |

| Kob |  |  |  | Snooper        |  |  |  | Brinely |  |  |  |        |
|-----|--|--|--|----------------|--|--|--|---------|--|--|--|--------|
|     |  |  |  | Sunstreak[n 1] |  |  |  | Dasher  |  |  |  | Spotty |

Some varieties of tropical fish don't follow the normal naming system; instead, they reference real-life fish species. In Java Edition, these unique fish are limited to the 22 common varieties. In Bedrock Edition, there are also 22 uniquely-named tropical fish, though they are not all the same as in Java Edition. These uniquely-named tropical fish aren't different from regular tropical fish in terms of design or behavior.

These varieties are:

| Name                                                              | Type                                                                    | Image |
|-------------------------------------------------------------------|-------------------------------------------------------------------------|-------|
| Anemone                                                           | Orange-Gray Stripey                                                     |       |
| Black Tang                                                        | Gray Flopper                                                            |       |
| Blue Tang‌[JE  only]                                              | Gray-Blue Flopper                                                       |       |
| Blue Dory‌[BE  only]                                              | Gray-Sky SunStreak                                                      |       |
| Butterflyfish‌[JE  only]<br/>Butterfly Fish‌[BE  only]            | White-Gray Clayfish                                                     |       |
| Cichlid                                                           | Blue-Gray Sunstreak‌[JE  only]<br/>Blue-Gray SunStreak‌[BE  only]       |       |
| Clownfish                                                         | Orange-White Kob                                                        |       |
| Cotton Candy Betta                                                | Pink-Light Blue Spotty‌[JE  only]<br/>Rose-Sky Spotty‌[BE  only]        |       |
| Dottyback                                                         | Purple-Yellow Blockfish‌[JE  only]<br/>Plum-Yellow Blockfish‌[BE  only] |       |
| Emperor Red Snapper                                               | White-Red Clayfish                                                      |       |
| Goatfish                                                          | White-Yellow Spotty                                                     |       |
| Moorish Idol                                                      | White-Gray Glitter                                                      |       |
| Ornate Butterflyfish‌[JE  only]<br/>Ornate Butterfly‌[BE  only]   | White-Orange Clayfish                                                   |       |
| Parrotfish                                                        | Cyan-Pink Dasher‌[JE  only]<br/>Teal-Rose Dasher‌[BE  only]             |       |
| Queen Angelfish‌[JE  only]<br/>Queen Angel Fish‌[BE  only]        | Lime-Light Blue Brinely‌[JE  only]<br/>Lime-Sky Brinely‌[BE  only]      |       |
| Red Cichlid                                                       | Red-White Betty                                                         |       |
| Red Lipped Blenny                                                 | Gray-Red Snooper                                                        |       |
| Red Snapper                                                       | Red-White Blockfish                                                     |       |
| Threadfin                                                         | White-Yellow Flopper                                                    |       |
| Tomato Clownfish‌[JE  only]                                       | Red-White Kob                                                           |       |
| Tomato Clown‌[BE  only]                                           | Red-White SunStreak                                                     |       |
| Triggerfish                                                       | Gray-White Sunstreak‌[JE  only]<br/>Gray-White SunStreak‌[BE  only]     |       |
| Yellowtail Parrotfish‌[JE  only]<br/>Yellowtail Parrot‌[BE  only] | Cyan-Yellow Dasher‌[JE  only]<br/>Teal-Yellow Dasher‌[BE  only]         |       |
| Yellow Tang                                                       | Yellow Flopper                                                          |       |

1. ↑Sunstreak in Java Edition, SunStreak in Bedrock Edition.

## Data values
### ID
Java Edition:

| Name          | Identifier      | Entity tags                                                                                                                   | Translation key                  |
|---------------|-----------------|-------------------------------------------------------------------------------------------------------------------------------|----------------------------------|
| Tropical Fish | `tropical_fish` | `aquatic`<br/>`axolotl_hunt_targets`<br/>`can_breathe_under_water`<br/>`not_scary_for_pufferfish`<br/>`sensitive_to_impaling` | `entity.minecraft.tropical_fish` |

Bedrock Edition:

| Name          | Identifier     | Numeric ID | Translation key            |
|---------------|----------------|------------|----------------------------|
| Tropical Fish | `tropicalfish` | `111`      | `entity.tropicalfish.name` |

### Entity data
Tropical fish have entity data associated with them that contains various properties.

Bedrock Edition:

SeeBedrock Edition level format/Entity format.
Java Edition:

Main article: Entity format
- Entity data
	- 
	- Tags common to all entities
	- 
	- Tags common to all mobs
	- FromBucket: 1 or 0 (true/false) - Whether the fish had ever been released from a bucket.
	- Variant: A 4-byte integer.
		- The least significant byte has a value of either 0 for a small fish, or 1 for a large fish.  Values above 1 result in an invisible fish.
		- The next byte has a value from 0–5, representing the pattern on the fish.  Values above 5 result in a fish with no pattern.
		- The next byte has a value from 0–15, representing the color of the fish's body.
		- The most significant byte has a value from 0–15, representing the color of the fish's pattern.


Color
Main article: Tropical Fish/DV[edit]

The fish sizes and patterns are depicted in the following table, with white body color and dark-gray pattern color.

| Flopper    Glitter    Betty       Stripey    Blockfish    Clayfish |           |         |           |         |          |
|--------------------------------------------------------------------|-----------|---------|-----------|---------|----------|
| Flopper                                                            |           | Glitter |           | Betty   |          |
|                                                                    | Stripey   |         | Blockfish |         | Clayfish |
|                                                                    |           |         |           |         |          |
| Kob    Snooper    Brinely       Sunstreak    Dasher    Spotty      |           |         |           |         |          |
| Kob                                                                |           | Snooper |           | Brinely |          |
|                                                                    | Sunstreak |         | Dasher    |         | Spotty   |

| Flopper |  |  |  | Glitter |  |  |  | Betty     |  |  |  |          |
|---------|--|--|--|---------|--|--|--|-----------|--|--|--|----------|
|         |  |  |  | Stripey |  |  |  | Blockfish |  |  |  | Clayfish |

| Kob |  |  |  | Snooper   |  |  |  | Brinely |  |  |  |        |
|-----|--|--|--|-----------|--|--|--|---------|--|--|--|--------|
|     |  |  |  | Sunstreak |  |  |  | Dasher  |  |  |  | Spotty |

The 22 varieties of tropical fish most commonly found throughout the world have Variant tag values from the following table, which also lists what color/shape/patterns come from that value.

| Shape | Pattern | Base color | Pattern color | Variant   | Type                    | Name                  |
|-------|---------|------------|---------------|-----------|-------------------------|-----------------------|
| 0     | 0       | 1          | 0             | 65536     | Orange-White Kob        | Clownfish             |
| 0     | 1       | 7          | 0             | 459008    | Gray-White Sunstreak    | Triggerfish           |
| 0     | 0       | 14         | 0             | 917504    | Red-White Kob           | Tomato Clownfish      |
| 1     | 3       | 14         | 0             | 918273    | Red-White Blockfish     | Red Snapper           |
| 1     | 4       | 14         | 0             | 918529    | Red-White Betty         | Red Cichlid           |
| 1     | 5       | 0          | 1             | 16778497  | White-Orange Clayfish   | Ornate Butterflyfish  |
| 0     | 4       | 5          | 3             | 50660352  | Lime-Light Blue Brinely | Queen Angelfish       |
| 0     | 5       | 6          | 3             | 50726144  | Pink-Light Blue Spotty  | Cotton Candy Betta    |
| 1     | 0       | 0          | 4             | 67108865  | White-Yellow Flopper    | Threadfin             |
| 0     | 5       | 0          | 4             | 67110144  | White-Yellow Spotty     | Goatfish              |
| 1     | 0       | 4          | 4             | 67371009  | Yellow Flopper          | Yellow Tang           |
| 0     | 3       | 9          | 4             | 67699456  | Cyan-Yellow Dasher      | Yellowtail Parrotfish |
| 1     | 3       | 10         | 4             | 67764993  | Purple-Yellow Blockfish | Dottyback             |
| 0     | 3       | 9          | 6             | 101253888 | Cyan-Pink Dasher        | Parrotfish            |
| 1     | 2       | 0          | 7             | 117441025 | White-Gray Glitter      | Moorish Idol          |
| 1     | 5       | 0          | 7             | 117441793 | White-Gray Clayfish     | Butterflyfish         |
| 1     | 1       | 1          | 7             | 117506305 | Orange-Gray Stripey     | Anemone               |
| 1     | 0       | 7          | 7             | 117899265 | Gray Flopper            | Black Tang            |
| 0     | 1       | 11         | 7             | 118161664 | Blue-Gray SunStreak     | Cichlid               |
| 1     | 0       | 7          | 11            | 185008129 | Gray-Blue Flopper       | Blue Tang             |
| 1     | 5       | 0          | 14            | 234882305 | White-Red Clayfish      | Emperor Red Snapper   |
| 0     | 2       | 7          | 14            | 235340288 | Gray-Red Snooper        | Red Lipped Blenny     |

The variant number is the sum of the most significant byte × 224 + second most significant byte × 216 +  second least significant byte × 28 + least significant byte.




