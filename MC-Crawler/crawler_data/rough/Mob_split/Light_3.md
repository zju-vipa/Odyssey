### Smooth lighting
The difference between Smooth Lighting on and off.
Smooth lighting is a lighting engine that blends light levels across block faces and darkens corners using ambient occlusion to add semi-realistic shadows and glowing from light sources. It affects only rendered brightness, not the light level, so it has no effect on mob spawning or crop growth. It is set on by default. Paintings, item frames[1] and water surfaces[2] are unaffected.‌[Java Edition  only]

Smooth lighting can be turned on or off in the video settings.


### Ambient occlusion in Minecraft

  

This section needs cleanup to comply with the style guide. [discuss]
Please help improve this page. The talk page may contain suggestions.


In many newer games, ambient occlusion is mainly generated dynamically by the GPU.
But Minecraft calculates ambient occlusion in the code based on voxel placement and brightness levels. 

Ambient occlusion is responsible for adding shading to an ordinary texture. It is a layer of translucent textures, on top of the normal textures.
Overlaying these AO textures onto a texture is called AO mapping.
There are about five AO texture patterns used in Minecraft's smooth lighting, excluding flips and rotations, and only three patterns algorithmically. Strictly speaking, it's probably more than that. That's when the intensity changes with the brightness level. But they are solved by tint.

### AO texture pattern

  

This section needs cleanup to comply with the style guide. [discuss]
Please help improve this page. The talk page may contain suggestions.


If AO mapping is selected only to the northwest of the voxel, the following pattern is possible.

| Number | Image |
|--------|-------|
| 0      |       |
| 1      |       |
| 2      |       |
| 3      |       |

These classifications allow one the ability to deduce a pattern from the placement of each voxel.
The following function can then be used to compute the opacity of the voxels' vertices, depending on the presence of the side and corner voxels.

function vertexAO(side1, side2, corner) {
  return 3 - (side1 + side2 + corner)
}

This generates a 2×2 pixel image using the values of each vertex. The pixels are small, but when zoomed in using anti-aliasing, it gradates.

 


