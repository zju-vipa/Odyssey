## Data values
### ID
Java Edition:

| Name            | Identifier        | Form | Translation key                  |
|-----------------|-------------------|------|----------------------------------|
| Suspicious Stew | `suspicious_stew` | Item | `item.minecraft.suspicious_stew` |

Bedrock Edition:

| Name            | Identifier        | Numeric ID | Form | Translation key             |
|-----------------|-------------------|------------|------|-----------------------------|
| Suspicious Stew | `suspicious_stew` | `590`      | Item | `item.suspicious_stew.name` |

### Item data
In Java Edition, suspicious stew uses the following NBT data:

- tag: The item'stagtag.

- 
	- effects: Thestatus effectsthis suspicious stew has.
		- One of these for each effect.
			- id: Theresource location of the effect.
			- duration: The duration of the effect inticks. Values 0 or lower are treated as 1. Optional, and defaults to 160 ticks (8 seconds).

### Metadata
In Bedrock Edition, suspicious stew uses the following data values:

|  | DV | Description                 |
|--|----|-----------------------------|
|  | 0  | Night VisionfromPoppy       |
|  | 1  | Jump Boost                  |
|  | 2  | Weakness                    |
|  | 3  | Blindness                   |
|  | 4  | Poison                      |
|  | 5  | SaturationfromDandelion     |
|  | 6  | SaturationfromBlue Orchid   |
|  | 7  | Fire Resistance             |
|  | 8  | Regeneration                |
|  | 9  | Wither                      |
|  | 10 | Night VisionfromTorchflower |


