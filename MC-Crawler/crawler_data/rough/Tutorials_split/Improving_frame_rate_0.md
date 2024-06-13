# Tutorials/Improving frame rate
Frame rate (also known as fps) is the frequency rate at which a video device produces unique consecutive images called frames. Frames are still pictures that when in a sequence form a fluid animation that is the basis for all moving media. Frame rate is most often expressed in frames per second (FPS).

Low FPS will result in a "choppy" gaming experience, as far as looking like a slideshow in extreme cases. Difficult calculations (like blowing up large amounts of TNT or spawning in a large number of mobs) can temporarily decrease the FPS to a complete stop.

## Contents
- 1 Monitoring frame rate
- 2 Game Settings
- 3 Gameplay Issues
- 4 Outside of Minecraft
- 5 JVM optimizations
- 6 Stuttering on Mac
- 7 Alternative Minecraft launchers
- 8 Modded clients and modpacks
- 9 External links
- 10 Notes

## Monitoring frame rate
Press F3 to bring up the debug screen. The frame rate will be shown under the Minecraft version at the top left.

Note that the debug screen is known to cause more load to your system, resulting in lower FPS than you would normally achieve, so your FPS might increase as soon as you close the display. You can still see the FPS in other ways, such as downloading GUI mods. to bring up pie chart, press f3 plus shift of mac and f3 plus 1 on acer

## Game Settings
Most of the following suggestions are configurable in the game's Options menu, accessible by pressing Esc.

- Turn down your render and simulation distances.
- Set Maximum FPS to Unlimited; however, lower-mid end PCs will experience stutter.
- Reduce Graphics fromFabulous!to Fancy or Fast.
- Turn off smooth lighting and clouds.
- Reduce your FOV.
- Reduce Particles to Decreased or Minimal.
- Turn off V-Sync.
- If the mouse cursor is lagging, change the mouse sensitivity to HYPERSPEED!!!.
- Reduce or disable mipmaps. Note that this can result in water/lava drips not being visible, and thus taking a lava bath.
- Reduce or disable biome blending. This will make the color of certain blocks change less smoothly between biomes.
- Reduce the size of the game's window, as this makes the game render less, making the game run a little bit faster.
	- If your computer has a better graphics card, you might want to enable full screen, as this will make your GPU focus more on Minecraft and less on other programs. Test both ideas and see which setting works best!
- Install optimization mods.
	- OptiFineis the most well-known optimization mod, but only supports either running by itself or as a Forge mod. However, in more recent times there have been mods such asSodium, made for Fabric.
	- Note thatSodiumonlysupports Minecraft 1.16+ with Fabric/Quilt and can't be installed together with OptiFine, but provides significantly higher performance than OptiFine on most PCs.Sodium Extracan also be used to add many of OptiFine's options. Sodium can be paired withLithiumto speed up the game's internal server. On Minecraft versions before 1.20,StarlightandPhosphorare helpful to speed up lightning calculations. Other optimization mods to use alongsideSodiumfor Fabric include:
		- LazyDFUspeeds up the game's startup (not needed on Minecraft 1.19.4 and up).
		- ImmediatelyFastimproves the performance of rendering entities, GUIs and more.
		- More Cullingimproves culling of invisible block faces in many parts of the game and adds optional leaves culling akin toCull Leavesto improve FPS.
		- DynamicFPSlowers the game's FPS when the game's window is not in focus.
		- FerriteCoreoptimizes RAM usage. This is unlikely to improve FPS in most cases, but could allow other running programs to use more RAM.
		- ModernFixreduces the game's RAM usage as well as load times with many optimizations.
		- Enhanced Block Entitiesmakes some block entities use block models rather than laggy entity models.
		- If you want to run shaders, useIrisinstead of OptiFine. Iris has compatibility with most OptiFine shaders(withsome exceptions) and is much faster due to being an add-on forSodium.
	- However, if you absolutely want to run Forge mods, then here are some options:
		- There are multiple Forge ports of Sodium available. They areNOTand will never be compatible with OptiFine or each other.
			- Rubidiumseems to be more up-to-date than Magnesium.
			- Magnesiumthough is a bit more popular.
			- Embeddium, a fork of Rubidium with better compatibility.
		- Starlight Forgeis the official Forge version of Starlight, to optimize the lighting engine.
		- RoadRunneris an unofficial port of Lithium for Forge, to optimize general game systems.
		- FerriteCore Forgeis the official Forge version of FerriteCore, to reduce RAM usage.
		- Oculusis a port of Iris to Forge, recommended to be used with Rubidium.
- If your computer is hot or your fan is loud, avoid running mods which add a lot of content and don't do anything that causes your computer to run a lot of calculations. This means closing any browsers or other games. The simplest way to reduce the game's resource usage for improved temperatures or battery life is to set an FPS cap or enable VSync.

## Gameplay Issues
- Try not to go to theNetheron lower-end PCs.  Particularly complex terrain like mountains, jungles, mangrove swamps, or even ancient cities, can also be troublesome.
- If inmultiplayer, move away from areas densely populated by players.
- Large numbers of item frames in view (even through walls) can cause lag. This includes map walls!
- Be careful about building large farms or other devices.
	- While crop growth is not usually burdensome, for sufficiently large farms even plant growth can add up.
	- Farms that produce large amounts of animals or item entities can cause lag.
	- Large and complex redstone devices, especially those driven by fast clocks, can likewise make trouble.  Keeping redstone dust and other changeable blocks out of sight can be helpful.
		- Rapid changes in lighting are especially troublesome.  Several redstone devices emit changeable light:  Even switching a redstone torch can require updating the light levels for blocks up to 6 spaces away.  Redstone lamps (and mobile glowstone or other lights), can affect much larger areas, especially if they are illuminating a complex landscape or build.

