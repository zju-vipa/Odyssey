## Order-sensitive combination locks
Order-sensitive combination locks are sometimes known as permutation locks.

### Order-sensitive changing code XNOR Combo Lock
Opens when a certain order of switches are pressed.
You can change the order.
(Note: A moderate understanding of logic gates is needed for this device.)
Have 4 blocks near each other with a switch and a sign saying 4,3,2 or 1 respectively.
10 blocks to the right and 2 blocks down place a block then place 2 more with a 5 block space. 6 right and 3 up place the block. Label them 4-3-2-1 respectively.
Have a 11 block wire or 13 for left to a repeater on the 9th block or 11th for left and on the right side. Place a repeater 2 blocks over with the same wire from it. Connect the left repeaters.
to the code changing module. (You may use bridges of cobblestone for getting over other wire and repeaters for boosting the signal. Construct a XNOR Gate where).
2 of the wires meet. Connect to adjacent outputs with AND gates. These Outputs are connected to final AND gate. Final AND gate if connected to iron door.

### Order-sensitive RS NOR Combo Lock
A door that opens when buttons are pressed in certain order.

(Note: A moderate understanding of logic gates is needed for this device.)

Make a series of buttons, and connect only one to an RS NOR latch. Then connect both the RS NOR latch and a second button to an AND gate, which feeds to another RS NOR latch. Do this continually until you have either filled all of the buttons or are satisfied with the lock. Connect the final RS NOR latch to a separate AND gate with a signal from an enter button. Feed that to the output RS NOR latch. Then connect any of the left-over buttons to the enter button and send reset signals to all of the RS NOR latches. A pressure plate next to a door can reset the door. This type of lock has severe limitations its security. For example, not all the buttons could be used in the pin or there would be nothing to reset the system.

For a lock that can have a combination of any size, using all the buttons, and still have a wrong entry reset the system, you need a different way for it to reset. To construct this, hook up a panel of buttons (any number, but four or more is preferred) to a parallel series of adjacent repeaters. Invert as necessary so that all the repeaters are powered and are unpowered by the press of the corresponding button. These repeaters power a row of blocks. On top of the blocks, place a torch corresponding to the incorrect buttons for the fist number in the PIN. For the correct button/number, place dust under the powered block which leads to a RS NOR Latch. Place a row of blocks above the torches for the incorrect buttons, with redstone dust on top. Then connect this dust to the reset of the first RS NOR Latch. Only the correct button will set the RS NOR Latch and all others will reset it. Connect the output of the RS NOR LATCH to half of an AND gate. After the first row of blocks with the reset torches, place another row of repeaters and another row of blocks. Again place torches for the incorrect buttons and dust under the correct button's line. Power will be fed from the buttons through the rows of repeaters and blocks for as many rows as there are digits in the PIN number. Connect the dust from the correct button to the other half of the AND gate coming from the first RS NOR Latch. Only if the two conditions are met, that the first button was pushed correctly, setting the first RS NOR Latch, and the second button is pushed correctly will the AND gate send a signal to set the second RS NOR Latch. Again, connect a reset line from the incorrect button's torches to the reset of the second RS NOR Latch. Delay the reset signals by one full repeater to give time for the next RS NOR Latch to be set before the reset happens. Continue building the array in the same manner until you reach the desired number of digits. In operation, when a button is hit, each RS NOR Latch checks (through the AND gate) to see if the previous RS NOR Latch is set, and the correct button for this RS NOR Latch has been pushed. Only when the correct buttons are pressed in order, will the signal progress through the conditional RS NOR Latches to the end. Connect the output of the last RS NOR Latch to a door and attach a line to a pressure plate inside the door to reset the last RS NOR Latch.

#### Tutorial Video
Combination Lock RS NOR




There is also another way to make order-sensitive combination locks. It is based on several RS NOR latches that is placed on a row. The RS NOR latches are connected together, and each latch is connected to one button. The combination lock opens when all the latches are activated. To activate all of them, the latches have to be activated in the right order. If wrong button is pressed, the lock automatically sends a reset signal to the first latch, and resets the entire lock. The circuit also has a T flip-flop that controls the output. The T flip-flop turns on and stays on when the right combination is pressed. When the lock is open, all the buttons works like a reset button. This makes it easy to close the door from the outside. Just press a random button. It is also possible to connect buttons that overrides the lock and makes the output signal toggle like on a normal T flip-flop.

