# Minecart with Furnace
A minecart with furnace is a furnace inside a minecart. It can be powered with coal or charcoal to propel it across a rail line for a limited time, which can be used to move other minecarts.

## Contents
- 1 Obtaining
	- 1.1 Crafting
- 2 Usage
	- 2.1 Train mechanics
- 3 Properties
- 4 Sounds
- 5 Data values
	- 5.1 ID
	- 5.2 Entity data
- 6 History
- 7 Issues
- 8 Trivia
- 9 Gallery
	- 9.1 Screenshots
- 10 References

## Obtaining
Minecarts with furnace can be retrieved by attacking them, and by doing so they drop as an item. Critical hits are not applied to them, although the particles suggest otherwise.

### Crafting
| Ingredients      | Crafting recipe |
|------------------|-----------------|
| Furnace+Minecart |                 |

## Usage
Minecarts with furnaces are placed in the same way as other minecarts. They do not have a GUI, unlike a furnace.

Minecarts with furnaces can be powered, done by feeding fuel (coal or charcoal) into the furnace minecart with the use button. The fuel is consumed immediately and it starts to move in the same direction the player clicked toward. Pressing use always turns it to that direction, even when not holding coal.

Any piece of valid fuel, added at any time, increases the total range by an additional 3600 ticks (equal to 180 seconds or 3 minutes). The upper limit is 32767 ticks, approximately 27 minutes.

When powered, minecarts with furnaces cover 240m per minute (about 4 m/s, slightly slower than walking speed) or 720m per piece of coal. They do not accelerate beyond this speed when going downhill or on active powered rails, and as long as they remain powered, they do not slow down when going uphill, on inactive powered rails, or when pushing or pulling other minecarts.

If a powered furnace minecart is derailed and then pushed back onto a rail, it starts moving again in the direction it came from, so they are not easily turned around in this state unless a player is nearby to redirect it with use.

Minecarts with furnaces can climb up steep inclines while pushing other minecarts as long as they have fuel. If a minecart with furnace reaches a slope while pulling another minecart, the pulled minecart is switched to the forward position so that it can be pushed along the slope instead of pulled.

When a minecart with furnace bumps into another minecart or multiple minecarts, the other minecarts are pushed forward with great speed. The furnace minecart continues on with its own speed. Because of this speed difference, some of the minecarts may end up inside unloaded chunks on straight tracks.

### Train mechanics

























weakly-shunted 1-cart train, one cart was used only to push the train together and is left behind



























Creating a strongly-shunted 1-cart train. The sloped rail must be replaced with a horizontal rail before powering.
A Minecart train powered by furnace minecarts.
A furnace minecart can be made to pull up to four other minecarts. All minecarts in this train move at the constant speed of the furnace minecart. Trains are formed when a minecart is pushed into the back of a powered furnace minecart or a short-enough train. These shunts are fragile at best and easily come undone, but some methods are stronger than others. For example, pushing a minecart into a furnace minecart and then powering the furnace gives a weaker shunt than pushing the furnace minecart into the other minecart against a wall, and then powering the furnace in the other direction.

A high-speed minecart running into the back of a furnace minecart going in the same direction automatically creates a weak shunt with it, pulling it along.

Pulling a minecart with TNT causes it to explode.

| Condition                                                                               | Result                                                               |
|-----------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| Furnace loses power/speed                                                               | Shunt comes undone                                                   |
| Entity bumping besides those part of the train                                          | Jettisoned forward                                                   |
| Upward sloped track                                                                     | Jettisoned forward                                                   |
| Downward sloped track                                                                   | Jettisoned forward (strong shunt) or shunt comes undone (weak shunt) |
| 90° turn in track                                                                       | Jettisoned backward                                                  |
| Turn toward north/south or east/west that is not the direction the train was shunted in | Train derails                                                        |

When a train comes to a turn, the shunt comes undone with the pulled minecart jettisoned backward. The correct way to make such a turn is having the shunt undone before a turn, and then make the two rejoin on a straight rail later by having the pulled cart catch up with the minecart with furnace.[1]

Since the train runs slower on a fully powered track than a normal minecart (~5 m/s compared to 8m/s), a train pulled by an unpowered furnace minecart is ideal for AFK farms involving breaking or placing blocks like nether wart.[1]

