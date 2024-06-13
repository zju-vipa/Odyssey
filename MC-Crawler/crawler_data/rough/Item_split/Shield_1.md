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


