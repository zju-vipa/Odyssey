# Build disallow block
Build disallow block is one of the first custom blocks added to MinecraftEdu. It can be used to set up areas where students cannot build even if student building is enabled in the world.

## Contents
- 1 Usage
- 2 Behavior
- 3 Availability
- 4 Data values
- 5 Video
- 6 History

## Usage
Build disallow block prohibits student creation or destruction of blocks, even if student building in general is enabled.

## Behavior
- Disallows students to place blocks or dig anywhere directly above this block.
- Students can place blocks and dig under this block (if student building is allowed).
- Cannot be broken by students (not even when student building is enabled).
- Teachers can break at anytime.

## Availability
- Block can be found in Creative inventory. Only teachers can see this block in their inventory.
- Can also be given inTeacher menu "give"section.
- Can be distributed by console command or with acommand block.

## Data values
ID of this block is 3720.

| Name                 | Identifier           | Translation key                      |
|----------------------|----------------------|--------------------------------------|
| Build disallow block | `blockDialogMessage` | `block.minecraft.blockDialogMessage` |

