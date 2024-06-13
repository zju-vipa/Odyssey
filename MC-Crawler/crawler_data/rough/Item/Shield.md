# Shield
A shield is a tool that can be used to block damage from melee attacks, ranged attacks and explosions. Shields can be temporarily disabled by getting hit with an axe, and some attacks ignore a shield's protection. Shields can have ornamental banner designs applied to them.

## Contents
- 1 Obtaining
	- 1.1 Crafting
	- 1.2 Repairing
		- 1.2.1 Combining
		- 1.2.2 Unit repair
	- 1.3 Trading
- 2 Usage
	- 2.1 Defense
	- 2.2 Disabling
	- 2.3 Applying patterns
	- 2.4 Enchantments
- 3 Sounds
- 4 Data values
	- 4.1 ID
- 5 Advancements
- 6 History
- 7 Issues
- 8 Gallery
	- 8.1 Renders
	- 8.2 Screenshots
- 9 References
- 10 External links

## Obtaining
### Crafting
| Ingredients                | Crafting recipe |
|----------------------------|-----------------|
| AnyPlanks+<br/>Iron Ingot  |                 |
| Shield+<br/>MatchingBanner |                 |

### Repairing
#### Combining
| Ingredients       | Crafting recipe | Description                                                                                                           |
|-------------------|-----------------|-----------------------------------------------------------------------------------------------------------------------|
| 2× Damaged Shield |                 | The durability of the two shields is added together, plus an extra 5% durability. The repaired shield has no pattern. |

| Ingredients       | Grinding recipe | Description                                                                                                           |
|-------------------|-----------------|-----------------------------------------------------------------------------------------------------------------------|
| 2× Damaged Shield |                 | The durability of the two shields is added together, plus an extra 5% durability. The repaired shield has no pattern. |

#### Unit repair
Main article: Anvil mechanics § Unit repair
Repair & NameDamaged Shield
A shield can be repaired in an anvil by adding planks or another shield. Shields repaired on anvils retain their pattern. One plank restores 25% of the shield's durability.[verify]

### Trading
Journeyman-level armorer villagers have 1⁄3‌[BE  only]/2⁄5‌[JE  only] chance of selling a shield for 5 emeralds as their sixth trade.

## Usage
Despite using iron in its crafting recipe, it cannot be smelted into iron nuggets.[1]

### Defense
Shields are used for blocking incoming attacks. Using‌[JE  only] or sneaking‌[BE  only] causes a player to slow to a sneaking pace, and after 5 game ticks (0.25 seconds)[2], attacks coming from in front of the player are blocked, dealing no damage. When the shield blocks an attack of 3 or stronger, it takes durability damage equal to the strength of the attack rounded up. When a player enters a boat, their shields exhibit the blocking animation.  

Most blocked projectiles that carry status effects (such as shulker bullets‌[JE  only], flaming arrows, or tipped arrows) do not affect the blocker. Tridents & arrows can be deflected into other targets. Knockback from melee attacks and projectiles is prevented, while knockback from explosions, hoglin, and ravager attacks are significantly reduced.

The shield directionally blocks all attacks coming from within the FOV of the direction the wielder is facing, providing a full hemisphere of coverage to them.

Mobs that deal continuous contact damage such as the slime, magma cube, and blaze rapidly drain the shield's durability for as long as the shielded player remains within the mob's hitbox.[3][4]

Blockable attacks include:

- Melee attacks from all sources. When blocking melee attacks from axe-wielding mobs, axe-wielding players, andwardens, only a single attack can be blocked before a shield is disabled for 5 seconds.
	- Status effects do not carry through to the blocker.
- Normal, tipped, and spectralarrows
	- Arrows other thanPiercingare totally deflected and can hit other targets.
	- Status effects do not carry through to the blocker‌[JE  only].
		- This can be used to damage the attacker or another mob down there.
- Flaming arrows
	- Burning does not carry through to the blocker‌[JE  only].
- Tridents
- Snowballsandeggs
- Spines frompufferfish
- Bullets fromshulkers
	- The levitation effect does not carry through to the blocker‌[JE  only].
- Spit fromllamas
- Fireballs, such as fromblazesandfire charges
	- Burning does not carry through to the blocker.
