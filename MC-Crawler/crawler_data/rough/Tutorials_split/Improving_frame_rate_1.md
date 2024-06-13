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

