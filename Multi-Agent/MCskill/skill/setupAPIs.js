async function initializeCombatScene(bot, team_name, combat_scene, username_list) {
    // Variables to store interval IDs
    let crystalInterval;
    let bossHealthInterval;
    let playerCheckInterval;

    // Counter to track consecutive offline states
    let consecutiveOfflineCount = 0;

    let success = false; // Variable to track success

    // Record the start time
    const start_time = Date.now();

    try {
        bot.chat(`/gamemode spectator`);
        bot.chat(`/scoreboard objectives remove bossHealth`); // Remove the scoreboard if it already exists
        bot.chat(`/scoreboard objectives add bossHealth dummy "Boss Health"`); // Create a scoreboard to record boss health
        bot.chat(`/scoreboard objectives setdisplay sidebar bossHealth`); // Display the scoreboard
        bot.chat(`/scoreboard players reset * bossHealth`); // Clear the scoreboard
        bot.chat(`/kill @e[type=item]`); // Clear all items in the world
        bot.chat(`/execute in overworld run kill @e[tag=boss]`);
        bot.chat(`/execute in the_nether run kill @e[tag=boss]`);
        bot.chat(`/execute in the_end run kill @e[tag=boss]`); // Make sure only one boss is present

        if (combat_scene == 'End') {
            let lastCrystalCount = 0; // Variable to track last crystal count
            const end_crystal_pos = [
                new Vec3(33, 101, -25), new Vec3(12, 92, -40), new Vec3(-13, 104, -40), new Vec3(-34, 86, -25),
                new Vec3(-42, 83, -1), new Vec3(-34, 80, 24), new Vec3(-13, 77, 39), new Vec3(12, 89, 39),
                new Vec3(33, 98, 24), new Vec3(42, 95, 0)
            ];

            bot.chat(`/execute in the_end run tp @s 0 70 0`); // Teleport to the End
            bot.chat(`/execute in the_end run kill @e[type=minecraft:ender_dragon]`); // Make sure there are no redundant ender dragons summoned
            bot.chat(`/execute in the_end run summon ender_dragon 0 70 0 {Tags:["boss"]}`); // Summon ender dragon
            await bot.waitForTicks(20);  // Wait for a few ticks to ensure entities are loaded

            bot.chat(`/execute in the_end run kill @e[type=minecraft:end_crystal]`);
            for (const pos of end_crystal_pos) {
                bot.chat(`/execute in the_end run summon end_crystal ${pos.x} ${pos.y} ${pos.z}`);
                await bot.waitForTicks(5);
            }

            let i = 0;
            // Listen for changes in end crystal count
            crystalInterval = setInterval(() => {
                let crystal_count = 0;
                for (const [id, entity] of Object.entries(bot.entities)) {
                    if (entity.name === 'end_crystal') {
                        crystal_count++;
                    }
                }

                // Only call chatMessage if the crystal count has changed
                if (crystal_count !== lastCrystalCount) {
                    console.log(`Number of End Crystals remaining: ${crystal_count}`);
                    chatMessage(bot, `Number of End Crystals Remaining: ${crystal_count}`, team_name);
                    lastCrystalCount = crystal_count; // Update last crystal count
                }
                if (crystal_count == 0) {
                    i = i + 1;
                    if (i == 10) {
                        console.log('All End Crystals have been destroyed.');
                        chatMessage(bot, 'All End Crystals have been destroyed.', team_name);
                        i = 0;
                    }
                }
            }, 1000); // Check every second

        } else if (combat_scene == 'Nether') {
            bot.chat('/gamerule mobGriefing false'); // Disable mob griefing
            bot.chat(`/execute in the_nether run kill @e[type=minecraft:wither]`); // Make sure there are no redundant wither summoned
            bot.chat(`/execute in the_nether run summon wither 105 110 -40 {Tags:["boss"]}`); // Summon the wither
            bot.chat(`/execute in the_nether run tp 105 110 -40`);
        } else if (combat_scene == 'Ocean') {
            bot.chat(`/execute in overworld run kill @e[type=minecraft:elder_guardian]`); // Make sure there are no redundant elder_guardian summoned
            bot.chat(`/execute in overworld run kill @e[type=guardian]`); // Make sure there are no redundant guardian summoned
            const pos = new Vec3(0, 129, 0);
            bot.chat(`/execute in overworld run summon elder_guardian ${pos.x} ${pos.y} ${pos.z} {Tags:["boss"]}`); // Summon the elder guardian
            bot.chat(`/execute in overworld run summon guardian ${pos.x + 10} ${pos.y} ${pos.z}`);
            bot.chat(`/execute in overworld run summon guardian ${pos.x - 10} ${pos.y} ${pos.z}`);
            bot.chat(`/execute in overworld run summon guardian ${pos.x} ${pos.y} ${pos.z + 10}`);
            bot.chat(`/execute in overworld run summon guardian ${pos.x} ${pos.y} ${pos.z - 10}`);
            bot.chat(`/execute in overworld run tp 0 129 0`);
        }

        // Function to check boss health
        const checkBossHealth = () => {
            const scoreboard = bot.scoreboard.sidebar;

            // Debugging: Check if the scoreboard is found
            if (!scoreboard) {
                console.log('Scoreboard not found.');
                clearInterval(bossHealthInterval);
                return;
            } else if (!scoreboard.items || scoreboard.items.length === 0) {
                console.log('No items in the scoreboard. The boss has been beaten.');
                chatMessage(bot, 'Success', team_name); // Notify success
                success = true;
                bot.chat('/scoreboard objectives remove bossHealth'); // Remove the scoreboard
            } else {
                console.log('Scoreboard items:', scoreboard.items);
                // Look for the boss health entry in the scoreboard
                const boss_item = scoreboard.items[0];
                let current_health = boss_item.value;
                console.log(`Boss Health: ${current_health}`);
                chatMessage(bot, `Boss Health: ${current_health}`, team_name); // Update boss health
            }
        };

        // Start polling boss health every 10 seconds
        bossHealthInterval = setInterval(checkBossHealth, 10000);

        // Function to check if all players are offline
        const checkPlayersOffline = async () => {
            const allPlayersOffline = username_list.every(username => {
                const player = bot.players[username];
                return !player || !player.entity; // Player is offline if not in bot.players or has no entity
            });

            if (allPlayersOffline) {
                consecutiveOfflineCount++;
                console.log(`All players are offline. Consecutive count: ${consecutiveOfflineCount}`);
            } else {
                consecutiveOfflineCount = 0; // Reset counter if any player is online
            }

            // If all players are offline for 3 consecutive checks, exit the process
            if (consecutiveOfflineCount >= 3) {
                console.log('All players have been offline for 3 consecutive checks. Exiting...');
                clearInterval(crystalInterval);
                clearInterval(bossHealthInterval);
                clearInterval(playerCheckInterval);

                // Calculate total time
                const end_time = Date.now();
                const total_time = (end_time - start_time) / 1000; // Convert to seconds

                console.log('All memory files updated. Exiting...');

                const curDir = path.dirname(path.resolve(__filename));
                const memoryDir = path.join(curDir, `../../../memory/${team_name}`);
                const { total_health, lowest_boss_health } = await calculateHealthStats(memoryDir, username_list);

                const results = {
                    "combat_scene": combat_scene,
                    "agent_count": username_list.length,
                    "success": success,
                    "timestamp": new Date().toISOString(),
                    "total_health": total_health,
                    "lowest_boss_health": lowest_boss_health,
                    "total_time": total_time // Add total_time to results
                };

                await logCombatResults(results);
                console.log('Combat results logged. Exiting...');
                await process.exit(0); // Exit the process
            }
        };

        // Start checking player status every 5 seconds
        playerCheckInterval = setInterval(checkPlayersOffline, 5000);

    } catch (error) {
        console.error('Error during combat scene initialization:', error);
    }
}

