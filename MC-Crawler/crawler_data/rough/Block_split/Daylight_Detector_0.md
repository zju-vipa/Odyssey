# Daylight Detector
A daylight detector (in Java Edition) or daylight sensor (in Bedrock Edition) is a block that outputs a redstone signal based on sunlight.

Using the detector inverts it, causing it instead to output a redstone signal based on the darkness of the sky.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
- 2 Usage
	- 2.1 Redstone component
		- 2.1.1 Daylight detector
		- 2.1.2 Inverted daylight detector
	- 2.2 Fuel
	- 2.3 Note blocks
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Block data
- 5 History
- 6 Gallery
	- 6.1 Screenshots
- 7 Issues
- 8 References
- 9 External links

## Obtaining
### Breaking
Daylight detectors can be mined by hand or with any tool, but axes are the quickest. Inverted daylight detectors cannot be collected directly; they drop a regular daylight detector. In Bedrock Edition, the inverted sensor may be obtained via inventory editing or add-ons.

| Block     | Daylight Detector     |
|-----------|-----------------------|
| Hardness  | 0.2                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 0.3                   |
| Wooden    | 0.15                  |
| Stone     | 0.1                   |
| Iron      | 0.05                  |
| Diamond   | 0.05                  |
| Netherite | 0.05                  |
| Golden    | 0.05                  |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Crafting
| Ingredients                                  | Crafting recipe |
|----------------------------------------------|-----------------|
| Glass+<br/>Nether Quartz+<br/>AnyWooden Slab |                 |

## Usage
### Redstone component
Graphed daylight detector output in clear weather.
See also: Redstone circuit

A daylight detector can be used to produce redstone power in proportion to the daylight cycle.

A daylight detector is 0.375 blocks high (3/8ths of a block). Daylight detectors can be moved by pistons.‌[Bedrock Edition  only] Water and lava flow around daylight detectors without affecting them. 

** Placement **
To place a daylight detector, use the "Use Item/Place Block" control.
A daylight detector can be "inverted", which reverses the power levels produced by the daylight detector. To invert a daylight detector, aim at the placed daylight detector and use the "Use Item/Place Block" control.
** Activation **
A daylight detector activates when exposed to sufficient daylight (daylight detectormode) or when exposure to daylight is low enough (inverted daylight detectormode).
Sources of block light (torches,glowstone, etc.) cannot activate a daylight detector.
** Behavior **
An active daylight detector:
- powers adjacentredstone dust, including below it, andredstone comparatorsfacing away from the daylight detector, to a power level that depends on the time of day, the weather, and theinternal sky light level(see tables below)
- powers adjacentredstone repeatersfacing away from the daylight detector to power level 15
- activates adjacentredstone mechanisms, including above and below, such aspistons,redstone lamps, etc.

A daylight detector has no effect on other adjacent blocks (for example, it cannot power a block the way a repeater can).
The output signal of daylight detectors in the loaded chunk is updated every 20 gametime‌[JE  only]/daytime‌[BE  only]. Block update have no effect on daylight detectors.
#### Daylight detector
The daylight detector power level depends on the time of day, the weather, and the internal sky light level.

