### IMPLY gate
| A           | On | On  | Off | Off |
|-------------|----|-----|-----|-----|
| B           | On | Off | On  | Off |
| A IMPLIES B | ON | off | ON  | ON  |

An IMPLY gate (A → B) turns on either if both inputs are on, or if the first input is off. Unlike the other gates here, the inputs are not interchangeable; it is not commutative. This represents material implication or a conditional statement, "if A then B", or "A implies B". The output is off only if the antecedent A is true, but the consequent B is false. It is the logical equivalent of B ∨ ¬A, and the mathematical equivalent of A ≤ B.

Design C has a speed of 2 ticks if output is 1, but 1 tick if the output is 0. Similarly, the other designs take 1 tick if the output is 0, but are immediate (and not isolated) if the output is 1. If the player must synchronize (or isolate) the output, consider placing a 1-tick repeater in front of the "fast" input (input A for C, input B for the others).


Note if the IMPLY gate powers a block that needs to be powered again to be activated (e.g. dropper, dispenser) then either, A has to be on, or A and B, as it is already on. The logic may opposingly apply to NIMPLY gates.
Schematic gallery: IMPLY gate View at: Mechanics/Redstone/Logic circuit/IMPLIES [edit]


