# Bamboo (feature)
A bamboo is a feature that consist of bamboo blocks, found throughout jungle biomes.

## Contents
- 1 Generation
- 2 Data values
	- 2.1 ID
	- 2.2 Config
- 3 History
- 4 Gallery
	- 4.1 Screenshots
- 5 References

## Generation
A bamboo is a feature that represents a bamboo plant, made of bamboo blocks. They can be found in the Jungle, Sparse Jungle‌‌[Bedrock Edition  only] and Bamboo Jungle biomes at the surface. They're less common in Jungle and Sparse Jungle‌‌[BE  only] biomes.

In Jungle and Sparse Jungle‌‌[BE  only], there's no podzol under the bamboo, while in Bamboo Jungle, podzol sometimes generates.

Bamboos' height varies between 5 and 16 blocks, and if there's an obstacle preventing growth, it may be even shorter.

## Data values
### ID
Java Edition:

| Feature type        | Identifier |
|---------------------|------------|
| [No displayed name] | `bamboo`   |

| Configured feature  | Identifier           |
|---------------------|----------------------|
| [No displayed name] | `bamboo_no_podzol`   |
| [No displayed name] | `bamboo_some_podzol` |

Bedrock Edition:

| Feature             | Identifier                |
|---------------------|---------------------------|
| [No displayed name] | `bamboo_feature`          |
| [No displayed name] | `optional_podzol_feature` |

which are used in:

| Feature             | Identifier                   |
|---------------------|------------------------------|
| [No displayed name] | `bamboo_then_podzol_feature` |

### Config
Main article: Configured feature
Java Edition:

- config
	- probabilityThe probability for a podzol disk to generate below the bamboo. The disk has a radius of 1 to 4 blocks. Value between 0.0 and 1.0 (inclusive).




An example

{
  "type": "minecraft:bamboo",
  "config": {
    "probability": 0.2
  }
}



