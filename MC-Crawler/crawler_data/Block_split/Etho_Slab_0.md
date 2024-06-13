# Etho Slab
The etho slab is a joke slab introduced exclusively in Java Edition 2.0. Its name is a reference to the YouTube channel EthosLab.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
- 2 Usage
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Damage value
- 5 History
- 6 Issues

## Obtaining
### Breaking
Punching the block breaks it instantly and it drops in item form.

### Crafting
| Ingredients | Crafting recipe |
|-------------|-----------------|
| TNT         | 6               |

## Usage
Etho slabs behave like TNT, with the only difference being that there is a 25% chance that it will spawn a falling anvil one block above the nearest player in a 20 block radius, due to the real EthosLab's fondness in pranking his friends with a falling anvil.

## Data values
Blocks with data value 1 are called "Etho Slab (Lit??)" and explode on punch.

### ID
| Name             | Numeric ID | Form         | Translation key                                      |
|------------------|------------|--------------|------------------------------------------------------|
| Double Etho Slab | 159        | Block        | tile.ethoSlab.tntUnlit.nametile.ethoSlab.tntLit.name |
| Etho Slab        | 160        | Block & Item | tile.ethoSlab.tntUnlit.nametile.ethoSlab.tntLit.name |

### Damage value
| Bit     | Effect                                                                         |
|---------|--------------------------------------------------------------------------------|
| 1 (0x1) | If this bit is set, the Etho slab is triggered on punch rather than destroyed. |
| 4 (0x8) | If this bit is set, the Etho slab is a top slab.                               |