async function teleportToCombatScene(bot, combat_scene) {
    // This function is used to teleport players to the combat area
    if (combat_scene == 'End') {
        const random_x = Math.floor(Math.random() * 40) - 20;
        const random_z = Math.floor(Math.random() * 40) - 20;
        bot.chat(`/execute in the_end run tp @s ${random_x} 70 ${random_z}`); // Teleport to the End
    } else if (combat_scene == 'Nether') {
        const random_x = Math.floor(Math.random() * 10) + 100;
        const random_z = Math.floor(Math.random() * 10) - 45;
        bot.chat(`/execute in the_nether run tp ${random_x} 110 ${random_z}`); // Teleport to the Nether
    } else if (combat_scene == 'Ocean') {
        const random_x = Math.floor(Math.random() * 4) - 2;
        const random_z = Math.floor(Math.random() * 4) - 2;
        bot.chat(`/execute in overworld run tp @s ${random_x} 129 ${random_z}`); // Teleport to the pre-defined scene
    }
    return;
}

function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function calculateHealthStats(memoryDir, username_list) {
    const chatLogPath = path.join(memoryDir, 'chat_log.json');
    let chatLog = {};

    try {
        const chatLogData = await fs.readFile(chatLogPath, 'utf-8');
        chatLog = JSON.parse(chatLogData);
    } catch (err) {
        console.error(`Failed to parse chat_log.json: ${err.message}`);
    }

    let lowestBossHealth = Infinity;
    for (const key in chatLog) {
        if (Array.isArray(chatLog[key])) {
            chatLog[key].forEach(entry => {
                if (entry.startsWith('SystemInfo: Boss Health:')) {
                    const health = parseInt(entry.split(': ')[2], 10);
                    if (health < lowestBossHealth) {
                        lowestBossHealth = health;
                    }
                }
            });
        }
    }

    let totalHealth = 0;
    for (const username of username_list) {
        const userFilePath = path.join(memoryDir, 'obs', `${username}.json`);
        let user = { health: 0 };

        try {
            const userData = await fs.readFile(userFilePath, 'utf-8');
            user = JSON.parse(userData);
        } catch (err) {
            console.error(`Failed to parse ${username}.json: ${err.message}`);
        }

        totalHealth += user.health || 0;
    }

    return {
        total_health: totalHealth,
        lowest_boss_health: lowestBossHealth === Infinity ? null : lowestBossHealth
    };
}

