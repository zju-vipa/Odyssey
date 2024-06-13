# Ice Bomb
The ice bomb is a ranged weapon that is used to freeze water into ice.

## Contents
- 1 Obtaining
	- 1.1 Lab Table
- 2 Usage
- 3 Sounds
- 4 Data values
	- 4.1 ID
- 5 History
- 6 Issues
- 7 Trivia

## Obtaining
### Lab Table
| Result        | Materials Needed  |
|---------------|-------------------|
| <br/>Ice Bomb |                   |
|               | Sodium Acetate x4 |

## Usage
Ice bombs can be thrown by using them, similar to an egg. They are affected by gravity.

Similar to ender pearls, there is a short cooldown before the player can throw another ice bomb. The cooldown is shown in the hotbar by a white overlay that shrinks before the player is able to use it again.

Ice bombs explode upon hitting most blocks, including non-solid blocks, but not air. They also explode upon hitting other entities, but they do not deal damage, and unlike eggs and snowballs, the impact is not considered an attack and does no damage or knockback. When exploding, any water (including flowing water, but not waterlogged blocks) in a 3×3×3 cube around the ice bomb freezes into ice. Ice bombs can be used to contain and displace mobs in ice under water.

While endermen teleport away from arrows shot at them, they can be hit by ice bombs. 

Throwing an ice bomb while underwater encloses the player in ice.

| xy | -2    | -1    | 0        | 1     | 2     |
|----|-------|-------|----------|-------|-------|
| 64 | Air   | Air   | Air      | Air   | Air   |
| 63 | Air   | Air   | Ice bomb | Air   | Air   |
| 62 | Water | Ice   | Ice      | Ice   | Water |
| 61 | Water | Ice   | Ice      | Ice   | Water |
| 60 | Water | Water | Water    | Water | Water |

## Data values
### ID
| Name     | Identifier | Numeric ID | Form | Translation key      |
|----------|------------|------------|------|----------------------|
| Ice Bomb | `ice_bomb` | `595`      | Item | `item.ice_bomb.name` |

| Ice Bomb | Identifier | Numeric ID | Translation key        |
|----------|------------|------------|------------------------|
| Entity   | `ice_bomb` | `106`      | `entity.ice_bomb.name` |


