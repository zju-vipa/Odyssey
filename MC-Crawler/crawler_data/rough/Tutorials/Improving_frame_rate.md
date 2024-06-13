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

## Outside of Minecraft
- Close or minimize any programs in the background, making sure to definitely close Internet browsers such as Chrome, Firefox, Safari etc.
- On Windows, openTask Managerand go to the details section, findjavaw.exe(the one the game uses), right click it and set its priority to "High" (not"Realtime", as realtime will try to allocateallof the PC's resources (RAM/CPU/GPU) to the game, not leaving enough for Windows to function, causing it to freeze or even blue-screen).
- Make sure you have enough RAM available (in a program such as a task manager), else your computer may swap to disk, which could cause the game to stutter intermittently.
- On laptops and most pre-built desktops, uninstallbloatware.
- The current Minecraft Launcher is very, very slow and heavy to boot itself and the game. Instead of using it, try checking out some third-party launchers. Beware as they are not associated with Mojang and they may be dangerous, especially if they are not open source.MultiMCis a good choice if you don't play too much with many modpacks. It is fast and light, and it allows having multiple separate instances of Minecraft at once. The source code is hosted onGitHuband is under the Apache 2.0 license.
- Do frequent malware scans with an antivirus program, to ensure no malicious programs are consuming computer resources.
- Do not run other CPU- or GPU-intensive programs while the game is open.
- On Windows Vista through Windows 7, disable graphical effects such asWindows Aeroand taskbar transparency.
- Disablecompositing(sometimes called "desktop effects") on GNU/Linux. When compositing is disabled, all window managers tend to give similar performance, so there is no need to use a "lightweight" one.
- Update your graphics card drivers. You can find these on your GPU manufacturer's website.
- Disable anti-aliasing and anisotropic filtering in your GPU driver settings.
- Ensure the computer is running at a cool enough temperature so as to not causethermal throttling. This is especially effective for laptops and older desktops. If the computer is too hot, look into cleaning out dust.
- Reduce the display resolution.
- You may be able to switch your operating system to a GNU/Linux distribution, depending on what you use your computer for. Linux is generally easier on the computer's resources compared to Windows. However, it is important to research hardware/software compatibility (for example, Nvidia graphics cards) before switching operating systems. This makes the most effect on AMD graphics cards, which can see a 2x performance improvement from Linux drivers on OpenGL games such as Minecraft! There are many distributions to choose from, but you should stick to tried and trusted ones. Some recommended distros for beginners includeLinux Mint(Cinnamon desktop with a Windows-like interface, large community, wide application support, easy to install graphics drivers),Fedora(cutting-edge technologies, GNOME desktop (not the most familiar), also wide community) orPop!_OS(GNOME desktop, also very good graphics support).
	- Note that a lot of Windows software isn't available for Linux, including Adobe software, Microsoft Office, as well as many games (Minecraft is an exception, most Steam games also work). You may find alternatives though, such asLibreOffice.
	- If you'd like to have both operating systems, you should look into dual-booting.
- If you are playing on a desktop computer, look into upgrading your graphics card, which can help the game render objects faster.

## JVM optimizations
- Use a high performance garbage collector such as ZGC (for servers) or Shenandoah (for clients). These consume more CPU resources than the default one, but reduce lag spikes. See theMinecraft Performance Flags benchmarkfor more information.
- Allocate a reasonable amount of memory to Minecraft. Minecraft runs best with 2-4 GB of memory. Using ZGC or Shenandoah allows for large 16+ GB allocation without a performance penalty unlike the default G1GC collector. Be sure to leave memory for the system and other programs!
- Use the latest OpenJDK to play Minecraft. If you're on Windows, install OpenJDK fromAdoptium.

## Stuttering on Mac
- Try testing your performance while toggling the V-Sync option.
- The other option when V-Sync is off to stop the stuttering is to set the maximum FPS down to 30, matching the FPS seen when when having V-Sync off, rather than FPS being set to Unlimited as suggested above.

## Alternative Minecraft launchers
The official Minecraft Launcher (sometimes known as Mojang Launcher) is very slow and inefficient, so here are some trusted alternatives players can use.

- MultiMC- Allows you to have multiple, cleanly separated instances of Minecraft (each with their own mods, resource packs, saves, etc) and helps you manage them and their associated options with a simple and powerful interface.Prism Launcheris a popular fork of MultiMC with improved Linux support.
- ATLauncher- Allows you to easily download mods without having to download them from CurseForge and transferring those mods to your Minecraft folder.
- GDLauncher

## Modded clients and modpacks
There are also clients that improve performance and are mainly intended for PVP. Examples include:

- Lunar Client - Arguably the most popular and reliable client in Minecraft, Lunar can boost your performance and doesn't have a laggy GUI, though in modern versions it doesn't boost as much FPS as its main rival, Feather.
- Badlion
- Labymod

However, many PVP clients have been criticized for poor privacy practices, stealing mods, and selling capes (which is against the game's EULA). Using a selection of performance-optimizing mods such as Sodium and Lithium usually gives better frame rates than PVP clients.

There are many modpacks available that include a selection of performance mods, such as:

- Fabulously Optimized- includes performance mods as well as other quality of life mods and mods that provide parity with OptiFine (including Iris for shader support).
- Simply Optimized- contains only performance mods with no quality of life or visual enhancement mods, meaning frame rates will usually be slightly higher.
- Adrenaline- performance modpack with no quality-of life mods.
- Additive- modpack based on Adrenaline, which additionally includes quality of life mods aiming for OptiFine parity.

## Notes


| Introductory      |                                                                                                                                                                           |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Basics            | Menu screen<br/>Game terms<br/>                                                                                                                                           |
| Newcomer survival | The first day/beginner's guide<br/>The second day<br/>The third day<br/>Hunger management<br/>Things not to do<br/>Simple tips and tricks<br/>Your first ten minutes<br/> |
| Shelters          | Best biomes for homes<br/>Best building materials<br/>Building and construction<br/>Navigation<br/>Shelters<br/>Shelter types<br/>                                        |

| General                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| General                    | Achievement guide<br/>Advancement guide<br/>Best enchantments guide<br/>Breaking a fall<br/>Breaking bedrock<br/>Combat<br/>Complete main adventure<br/>Creating a village<br/>Downgrading<br/>Dual wielding<br/>End survival<br/>Exploring caverns<br/>Gathering resources on peaceful difficulty<br/>Getting food quickly<br/>Headless pistons<br/>Hitboxes<br/>Horses<br/>Indestructible end crystals<br/>Mapping<br/>Measuring distance<br/>Minecraft in education<br/>Mining Diamonds Fossils Ancient Debris<br/>Diamonds<br/>Fossils<br/>Ancient Debris<br/>Nether hub<br/>Nether portals<br/>Nether survival<br/>Organization<br/>Pillar jumping<br/>Playing with a controller<br/>PvP PvP bases<br/>PvP bases<br/>Spawn-proofing<br/>Summoning jockeys<br/>The Void<br/>Time-saving tips<br/>Thunderstorm survival<br/>Units of measure<br/>Village mechanics Trading<br/>Trading<br/>X-ray glitches<br/> |
| Enchanting<br/>andsmelting | Enchanting mechanics<br/>Anvil mechanics<br/>Automatic smelting<br/>Manual smelting<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

| Challenges                |                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| General                   | Acquiring a conduit<br/>Curing a zombie villager<br/>Defeating temples<br/>Defeating a village raid<br/>Defeating a Nether fortress<br/>Defeating a bastion remnant<br/>Defeating a monster room<br/>Defeating a pillager outpost<br/>Defeating a woodland mansion<br/>Defeating a monument<br/>Defeating an End city<br/>Defeating the Ender dragon<br/>Defeating the Wither<br/>Exploring an ancient city<br/>Obtaining every music disc<br/> |
| Non-standard<br/>survival | Adventure survival<br/>Half hearted hardcore<br/>Hardcore mode<br/>Surviving in a single area indefinitely<br/>Infinite desert survival<br/>Island survival<br/>Manhunt<br/>Mob switch<br/>Nomadic experience<br/>Skywars survival<br/>Superflat survival<br/>Flat survival<br/>Ultra hardcore survival<br/>                                                                                                                                    |
| Challenge maps            | Beating a challenge map<br/>Creating a challenge map<br/>                                                                                                                                                                                                                                                                                                                                                                                       |

| Constructions |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Constructions | Adding beauty to constructions<br/>Airlock<br/>Architectural terms<br/>Building a cruise ship<br/>Building a metropolis<br/>Building a rollercoaster<br/>Building safe homes<br/>Building water features<br/>Color palette<br/>Creating shapes<br/>Defense<br/>Desert shelter<br/>Elevators<br/>Endless circling pool<br/>Furniture<br/>Glazed terracotta patterns<br/>Making nice floors<br/>Pixel art<br/>Ranches<br/>Roof types Curved roofs Roof construction guidelines Roof decorations<br/>Curved roofs<br/>Roof construction guidelines<br/>Roof decorations<br/>Secret door<br/>Settlement guide<br/>Underwater home<br/>Walls and buttresses<br/>Water gate<br/>Water-powered boat transportation<br/> |
| Blockbreaking | Blast chamber<br/>Igniting TNT underwater<br/>Wither cage<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

| Farming        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Blocksanditems | Amethyst<br/>Armor<br/>Azalea<br/>Bamboo<br/>Basalt<br/>Bedrock<br/>Blaze rod<br/>Bone meal<br/>Cactus<br/>Chorus fruit<br/>Clay and mud<br/>Cobblestone<br/>Cocoa bean<br/>Copper<br/>Crops (Beetroot, Carrot, Potato, Wheat)<br/>Dirt<br/>Dragon's Breath<br/>Dripstone<br/>Egg<br/>Fern<br/>Fish<br/>Flower<br/>Froglight<br/>Glow berries<br/>Glow ink sac<br/>Glow lichen<br/>Goat horn<br/>Gold<br/>Hanging roots<br/>Honey<br/>Ice<br/>Iron<br/>Kelp<br/>Lava<br/>Meat<br/>Moss block<br/>Mushroom<br/>Music disc<br/>Nautilus shell<br/>Nether growth<br/>Nether vine<br/>Nether wart<br/>Obsidian<br/>Powder snow<br/>Pumpkin, Melon<br/>Rooted dirt<br/>Sculk growths<br/>Scute<br/>Seagrass<br/>Sea pickle<br/>Snow<br/>Soul soil<br/>Sugar cane<br/>Sweet berries<br/>Tree<br/>Trident<br/>Vine<br/>Villager trading hall<br/>Wither rose<br/>Wool<br/>Duplication<br/> |
| Mobs           | Mob farming<br/>Mob grinding<br/>Monster spawner traps<br/>Allay<br/>Animals<br/>Axolotl<br/>Blaze<br/>Cat<br/>Cave spider<br/>Creeper<br/>Drowned<br/>Ender dragon<br/>Enderman<br/>Frog<br/>Goat<br/>Guardian<br/>Hoglin<br/>Iron golem<br/>Magma cube<br/>Phantom<br/>Piglin bartering farm<br/>Raid<br/>Shulker<br/>Slime<br/>Squid<br/>Turtle<br/>Villager<br/>Wandering trader<br/>Warden<br/>Witch<br/>Wither<br/>Wither skeleton<br/>Zombie<br/>Zombie villager<br/>Zombified piglin<br/>                                                                                                                                                                                                                                                                                                                                                                                   |

| Mechanisms            |                                                                                                                                                                                                                                                                                                                                                                  |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Basicredstone         | Automatic respawn anchor recharger<br/>Basic logic gates<br/>Combination locks<br/>Command block<br/>Flying machines<br/>Hopper<br/>Item sorting<br/>Item transportation<br/>Mechanisms<br/>Observer stabilizer<br/>Randomizers<br/>Redstone music<br/>Redstone tips<br/>Rube Goldberg machine<br/>Shulker box storage<br/>Villager trading hall*Water tram<br/> |
| Detectors             | Block update detector<br/>Comparator update detector<br/>Daylight detector<br/>                                                                                                                                                                                                                                                                                  |
| Minecarts             | Train station<br/>Minecarts Storage Storage system<br/>Storage<br/>Storage system<br/>                                                                                                                                                                                                                                                                           |
| Traps                 | Snow golems<br/>TNT cannons<br/>Trapdoor uses<br/>Trap design<br/>Traps<br/>                                                                                                                                                                                                                                                                                     |
| Pistons               | Piston uses<br/>Piston circuits<br/>Quasi-connectivity<br/>Zero-ticking<br/>Instant repeaters<br/>                                                                                                                                                                                                                                                               |
| Advanced<br/>redstone | Advanced redstone circuits<br/>Arithmetic logic<br/>Calculator<br/>Command stats<br/>Hourly clock<br/>Morse code<br/>Printer<br/>Redstone computers<br/>Redstone telegraph<br/>                                                                                                                                                                                  |

| Servers      |                                                                                                                                                                                                                                                                      |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| General      | Playing on servers<br/>Multiplayer Survival<br/>Spawn jail<br/>Griefing prevention<br/>Joining a LAN world with alternate accounts<br/>                                                                                                                              |
| Server setup | Setting up a server<br/>Server startup script<br/>FreeBSD startup script<br/>OpenBSD startup script<br/>Ubuntu startup script<br/>Setting up a Hamachi server<br/>Setting up a Minecraft Forge server<br/>Setting up a Spigot server<br/>Ramdisk enabled server<br/> |

| Technical                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Technical                   | Improving frame rate<br/>Minecraft help FAQ (IRC channel)<br/>Running the data generator<br/>Update Java<br/>                                                                                                                                                                                                                                                                                                                                            |
| Maps                        | Custom maps<br/>Map downloads<br/>Command NBT tags<br/>Falling blocks<br/>Updating old terrain using MCEdit<br/>                                                                                                                                                                                                                                                                                                                                         |
| Resource packs              | Creating a resource pack<br/>Loading a resource pack<br/>Sound directory<br/>                                                                                                                                                                                                                                                                                                                                                                            |
| Data packs                  | Creating a data pack<br/>Installing a data pack<br/>Custom world generation<br/>                                                                                                                                                                                                                                                                                                                                                                         |
| Creating<br/>Minecraftmedia | Creating videos<br/>Livestreaming<br/>                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Game installation           | Installing snapshots<br/>Installing Minecraft Preview and beta versions<br/>How to get a crash report<br/>Installing Forge mods<br/>Custom Minecraft directory<br/>Playing and saving Minecraft on a thumb drive<br/>Playing and saving Minecraft on a thumb drive with the old launcher<br/>Recover corrupted saved world data<br/>Run Minecraft through Google Drive<br/>Save game data to Dropbox (world data only)<br/>Saved data Dropbox guide<br/> |

| Outdated |                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Outdated | Building micro shelters<br/>Custom texture packs<br/>Door-based iron golem farming<br/>End of light mob farms<br/>Far Lands<br/>How to get a crash report<br/>Installing mods<br/>Man-made lake<br/>Managing slimes in superflat mode<br/>Minecart booster<br/>Potion farming<br/>Repeater reboot system<br/>Survival with no enabled data packs<br/>Update LWJGL<br/>Update Minecraft<br/>Village chaining<br/>Water ladder<br/> |

