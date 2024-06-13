## Refining
Once the circuit is working, consider if it can be improved (without breaking it).

- Can the circuit be faster?
	- Shorter delays and pulses can make most circuits faster.
	- Reducing the number of components or distance a signal has to travel through can speed up the circuit.
- Can the circuit be smaller?
	- Can fewer blocks be used?
	- Is there a more efficient way of doing the same thing?
	- Can the redstone dust lines be shortened?
	- Are unnecessary components used?
- Can the circuit be more robust?
	- Will the circuit still work when activated by a very short pulse?
	- Will the circuit still work when activated and deactivated rapidly in succession?
	- If either of the above are a problem, can this be fixed by filtering the input?
	- Can the circuit be damaged if unloaded? Be careful with constantly running clocks.
- Did an update create the opportunity for a better circuit? (e.g., comparators, locking repeaters, observers, etc.)
- Can the circuit be quieter?
	- Fewer sound-producing blocks (e.g. pistons, dispensers and droppers, doors, trapdoors, fence gates, and note blocks) will make your device more stealthy around other players.
- Can any lag be reduced? Machines with many redstone components frequently changing state can cause light, sound, particle, or update lag.
	- Redstone dust creates hundreds of block updates whenever it changes states, and the more the signal strength changes, the more block updates it will produce. Reducing the length of redstone lines will significantly decrease lag. An alternative to redstone dust lines is to use lines of rails which update observers, as rails create much less block updates than dust.
	- Hoppers and hopper minecarts especially try to do several things every tick (accept items pushed into them, push items into other containers, check for item entities above them). Powering hoppers to disable them when not in use or placing containers (such as composters) above them to disable their item entity checks can help to reduce lag.
	- Redstone torches and redstone lamps change their light level when they change state. Light changes can cause block light updates inhundredsof block tiles around each component. Concealing the component in opaque blocks or placing permanent light sources (torches, glowstone, etc.) nearby can reduce light updates. While light updates no longer create lag on since they are on a separate thread, excessive light updates can light suppress which lags other actions such as chunkloading.
	- Several redstone components produce particles (redstone torches, redstone dust, but especially fireworks fired from dispensers). Too many particles may overloadMinecraft'sparticle rendering and then some particles may fail to render until old particles have disappeared.
	- Every time a block is moved by a piston, the piston makes many checks for movement and it produces block updates in its neighbors, so moving too many blocks at once can produce lag.


