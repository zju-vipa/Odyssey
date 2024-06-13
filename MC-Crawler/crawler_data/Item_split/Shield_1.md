### Disabling
- All of a user's shields are disabled for 5 seconds if hit by anaxe-wielding player while the user's shield is up.
- Strikes from a warden or any axe-wielding mob (e.g.,vindicators,piglin brutes,zombies, etc) also disable shields for 5 seconds.
- A shield cannot be disabled during their 250 millisecond blocking delay. The shield must be fully active to be disabled.

### Applying patterns
A custom shield.
Shields can be decorated by applying a banner.

| Ingredients           | Crafting recipe | Description                                                                                                                                                                      |
|-----------------------|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Shield+MatchingBanner |                 | Applies the banner pattern to the shield. The banner is consumed.The shield must have no preexisting patterns.Does not change existing durability or enchantments on the shield. |

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

| Name   | Identifier | Form | Translation key                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|--------|------------|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Shield | shield     | Item | item.minecraft.shielditem.minecraft.shield.whiteitem.minecraft.shield.orangeitem.minecraft.shield.magentaitem.minecraft.shield.light_blueitem.minecraft.shield.yellowitem.minecraft.shield.limeitem.minecraft.shield.pinkitem.minecraft.shield.grayitem.minecraft.shield.light_grayitem.minecraft.shield.cyanitem.minecraft.shield.purpleitem.minecraft.shield.blueitem.minecraft.shield.brownitem.minecraft.shield.greenitem.minecraft.shield.reditem.minecraft.shield.black |

Bedrock Edition:

| Name   | Identifier | Numeric ID | Form | Translation key                                                                                                                                                                                                                                                                                                                                                                     |
|--------|------------|------------|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Shield | shield     | 355        | Item | item.shield.nameitem.shield.white.nameitem.shield.orange.nameitem.shield.magenta.nameitem.shield.lightBlue.nameitem.shield.yellow.nameitem.shield.lime.nameitem.shield.pink.nameitem.shield.gray.nameitem.shield.silver.nameitem.shield.cyan.nameitem.shield.purple.nameitem.shield.blue.nameitem.shield.brown.nameitem.shield.green.nameitem.shield.red.nameitem.shield.black.name |


