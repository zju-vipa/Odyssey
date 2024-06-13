# Potato Battery
A potato battery is a toggleable block that emits a redstone signal and damages entities above it when activated in 24w14potato.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
- 2 Usage
	- 2.1 Redstone signal
	- 2.2 Damage
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Gallery

## Obtaining
### Breaking
A potato battery can be broken using any tool with equal efficiency, and always drops itself.

| Block    | Potato Battery      |
|----------|---------------------|
| Hardness | 3                   |
|          | Breakingtime (secs) |
| Default  | 4.5                 |

### Crafting
| Ingredients                                                           | Crafting recipe |
|-----------------------------------------------------------------------|-----------------|
| Iron Ingot+<br/>Copper Ingot+<br/>Poisonous Potato+<br/>Redstone Dust |                 |

## Usage
### Redstone signal
When used, a potato battery toggles its state. When active, it emits a redstone signal of 15.

### Damage
If an entity is on top of it while it is active, the entity is damaged by 0.5 × 0.25 per tick. However, due to damage immunity, the entity only actually recieves damage every half a second.

## Data values
### ID
| Name           | Identifier       | Translation key                  |
|----------------|------------------|----------------------------------|
| Potato Battery | `potato_battery` | `block.minecraft.potato_battery` |

### Block states
See also: Block states

The potato_battery block uses following block states:

| Name     | Default value | Allowed values     | Description                            |
|----------|---------------|--------------------|----------------------------------------|
| inverted | `false`       | `false`<br/>`true` | If true, the potato battery is active. |

