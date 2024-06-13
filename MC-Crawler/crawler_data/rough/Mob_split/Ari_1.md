### Respawn immunity
The player does not take damage for 60 game ticks (3 seconds) upon respawning from death.

## Movement
Main article: Controls § Configurable controls
There isn't a simple hard-coded maximum velocity for walking, sprinting, etc. The maximum is a result of a base acceleration countered by "friction" or air resistance. The base acceleration for walking is 0.098, and sprinting is 30% faster than that. Velocity is increased by this acceleration value every tick (1/20th of a second), then the player is moved by the resulting velocity, then the velocity is multiplied by the friction value of the block they are walking on. For most blocks, the friction value is 0.546. As the player walks forward, each tick their velocity goes +0.098, *0.546, +.098, *0.546, +0.098, and so on. The result is that eventually, the 0.546 multiplier counteracts the 0.098 increase, so the player doesn't go any faster. The formula for this "terminal velocity" is a/(1-r), where a is the acceleration, and r is the block's friction. 0.098/(1-0.546) ≈ 0.2159 meters/tick = 4.317 meters/second. Sprinting is 30% faster than that; About 5.612 meters/second. Flying is similar, but the base acceleration is 0.49 and the "friction" is 0.91, which comes out to ~10.89 m/s.

The player walks at a nominal rate of 4.317 meters (blocks) per second. That's about 15.5 kph or 9.7 mph, which is a 3:51 kilometer or a 6:12 mile. This means that the player can walk a total of 5181 blocks (5.2 km) in one Minecraft day, if walking in a straight line, ignoring hunger, and not sprinting or sneaking. For sneaking and sprinting statistics, see below.

### Sprinting
The player can sprint, draining the hunger bar considerably while doing so. The player sprints approximately 5.612 blocks per second, as opposed to the regular pace of 4.317. That's 20.2 kph or 12.6 mph, which is a 2:58 km or a 4:46 mile. The maximum distance a player can jump when sprinting is approximately 4.225 blocks. The swiftness effect increases momentum. The player cannot sprint if the hunger bar is at 6 () or less. Sprinting is activated by double-tapping the forward key (default W), then holding it, or by holding the sprint key (Ctrl [Cmd if using a Mac] by default) while pressing the forward key. Holding the sprint key in Creative mode while flying causes the player to fly faster.

### Sneaking
Sneaking is a feature activated by pressing and holding the sneak key (default is Shift). Sneaking prevents players from falling more than half a block, making it highly useful for building horizontally outward over space. Going past the edge of a block and stopping sneaking does not result in falling off that block. The player can still dismount blocks while sneaking by jumping over the block's edge. In Multiplayer Mode, a player's name tag is grayed out in Java Edition or completely disappears in Bedrock Edition when they sneak, to relate to the fact that sneaking makes them harder to see.

| Movement Mode | Speed (m/s) | Speed (km/h) | % of Walking Speed |
|---------------|-------------|--------------|--------------------|
| Walking       | 4.317       | 15.54        | 100%               |
| Sprinting     | 5.612       | 20.20        | 130%               |
| Sneaking      | 1.295       | 4.663        | 30%                |
| Flying        | 10.79       | 38.85        | 250%               |
| Sprint Flying | 21.58       | 77.71        | 500%               |
| Falling       | 77.71       | 279.75       | 1800%              |

### Jumping
The maximum height a player can jump without the jump boost effect is about 1.2522 blocks (1 1⁄4 blocks) in Java Edition. The jump height on Bedrock Edition is shorter because the game uses an outdated, pre-Combat Update value of 1.1875 (1 3⁄16 blocks).

### Swimming
Swimming occurs when the player is sprinting (by double pressing W or pressing Ctrl/Cmd) while the player is submerged underwater. Swimming has the same animation as crawling.

### Crawling
Main article: Crawling
Crawling occurs when the player is in an area less than 1.5 blocks high and prevents suffocation.

## Gameplay HUD
The onscreen heads-up display (HUD) consists of the player's health bar, hunger bar, experience bar, and hotbar. The armor rating bar appears above the health bar if the player is wearing armor and the oxygen bar appears if the player is submerged in water or is suffocating in a block‌[BE  only]. The HUD also contains the crosshair and a held object or fist. The HUD can also be toggled by F1.

As mentioned in the Gamemodes section, if the player is in Creative mode the health, hunger, and experience bars including armor rating and oxygen bubbles are hidden and only the hotbar is visible. Despite this, the player can still collect experience, wear armor, and still displays the screen tilting animation when dying from /kill or the void. In Spectator mode even the hotbar, crosshair, and held object/fist are hidden and the hotbar appears as a player spectating list when a number is pressed or the mouse is scrolled.

## Experience
Main article: Experience
Experience points (XP) can be gained via experience orbs when killing mobs or mining certain minerals. The current level is indicated by a green number above the HUD, and the experience points can be used to enchant weapons, tools, or armor with different useful attributes and skills (see enchanting table.) Anvils require experience to use.

The level increases by obtaining enough experience points. All levels and points are lost upon death but can be partially restored by picking up the experience orbs at the place of death.[2]

Experience is also obtained through activities such as mining, fishing, mob breeding, killing certain mobs, trading, or smelting.

## Game modes
Main articles: Survival, Creative, Hardcore, Adventure and Spectator
- In Survival mode, the player can place and destroy most blocks, and use all tools available. The player has limited health (icons), hunger (icons), and oxygen (bubble icons)
- In Creative mode, the player can fly by double-tapping the jump key (defaultSpace) and place an infinite number of blocks, but with limited use of crafting and tools. No mobs attack the player. The player cannot take damage (at all inBedrock Edition, and inJava Editiononly when falling into theVoidor typing thecommand/kill), has no hunger and has unlimited oxygen, and breaking blocks is instantaneous.
- In Hardcore mode‌[Java Edition  only], the player can respawn only inSpectatormode, and thedifficultylevel is locked on Hard mode.
- In Adventure mode, there are no changes from Survival mode aside from being unable to break or place blocks unless they possess a tool with theCanDestroyNBT data tag for that block, or have a block with theCanPlaceOntag. This game mode can be played only by havingcheatsenabled and typing the command/gamemode adventure,/gamemode a‌[Bedrock Edition  only],/gamemode 2‌[Bedrock Edition  only], or by opening amultiplayer(includingLAN) world.
- In Spectator mode, the player can spectate almost allmobs, ride them as if the player were in a minecart, fly through blocks, and open inventories, but cannot break blocks or change inventories. Along withAdventure, it can be accessed by typing in/gamemode spectator, pressingF3+F4until Spectator mode (the eye of ender) is selected orF3+Nwhile cheats are enabled, ordyinginHardcoremode. However, with theDebug Modeworld type, the gamemode is locked as Spectator mode unless changed with cheats enabled.