- Direct hits fromghastfireballs
	- These still cause environmental damage.
- All explosions‌[JE  only]
- Explosion damage fromcreepers
- TNTthat another player lit
- Ravagerheadbutts
	- These still knock the blocker back by about 3 blocks.
	- Blocking these strikes can stun the ravager for a moment, and it roars afterward.
- Ravager roars are blocked but still knock back the blocker.
- Beestings are blocked, but bees continuously attack until the player stops blocking and the player is stung.
- Beam attacks fromguardiansorelder guardians(only reduces damage by 50%)

They cannot block:

- Arrows from acrossbowenchanted withPiercing
	- This does not reduce the shield's durability.
	- Direct projectile damage is blocked, but the effect still carries through.
- Status effects from splash/lingeringpotions,evokers' fangs, or breath from theender dragon
- Beam attacks fromguardiansorelder guardians, or thewarden's sonic boom attack
- TNT that the blocking player lit themselves‌[BE  only]
- TNT that aredstone mechanismlit‌[BE  only]
- Fall damage, including that fromender pearls
	- This also includes when the player rides anentitythat died due to fall damage.

### Disabling
- All of a user's shields are disabled for 5 seconds if hit by anaxe-wielding player while the user's shield is up.
- Strikes from a warden or any axe-wielding mob (e.g.,vindicators,piglin brutes,zombies, etc) also disable shields for 5 seconds.
- A shield cannot be disabled during their 250 millisecond blocking delay. The shield must be fully active to be disabled.

### Applying patterns
A custom shield.
Shields can be decorated by applying a banner.

| Ingredients                | Crafting recipe | Description                                                                                                                                                                                |
|----------------------------|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Shield+<br/>MatchingBanner |                 | Applies the banner pattern to the shield. The banner is consumed.<br/>The shield must have no preexisting patterns.<br/>Does not change existing durability or enchantments on the shield. |

Unlike with banners, shields cannot be repainted or washed in a cauldron. Shields have only half the resolution of banners, making patterns look slightly different. In the game files, the pattern textures can be found in a separate directory called entity/shield.

In Java Edition, shields with patterns can also be obtained using the same commands as banners, except banner has to be replaced with shield.

### Enchantments
A shield can receive the following enchantments, but only through an anvil:

| Name               | Max Level | Method |
|--------------------|-----------|--------|
| Unbreaking         | III       | Anvil  |
| Mending            | I         | Anvil  |
| Curse of Vanishing | I         | Anvil  |

## Data values
### ID
Java Edition:

| Name   | Identifier | Form | Translation key                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|--------|------------|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Shield | `shield`   | Item | `item.minecraft.shield`<br/>`item.minecraft.shield.white`<br/>`item.minecraft.shield.orange`<br/>`item.minecraft.shield.magenta`<br/>`item.minecraft.shield.light_blue`<br/>`item.minecraft.shield.yellow`<br/>`item.minecraft.shield.lime`<br/>`item.minecraft.shield.pink`<br/>`item.minecraft.shield.gray`<br/>`item.minecraft.shield.light_gray`<br/>`item.minecraft.shield.cyan`<br/>`item.minecraft.shield.purple`<br/>`item.minecraft.shield.blue`<br/>`item.minecraft.shield.brown`<br/>`item.minecraft.shield.green`<br/>`item.minecraft.shield.red`<br/>`item.minecraft.shield.black` |

Bedrock Edition:

| Name   | Identifier | Numeric ID | Form | Translation key                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|--------|------------|------------|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Shield | `shield`   | `355`      | Item | `item.shield.name`<br/>`item.shield.white.name`<br/>`item.shield.orange.name`<br/>`item.shield.magenta.name`<br/>`item.shield.lightBlue.name`<br/>`item.shield.yellow.name`<br/>`item.shield.lime.name`<br/>`item.shield.pink.name`<br/>`item.shield.gray.name`<br/>`item.shield.silver.name`<br/>`item.shield.cyan.name`<br/>`item.shield.purple.name`<br/>`item.shield.blue.name`<br/>`item.shield.brown.name`<br/>`item.shield.green.name`<br/>`item.shield.red.name`<br/>`item.shield.black.name` |

