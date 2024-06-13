# Six-sided Piston
A six-sided piston was an extreme metadata variant of the piston. It could be used as update suppression agents.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 BUD piston method
	- 1.3 Block transmutation
- 2 Usage
	- 2.1 Update suppression
- 3 History
- 4 Issues
- 5 References

## Obtaining
### Breaking
Six-sided pistons can be broken in the same way normal pistons can. They cannot be obtained as an item, instead dropping normal pistons.

| Block     | Six-sided Piston      |
|-----------|-----------------------|
| Hardness  | ?                     |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | ?                     |
| Wooden    | ?                     |
| Stone     | ?                     |
| Iron      | ?                     |
| Diamond   | ?                     |
| Netherite | ?                     |
| Golden    | ?                     |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### BUD piston method
Six-sided pistons of metadata value 7 could be created if a placed piston updates a BUD-powered piston, such that it pushes or pulls the placed piston.

### Block transmutation
Multiple block transmutation methods can be used to create Six-sided Pistons in Java Edition. From Beta 1.7.2 to Beta 1.9 Prerelease Six-sided Pistons can be created using moving piston merge transmutation, from Beta 1.7.3 to 1.2.3, can be created using water transmutation, and from 13w36a-1 to 1.7.5 and 14w02a to 14w11b, can be created using arrow transmutation.

## Usage
### Update suppression
When powered, six-sided pistons of metadata 6 immediately crash the game. This game crash happens so quick that block updates are not processed correctly, and this can allow for otherwise-impossible arrangements of blocks to be achieved.

Every time the six-sided pistons is updated while receiving power, the game crashes again, so having it be in a position where it receives constant updates is not recommended due to effectively softlocking the world. Depowering the six-sided pistons should make it safe again. This has a possibility of corrupting singleplayer worlds, and it is much safer to perform this on a hosted server.

Analysis of the behavior of metadata 6 six-sided pistons using 1.7 releases and 1.8 snapshots suggests that they remain at data value 6 permanently, even upon loading a world, as opposed to converting to data value 14 - if they do indeed convert, this conversion is not saved.

