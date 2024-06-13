### Junction
Stations often have one line leading to one destination. Multiple destinations require multiple lines. A junction is a fork in the track where the rider can select which destination they wish to visit.

Two-way junction
This design uses a lever to switch the track. The powered rail becomes powered after a preset delay. The detector rail starts the delay. In this design, the lever always points toward the selected destination regardless of direction.

Four-way junction
A junction that has multiple destinations can be set up by expanding the junctions. In the design to the right, the rider is given much more time to select their destination than a two-way junction. They can select any destination by first selecting left or right, then forward or backward. This design doesn't scale well but can be used in sequence to create any number of destinations.

### Multiple destination selector
There are many, many styles of minecart destination selectors. Most are modular, meaning they can be extended to include more destinations. An RS-NOR latch array is often used to select a destination as these latches have a designated reset line (as opposed to a t-flip flop which has only one input).

This design was selected for its simplicity and for its ability to be expanded with relative ease. One of the buttons on the selection panel is a designated reset line since additional input doesn't clear the previous selection; that is to say, a player can select more than one destination with this design (although a launched minecart takes the left-most of the selected destinations).

"Video Tutorial" by CNB

The interior of the second design
The following design is heavily influenced by the previous but uses a different RS-NOR latch design involving pistons. It has a reset integrated in the selection such that a new input clears the previous one. By removing the designated reset line of the previous version, it allows for an additional station in a similar amount of space.

### Piston bolt
This consists of a lot of curved tracks and many pistons. The pistons push the minecart extremely quickly down the line.

| YouTube Video (view on YouTube) |
|---------------------------------|
|                                 |

## Troubleshooting
When a track system isn't working properly, it can be difficult to fix for someone unfamiliar with redstone and rails.
Common solutions include:

- Changing the delay of the circuit by adding a repeater or moving a detector rail to trigger earlier.
- Changing the speed of the minecart by adding powered rails or moving the current ones further away.
- Checking that powered rails are powered properly.
- Turn the design around, as direction can affect how it works. Generally, this isn't the issue, but it's good to rule it out.

Searching on the minecraft forums can help. If you need to create a new post, be sure to include the direction you're working (the F number), as directionality can be a factor in the design.


