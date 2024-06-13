# Screen effects
Screen effects encompass a variety of effects applied alongside or beneath the heads-up display as augmentations to the player's point of view as a method of conveying further information about a player's current state.

## Contents
- 1 Summary
- 2 Overlays
	- 2.1 Suffocation
	- 2.2 On fire
	- 2.3 Nether portal
	- 2.4 Underwater
	- 2.5 Distortion overlay
	- 2.6 Darkness vignette
	- 2.7 World border overlay
	- 2.8 Freezing overlay
	- 2.9 Pumpkin blur
	- 2.10 Spyglass scope
- 3 Animated sprites and models
	- 3.1 Elder Guardian ghost
	- 3.2 Totem of Undying
	- 3.3 Bad Omen
	- 3.4 Hero of the Village
- 4 Transformations
	- 4.1 Damage tilt
	- 4.2 View bobbing
	- 4.3 Distortion effects
	- 4.4 Speed FOV changes
	- 4.5 Underwater FOV changes
- 5 History
	- 5.1 Overlays
	- 5.2 Animated sprites
	- 5.3 Transformations
- 6 References

## Summary
| Effect                           | Java Edition |                              |                 | Bedrock Edition |                               |                        |
|----------------------------------|--------------|------------------------------|-----------------|-----------------|-------------------------------|------------------------|
|                                  | Image        | Visible inthird-person view? | Visible withF1? | Image           | Visible in third-person view? | Visible withF1?        |
|                                  |              |                              |                 |                 |                               | Overlays and vignettes |
| Suffocationinside a block        |              | No                           | Yes             |                 | No                            | Yes                    |
| When onfire                      |              | No                           | Yes             |                 | No                            | Yes                    |
| When in anether portal           |              | Yes[1]                       | No[2]           |                 | No                            | Yes                    |
| When underwater                  |              | No                           | Yes             |                 | No                            | Yes                    |
| Distortion effect overlay        |              | Yes                          | Yes[3]          |                 |                               | N/A                    |
| Darkness                         |              | Yes                          | No[4]           |                 | Yes                           | No                     |
| When near theworld border        |              | Yes                          | No[5]           |                 |                               | N/A                    |
| When insidepowder snow           |              | Yes                          | No[6]           |                 | Yes                           | Yes                    |
| When wearing apumpkin            |              | No                           | No[7]           |                 | No                            | Yes                    |
| When using aspyglass             |              | No                           | No[8]           |                 | No                            | Yes                    |
|                                  |              |                              |                 |                 |                               | Animated sprites       |
| Totem of Undyingwhen used        |              | Yes                          | No[9]           |                 | Yes                           | Yes                    |
| Bad Omenwhen obtained            |              |                              | N/A             |                 | Yes                           | Yes                    |
| Hero of the Villagewhen obtained |              |                              | N/A             |                 | Yes                           | Yes                    |
| Elder guardianghost              |              | Yes                          | Yes             |                 | Yes                           | Yes                    |
|                                  |              |                              |                 |                 |                               | Visual transformations |
| Screen tilting when damaged      |              | Yes[10]                      | Yes             |                 | Yes                           | Yes                    |
| View bobbing                     |              | Yes                          | Yes             |                 | Yes                           | Yes                    |
| Distortion effects               |              | Yes[11]                      | Yes             |                 | Yes                           | Yes                    |
| Speed-based FOV changes          |              | Yes[12]                      | Yes             |                 | Yes                           | Yes                    |
| Underwater FOV changes           |              | Yes                          | Yes             |                 | Yes                           | Yes                    |

## Overlays
### Suffocation
| Visible in second/third person? | No              |
|---------------------------------|-----------------|
| Visible with HUD disabled?      | Yes             |
| Visible in graphics settings    | [needs testing] |
| Can be controlled by            | None            |

{
    "title": "Suffocation overlay",
    "rows": [
        {
            "field": "No",
            "label": "Visible in second/third person?"
        },
        {
            "field": "Yes",
            "label": "Visible with HUD disabled?"
        },
        {
            "field": "<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i>[https://minecraft.wiki/w/Talk:Screen_effects <span title=\"An editor has requested that this be tested in the game to prove that it is a true statement. Once you have tested this in-game and you get the same results as this states, you may remove this template.\" >needs testing</span>]</i>]</sup>(link to Category:Testing needed article, displayed as Category:Testing needed)",
            "label": "Visible in graphics settings"
        },
        {
            "field": "None",
            "label": "Can be controlled by"
        }
    ],
    "invimages": [],
    "images": [
        "Inside of a block.png"
    ]
}

  

