# Wind Charge
A wind charge is a consumable ranged weapon that can knock entities back and interact with certain redstone components. It is the weapon used by breezes, and can also be shot by players and dispensers.

## Contents
- 1 Obtaining
	- 1.1 Crafting
	- 1.2 Container loot
- 2 Usage
- 3 Behavior
	- 3.1 When used by players and dispensers
- 4 Sounds
- 5 Data values
	- 5.1 ID
	- 5.2 Entity data
- 6 Advancements
- 7 History
- 8 Issues
- 9 Gallery
- 10 References

## Obtaining
### Crafting
| Ingredients | Crafting recipe | Description                      |
|-------------|-----------------|----------------------------------|
| Breeze Rod  | 4               | ‌[upcoming: JE 1.21 & BE 1.21.0] |

### Container loot
| Item        | Structure      | Container        | Quantity | Chance                         |
|-------------|----------------|------------------|----------|--------------------------------|
|             |                |                  |          | Java EditionandBedrock Edition |
| Wind Charge | Trial Chambers | Reward container | 4–12     | 9.6%                           |
|             |                |                  |          | Java Edition 1.21              |
| Wind Charge | Trial Chambers | Ominous Vault    | 8–12     | 46.2%                          |

## Usage
A wind charge can be thrown by using it. After it is thrown, the wind charge is consumed.

Wind charges have a cooldown of 10 ticks (0.5 seconds) before they can be used again. The cooldown is shown in the hotbar by a white overlay on the wind charge that shrinks and must disappear before the player can use it again. If there are other inventory or hotbar slots containing wind charges, they are covered with the white overlay as well.[1]

## Behavior
Wind charges, when fired either by players, dispensers, or breezes, fly in a straight line through the air. There is a random offset in a wind charge's trajectory due to a 'cone' of spread, which can cause wind charges to miss their target or hit something else.

When a wind charge directly hits an entity, the entity takes damage and knockback[more information needed], and a burst of wind appears. When hitting a block, only the burst of wind appears. 

The wind burst also interacts with these blocks:

- Non-irondoorsandtrapdoorsare flipped.
- Fence gatesare flipped.
- Buttonsare pressed.
- Leversare flipped.
- Bellsare rung and swung.
- Chorus flowersbreak, dropping in item form.
- Decorated potsshatter on impact, dropping their components (bricksand/orsherds) and their contents, if any.
- Litcandles(both standalone and oncake) are extinguished.

Wind charges can be deflected if hit with another projectile or a melee attack, similar to ghast fireballs.

Wind charges are distance attenuated by liquids such as water and lava. They also appear to fly in a straight line, similar to fireballs.[more information needed]

Wind charges are two separate entities depending on their source. Wind charges shot by breezes are breeze_wind_charges, while wind charges shot by players and dispensers are simply wind_charges. This distinction is in place as the two types of wind charges have some different properties.

### When used by players and dispensers
Wind charges fired by players and dispensers deal 10% more knockback than those fired by breezes, but have a much smaller burst area.[more information needed]

A player launched by wind charges shot by a player or a dispenser accumulates fall damage only when falling below the Y level where the wind burst hit. In Bedrock Edition, when throwing a wind charge, the projectile is slightly offset.

## Data values
### ID
Java Edition:

| Item        | Identifier    | Translation key              |
|-------------|---------------|------------------------------|
| Wind Charge | `wind_charge` | `item.minecraft.wind_charge` |

| Entity      | Identifier           | Entity tags          | Translation key                       |
|-------------|----------------------|----------------------|---------------------------------------|
| Wind Charge | `wind_charge`        | `impact_projectiles` | `entity.minecraft.wind_charge`        |
| Wind Charge | `breeze_wind_charge` | `impact_projectiles` | `entity.minecraft.breeze_wind_charge` |

Bedrock Edition:

| Item        | Identifier    | Numeric ID | Translation key         |
|-------------|---------------|------------|-------------------------|
| Wind Charge | `wind_charge` | `377`      | `item.wind_charge.name` |

| Entity      | Identifier                      | Numeric ID | Translation key                             |
|-------------|---------------------------------|------------|---------------------------------------------|
| Wind Charge | `wind_charge_projectile`        | `143`      | `entity.wind_charge_projectile.name`        |
| Wind Charge | `breeze_wind_charge_projectile` | `141`      | `entity.breeze_wind_charge_projectile.name` |

### Entity data
Wind charges have entity data associated with them that contain various properties.

Java Edition:

Main article: Entity format
- Entity data
	- 
	- Tags common to all entities
	- 
	- Tags common to all projectiles
	- 
	- Tags common to all hurting projectiles

Bedrock Edition:

SeeBedrock Edition level format/Entity format.