async function logCombatResults(results) {
    const curDir = path.dirname(path.resolve(__filename));
    const resultsFile = path.join(curDir, `../../../results/combat_results.json`);
    try {
        let existingResults = [];
        try {
            const data = await fs.readFile(resultsFile, 'utf-8');
            existingResults = JSON.parse(data);
        } catch (err) {
            if (err.code !== 'ENOENT') {
                throw err;
            }
        }

        existingResults.push(results);

        await fs.writeFile(resultsFile, JSON.stringify(existingResults, null, 2), 'utf-8');
        console.log('Results successfully logged to combat_results.json');
    } catch (err) {
        console.error('Failed to log combat results:', err);
    }
}

async function initializeResourceScene(bot, team_name, item_dict, username_list) {
    // Variables to store interval IDs
    let playerCheckInterval;
    // Counter to track consecutive offline states
    let consecutiveOfflineCount = 0;
    // Record the start time
    const start_time = Date.now();
    try {
        bot.chat(`/difficulty peaceful`);
        // Function to check if all players are offline
        const checkPlayersOffline = async () => {
            const allPlayersOffline = username_list.every(username => {
                const player = bot.players[username];
                return !player || !player.entity; // Player is offline if not in bot.players or has no entity
            });
            if (allPlayersOffline) {
                consecutiveOfflineCount++;
                console.log(`All players are offline. Consecutive count: ${consecutiveOfflineCount}`);
            } else {
                consecutiveOfflineCount = 0; // Reset counter if any player is online
            }
            // If all players are offline for 3 consecutive checks, exit the process
            if (consecutiveOfflineCount >= 3) {
                console.log('All players have been offline for 3 consecutive checks. Exiting...');
                clearInterval(playerCheckInterval);
                // Calculate total time
                const end_time = Date.now();
                const total_time = (end_time - start_time) / 1000; // Convert to seconds
                const results = {
                    "item_dict": item_dict,
                    "agent_count": username_list.length,
                    "timestamp": new Date().toISOString(),
                    "total_time": total_time // Add total_time to results
                };
                await logResourceResults(results);
                console.log('Resource results logged. Exiting...');
                await process.exit(0); // Exit the process
            }
        };
        // Start checking player status every 5 seconds
        playerCheckInterval = setInterval(checkPlayersOffline, 5000);
    } catch (error) {
        console.error('Error during resource scene initialization:', error);
    }
}

