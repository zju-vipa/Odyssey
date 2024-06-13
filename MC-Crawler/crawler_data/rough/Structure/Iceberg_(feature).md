# Iceberg (feature)
An iceberg is a feature composed of packed ice and/or blue ice.

## Contents
- 1 Generation
	- 1.1 Variants
		- 1.1.1 Composition
		- 1.1.2 Shape
		- 1.1.3 Dimensions
	- 1.2 Carved
	- 1.3 Spacing
	- 1.4 Blue ice
- 2 Data values
	- 2.1 ID
	- 2.2 Config
- 3 History
- 4 Gallery
	- 4.1 Renders
	- 4.2 Screenshots
- 5 References

## Generation
The "iceberg feature" (called a cone iceberg) generates a small iceberg, shaped like a rounded upside-down cone, or an ice cream cone. The "iceberg terrain feature" (a large iceberg) generates a large, mountainous iceberg.

Cone icebergs generate in frozen oceans and deep frozen oceans. They can consist of packed ice, blue ice, snow.

### Variants
#### Composition
Most cone icebergs are made of packed ice.

Each cone iceberg has:

- a 30% probability to be topped with snow (snow-capped). The snow is about 1 block thick
- an1⁄200‌[JE  only]or1⁄100‌[BE  only]independentprobability to try be a§ blue iceiceberg

This means that 3⁄2000 cone icebergs are snow-capped blue ice icebergs.

The iceberg has a 30%‌[JE  only] or 20%‌[BE  only] probability to be elliptic, and is circular otherwise.

#### Shape
Cone icebergs have two types:

- circular (circle-shaped)
- elliptic (ellipse-shaped)

#### Dimensions
A circular iceberg has a random radius from 0-11.

Example: (0-11)

Its max height above sea level is:

- 90% probability:
	- 3-17‌[JE  only]or3-13‌[BE  only]
- 10% probability (mutually exclusive):
	- 10-42‌[JE  only]or10-34‌[BE  only]

The max depth below sea level is:

- 3-18

An elliptic iceberg has:

- a semimajor axis of7-11‌[JE  only]or8-15‌[BE  only]
- a semiminor axis of3-5
- a max height above sea level of6-11‌[JE  only]or6-9‌[BE  only]
- a max depth below sea level of6-18

### Carved

  

This article is missing information about this section. 
Please expand the article to include this information. Further details may exist on the talk page.


This is probably some kind of recess (a crater or depression on the side or bottom of the iceberg), but more information is needed. This is probably related to the cave-like holes in large icebergs.

Each circular iceberg has a 30% probability of being carved.

Each elliptic iceberg  has a 90% chance of being carved.

### Spacing
In Java Edition, each chunk (of a valid occean) has an 1⁄16 ‌[JE  only] 1⁄8 ‌[BE  only] probability to try to generate a cone iceberg.

### Blue ice
Some packed ice icebergs sometimes have blue ice features attached to them. A blue ice feature is a pile of blue ices that generates adjacent to a packed ice, typically at the bottom of the iceberg.

## Data values
### ID
Java Edition:

| Feature type        | Identifier |
|---------------------|------------|
| [No displayed name] | `iceberg`  |

| Configured feature  | Identifier       |
|---------------------|------------------|
| [No displayed name] | `iceberg_blue`   |
| [No displayed name] | `iceberg_packed` |

Bedrock Edition:

| Feature             | Identifier         |
|---------------------|--------------------|
| [No displayed name] | `blue_ice_feature` |
| [No displayed name] | `iceberg_feature`  |

Used in:

| Feature             | Identifier                     |
|---------------------|--------------------------------|
| [No displayed name] | `minecraft:legacy:ice_feature` |

### Config
Main article: Configured feature
Java Edition:

- config
	- stateThe block to use.
		- 
		- Block state


An example

{
  "type": "minecraft:iceberg",
  "config": {
    "state": {
      "Name": "minecraft:packed_ice"
    }
  }
}



