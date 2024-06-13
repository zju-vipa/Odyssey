### NAND gate
| A        | On  | On  | Off | Off |
|----------|-----|-----|-----|-----|
| B        | On  | Off | On  | Off |
| A NAND B | off | ON  | ON  | ON  |

A NAND gate (A↑B or A⋅B‾) turns the output off only when both inputs are on, the reverse of an AND gate. All logic gates can be made from NAND gates.  As with NOR, large numbers of inputs are probably best handled by stacking up AND gates, then inverting the result. By De Morgan's Law, A⋅B‾ is identical to A‾+B‾.

All logic gates can be made from some combinations of the NAND gate.


Schematic gallery: NAND gate View at: Redstone circuits/Logic/NAND [edit]
### XOR gate
| A       | On  | On  | Off | Off |
|---------|-----|-----|-----|-----|
| B       | On  | Off | On  | Off |
| A XOR B | off | ON  | ON  | off |

An XOR gate (A⊻B, A↮B or A⊕B) is a gate that uses two inputs and the output is toggled to "on" when one switch is "on" and one switch is "off". XOR is pronounced "zor" or "exor", a shortening of "exclusive or", because each input is mutually exclusive with the output. It is useful for controlling a mechanism from multiple locations. Because of these properties, XOR gates are commonly found in complex redstone circuits. In some cases, it is possible to get an OR gate output and an AND gate output on different channels. Design F is composed of AND gates, OR gates and NOT gates. The whole circuit is (A⋅B)+A‾‾+(A⋅B)+B‾‾, which can be further simplified into (A‾⋅B)+(A⋅B‾) (or, equivalently, (A+B)⋅A⋅B‾).

A useful feature is that an XOR (or XNOR) gate always changes its output when one of its inputs changes, hence it is useful for controlling a mechanism from multiple locations. When controls (such as levers) are combined in an XOR gate, toggling any control toggles the XOR gate's output (like a light bulb controlled by two light switches — players can flip either one to turn the light on or off, or either of which can always open or close a door, or turn some other device on or off.

Like AND and OR gates, XOR gates can freely be "stacked" together, with gates gathering groups of inputs and their outputs being gathered in turn. The result of XORing more than two inputs is called "parity" — the result is 1 if and only if an odd number of inputs are 1.   

Design D is tiny, but useful if players want the levers to be fixed to the circuit. The shaded block indicates the block the levers and the lit torch are attached to, along with the block that one is resting on.

Design F is the most widely used of the torch-only designs, but newer components can do much better. Design H uses pistons, and is both faster and more compact.   

Beyond torches and pistons, various diodes can be used to produce fairly compact and cheap XOR gates. Design I can have its input repeaters coming in from either side or underneath, changing its size accordingly to fit tight spaces. Design J uses transparent blocks for a cheaper option.

Schematic gallery: XOR gate View at: Redstone circuits/Logic/XOR [edit]
The introduction of the comparator allows for several variations of a new design, the "subtraction XOR gate", which is flat, fast and silent (also easy to remember). The cons in Survival mode is that making comparators requires the access to the Nether to obtain nether quartz.

Each input is the same distance to the rear and side of the comparator closest to it, suppressing its own signal there, but travels farther to get to the side of the further comparator, so doesn't suppress its signal in the further comparator. Only if both inputs are on do both comparators get suppressed by a side input.

However, that is true only if the inputs are the same power level (or at least not different by more than 1), otherwise one signal could overwhelm the other's attempt to suppress its signal. If this circuit is sure to receive inputs of the same power level (because the system it's part of has been designed that way), then the "basic" version can be used. Otherwise, some method should be used to ensure the inputs are equal — for example, with repeaters (the "repeated" version) or with torches (the "inverted" version).

Schematic gallery: subtraction XOR gate View at: Redstone circuits/Logic/subtraction xor gate [edit]
### XNOR gate
| A        | On | On  | Off | Off |
|----------|----|-----|-----|-----|
| B        | On | Off | On  | Off |
| A XNOR B | ON | off | off | ON  |

An XNOR gate (A↔B or A⊙B) is the opposite of an XOR gate. This is commonly referred to as "if and only if" ("iff" [sic] for short), "bi-conditional", or "equivalence". It uses two inputs. When both switches are in the same state (both switches are "on" or both switches are "off"), then the output is toggled to "on". Otherwise, if the switches differ, the output is toggled to "off". Similar to the XOR gate, when either input changes, the output changes.

An XNOR gate can be built by inverting either the output, or one input, of an XOR gate. 

Design A is a pure-torch design. If external input isn't needed, the back-facing torches can be replaced with levers, yielding B. Design F is larger but highlights the logic, while I is an inverted variant of XOR gate H. Note that the output inverter can also be placed in line with the rest of the gate, or even in a pit attached to one of the output redstone's support blocks.


Schematic gallery: XNOR gate View at: Redstone circuits/Logic/XNOR [edit]
