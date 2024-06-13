# Mining Fatigue
Mining Fatigue is an effect that reduces mining and attack speed, opposite to Haste.

## Contents
- 1 Effect
- 2 Causes
- 3 Notes
- 4 Advancements
- 5 Data values
	- 5.1 ID
- 6 History
- 7 Issues

## Effect
** Attack speed **
The effect decreases attack speed by 10% × level, equivalent to the attack speed cooldown attribute‌[Java Edition  only] decreasing by 0.2 × level. For the in-game default level III, attack speed decreases by 30% (attack speed cooldown attribute decreases by 0.6).

** Mining speed **
The mining speed is reduced to 0.30^level of the normal mining speed. For the in-game default level III, the speed is reduced to 0.33 (0.027×) of normal speed, taking 37 times longer than usual to break a block with the proper tool for that block.

|              | Level 1    | Level 2    | Level 3    | Level 4+       |
|--------------|------------|------------|------------|----------------|
| Attack speed | 90%        | 80%        | 70%        | 60%            |
| Mining speed | 30% (3.3×) | 9% (11.1×) | 2.7% (37×) | 0.81% (123.5×) |

Negative levels increase attack speed, but still act as level 4 with respect to mining.

While afflicted, a player can still craft and ride entities as usual, but cannot remove most vehicles due to how slowly the vehicle can be broken.

The affliction is cured by drinking milk, although milk does not prevent a subsequent affliction by an elder guardian, which can happen within a few seconds‌[Java Edition  only] or immediately.‌[Bedrock Edition  only] Axolotls can also remove this effect, if the player helps an axolotl kill a mob while an axolotl was battling that mob.

## Causes
The only natural cause of Mining Fatigue is from affliction by an elder guardian, and the only natural effect level is III. Other levels can be achieved via commands. 

In Java Edition, once per minute, elder guardians in the vicinity search for any player within 50 blocks to afflict with Mining Fatigue III. A player cannot defend from this attack. Concealment behind blocks, underground, or by a potion of invisibility offers no defense.

In Bedrock Edition, elder guardians within range afflict Mining Fatigue III immediately. Drinking milk to remove the effect results in re-infliction immediately after drinking the milk.

| Cause          | Potency | Length | Notes                                 |
|----------------|---------|--------|---------------------------------------|
| Elder Guardian | III     | 5:00   | Only when the player is not affected. |

## Notes
- The effect does not affectblockbreaking inCreativemode, or blocks that arebroken instantlyby default.
- Other conditions which reduce mining speed include: being underwater; riding ahorseorpig, being on aladder, or in aboatorminecart.

## Data values
### ID
Java Edition:

| Name           | Identifier       | Numeric ID | Translation key                   |
|----------------|------------------|------------|-----------------------------------|
| Mining Fatigue | `mining_fatigue` | `4`        | `effect.minecraft.mining_fatigue` |

Bedrock Edition:

| Name           | Identifier       | Numeric ID | Translation key      |
|----------------|------------------|------------|----------------------|
| Mining Fatigue | `mining_fatigue` | `4`        | `potion.digSlowDown` |


