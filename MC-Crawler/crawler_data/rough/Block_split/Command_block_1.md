### Activation
Command blocks are redstone mechanisms and can be activated by:

- An adjacent activepower component: for example, alever, ablock of redstone, adaylight sensor, abuttonetc.
- An adjacentpowered block(for example, an opaque block with an active redstone torch under it)
- A poweredredstone comparatororredstone repeaterfacing the mechanism component
- Poweredredstone dustconfigured to point at the command block (or on top of it) or directionless; a command block isnotactivated by adjacent powered redstone dust that is configured to point away from it.

A command block can also be activated by setting it to "Always Active" mode.

When activated, a command block executes its command, depending on the command block's type:

- An impulse command block executes its command once.
- A chain command block does not execute its command until it is triggered.
- A repeat command block executes its command once every one game tick (or more‌[BE  only]) until no longer activated.

### Execution
An impulse command block, when it is activated, checks whether the command block behind it has executed successfully (if in conditional mode). After the delay of 1 game tick (or more‌[BE  only]), if the condition is met before the delay (if in "Conditional" mode), it executes its command once and triggers the chain command block it is pointing to.

A repeat command block, when it is activated, after 1 game tick (always 1 no matter how many "Delay in Ticks" is), checks whether the command block behind it has executed successfully (if in conditional mode). If the condition is met, and if "Execute on First Tick" is enabled in Bedrock Edition, it executes its command once and triggers the chain command block it is pointing to. If it is still activated, it then checks, executes, and triggers the chain command block again after 1 game tick (or more‌[BE  only]).

When executing a command, it also updates its success count: If in "Conditional" mode, if the command block behind it didn't execute successfully, it sets its success count to 0. Otherwise, it sets it to the success count of the command.

Also:

- When an impulse or repeat command block in "Needs Redstone" mode with a command is placed or is cloned by a command to a powered location, the new command block executes its command only if it hasn't been activated with redstone. InJava Edition, it also needs a block update to execute its command.
- When an impulse or repeat command block in "Always Active" mode with a command is placed or is cloned by a command to a powered location, the new command block executes its command only if it hasn't been activated with redstone.
- When an impulse or chain command block is set to "Repeat", if it has been activated, checks whether the command block behind it has executed successfully (if in conditional mode). After 1 game tick (always 1 no matter how many "Delay in Ticks" is), if the condition is met, it executes its command once and triggers the chain command block it is pointing to. Then it checks, executes, and triggers the chain command block again after 1 game tick (or more‌[BE  only]).

#### Trigger and chaining
If any command block having executed its command (whether successfully or unsuccessfully) faces a chain command block, it triggers the chain command block to also attempt execution.

When a chain command block is triggered,

- If it has been activated,
	- It checks whether it is in "Conditional" mode and the command block behind it hasn't executed successfully (Behind in the sense of the direction it is facing, not in the sense of which command block chained to it),
		- If true, it triggers another chain command block it is facing, without executing the command.
		- If false, it checks whether it has been already executed in this game tick. If false, it executes the command and triggers another chain command block it is facing. If true, it does nothing. That means that chained execution cannot be passed to a command block that has already executed in that game tick (loops execute only once).
- If it has not been activated, it triggers the chain command block it is facing to attempt execution.

Chained command blocks execute simultaneously in the same game tick in the order they are chained.

In Bedrock Edition, it can also delay before executing commands if "Delay in Ticks" is not 0:

When it is triggered,
- If it has been activated, the chain command block checks whether the command block behind it has executed successfully (if in conditional mode), then it delays.
	- After a delay, if the condition is met before the delay (if in "Conditional" mode), it executes its command once and triggers the chain command block it is pointing to no matter whether the condition met.
- If it has not been activated, it triggers (without delay) the chain command block it is facing to attempt execution.

In Java Edition, it can execute multiple times in the same game tick if "UpdateLastExecution" is set to false. In this case, it does not check whether it has already executed in this game tick.

If the chain command block has been activated when triggered, it also updates its success count: If in "Conditional" mode, if the command block behind it didn't execute successfully, it sets its success count to 0. Otherwise, it sets it to the success count of the command.

