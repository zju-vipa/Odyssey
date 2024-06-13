# Ominous Trial Spawner
An ominous trial spawner is a variant of the trial spawner that gives better loot and spawns more armored mobs (when applicable). It replaces a normal trial spawner during an ominous trial, and it can reward players with ominous trial keys instead of normal trial keys.

## Contents
- 1 Obtaining
	- 1.1 Ominous trial
	- 1.2 Breaking
- 2 Usage
	- 2.1 Mob spawning
	- 2.2 Projectile spawning
	- 2.3 Loot
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
- 5 History
- 6 Gallery
	- 6.1 Renders

## Obtaining
The ominous trial spawner cannot be obtained as an item, because it is technically a block state of the normal trial spawner, not a separate block. It can only be obtained by using commands, such as /give @s minecraft:trial_spawner[minecraft:block_state={ominous:"true"}]‌[Java Edition  only] or /setblock x y z minecraft:trial_spawner[ominous=true]‌[Java Edition  only] / /setblock x y z trial_spawner ["ominous"=true].‌[Bedrock Edition  only]

### Ominous trial
Trial spawners convert to ominous trial spawners if a player with the Trial Omen effect enters the 14 block detection area and is in the line of sight of the trial spawner. This also happens when the player has the Bad Omen effect, which gets converted into Trial Omen. When a trial spawner becomes ominous, all of its existing mobs are despawned. If the spawner was on cooldown and was not ominous before going on cooldown, the cooldown is skipped when becoming ominous. The ominous trial spawner then immediately becomes active.

### Breaking
A ominous trial spawner can be broken, but it does not drop itself as an item, and it takes a long time to break.

Due to their high blast resistance, ominous trial spawners are immune to explosions, but can still be destroyed by the wither's block-breaking attack and blue wither skulls.

| Block    | Ominous trial spawner |
|----------|-----------------------|
| Hardness | 50                    |
|          | Breakingtime (secs)   |
| Default  | 250                   |

## Usage
The ominous trial spawner is similar to the trial spawner, but releases more difficult mobs and ejects more powerful loot.

### Mob spawning
See also: Trial Spawner § Mob spawning and Trial Chambers § Trial spawners

Ominous trial spawners converted from trial spawners that generate naturally in trial chambers spawn mobs with (better) weapons and wearing armor. Mobs that can't wear armor are unchanged. The total amount of mobs and the amount of simultaneous mobs is unchanged. 

Each armor set consists of only a chestplate and helmet with each piece having a 50% chance of being missing. All armor is enchanted with Fire Protection IV, Projectile Protection IV and Protection IV. The armor is selected from:

- chainmail armorwithbolt armor trimincopper(4 in 7)
- iron armorwithflow armor trimincopper(2 in 7)
- diamond armorwithflow armor trimincopper(1 in 7)

Melee mobs spawn with a weapon selected from:

- Iron Sword(4 in 7)
- Iron SwordwithSharpnessI (1 in 7)
- Iron SwordwithKnockbackI (1 in 7)
- Diamond Sword(1 in 7).

Ranged mobs spawn with a Bow with:

- no enchantment (2 in 4)
- PowerI (1 in 4)
- PunchI (1 in 4).

Ominous trial spawners converted from manually placed trial spawners will continue to spawn the same mob as the trial spawner.

