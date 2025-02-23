async function combatWithEntity(bot, mob_name, weapon = "sword", loop = false, timeout = 300) {
    // return if mob_name is not string
    if (typeof mob_name !== "string") {
        throw new Error(`mob_name for combatWithEntity must be a string`);
    }
    // return if weapon is not string
    if (typeof weapon !== "string") {
        throw new Error(`weapon for combatWithEntity must be a string`);
    }
    // return if timeout is not number
    if (typeof timeout !== "number") {
        throw new Error(`timeout for combatWithEntity must be a number`);
    }

    // Equip armor at the start of the combat
    await equipBestArmor(bot);

    // Equip weapon
    if (weapon === "sword") {
        await equipBestToolOrArmor(bot, "sword");
    } else {
        const weapon_item = bot.inventory.findInventoryItem(mcData.itemsByName[weapon].id);
        if (weapon_item) {
            await bot.equip(weapon_item, "hand");
        } else {
            bot.chat(`No ${weapon} found in inventory.`);
        }
    }

    const weaponsForShooting = [
        "bow", "crossbow", "snowball", "ender_pearl", "egg",
        "splash_potion", "trident"
    ];
    const mainHandItem = bot.inventory.slots[bot.getEquipmentDestSlot("hand")];

    let entity;
    let _combatFailCount = 0; // Initialize fail count

    await setGamemode(bot, 'survival'); // Ensure combat test in survival mode

    do {
        entity = bot.nearestEntity((entity) =>
            entity.name === mob_name &&
            entity.position.distanceTo(bot.entity.position) < 128
        );

        if (!entity) {
            bot.chat(`No ${mob_name} nearby, please explore first`);
            _combatFailCount++;
            if (_combatFailCount > 10) {
                throw new Error(`combatWithEntity failed too many times, make sure you explore before calling combatWithEntity`);
            }
            break;
        }

        let droppedItem;

        while (entity) {
            if (mainHandItem && weaponsForShooting.includes(mainHandItem.name)) {
                bot.hawkEye.autoAttack(entity, mainHandItem.name);
                droppedItem = await waitForMobShot(bot, entity, timeout);
            } else {
                await bot.pvp.attack(entity);
                droppedItem = await waitForMobRemoved(bot, entity, timeout);
            }

            if (droppedItem) {
                await bot.collectBlock.collect(droppedItem, { ignoreNoPath: true });
            }

            // Check if the mob is still alive
            entity = bot.nearestEntity((e) =>
                e.name === mob_name &&
                e.position.distanceTo(bot.entity.position) < 48
            );
        }

        bot.save(`${mob_name}_killed`);
    } while (loop); // Repeat if loop is true
}

async function combatWithPlayer(bot, player_name, weapon = "sword") {
    // return if player_name is not string
    if (typeof player_name !== "string") {
        throw new Error(`player_name for combatWithEntity must be a string`);
    }
    // return if weapon is not string
    if (typeof weapon !== "string") {
        throw new Error(`weapon for combatWithEntity must be a string`);
    }

    // Equip armor at the start of the combat
    await equipBestArmor(bot);
    // Equip weapon
    if (weapon === "sword") {
        await equipBestToolOrArmor(bot, "sword");
    } else {
        const weapon_item = bot.inventory.findInventoryItem(mcData.itemsByName[weapon].id);
        if (weapon_item) {
            await bot.equip(weapon_item, "hand");
        } else {
            bot.chat(`No ${weapon} found in inventory.`);
        }
    }

    const weaponsForShooting = [
        "bow", "crossbow", "snowball", "ender_pearl", "egg",
        "splash_potion", "trident"
    ];
    const mainHandItem = bot.inventory.slots[bot.getEquipmentDestSlot("hand")];

    let entity;

    await setGamemode(bot, 'survival'); // Ensure combat test in survival mode

    entity = bot.nearestEntity((entity) =>
        entity.name === 'player' &&
        entity.username === player_name &&
        entity.position.distanceTo(bot.entity.position) < 128
    );

    if (!entity) {
        bot.chat(`${player_name} is not nearby, please find the player first.`);
        return;
    }

    while (entity) {
        if (mainHandItem && weaponsForShooting.includes(mainHandItem.name)) {
            bot.hawkEye.autoAttack(entity, mainHandItem.name);
            await waitForMobShot(bot, entity);
        } else {
            await bot.pvp.attack(entity);
            await waitForMobRemoved(bot, entity);
        }

        // Check if the mob is still alive
        entity = bot.nearestEntity((e) =>
            e.name === 'player' &&
            e.username === player_name &&
            e.position.distanceTo(bot.entity.position) < 128
        );
    }

    return;
}