| Power | Clear                                                                                  |                                                                                        | Rain or snowfall                                                                    |                                                                                              | Thunder                                   |                                                                                                       |
|-------|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|-------------------------------------------|-------------------------------------------------------------------------------------------------------|
|       | Time ↓                                                                                 | Time ↑                                                                                 | Time ↓                                                                              | Time ↑                                                                                       | Time ↓                                    | Time ↑                                                                                                |
| 0     |                                                                                        | 13,670–(Midnight/18,000)-22,330(8,660 Gtk/7:13)                                        |                                                                                     | 13,670-(Midnight/18,000)–22,330(8,660 Gtk/7:13)                                              |                                           | 13,670-(Midnight/18,000)–22,330(8,660 Gtk/7:13)                                                       |
| 1     | 22,331–22,781(450 Gtk/22.5 sec)                                                        | 13,219–13,669(450 Gtk/22.5 sec)                                                        | 22,331–22,798(467 Gtk/23.35 sec)                                                    | 13,203–13,669(466 Gtk/23.3 sec)                                                              | 22,331–22,943(612 Gtk/30.6 sec)           | 13,058–13,669(611 Gtk/30.55 sec)                                                                      |
| 2     | 22,782–23,069‌[JE  only]/23,070‌[BE  only]J: (287 Gtk/14.35 sec) B: (288 Gtk/14.4 sec) | 12,931–13,218(287 Gtk/14.35 sec)                                                       | 22,799–23,231(432 Gtk/21.6 sec)                                                     | 12,769‌[JE  only]/12,770‌[BE  only]-13,202J: (433 Gtk/21.65 sec) B: (432 Gtk/21.6 sec)       | 22,944–23,352(408 Gtk/20.4 sec)           | 12,648–13,057(409 Gtk/20.45 sec)                                                                      |
| 3     | 23,070‌[JE  only]/23,071‌[BE  only]-23,296J: (226 Gtk/11.3 sec) B: (225 Gtk/11.25 sec) | 12,705–12,930(225 Gtk/11.25 sec)                                                       | 23,232–23,504(272 Gtk/13.6 sec)                                                     | 12,497–12,768‌[JE  only]/12,769‌[BE  only]J: (271 Gtk/13.55 sec) B: (272 Gtk/13.6 sec)       | 23,353–23,700(347 Gtk/17.35 sec)          | 12,300–12,647(347 Gtk/17.35 sec)                                                                      |
| 4     | 23,297–23,529(232 Gtk/11.6 sec)                                                        | 12,471–12,704(233 Gtk/11.65 sec)                                                       | 23,505–23,745(240 Gtk/12 sec)                                                       | 12,256–12,496(240 Gtk/12 sec)                                                                | 23,701-(Dawn/24,000/0)–59(240 Gtk/12 sec) | 11,941‌[JE  only]/11,942‌[BE  only]-(Dusk/12,000)-12,299J: (358 Gtk/17.9 sec)  B: (357 Gtk/17.85 sec) |
| 5     | 23,530–23,767(237 Gtk/11.85 sec)                                                       | 12,233–12,470(237 Gtk/11.85 sec)                                                       | 23,746–23,991(245 Gtk/12.25 sec)                                                    | 12,010–12,255(245 Gtk/12.25 sec)                                                             | 60–441(381 Gtk/19.05 sec)                 | 11,560–11,940‌[JE  only]/11,941‌[BE  only]J:(380 Gtk/19 sec) B: (381 Gtk/19.05 sec)                   |
| 6     | 23,768–23,960(192 Gtk/9.6 sec)                                                         | 12,041–12,232(191 Gtk/9.55 sec)                                                        | 23,992–(Dawn/24,000/0)-394(386 Gtk/19.3 sec)                                        | 11,607–(Dusk/12,000)-12,009(402 Gtk/20.1 sec)                                                | 442–1,039(597 Gtk/29.85 sec)              | 10,962–11,559(597 Gtk/29.85 sec)                                                                      |
| 7     | 23,961–(Dawn/24,000/0)-166(127 Gtk/6.35 sec)                                           | 11,835–(Dusk/12,000)-12,040 (205 Gtk/10.25 sec)                                        | 395–882(487 Gtk/24.35 sec)                                                          | 11,119–11,606(487 Gtk/24.35 sec)                                                             | 1,040–1,735(695 Gtk/34.75 sec)            | 10,266–10,961(695 Gtk/34.75 sec)                                                                      |
| 8     | 167–535(368/18.4 sec)                                                                  | 11,465‌[JE  only]/11,466‌[BE  only]-11,834J: (369 Gtk/18.45 sec) B: (368 Gtk/18.4 sec) | 883–1,429‌[JE  only]/1,430‌[BE  only]J: (546 Gtk/27.3 sec) B: (547 Gtk/27.35 sec)   | 10,571–11,118(547 Gtk/27.35 sec)                                                             | 1,736–2,608(872 Gtk/43.6 sec)             | 9,392–10,265(873 Gtk/43.65 sec)                                                                       |
| 9     | 536–933(397 Gtk/19.85 sec)                                                             | 11,067–11,464‌[JE  only]/11,465‌[BE  only]J: (397 Gtk/19.85 sec) B: (398 Gtk/19.9 sec) | 1,430‌[JE  only]/1,431‌[BE  only]-2,069J: (639 Gtk/31.95 sec) B: (638 Gtk/31.6 sec) | 9,931–10,570(639 Gtk/31.95 sec)                                                              | 2,609–3,942(1,333 Gtk/1:06.65 sec)        | 8,059–9,391(1,332 Gtk/1:06.6 sec)                                                                     |
| 10    | 934–1,371(437 Gtk/21.85 sec)                                                           | 10,629–11,066(737 Gtk/36.85 sec)                                                       | 2,070–2,875(805 Gtk/40.25 sec)                                                      | 9,125‌[JE  only]/9,126‌[BE  only]-9,930J: (805 Gtk/40.25 sec) B: (804 Gtk/40.2 sec)          |                                           | 3,943–(Noon/6,000)-8,058(4115 Gtk/3:25)                                                               |
| 11    | 1,372–1,865(493 Gtk/24.65 sec)                                                         | 10,136–10,628(492 Gtk/24.6 sec)                                                        | 2,876–4,108(1,232 Gtk/1:01.6)                                                       | 7,892–9,124‌[JE  only]/7,893–9,125‌[BE  only]J: (1,232 Gtk/1:01.6) B: (1,232 Gtk/1:01.6)     | N/A                                       | N/A                                                                                                   |
| 12    | 1,866–2,444(578 Gtk/28.9 sec)                                                          | 9,557–10,135(578 Gtk/28.9 sec)                                                         |                                                                                     | 4,109–(Noon/6,000)-7,891‌[JE  only]/7,892‌[BE  only]J:(3,410 Gtk/2:50) B: (3,783 Gtk/3:9.15) | N/A                                       | N/A                                                                                                   |
| 13    | 2,445–3,175(730 Gtk/36.5 sec)                                                          | 8,826–9,556(730 Gtk/36.5 sec)                                                          | N/A                                                                                 | N/A                                                                                          | N/A                                       | N/A                                                                                                   |
| 14    | 3,176–4,294(1,118 Gtk/55.9 sec)                                                        | 7,706–8,825(1,119 Gtk/55.95 sec)                                                       | N/A                                                                                 | N/A                                                                                          | N/A                                       | N/A                                                                                                   |
| 15    |                                                                                        | 4,295–(Noon/6,000)-7,705(3,410 Gtk/2:50)                                               | N/A                                                                                 | N/A                                                                                          | N/A                                       | N/A                                                                                                   |

