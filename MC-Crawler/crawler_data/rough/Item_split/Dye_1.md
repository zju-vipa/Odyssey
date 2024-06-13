### Dyeing wool and mobs
Wool can be dyed by placing wool and any dye in a crafting grid.

| Ingredients              | Crafting recipe |
|--------------------------|-----------------|
| AnyWool+<br/>MatchingDye |                 |

Dyes can be used on sheep to change the color of the wool. Shearing a colored sheep drops the corresponding color of the wool, and the sheep retains the color when the wool regenerates. Breeding colored sheep produces a lamb colored as one of the parent sheep, or a color resulting from the combination of both parents' color. The color combining follows the same rules that dyes use – red and yellow sheep produce an orange lamb, but a blue and yellow sheep cannot create a green lamb. The unlimited reproduction of colored sheep makes dyeing and shearing sheep infinitely more efficient than just dyeing wool directly.

Dye can also be used on a tamed wolf or cat to change the color of its collar from the default red to the color of the dye.

### Dyeing carpets
Carpets can be dyed.

| Ingredients                | Crafting recipe |
|----------------------------|-----------------|
| AnyCarpet+<br/>MatchingDye |                 |

### Dyeing terracotta
Terracotta can be dyed by placing 8 blocks around a dye on a crafting table.

| Ingredients                 | Crafting recipe  |
|-----------------------------|------------------|
| Terracotta+<br/>MatchingDye | 8888888888888888 |

### Creating concrete powder
Dyes can also be used to craft concrete powder, which can then be set into their respective concrete blocks (these cannot be dyed directly).

| Ingredients                       | Crafting recipe  |
|-----------------------------------|------------------|
| Sand+<br/>Gravel+<br/>MatchingDye | 8888888888888888 |

### Staining glass
Stained glass can be stained by placing 8 blocks of glass around a dye on a crafting table. Just like regular glass, stained glass can be crafted into stained glass panes. The recipe for this is the same as with regular glass.

| Name               | Ingredients                 | Crafting recipe  |
|--------------------|-----------------------------|------------------|
| Stained Glass      | Glass+<br/>MatchingDye      | 8888888888888888 |
| Stained Glass Pane | Glass Pane+<br/>MatchingDye | 8888888888888888 |

### Dyeing shulker boxes
Shulker boxes are generated in a light shade of purple (like the purpur block), but can be dyed any color. They can also be re-dyed as often as desired.

| Ingredients                     | Crafting recipe |
|---------------------------------|-----------------|
| AnyShulker Box+<br/>MatchingDye |                 |

### Dyeing beds
Beds can be dyed.

| Ingredients             | Crafting recipe |
|-------------------------|-----------------|
| AnyBed+<br/>MatchingDye |                 |

### Dyeing candles
Players can dye candles by placing an undyed candle and any color dye in a crafting grid.

| Ingredients             | Crafting recipe |
|-------------------------|-----------------|
| Candle+<br/>MatchingDye |                 |

### Banner patterns
Main article: Banner § Patterns
Dyes are used in most banner patterns to determine the pattern and color displayed.

### Dyeing armor
A graph showing all combinations of two dyes on a tunic.
An interactive widget is being loaded. If this does not work for you, please reload the page or check if JavaScript is enabled.
Leather armor or wolf armor can be dyed by:

- Crafting dyes with a piece of leather armor, leatherhorse armoror wolf armor.‌[Java Edition  only]
- Dousing the leather armor or leather horse armor in acauldronto which dyes have been added.‌[Bedrock Edition  only]

It is possible to put more than one dye alongside the leather armor. Armor can be dyed multiple times with previous colors affecting the final outcome. Colored armor can be reverted to their original color using a cauldron with undyed water.

The game has a specific formula for calculating the color of dyed armor: each color, in the RGB color model, has a red value, green value, and blue value. For each dye in the crafting grid, and the armor itself (if it is already dyed), the red, green, and blue values are added to running totals. In addition, a running total of the highest value (be it red, green, or blue) is also kept. After this, each total is divided by the number of colors used. This effectively produces the average red, green, blue, and maximum values. The maximum value of the average RGB values is also calculated. Finally, each average RGB value is multiplied by the average maximum value and divided by the maximum of the average RGB values. The modified average RGB values are then used as the final color. This procedure can be summed up with the following pseudocode:

set all "total" variables to 0
set numberOfColors to 0
for each color:
 set totalRed to: totalRed + redValue
 set totalGreen to: totalGreen + greenValue
 set totalBlue to: totalBlue + blueValue
 set totalMaximum to: totalMaximum + (max of redValue, greenValue, blueValue)
 set numberOfColors to: numberOfColors + 1

set averageRed to: totalRed / numberOfColors
set averageGreen to: totalGreen / numberOfColors
set averageBlue to: totalBlue / numberOfColors
set averageMaximum to: totalMaximum / numberOfColors

set maximumOfAverage to: max of averageRed, averageGreen, averageBlue
set gainFactor to: averageMaximum / maximumOfAverage

set resultRed to: averageRed * gainFactor
set resultGreen to: averageGreen * gainFactor
set resultBlue to: averageBlue * gainFactor

Due to the way this formula works, the resulting color can never be darker than the average of the input colors and is often lighter and more saturated. Of course, the resulting color can never be lighter or more saturated than the lightest or most saturated input color. In addition, this formula never creates an RGB value higher than 255 (which would be invalid in the 8-bit RGB color model).

If leather armor is renamed on an anvil, it retains its name when dyed or undyed.

** Mixing samples **
+= #FED83D
++= #C898BE
++= #B56D51
