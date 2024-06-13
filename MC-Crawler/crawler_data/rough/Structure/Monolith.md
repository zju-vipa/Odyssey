# Monolith
Monoliths were glitched areas of terrain that happened in the later versions of Infdev and early Alpha eras of the game. These monoliths would cause the terrain to abruptly invert, with natural terrain generation replacing the air/water up to the height limit and vice versa.

## Contents
- 1 Generation
- 2 Structure
- 3 History
- 4 Issues
- 5 Trivia
- 6 Gallery
	- 6.1 Renders
	- 6.2 Screenshots

## Generation
Monoliths would generate in seemingly random locations throughout the world. They tended to generate around flattish terrain. They were caused by an error in the Perlin noise generator. Specifically, the hilliness of the terrain (the "terrain scale") was controlled by a noise map. The reciprocal of the value of this noise was then used as the intensity of a gradient applied to the terrain. Because the reciprocal is used, flatter terrain is caused by lower values (where the terrain bias gradient drops off faster), and hillier terrain is caused by higher values. Because the reciprocals of small negative numbers are very large negative numbers, the terrain abruptly changes when zero is crossed, causing the gradient to bias higher elevations toward being ground, and lower elevations toward being air. Thus, when terrain scale becomes negative, terrain generates upside-down, generating monoliths. This was possible in early Alpha because the noise map that determined terrain scale could return a negative value.[more information needed]

## Structure
The monoliths would cause the terrain to abruptly generate up to the height limit, with natural grass block and ore generation. They could theoretically generate infinitely upward, being stopped only by the height limit, which - at this point in the game's development - was 128 blocks. The area below the monoliths was completely hollow, except for water generating at sea level and a layer of bedrock at the bottom, making the normal terrain seem like inverse monoliths. It is possible to find small crevices in large monoliths, where normal terrain was generated.