function waitForMobRemoved(bot, entity, timeout = 300) {
    return new Promise((resolve, reject) => {
        let success = false;
        let droppedItem = null;
        // Set up timeout
        const timeoutId = setTimeout(() => {
            success = false;
            bot.pvp.stop();
        }, timeout * 1000);

        // Function to handle entityRemoved event
        function onEntityGone(e) {
            if (e === entity) {
                success = true;
                clearTimeout(timeoutId);
                bot.chat(`Killed ${entity.name}!`);
                bot.pvp.stop();
            }
        }

        function onItemDrop(item) {
            if (entity.position.distanceTo(item.position) <= 1) {
                droppedItem = item;
            }
        }

        function onStoppedAttacking() {
            clearTimeout(timeoutId);
            bot.removeListener("entityGone", onEntityGone);
            bot.removeListener("stoppedAttacking", onStoppedAttacking);
            bot.removeListener("itemDrop", onItemDrop);
            if (!success) reject(new Error(`Failed to kill ${entity.name}.`));
            else resolve(droppedItem);
        }

        // Listen for entityRemoved event
        bot.on("entityGone", onEntityGone);
        bot.on("stoppedAttacking", onStoppedAttacking);
        bot.on("itemDrop", onItemDrop);
    });
}


function waitForMobShot(bot, entity, timeout = 300) {
    return new Promise((resolve, reject) => {
        let success = false;
        let droppedItem = null;
        // Set up timeout
        const timeoutId = setTimeout(() => {
            success = false;
            bot.hawkEye.stop();
        }, timeout * 1000);

        // Function to handle entityRemoved event
        function onEntityGone(e) {
            if (e === entity) {
                success = true;
                clearTimeout(timeoutId);
                bot.chat(`Shot ${entity.name}!`);
                bot.hawkEye.stop();
            }
        }

        function onItemDrop(item) {
            if (entity.position.distanceTo(item.position) <= 1) {
                droppedItem = item;
            }
        }

        function onAutoShotStopped() {
            clearTimeout(timeoutId);
            bot.removeListener("entityGone", onEntityGone);
            bot.removeListener("auto_shot_stopped", onAutoShotStopped);
            bot.removeListener("itemDrop", onItemDrop);
            if (!success) reject(new Error(`Failed to shoot ${entity.name}.`));
            else resolve(droppedItem);
        }

        // Listen for entityRemoved event
        bot.on("entityGone", onEntityGone);
        bot.on("auto_shot_stopped", onAutoShotStopped);
        bot.on("itemDrop", onItemDrop);
    });
}

// shoot 1 pig with a bow: shoot(bot, "bow", "pig");
async function shoot(bot, weapon, target) {
    const validWeapons = [
        "bow",
        "crossbow",
        "snowball",
        "ender_pearl",
        "egg",
        "splash_potion",
        "trident",
    ];
    if (!validWeapons.includes(weapon)) {
        bot.chat(`${weapon} is not a valid weapon for shooting`);
        return;
    }

    const weaponItem = mcData.itemsByName[weapon];
    if (!bot.inventory.findInventoryItem(weaponItem.id, null)) {
        bot.chat(`No ${weapon} in inventory for shooting`);
        return;
    }

    const targetEntity = bot.nearestEntity(
        (entity) =>
            entity.name === target
    );
    if (!targetEntity) {
        bot.chat(`No ${target} nearby`);
        return;
    }
    bot.hawkEye.autoAttack(targetEntity, "bow");
    bot.on('auto_shot_stopped', (target) => {
    })
}

async function consumeItem(bot, type, loop=false) {
    await setGamemode(bot, 'survival');
    const item = bot.inventory.findInventoryItem(mcData.itemsByName[type].id);
    if (!item) {
        await bot.chat(`No ${type} in inventory.`);
    } else {
        await bot.equip(item, "hand");
        await bot.consume();
    }
}