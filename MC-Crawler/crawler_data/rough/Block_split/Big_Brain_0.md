# Big Brain
A big brain is a block in 24w14potato used to obtain potatoes of knowledge.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
- 2 Usage
	- 2.1 Potatoes of knowledge
	- 2.2 Piston interactivity
	- 2.3 Note blocks
- 3 Data values
	- 3.1 ID
	- 3.2 Block states
	- 3.3 Block data
- 4 History
- 5 Issues

## Obtaining
### Breaking
A big brain can be broken using anything, but an axe is the fastest. Big brains always drop themselves and a potato of knowledge when mined.

| Block     | Big brain             |
|-----------|-----------------------|
| Hardness  | 2                     |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 3                     |
| Wooden    | 1.5                   |
| Stone     | 0.75                  |
| Iron      | 0.5                   |
| Diamond   | 0.4                   |
| Netherite | 0.35                  |
| Golden    | 0.25                  |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Crafting
| Ingredients                       | Crafting recipe |
|-----------------------------------|-----------------|
| Poisonous Potato+<br/>Zombie Head |                 |

## Usage
### Potatoes of knowledge
Big brains absorb nearby experience orbs. When broken, a big brain drops a potato of knowledge with a knowledge amount equal to how much experience it absorbed (if it didn't absorb anything, potato of knowledge still drops, with 0 knowledge). Maximum possible amount stored in a single potato of knowledge is equal to 1000 experience points; if big brain absorbs this much experience, a potato of knowledge with 1000 experience is dropped by it automatically, without breaking the block.

### Piston interactivity
Big brains cannot be pushed or pulled by pistons.

### Note blocks
Big brains can be placed under note blocks to produce "bass" sounds.

## Data values
### ID
| Name      | Identifier  | Block tags     | Translation key             |
|-----------|-------------|----------------|-----------------------------|
| Big Brain | `big_brain` | `mineable/axe` | `block.minecraft.big_brain` |

### Block states
See also: Block states

| Name   | Default value | Allowed values                            | Description                           |
|--------|---------------|-------------------------------------------|---------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the big brain is facing |

### Block data
See also: Block entity format

A barrel has a block entity associated with it that holds additional data about the block.

- Block entity data
	- 
	- Tags common to all block entities
	- amount: The amount of experience stored in this big brain.
	- delay: An integer that oscillates between 5 and 1 (inclusive) by decreasing by 1 every tick. Experience orbs can only enter this big brain whendelayis 1.