This section is named by the community. 
An official name has not been given. Please update the name if confirmed by reliable sources.


This effect manifests when an applicable mob's eye level intersects specific blocks; generally those that are full solid cubes and block both vision and movement, with the exception of ice.

In Java Edition this effect involves a darkened version of the block texture covering the entire area of the screen.

In Bedrock Edition, the block's texture is instead arranged into a cube, and this cube is fixed around the player's point of view. This is the case regardless of the player's placement inside the block; they can be at the edge of it (such that their view is partially outside of it and the outside texture is clearly visible) and they are still rendered as if at the exact center of the cube.

### On fire
| Visible in second/third person? | No              |
|---------------------------------|-----------------|
| Visible with HUD disabled?      | Yes             |
| Visible in graphics settings    | [needs testing] |
| Can be controlled by            | None            |

{
    "title": "Fire overlay",
    "rows": [
        {
            "field": "No",
            "label": "Visible in second/third person?"
        },
        {
            "field": "Yes",
            "label": "Visible with HUD disabled?"
        },
        {
            "field": "<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i>[https://minecraft.wiki/w/Talk:Screen_effects <span title=\"An editor has requested that this be tested in the game to prove that it is a true statement. Once you have tested this in-game and you get the same results as this states, you may remove this template.\" >needs testing</span>]</i>]</sup>(link to Category:Testing needed article, displayed as Category:Testing needed)",
            "label": "Visible in graphics settings"
        },
        {
            "field": "None",
            "label": "Can be controlled by"
        }
    ],
    "invimages": [],
    "images": [
        "On fire.png"
    ]
}

  

This section is named by the community. 
An official name has not been given. Please update the name if confirmed by reliable sources.


When the player is on fire, this effect is applied to the screen. This is caused by being inside of fire or lava (even in Creative mode, although not in Spectator), after exiting such a block (except in Creative/Spectator), or being set on fire through the attack of a burning mob or a burning arrow.

This overlay always displays as fire, even if the player in question is inside of soul fire.

In Java Edition this effect involves two intersecting texture planes being rendered across the bottom half of the screen with the fire texture.

In Bedrock Edition, a single fire texture is stretched across the bottom two-thirds of the screen.

### Nether portal
| Visible in second/third person? | JE: YesBE: No   |
|---------------------------------|-----------------|
| Visible with HUD disabled?      | JE: NoBE: Yes   |
| Visible in graphics settings    | [needs testing] |
| Can be controlled by            | None            |

{
    "title": "Nether Portal overlay",
    "rows": [
        {
            "field": "'''(link to Java Edition article, displayed as JE):''' Yes<br>'''(link to Bedrock Edition article, displayed as BE):''' No",
            "label": "Visible in second/third person?"
        },
        {
            "field": "'''(link to Java Edition article, displayed as JE):''' No<br>'''(link to Bedrock Edition article, displayed as BE):''' Yes",
            "label": "Visible with HUD disabled?"
        },
        {
            "field": "<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i>[https://minecraft.wiki/w/Talk:Screen_effects <span title=\"An editor has requested that this be tested in the game to prove that it is a true statement. Once you have tested this in-game and you get the same results as this states, you may remove this template.\" >needs testing</span>]</i>]</sup>(link to Category:Testing needed article, displayed as Category:Testing needed)",
            "label": "Visible in graphics settings"
        },
        {
            "field": "None",
            "label": "Can be controlled by"
        }
    ],
    "invimages": [],
    "images": [
        "Nether portal overlay.png"
    ]
}

  

This section is named by the community. 
An official name has not been given. Please update the name if confirmed by reliable sources.


Note: this section discusses the nether portal texture overlay. The nether portal/nausea effect is discussed in the Distortion effect/Distortion overlay sections.

When the player is inside of a nether portal, this effect is applied to the screen. It always coincides with either the distortion effect and/or its overlay.

In Java Edition this effect involves the nether portal texture being stretched across the entirety of the screen.

In Bedrock Edition, the texture is instead arranged into a cube, fixed around the player's point of view much like the suffocation effect.

### Underwater

The underwater effect is similar to the vignette (screen effect giving a circular shadow around the screen) with a blue tint.

  

