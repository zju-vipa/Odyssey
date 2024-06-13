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