async function logResourceResults(results) {
    const curDir = path.dirname(path.resolve(__filename));
    const resultsFile = path.join(curDir, `../../../results/resource_results.json`);
    try {
        let existingResults = [];
        try {
            const data = await fs.readFile(resultsFile, 'utf-8');
            existingResults = JSON.parse(data);
        } catch (err) {
            if (err.code !== 'ENOENT') {
                throw err;
            }
        }

        existingResults.push(results);

        await fs.writeFile(resultsFile, JSON.stringify(existingResults, null, 2), 'utf-8');
        console.log('Results successfully logged to resource_results.json');
    } catch (err) {
        console.error('Failed to log resource results:', err);
    }
}

async function teleportToPvpScene(bot) {
    // This function is used to teleport players to the PvP area
    const random_x = Math.floor(Math.random() * 30) - 15;
    const random_z = Math.floor(Math.random() * 30) - 15;
    bot.chat(`/execute in overworld run tp @s ${random_x} 71 ${random_z}`); // Teleport to the PvP area
    return;
}

async function initializePVPScene(bot, username_list) {
    bot.chat(`/gamemode spectator`);
    bot.chat(`/scoreboard objectives setdisplay sidebar Health`);

    const teamA = username_list.slice(0, username_list.length / 2);
    const teamB = username_list.slice(username_list.length / 2);

    let success = false; // Variable to track success

    // Function to check if a team is defeated
    const checkTeamDefeated = () => {
        let teamAHealth = 0;
        let teamBHealth = 0;

        // Get health for team A
        teamA.forEach(username => {
            const player = bot.players[username];
            if (player.scoreboard) {
                const healthScore = player.scoreboard.items.find(item => item.name === 'Health');
                if (healthScore) {
                    teamAHealth += healthScore.value;
                } else {
                    teamAHealth += 0; // Default to 0 if health score not found
                }
            } else {
                teamAHealth += 0; // Default to 0 if scoreboard not found
            }
        });

        // Get health for team B
        teamB.forEach(username => {
            const player = bot.players[username];
            if (player && player.entity) { // Check if player is online
                if (player.scoreboard) {
                    const healthScore = player.scoreboard.items.find(item => item.name === 'Health');
                    if (healthScore) {
                        teamBHealth += healthScore.value;
                    } else {
                        teamBHealth += 0; // Default to 0 if health score not found
                    }
                } else {
                    teamBHealth += 0; // Default to 0 if scoreboard not found
                }
            } else {
                teamBHealth += 0; // Player is offline, treat health as 0
            }
        });

        console.log(`Team A Health: ${teamAHealth}`);
        console.log(`Team B Health: ${teamBHealth}`);

        if (teamAHealth <= 0) {
            // Team B wins
            success = true;
            const results = {
                "teamA_count": teamA.length,
                "teamB_count": teamB.length,
                "winning_team": 'B',
                "teamA_health": 0,
                "teamB_health": teamBHealth,
                "timestamp": new Date().toISOString()
            };
            logPVPResults(results);
            return true;
        } else if (teamBHealth <= 0) {
            // Team A wins
            success = true;
            const results = {
                "teamA_count": teamA.length,
                "teamB_count": teamB.length,
                "winning_team": 'A',
                "teamA_health": teamAHealth,
                "teamB_health": 0,
                "timestamp": new Date().toISOString()
            };
            logPVPResults(results);
            return true;
        }

        return false; // No team is defeated yet
    };

    // Polling function to check if a team is defeated
    const healthInterval = setInterval(() => {
        if (checkTeamDefeated()) {
            clearInterval(healthInterval); // Stop polling once a team is defeated
        }
    }, 1000); // Check every second
}

// Log PVP results to a JSON file
async function logPVPResults(results) {
    const curDir = path.dirname(path.resolve(__filename));
    const resultsFile = path.join(curDir, `../../../results/pvp_results.json`);
    try {
        let existingResults = [];
        try {
            const data = await fs.readFile(resultsFile, 'utf-8');
            existingResults = JSON.parse(data);
        } catch (err) {
            if (err.code !== 'ENOENT') {
                throw err;
            }
        }

        existingResults.push(results);

        await fs.writeFile(resultsFile, JSON.stringify(existingResults, null, 2), 'utf-8');
        console.log('PVP results successfully logged.');
    } catch (err) {
        console.error('Failed to log PVP results:', err);
    }
}