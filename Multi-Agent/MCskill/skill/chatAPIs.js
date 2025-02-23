// get Minecraft in-game time
function getMinecraftTime(bot) {
    const ticks = bot.time.time; // Get the current day time in ticks
    const day = Math.floor(ticks / 24000) + 1; // Calculate the current day (starting from 1)
    const tick = ticks % 24000; // Calculate the tick within the day
    let timeOfDay;
    if (tick >= 0 && tick < 4800) {
        timeOfDay = "Morning";
    } else if (tick >= 4800 && tick < 9600) {
        timeOfDay = "Noon";
    } else if (tick >= 9600 && tick < 14400) {
        timeOfDay = "Afternoon";
    } else if (tick >= 14400 && tick < 19200) {
        timeOfDay = "Evening";
    } else {
        timeOfDay = "Night";
    }
    return `Day ${day} - ${timeOfDay}`;
}

// async implementation of fs.existsSync
async function fileExists(filePath) {
    try {
        await fs.access(filePath);
        return true;
    } catch {
        return false;
    }
}

// chat a message and write to chat log
async function chatMessage(bot, message, team_name='A') {
    // return if no need to send message
    if (message === "None") return;

    bot.chat(message);

    const cur_dir = path.dirname(path.resolve(__filename));
    const chatLogPath = path.join(cur_dir, `../../../memory/${team_name}/chat_log.json`);

    try {
        // Get Minecraft game time
        const gameTime = getMinecraftTime(bot);

        // Format the message as "username: message"
        const chatEntry = `${bot.username}: ${message}`;

        // Log the message to the chat log file by calling writeChatEntry
        await writeChatEntry(chatLogPath, gameTime, chatEntry);
    } catch (error) {
        console.error('Error in logging chat message: ' + error.message);
        // Optionally, you can also notify the user in-game
        bot.chat('Error logging chat message.');
    }
}

// Helper function to write chat entry to the log file
async function writeChatEntry(filePath, gameTime, chatEntry) {
    const lockFilePath = filePath + '.lock'; // Path for the lock file

    try {
        // Wait for the lock file to be released (if it exists)
        while (await fileExists(lockFilePath)) {
            await new Promise(resolve => setTimeout(resolve, 100)); // Polling every 100ms
        }

        // Create the lock file
        await fs.writeFile(lockFilePath, '');

        // Read the current chat log
        let chatLog = {};
        if (await fileExists(filePath)) {
            const data = await fs.readFile(filePath, 'utf8');
            chatLog = JSON.parse(data);
        }

        // Check if the current game time already exists as a key
        if (!chatLog[gameTime]) {
            // If not, create a new time entry with an empty array
            chatLog[gameTime] = [];
        }

        // Add the new message to the list for the current time
        chatLog[gameTime].push(chatEntry);

        // Write the updated chat log back to the file
        await fs.writeFile(filePath, JSON.stringify(chatLog, null, 2));

    } catch (error) {
        console.error('Error reading or writing chat log file: ' + error.message);
    } finally {
        // Delete the lock file
        if (await fileExists(lockFilePath)) {
            await fs.unlink(lockFilePath);
        }
    }
}

// whisper to a single player
async function whisperMessage(bot, target_player, message) {
    bot.whisper(target_player, message)
}

// listen and return a chat or whisper
async function listenChat(bot, human_player_name) {
    return new Promise((resolve) => {
        const onChat = (username, message) => {
            if (username === human_player_name) {
                clearListening();
                bot.chat(`Received chat message from ${human_player_name}: ${message}`);
                resolve(message);
            }
        };

        const onWhisper = (username, message) => {
            if (username === human_player_name) {
                clearListening();
                bot.chat(`Received whisper from ${human_player_name}: ${message}`);
                resolve(message);
            }
        };

        bot.on('chat', onChat); // Listen for chat messages
        bot.on('whisper', onWhisper); // Listen for whisper messages

        // Send a message every 10 seconds to indicate that the bot is listening
        const intervalId = setInterval(() => {
            bot.chat(`Listening for chat or msg from ${human_player_name}...`);
        }, 10000);

        // Clear listeners and interval when a message is received
        function clearListening() {
            bot.removeListener('chat', onChat);
            bot.removeListener('whisper', onWhisper);
            clearInterval(intervalId);
        }
    });
}

// listen all chats in one game and write to chat log
async function chatLog(bot) {
    const cur_dir = path.dirname(path.resolve(__filename));
    const chatLogPath = path.join(cur_dir, '../../../memory/chat_log.json');

    // Initialize or clear the chat log file
    try {
        await fs.writeFile(chatLogPath, JSON.stringify([]));
        console.log('Chat log file initialized.');
    } catch (error) {
        console.error('Error initializing chat log file: ' + error.message);
    }

    // Listen for chat messages
    bot.on('chat', async (username, message) => {
        // Ignore messages from the bot itself
        if (username !== bot.username) {
            try {
                // Get Minecraft game time
                const gameTime = getMinecraftTime(bot);

                // Format the message as an object
                const chatEntry = {
                    username: username,
                    message: message,
                    timestamp: gameTime, // Use game time instead of real time
                };

                // Log the message to the chat log file
                await writeChatEntry(chatLogPath, gameTime, JSON.stringify(chatEntry));

                console.log(`Logged chat from ${username}: ${message}`);
            } catch (error) {
                console.error('Error in logging chat message: ' + error.message);
            }
        }
    });

    console.log('Chat listener started.');

    // Keep the process running
    bot.once('end', () => {
        console.log('Bot disconnected. Stopping chat listener.');
        process.exit(); // Optional: Remove this if you want to keep the process running
    });
}

// listen and log chat or whisper from a specific human player
function listenHumanPlayer(bot, human_player_name, team_name) {
    const cur_dir = path.dirname(path.resolve(__filename));
    const chatLogPath = path.join(cur_dir, `../../../memory/${team_name}/chat_log.json`);
    // Set to spectator mode
    setGamemode(bot, 'spectator');
    // Define the handler for chat and whisper events
    const handleChat = async (username, message) => {
        if (username === human_player_name) {
            try {
                // Get Minecraft game time
                const gameTime = getMinecraftTime(bot);

                // Format the message as "username: message"
                const chatEntry = `${username}: ${message}`;

                // Log the message to the chat log file
                await writeChatEntry(chatLogPath, gameTime, chatEntry);
                console.log(`Logged chat from ${human_player_name}: ${message}`);
            } catch (error) {
                console.error('Error in logging chat message: ' + error.message);
            }
        }
    };

    // Attach the handlers to the bot's chat and whisper events
    bot.on('chat', handleChat);
    bot.on('whisper', handleChat);

    // Optionally, you can return a function to remove these listeners later
    return () => {
        bot.removeListener('chat', handleChat);
        bot.removeListener('whisper', handleChat);
    };
}