This section of the article is empty. 
You can help by make more long adding to it.


### Distortion overlay

  

This section of the article is empty. 
You can help by adding to it.


### Darkness vignette

  

This section of the article is empty. 
You can help by adding to it.


### World border overlay

The world border effect is similar to the vignette and underwater effect but with a red tint.

  

This section of the article is empty. 
You can help by adding to it.


### Freezing overlay

The freezing overlay is a circular formation of crystals and snow flakes, appearing when frozen in powdered snow.

  

This section of the article is empty. 
You can help by adding to it.


### Pumpkin blur

The pumpkin blur is a cutout shape of the pumpkin's face which appears when wearing a pumpkin.

  

This section of the article is empty. 
You can help by adding to it.


### Spyglass scope

The spyglass scope is a square in the middle of the screen which appears when using a spyglass. 

  

This section of the article is empty. 
You can help by adding to it.


## Animated sprites and models
### Elder Guardian ghost
| Visible in second/third person? | Yes             |
|---------------------------------|-----------------|
| Visible with HUD disabled?      | Yes             |
| Visible in graphics settings    | [needs testing] |
| Can be controlled by            | None            |

{
    "title": "\"Elder Guardian curse\"",
    "rows": [
        {
            "field": "Yes",
            "label": "Visible in second/third person?"
        },
        {
            "field": "Yes",
            "label": "Visible with HUD disabled?"
        },
        {
            "field": "<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i>[https://minecraft.wiki/w/Talk:Screen_effects <span title=\"An editor has requested that this be tested in the game to prove that it is a true statement. Once you have tested this in-game and you get the same results as this states, you may remove this template.\" >needs testing</span>]</i>]</sup>(link to Category:Testing needed article, displayed as Category:Testing needed)",
            "label": "Visible in graphics settings"
        },
        {
            "field": "None",
            "label": "Can be controlled by"
        }
    ],
    "invimages": [],
    "images": [
        "Elder guardian curse.gif"
    ]
}

  

This section is named by the community. 
An official name has not been given. Please update the name if confirmed by reliable sources.


When within a spherical radius of 50 blocks of an elder guardian, the player is inflicted with Mining Fatigue III. This is indicated by a ghost of an elder guardian appearing in the players view, moving from the top of the screen to the bottom.

This occurrence is considered a particle effect and can be summoned with the /particle minecraft:elder_guardian command.‌[Java Edition  only]

The model of the elder guardian is used for this effect. This means that changing the texture and model associated with the elder guardian will also change what appears on the players screen. 

### Totem of Undying
| Visible in second/third person? | JE: YesBE: Yes |
|---------------------------------|----------------|
| Visible with HUD disabled?      | JE: NoBE: Yes  |

{
    "title": "Totem of Undying",
    "rows": [
        {
            "field": "'''(link to Java Edition article, displayed as JE):''' Yes<br>'''(link to Bedrock Edition article, displayed as BE):''' Yes",
            "label": "Visible in second/third person?"
        },
        {
            "field": "'''(link to Java Edition article, displayed as JE):''' No<br>'''(link to Bedrock Edition article, displayed as BE):''' Yes",
            "label": "Visible with HUD disabled?"
        }
    ],
    "invimages": [],
    "images": [
        "Totem of Undying Animation.gif"
    ]
}
The effect is used when a totem of undying is popped (saved the player from a death). The totem spins to the middle of the screen and disappears.

  

This section of the article is empty. 
You can help by adding to it.


### Bad Omen

  

This section of the article is empty. 
You can help by adding to it.


### Hero of the Village

  

This section of the article is empty. 
You can help by adding to it.


## Transformations
### Damage tilt

When the player recieves damage, their screen tilts to the direction opposite of the entity or block who damaged the player.

  

This section of the article is empty. 
You can help by adding to it.


### View bobbing

This is a toggleable feature which adds a slight movement of the screen from left to right when walking.

  

This section of the article is empty. 
You can help by adding to it.


### Distortion effects

  

This section of the article is empty. 
You can help by adding to it.


### Speed FOV changes

When sprinting or being affected of a speed effect, the FOV (field of view) increases.

  

This section of the article is empty. 
You can help by adding to it.


### Underwater FOV changes

When in water, lava or powdered snow, the FOV decreases.

  

This section of the article is empty. 
You can help by adding to it.


